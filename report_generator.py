from datetime import datetime

def build_analysis_report(resume_name, target_role, target, ranked, roadmap):
    lines = [
        "AI RESUME ANALYZER AND JOB RECOMMENDATION SYSTEM",
        "=" * 55,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Resume: {resume_name}",
        f"Target Role: {target_role}",
        f"Target Role Match Score: {target['match_score']:.1f}%",
        "",
        "SKILLS FOUND",
        "-" * 20,
        *[f"- {s}" for s in target["found_skills"]],
        "",
        "MISSING / NOT DETECTED SKILLS",
        "-" * 30,
        *[f"- {s}" for s in target["missing_skills"]],
        "",
        "ROLE RECOMMENDATIONS",
        "-" * 25,
    ]
    for i, row in ranked.head(3).iterrows():
        lines.append(f"{i + 1}. {row['role']} - {row['match_score']:.1f}%")

    lines += ["", "LEARNING ROADMAP", "-" * 20]
    for item in roadmap:
        lines.append(f"Week {item['week']}: {item['skill']} - {item['topic']}")

    lines += [
        "",
        "RESPONSIBLE AI NOTE",
        "-" * 25,
        "This report is an educational estimate. It does not make hiring, rejection, "
        "or candidate-ranking decisions based on protected personal information.",
        "A missing keyword does not necessarily mean a person lacks the underlying ability.",
    ]
    return "\n".join(lines)
