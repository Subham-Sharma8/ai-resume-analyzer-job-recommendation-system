# PROJECT REPORT
## AI RESUME ANALYZER AND JOB RECOMMENDATION SYSTEM

### 1. Abstract
The AI Resume Analyzer and Job Recommendation System is an educational NLP/ML application designed to help students understand how their resume content aligns with selected job roles. The system accepts PDF and DOCX resumes, extracts and cleans text, identifies job-related technical skills, compares the resume against a controlled job-role dataset and calculates an estimated role match score. It also reports missing skills and produces a basic learning roadmap.

### 2. Problem Statement
Students often do not know whether their resume contains the skills expected for a particular role. Recruiters also receive many resumes and need a quick way to compare job-related information. This project creates an educational matching system that focuses on skills, projects, education and relevant experience.

### 3. Objectives
1. Extract text from PDF and DOCX resumes.
2. Clean and normalize unstructured resume text.
3. Identify at least 20–30 job-related technical skills.
4. Compare a resume against at least five job roles.
5. Calculate an estimated resume-to-role match score.
6. Recommend the top three suitable roles.
7. Identify missing skills for a selected target role.
8. Generate a basic learning roadmap.
9. Provide a Streamlit dashboard.
10. Provide a downloadable analysis report.

### 4. System Workflow
Upload resume → Extract text → Clean text → Extract skills → Load job roles → TF-IDF vectorization → Cosine similarity → Skill coverage → Match score → Role ranking → Skill-gap analysis → Learning roadmap → Report.

### 5. System Architecture
The application is organized into:
- Presentation layer: Streamlit
- Parsing layer: pypdf and python-docx
- NLP preprocessing: regex/text cleaning
- Skill extraction: controlled dictionary
- ML matching: TF-IDF and cosine similarity
- Recommendation layer: weighted score and ranking
- Gap analysis: required skill vs detected skill
- Roadmap layer: rule-based learning topics
- Reporting layer: downloadable text report
- Data layer: CSV datasets

### 6. Algorithm
For each job role:
1. Construct role text from role name, description and required skills.
2. Create a TF-IDF representation of resume + role text.
3. Calculate cosine similarity.
4. Calculate required-skill coverage.
5. Combine the two values using the weighted score.

Formula:
Match Score = (0.60 × Cosine Similarity + 0.40 × Skill Coverage) × 100

### 7. Dataset
The project uses a manually verified CSV dataset containing 10 example roles and a controlled skill dictionary containing more than 30 job-related skills.

Roles include:
- Data Analyst
- Machine Learning Engineer
- AI Engineer
- NLP Engineer
- Computer Vision Engineer
- Python Developer
- Data Scientist
- Backend Developer
- Cloud/DevOps Engineer
- MLOps Engineer

### 8. User Interface
The Streamlit interface provides:
- Resume upload
- Overview metrics
- Detected skills
- Role recommendation chart/table
- Target-role selector
- Found and missing skills
- Learning roadmap
- Downloadable analysis report
- Extracted text view

### 9. Responsible AI
The system must be used for guidance, not automatic hiring or rejection. Protected personal information is excluded from scoring. Match scores are estimates. Missing keywords do not necessarily mean missing ability.

### 10. Testing and Evaluation
Evaluation should cover:
- extraction quality
- skill precision
- skill recall
- role ranking
- score consistency
- fairness
- usability

The supplied `tests/test_cases.csv` is the evaluation sheet.

### 11. Limitations
1. Keyword matching can miss synonyms.
2. TF-IDF does not provide full semantic understanding.
3. Small manually created role dataset.
4. No labelled hiring dataset is used.
5. PDF extraction may vary with document layout.
6. Match scores are not equivalent to recruiter decisions.

### 12. Future Scope
Sentence Transformers, spaCy, job-description upload, controlled LLM feedback, FastAPI, PostgreSQL, authentication, PDF reporting, analytics and Docker deployment can be added.

### 13. Conclusion
The system demonstrates a complete beginner-to-intermediate NLP/ML workflow: document parsing, preprocessing, skill extraction, vectorization, similarity calculation, recommendation, gap analysis and dashboard visualization. It is suitable as an academic project while keeping hiring-related decisions outside the scope of the application.
