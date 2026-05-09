# SHL Assessment Recommendation System

## Overview

This project is an AI-powered conversational assessment recommendation system developed for the SHL AI Internship Assignment.

The system recommends relevant SHL assessments based on natural language hiring queries and job descriptions using semantic retrieval and conversational logic.

The solution supports:

* conversational recommendation flow
* clarification questions
* recommendation refinement
* assessment comparison
* off-topic refusal handling
* evaluation metrics using Recall@5 testing

---

## Features

* AI-based assessment recommendation
* Conversational recommendation flow
* Clarification question handling
* Recommendation refinement support
* Assessment comparison support
* Off-topic refusal handling
* FastAPI backend API
* Streamlit frontend UI
* TF-IDF semantic similarity matching
* SHL assessment dataset retrieval
* JSON API responses
* Recall@5 evaluation testing
* Recommendation relevance validation

---

## Technologies Used

* Python
* FastAPI
* Streamlit
* Scikit-learn
* Pandas
* TF-IDF Vectorization

---

## Project Structure

* `app.py` → Streamlit frontend
* `api.py` → FastAPI backend
* `recommender.py` → Recommendation engine
* `conversation.py` → Conversational agent logic
* `evaluation.py` → Retrieval evaluation pipeline
* `assessments.csv` → SHL assessment dataset
* `requirements.txt` → Project dependencies

---

## Run Backend

```bash
uvicorn api:app --reload
```

---

## Run Frontend

```bash
streamlit run app.py
```

---

## API Endpoints

### GET /health

Health check endpoint.

Example response:

```json
{
  "status": "ok"
}
```

---

### POST /chat

Conversational recommendation endpoint.

Example request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Need a Python developer with SQL and API skills"
    }
  ]
}
```

Example response:

```json
{
  "reply": "Here are 5 recommended SHL assessments.",
  "recommendations": [
    {
      "name": "Python Developer Test",
      "url": "https://www.shl.com",
      "test_type": "Technical"
    }
  ],
  "end_of_conversation": true
}
```

---

## Evaluation Methodology

The project includes evaluation-oriented testing and validation using multiple conversational hiring scenarios.

Implemented evaluation areas include:

* recommendation relevance testing
* retrieval quality validation
* Recall@5 evaluation
* conversational consistency testing
* grounded SHL-only recommendation validation
* clarification flow testing
* off-topic refusal testing

Run evaluation:

```bash
python evaluation.py
```

Example output:

```text
Recall@5: 1.00
Average Recall@5: 1.00
```

---

## Conversational Behaviors

The conversational agent supports:

* clarification questions for vague queries
* recommendation refinement
* assessment comparison
* stateless multi-turn interaction
* grounded catalog-based recommendations

Example vague query:

```text
Hiring a developer
```

Agent response:

```text
Could you share more details such as role, skills, experience level, or assessment type?
```

---

## Live Application

Streamlit App:

https://shl-assessment-recommendation-system-celez5asq28fqskpcgtrz2.streamlit.app/

---

## GitHub Repository

Repository:

https://github.com/IncharaGowda14/shl-assessment-recommendation-system

---

## Author

Inchara B V
