import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def _role_text(row) -> str:
    return f"{row['role']} {row['description']} {row['required_skills']}"

def _skill_list(value: str) -> list[str]:
    return [x.strip().lower() for x in str(value).split(",") if x.strip()]

def rank_roles(resume_text: str, roles_df: pd.DataFrame) -> pd.DataFrame:
    role_texts = [_role_text(row) for _, row in roles_df.iterrows()]
    corpus = [resume_text] + role_texts
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
    matrix = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(matrix[0:1], matrix[1:]).flatten()

    result = roles_df.copy()
    result["similarity"] = similarities

    # Blend semantic/text similarity with a controlled required-skill coverage score.
    coverage_scores = []
    resume_lower = resume_text.lower()
    for _, row in result.iterrows():
        required = _skill_list(row["required_skills"])
        present = sum(
            1 for skill in required
            if re.search(r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])", resume_lower)
        )
        coverage_scores.append((present / len(required)) if required else 0)

    result["skill_coverage"] = coverage_scores
    result["match_score"] = (0.60 * result["similarity"] + 0.40 * result["skill_coverage"]) * 100
    return result.sort_values("match_score", ascending=False).reset_index(drop=True)

def analyze_target_role(resume_text: str, role: str, roles_df: pd.DataFrame, skill_dictionary):
    ranked = rank_roles(resume_text, roles_df)
    row = roles_df[roles_df["role"] == role].iloc[0]

    required = _skill_list(row["required_skills"])
    found = []
    missing = []
    for skill in required:
        pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])"
        if re.search(pattern, resume_text.lower()):
            found.append(skill)
        else:
            missing.append(skill)

    score = float(ranked.loc[ranked["role"] == role, "match_score"].iloc[0])
    return {
        "role": role,
        "match_score": score,
        "found_skills": found,
        "missing_skills": missing,
    }
