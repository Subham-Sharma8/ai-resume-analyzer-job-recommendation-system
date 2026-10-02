# VIVA QUESTIONS AND ANSWERS

## 1. How do you extract text from a resume?
PDF text is extracted using pypdf. DOCX text is extracted using python-docx.

## 2. What is TF-IDF?
TF-IDF assigns importance to terms based on how often they occur in a document while reducing the importance of terms that occur across many documents.

## 3. What does cosine similarity measure?
It measures the angle-based similarity between two vector representations. A value closer to 1 indicates greater directional similarity.

## 4. Why can keyword matching miss relevant skills?
A resume may use synonyms, abbreviations or descriptions that do not exactly match the controlled dictionary.

## 5. When should Sentence Transformers be used?
They are useful when semantic similarity is more important than exact word overlap and sufficient compute/resources are available.

## 6. Why should protected attributes be excluded?
They are unrelated to job skill requirements and can introduce unfair or inappropriate decision-making.

## 7. How is the match score calculated?
The project combines TF-IDF cosine similarity and required-skill coverage using 60% and 40% weights respectively.

## 8. What are the limitations?
Keyword extraction and TF-IDF are limited in semantic understanding; the role dataset is small and manually defined; the score is an educational estimate.

## 9. Why use Streamlit?
It provides a simple Python-based interface suitable for an academic dashboard without requiring a separate frontend framework.

## 10. Why is no labelled ML classifier used?
The supplied guidance recommends labelled machine-learning models only when a suitable labelled dataset is available. This project does not rely on a hiring-labelled dataset.
