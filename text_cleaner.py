import re

def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    text = text.lower().strip()

    # Preserve important technical tokens.
    replacements = {
        "c plus plus": "c++",
        "c sharp": "c#",
        "dot net": ".net",
        "scikit learn": "scikit-learn",
        "machine learning": "machine learning",
        "deep learning": "deep learning",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove most punctuation while retaining technical symbols.
    text = re.sub(r"[^a-z0-9+#./_-]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
