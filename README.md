# Intelligent Resume Ranking System

## Overview

The Intelligent Resume Ranking System is an NLP-based application that ranks candidates according to their relevance to a given Job Description.

The system uses Text Preprocessing, TF-IDF Vectorization, and Cosine Similarity to calculate the match percentage between resumes and the job description.

A Streamlit-based user interface allows recruiters to upload a job description and multiple resumes, view rankings, and download results.

---

## Features

### Core Features

* Upload a Job Description
* Upload Multiple Resumes
* Text Preprocessing

  * Lowercase conversion
  * Punctuation removal
  * Stopword removal
* TF-IDF Keyword Extraction
* Cosine Similarity Matching
* Candidate Ranking
* Match Percentage Calculation

### Bonus Features

* Streamlit Web Interface
* CSV Export
* Dynamic Resume Processing
* Real-Time Ranking

---

## Project Architecture

```text
Job Description
        |
        v
Text Preprocessing
        |
        v
TF-IDF Vectorization
        |
        v
Cosine Similarity
        |
        v
Match Score Calculation
        |
        v
Candidate Ranking
        |
        v
Streamlit Dashboard + CSV Export
```

---

## Technologies Used

* Python
* Streamlit
* Scikit-Learn
* NLTK
* Pandas

---

## Folder Structure

```text
Resume-Ranking-System/

│
├── streamlit_app.py
├── app.py
├── requirements.txt
│
├── data/
│   ├── job_description.txt
│   └── resumes/
│
├── output/
│   └── rankings.csv
│
└── utils/
    ├── preprocess.py
    ├── similarity.py
    └── csv_export.py
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Resume-Ranking-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Streamlit Application

```bash
streamlit run streamlit_app.py
```

---

## How It Works

### Step 1: Text Preprocessing

The job description and resumes are cleaned using:

* Lowercasing
* Punctuation Removal
* Stopword Removal

### Step 2: TF-IDF Vectorization

The cleaned text is converted into numerical feature vectors using TF-IDF.

### Step 3: Cosine Similarity

Cosine Similarity is used to measure how closely each resume matches the job description.

### Step 4: Candidate Ranking

Candidates are ranked according to their similarity scores.

### Step 5: Export Results

Rankings can be exported to CSV format.

---

## Sample Output

| Rank | Candidate | Match Score |
| ---- | --------- | ----------- |
| 1    | Priya     | 89%         |
| 2    | Aman      | 82%         |
| 3    | Rahul     | 74%         |

---

## Future Improvements

* PDF Resume Support
* DOCX Resume Support
* Skill Extraction Dashboard
* Resume Keyword Highlighting
* Recruiter Analytics
* AI-Based Resume Feedback

---

## Author

Archee Sinha

B.Tech CSE (AI)
ABES Institute of Technology

---

## License

This project was developed as part of an AI Intern Assessment.
