import streamlit as st
import pandas as pd

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
# Sidebar
# ===================================

with st.sidebar:

    st.title("📄 Resume Ranking")

    st.markdown("""
    ### Features

    ✅ Text Preprocessing

    ✅ TF-IDF Vectorization

    ✅ Cosine Similarity

    ✅ Candidate Ranking

    ✅ CSV Export
    """)

    st.info(
        "Upload one Job Description and multiple resumes."
    )

# ===================================
# Header
# ===================================

st.markdown(
    """
    <h1 style='text-align:center;'>
        📄 Intelligent Resume Ranking System
    </h1>

    <p style='text-align:center; font-size:18px;'>
        AI-Powered Candidate Screening using TF-IDF and Cosine Similarity
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ===================================
# Upload Files
# ===================================

col1, col2 = st.columns(2)

with col1:

    job_description_file = st.file_uploader(
        "📋 Upload Job Description",
        type=["txt"]
    )

with col2:

    resume_files = st.file_uploader(
        "📄 Upload Resumes",
        type=["txt"],
        accept_multiple_files=True
    )

# ===================================
# Rank Candidates
# ===================================

if st.button("🚀 Rank Candidates", use_container_width=True):

    if not job_description_file:

        st.error(
            "Please upload a Job Description."
        )

        st.stop()

    if not resume_files:

        st.error(
            "Please upload at least one Resume."
        )

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

    cleaned_jd = clean_text(
        job_description
    )

    cleaned_resumes = {}

    for filename, content in resumes.items():

        cleaned_resumes[filename] = (
            clean_text(content)
        )

    # ===================================
    # TF-IDF + Similarity
    # ===================================

    with st.spinner(
        "Analyzing resumes..."
    ):

        tfidf_matrix, vectorizer = (
            create_tfidf_vectors(
                cleaned_jd,
                cleaned_resumes
            )
        )

        similarity_scores = (
            calculate_similarity(
                tfidf_matrix
            )
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

        results.append(
            {
                "Candidate":
                    candidate_name,

                "Match Score (%)":
                    round(score * 100, 2)
            }
        )

    results.sort(
        key=lambda x:
        x["Match Score (%)"],
        reverse=True
    )

    final_results = []

    for rank, candidate in enumerate(
        results,
        start=1
    ):

        medal = ""

        if rank == 1:
            medal = "🥇"

        elif rank == 2:
            medal = "🥈"

        elif rank == 3:
            medal = "🥉"

        final_results.append(
            {
                "Rank":
                    f"{medal} {rank}",

                "Candidate":
                    candidate["Candidate"],

                "Match Score (%)":
                    candidate["Match Score (%)"]
            }
        )

    df = pd.DataFrame(
        final_results
    )

    # ===================================
    # Statistics
    # ===================================

    st.success(
        "Ranking Completed Successfully!"
    )

    st.subheader(
        "📊 Dashboard Statistics"
    )

    total_resumes = len(df)

    best_match = (
        df["Match Score (%)"]
        .max()
    )

    average_match = round(
        df["Match Score (%)"]
        .mean(),
        2
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Resumes",
        total_resumes
    )

    col2.metric(
        "Best Match",
        f"{best_match}%"
    )

    col3.metric(
        "Average Match",
        f"{average_match}%"
    )

    # ===================================
    # Ranking Table
    # ===================================

    st.subheader(
        "🏆 Candidate Rankings"
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # ===================================
    # Visualization
    # ===================================

    st.subheader(
        "📈 Match Score Comparison"
    )

    chart_df = df.copy()

    chart_df["Rank"] = (
        chart_df["Rank"]
        .astype(str)
    )

    chart_df = chart_df.set_index(
        "Candidate"
    )

    st.bar_chart(
        chart_df["Match Score (%)"]
    )

    # ===================================
    # Download CSV
    # ===================================

    st.subheader(
        "📥 Export Results"
    )

    csv_data = (
        df.to_csv(
            index=False
        )
    )

    st.download_button(
        label="Download Rankings CSV",
        data=csv_data,
        file_name="rankings.csv",
        mime="text/csv"
    )