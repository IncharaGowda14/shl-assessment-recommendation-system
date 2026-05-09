from fastapi import FastAPI
from pydantic import BaseModel
from recommender import recommend_assessments

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {
        "message": "SHL Assessment Recommendation API"
    }

@app.post("/recommend")
def recommend(request: QueryRequest):

    results = recommend_assessments(request.query)

    return {
        "query": request.query,
        "recommendations": results
    }