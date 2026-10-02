import io
from datetime import datetime
import pandas as pd
import streamlit as st

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import extract_skills, load_skills
from job_matcher import rank_roles, analyze_target_role
from roadmap_generator import generate_roadmap
from report_generator import build_analysis_report

st.set_page_config(
    page_title="AI Resume Analyzer & Job Recommendation System",
    page_icon="📄",
    layout="wide",
)

st.title("AI Resume Analyzer & Job Recommendation System")
st.caption("NLP/ML-based educational tool for resume-to-role matching. Match scores are estimates, not hiring decisions.")

@st.cache_data
def get_data():
    roles = pd.read_csv("data/job_roles.csv")
    skills = load_skills("data/skill_dictionary.csv")
    return roles, skills

roles_df, skill_dict = get_data()

with st.sidebar:
    st.header("Project Controls")
    st.write("Upload a PDF or DOCX resume to begin.")
    max_mb = 5
    st.info(f"Maximum file size: {max_mb} MB")
    st.markdown("**Responsible AI**")
    st.write("Only job-related skills, projects, education and relevant experience are considered.")
    st.write("Protected attributes such as age, gender, religion, nationality, marital status, disability and photographs are not scored.")

uploaded = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if not uploaded:
    st.markdown("""
    ### What this application does
    1. Extracts text from a PDF/DOCX resume.
    2. Cleans and normalizes the text.
    3. Detects job-related technical skills.
    4. Compares the resume with predefined job roles using TF-IDF and cosine similarity.
    5. Identifies skill gaps and produces a learning roadmap.
    6. Provides a downloadable analysis report.
    """)
    st.stop()

if uploaded.size > 5 * 1024 * 1024:
    st.error("File is larger than the allowed 5 MB limit.")
    st.stop()

try:
    raw_text = extract_resume_text(uploaded.getvalue(), uploaded.name)
except Exception as exc:
    st.error(f"Could not read the resume: {exc}")
    st.stop()

cleaned = clean_text(raw_text)
skills_found = extract_skills(cleaned, skill_dict)

st.success(f"Processed: {uploaded.name}")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Overview", "Role Recommendations", "Skill Gap & Roadmap", "Extracted Resume Text"]
)

with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("Characters Extracted", f"{len(raw_text):,}")
    c2.metric("Detected Skills", len(skills_found))
    c3.metric("Job Roles Compared", len(roles_df))

    st.subheader("Detected Skills")
    if skills_found:
        st.write(", ".join(sorted(skills_found)))
    else:
        st.warning("No controlled-dictionary skills were detected.")

with tab2:
    ranked = rank_roles(cleaned, roles_df)
    ranked_display = ranked[["role", "match_score"]].copy()
    ranked_display["match_score"] = ranked_display["match_score"].round(1)
    ranked_display.index = range(1, len(ranked_display) + 1)

    st.subheader("Recommended Roles")
    st.bar_chart(ranked_display.set_index("role")["match_score"])
    st.dataframe(
        ranked_display.rename(columns={"role": "Job Role", "match_score": "Match Score (%)"}),
        use_container_width=True,
    )

    st.info("The ranking is based on job-related text similarity and is intended for educational guidance.")

with tab3:
    selected_role = st.selectbox("Select a target role", roles_df["role"].tolist())
    target = analyze_target_role(cleaned, selected_role, roles_df, skill_dict)

    c1, c2, c3 = st.columns(3)
    c1.metric("Target Role Match", f"{target['match_score']:.1f}%")
    c2.metric("Skills Found", len(target["found_skills"]))
    c3.metric("Missing Skills", len(target["missing_skills"]))

    left, right = st.columns(2)
    with left:
        st.subheader("Skills Found")
        if target["found_skills"]:
            for s in target["found_skills"]:
                st.success(s)
        else:
            st.write("No required skills detected.")

    with right:
        st.subheader("Missing / Not Detected Skills")
        if target["missing_skills"]:
            for s in target["missing_skills"]:
                st.warning(s)
        else:
            st.success("No missing required skills detected from the controlled dictionary.")

    st.subheader("Learning Roadmap")
    roadmap = generate_roadmap(target["missing_skills"], skill_dict)
    if roadmap:
        for item in roadmap:
            st.markdown(f"**Week {item['week']}: {item['skill']}** — {item['topic']}")
    else:
        st.write("No roadmap items are required from the detected skill gaps.")

    report = build_analysis_report(
        resume_name=uploaded.name,
        target_role=selected_role,
        target=target,
        ranked=ranked,
        roadmap=roadmap,
    )
    st.download_button(
        "Download Analysis Report",
        data=report.encode("utf-8"),
        file_name="resume_analysis_report.txt",
        mime="text/plain",
    )

with tab4:
    st.text_area("Extracted Text", raw_text, height=500)
