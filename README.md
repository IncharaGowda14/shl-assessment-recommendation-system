# SHL Assessment Recommendation System

## Overview
This project is an AI-powered assessment recommendation system developed for the SHL AI Internship Assignment.

The system recommends relevant SHL assessments based on natural language job descriptions or hiring queries.

## Features
- AI-based assessment recommendation
- FastAPI backend API
- Streamlit frontend UI
- TF-IDF similarity matching
- Large assessment dataset
- JSON API responses

## Technologies Used
- Python
- FastAPI
- Streamlit
- Scikit-learn
- Pandas

## Project Structure
- app.py → Streamlit frontend
- api.py → FastAPI backend
- recommender.py → Recommendation engine
- assessments.csv → Assessment dataset

## Run Backend

```bash
uvicorn api:app --reload

## Run Frontend

```bash
streamlit run app.py
```

## API Endpoint

POST /recommend

Example request:

```json
{
  "query": "Need a Python developer with SQL skills"
}
```

## Author

Inchara Gowda