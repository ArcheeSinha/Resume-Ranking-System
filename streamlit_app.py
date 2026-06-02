import streamlit as st

from utils.preprocess import clean_text
from utils.similarity import (
    create_tfidf_vectors,
    calculate_similarity
)

# ===================================
# Page Configuration
# ===================================

st.set_page_config(
    page_title="Resume Ranking System",
    page_icon="📄",
    layout="wide"
)

# ===================================
# Title
# ===================================

st.title("📄 Intelligent Resume Ranking System")
st.write(
    "Rank candidates using TF-IDF and Cosine Similarity"
)

# ===================================
# File Uploaders
# ===================================

job_description_file = st.file_uploader(
    "Upload Job Description",
    type=["txt"]
)

resume_files = st.file_uploader(
    "Upload Resume Files",
    type=["txt"],
    accept_multiple_files=True
)

# ===================================
# Rank Button
# ===================================

if st.button("Rank Candidates"):

    if not job_description_file:
        st.error("Please upload a Job Description.")
        st.stop()

    if not resume_files:
        st.error("Please upload at least one Resume.")
        st.stop()

    # ===================================
    # Read Files
    # ===================================

    job_description = (
        job_description_file
        .read()
        .decode("utf-8")
    )

    resumes = {}

    for file in resume_files:

        resumes[file.name] = (
            file.read()
            .decode("utf-8")
        )

    # ===================================
    # Preprocessing
    # ===================================

    cleaned_jd = clean_text(job_description)

    cleaned_resumes = {}

    for filename, content in resumes.items():

        cleaned_resumes[filename] = clean_text(
            content
        )

    # ===================================
    # TF-IDF
    # ===================================

    tfidf_matrix, vectorizer = create_tfidf_vectors(
        cleaned_jd,
        cleaned_resumes
    )

    # ===================================
    # Similarity Scores
    # ===================================

    similarity_scores = calculate_similarity(
        tfidf_matrix
    )

    # ===================================
    # Ranking
    # ===================================

    results = []

    for filename, score in zip(
        cleaned_resumes.keys(),
        similarity_scores
    ):

        candidate_name = (
            filename
            .replace(".txt", "")
            .title()
        )

        match_percentage = round(
            score * 100,
            2
        )

        results.append(
            {
                "Candidate": candidate_name,
                "Match Score (%)": match_percentage
            }
        )

    # Sort Highest First

    results.sort(
        key=lambda x: x["Match Score (%)"],
        reverse=True
    )

    # ===================================
    # Add Rank
    # ===================================

    final_results = []

    for rank, candidate in enumerate(
        results,
        start=1
    ):

        final_results.append(
            {
                "Rank": rank,
                "Candidate": candidate["Candidate"],
                "Match Score (%)":
                    candidate["Match Score (%)"]
            }
        )

    # ===================================
    # Display Results
    # ===================================

    st.success("Ranking Completed!")

    st.subheader("🏆 Candidate Rankings")

    st.table(final_results)