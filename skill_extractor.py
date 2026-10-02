import re
import pandas as pd

def load_skills(path: str):
    df = pd.read_csv(path)
    return df.to_dict("records")

def _contains_skill(text: str, skill: str) -> bool:
    skill_norm = skill.lower().strip()
    if not skill_norm:
        return False
    # Phrase matching avoids many accidental partial matches.
    pattern = r"(?<![a-z0-9])" + re.escape(skill_norm) + r"(?![a-z0-9])"
    return bool(re.search(pattern, text.lower()))

def extract_skills(text: str, skill_dictionary) -> list[str]:
    found = []
    for row in skill_dictionary:
        skill = str(row["skill"]).strip()
        if _contains_skill(text, skill):
            found.append(skill)
    return sorted(set(found))
