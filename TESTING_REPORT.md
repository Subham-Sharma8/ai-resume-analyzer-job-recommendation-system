# TESTING AND EVALUATION REPORT

## 1. Testing Objective
The objective is to verify that the application correctly processes resumes, extracts skills, computes role similarity, identifies gaps and presents understandable results.

## 2. Functional Testing
See `tests/test_cases.csv` for the test matrix.

### Core test areas
- PDF extraction
- DOCX extraction
- File-type validation
- File-size validation
- Text normalization
- Skill extraction
- Role ranking
- Skill-gap analysis
- Roadmap generation
- Report generation
- Responsible-AI behavior

## 3. Evaluation Metrics

### Extraction Quality
Check whether text from every resume page/paragraph is available to downstream processing.

### Skill Precision
Precision = correctly detected job-related skills / all detected skills.

### Skill Recall
Recall = correctly detected job-related skills / relevant skills actually present.

### Role Ranking
Compare the top predicted role against manually labelled expected roles for a small evaluation set.

### Score Consistency
Add/remove a relevant skill and verify that the corresponding role's skill coverage does not move in an illogical direction.

### Fairness
Add protected information to a resume and verify that it is not used by the scoring logic.

### Usability
A student should be able to upload a resume, understand the score, see gaps and identify next learning steps without reading the source code.

## 4. Acceptance Criteria
- Valid PDF/DOCX resumes are processed.
- Unsupported file types are rejected.
- Resumes above 5 MB are rejected.
- At least 30 controlled skills are available.
- At least five roles are compared.
- Top three recommendations are visible.
- Target-role gaps are visible.
- Roadmap is generated from gaps.
- Report can be downloaded.
- Protected attributes are not part of the score formula.

## 5. Known Limitations
The application should not be evaluated as a hiring classifier. It is an educational recommendation system with a manually defined dataset and lexical similarity model.
