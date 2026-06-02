import os
from utils.csv_export import export_to_csv
from utils.preprocess import clean_text
from utils.similarity import (
    create_tfidf_vectors,
    calculate_similarity
)

# =========================
# Read Job Description
# =========================

with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

print("\n===== JOB DESCRIPTION =====\n")
print(job_description)

# =========================
# Read Resumes
# =========================

resume_folder = "data/resumes"

resumes = {}

for filename in os.listdir(resume_folder):

    if filename.endswith(".txt"):

        file_path = os.path.join(resume_folder, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            resumes[filename] = file.read()

print("\n===== RESUMES =====\n")

for filename, content in resumes.items():

    print(f"\n{filename}")
    print("-" * 40)
    print(content)

# =========================
# Clean Job Description
# =========================

cleaned_jd = clean_text(job_description)

print("\n===== CLEANED JOB DESCRIPTION =====\n")
print(cleaned_jd)

# =========================
# Clean Resumes
# =========================

cleaned_resumes = {}

for filename, content in resumes.items():
    cleaned_resumes[filename] = clean_text(content)

print("\n===== CLEANED RESUMES =====\n")

for filename, content in cleaned_resumes.items():

    print(f"\n{filename}")
    print("-" * 40)
    print(content)

# =========================
# TF-IDF Vectorization
# =========================

tfidf_matrix, vectorizer = create_tfidf_vectors(
    cleaned_jd,
    cleaned_resumes
)

print("\n===== TF-IDF MATRIX INFO =====")

print("Rows:", tfidf_matrix.shape[0])
print("Columns:", tfidf_matrix.shape[1])

# =========================
# Vocabulary
# =========================

print("\n===== VOCABULARY =====\n")
print(vectorizer.get_feature_names_out())

# =========================
# Cosine Similarity
# =========================

similarity_scores = calculate_similarity(tfidf_matrix)

print("\n===== SIMILARITY SCORES =====\n")

for filename, score in zip(
    cleaned_resumes.keys(),
    similarity_scores
):

    percentage = round(score * 100, 2)

    print(f"{filename}: {percentage}%")

# =========================
# Candidate Ranking
# =========================

results = []

for filename, score in zip(
    cleaned_resumes.keys(),
    similarity_scores
):

    candidate_name = filename.replace(".txt", "").title()

    match_percentage = round(score * 100, 2)

    results.append(
        {
            "candidate": candidate_name,
            "score": match_percentage
        }
    )

# Sort by score (highest first)

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

# =========================
# Display Final Ranking
# =========================

print("\n===== FINAL RANKING =====\n")

print(f"{'Rank':<6}{'Candidate':<15}{'Match Score'}")

for rank, candidate in enumerate(results, start=1):

    print(
        f"{rank:<6}"
        f"{candidate['candidate']:<15}"
        f"{candidate['score']}%"
    )
    
# =========================
# Export Results
# =========================

export_to_csv(
    results,
    "output/rankings.csv"
)

print(
    "\nRankings exported to output/rankings.csv"
)