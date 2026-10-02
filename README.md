# AI Resume Analyzer and Job Recommendation System

## 1. Project Overview
This is an educational NLP/ML application that analyzes a PDF or DOCX resume, extracts job-related technical skills, compares the resume with predefined job roles, calculates estimated match scores, recommends roles, identifies skill gaps and creates a learning roadmap.

The implementation follows the supplied project guidance: PDF/DOCX extraction, text cleaning, controlled skill extraction, a manually verified role dataset, TF-IDF/cosine similarity, skill-gap analysis, Streamlit UI, downloadable analysis report, testing sheet and deployment-ready files.

## 2. Main Features
- PDF and DOCX resume upload
- 5 MB upload validation
- Resume text extraction
- Text cleaning and normalization
- Controlled dictionary with 30+ job-related skills
- 10 predefined job roles
- TF-IDF + cosine similarity
- Required-skill coverage component
- Top role recommendations
- Target-role skill-gap analysis
- Week-by-week learning roadmap
- Downloadable analysis report
- Responsible-AI constraints
- Automated tests for core modules

## 3. Technology Stack
- Python
- Streamlit
- pypdf
- python-docx
- Pandas / NumPy
- Scikit-learn
- Plotly-compatible Streamlit charts
- Pytest

## 4. Folder Structure
```text
ai_resume_analyzer/
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
├── report_generator.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── data/
│   ├── job_roles.csv
│   └── skill_dictionary.csv
├── sample_resumes/
├── reports/
└── tests/
    └── test_cases.csv
```

## 5. Installation
Python 3.10+ is recommended.

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## 6. Run
```bash
streamlit run app.py
```

Open the local Streamlit URL shown in the terminal.

## 7. Matching Method
The role score combines:
- 60% TF-IDF cosine similarity between resume text and role text
- 40% required-skill coverage

Final score:
`match_score = (0.60 × cosine_similarity + 0.40 × skill_coverage) × 100`

This is an estimate for educational guidance, not a recruiter decision.

## 8. Responsible AI
The project does not score:
- gender
- age
- religion
- nationality
- photograph
- marital status
- disability

Only job-related skills and relevant resume content are considered. A missing keyword does not prove that the applicant lacks the underlying ability.

## 9. Testing
The supplied `tests/test_cases.csv` contains the project evaluation sheet. For code-level tests, add unit tests under `tests/` and run:

```bash
pytest
```

## 10. GitHub
```bash
git init
git add .
git commit -m "Initial AI resume analyzer project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## 11. Deployment
For Streamlit Community Cloud:
1. Push the project to GitHub.
2. Create a new Streamlit app.
3. Select `app.py` as the entry point.
4. Deploy.

For Docker or Render, the same Python dependencies can be used; a production Dockerfile can be added if required by the hosting platform.

## 12. Limitations
- Keyword extraction can miss synonyms and implied skills.
- TF-IDF is lexical and may not understand deep semantic equivalence.
- The manually created role dataset is small.
- Scores are not validated against recruiter decisions.
- Resume formatting can affect extraction quality.
- The application is not intended for automated hiring or rejection.

## 13. Future Enhancements
- Sentence Transformers semantic matching
- spaCy section/entity extraction
- User-supplied job-description upload
- LLM-based controlled feedback
- FastAPI backend
- PostgreSQL persistence
- Authentication and saved reports
- PDF report generation
- Admin analytics dashboard
