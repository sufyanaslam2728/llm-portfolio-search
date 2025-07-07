from sentence_transformers import SentenceTransformer, util

class ProjectRetriever:
    def __init__(self, projects):
        self.projects = projects
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.project_texts = [proj["description"] for proj in projects]
        self.embeddings = self.model.encode(self.project_texts, convert_to_tensor=True)

    def search(self, query, top_k=5):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        hits = util.semantic_search(query_embedding, self.embeddings, top_k=top_k)[0]
        return [self.projects[hit['corpus_id']] for hit in hits]
