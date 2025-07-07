from fastapi import FastAPI
from pydantic import BaseModel
from app.data_loader import load_projects
from app.retriever import ProjectRetriever
from app.llm_rag import RAGPipeline

app = FastAPI()

projects = load_projects()
retriever = ProjectRetriever(projects)
pipeline = RAGPipeline(retriever)

class QueryRequest(BaseModel):
    question: str

@app.get('/')
def hello():
    return {"message": "This is Faisal's PingCRM"}

@app.post("/search")
async def search_projects(request: QueryRequest):
    result = pipeline.generate_answer(request.question)
    return result
