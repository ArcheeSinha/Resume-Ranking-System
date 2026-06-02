from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def create_tfidf_vectors(job_description, resumes):

    documents = [job_description]

    for resume in resumes.values():
        documents.append(resume)

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    return tfidf_matrix, vectorizer


def calculate_similarity(tfidf_matrix):

    job_description_vector = tfidf_matrix[0]

    resume_vectors = tfidf_matrix[1:]

    similarity_scores = cosine_similarity(
        job_description_vector,
        resume_vectors
    )[0]

    return similarity_scores