from io import BytesIO
from pathlib import Path

import pandas as pd

from text_cleaner import clean_text
from skill_extractor import extract_skills, load_skills
from job_matcher import rank_roles
from roadmap_generator import generate_roadmap

BASE = Path(__file__).resolve().parents[1]

def test_clean_text_preserves_technical_tokens():
    text = "Python   C++   C#   .NET"
    cleaned = clean_text(text)
    assert "python" in cleaned
    assert "c++" in cleaned
    assert "c#" in cleaned
    assert ".net" in cleaned

def test_skill_extraction():
    skills = load_skills(str(BASE / "data" / "skill_dictionary.csv"))
    found = extract_skills("Experienced in Python, SQL and Pandas.", skills)
    assert "python" in found
    assert "sql" in found
    assert "pandas" in found

def test_role_ranking_returns_all_roles():
    roles = pd.read_csv(BASE / "data" / "job_roles.csv")
    result = rank_roles("python sql pandas excel power bi statistics", roles)
    assert len(result) == len(roles)
    assert result["match_score"].between(0, 100).all()

def test_roadmap_generation():
    skills = load_skills(str(BASE / "data" / "skill_dictionary.csv"))
    roadmap = generate_roadmap(["docker", "fastapi"], skills)
    assert len(roadmap) == 2
    assert roadmap[0]["week"] == 1
