from app.retriever import ProjectRetriever
from ollama import Client
import time

class RAGPipeline:
    def __init__(self, retriever: ProjectRetriever):
        self.retriever = retriever
        self.client = Client()  # connects to localhost:11434

    def generate_answer(self, query: str):
        start_time = time.time()  # Start timer
        relevant_projects = self.retriever.search(query)
        context = "\n\n".join([f"{p['name']}: {p['description']}" for p in relevant_projects])

        prompt = (
            f"You are an assistant helping users find relevant software projects.\n"
            f"User query: {query}\n"
            f"Relevant project descriptions:\n{context}\n\n"
            f"Based on the above, summarize or recommend the most relevant projects."
        )

        response = self.client.chat(
            model='gemma:2b',
            messages=[{"role": "user", "content": prompt}]
        )
        end_time = time.time()    # End timer
        duration = round(end_time - start_time, 2)
        print(f"⏱️ get_answer completed in {duration} seconds")
        return {
            "summary": response['message']['content'],
            "projects": relevant_projects,
            "time_taken_seconds": duration
        }
