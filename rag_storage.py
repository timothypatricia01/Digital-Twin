import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from groq import Groq
import pypdf
from dotenv import load_dotenv

load_dotenv()

class DigitalTwinRAG:
    def __init__(self):
        # Using Groq client for embeddings instead of OpenAI
                # Using :memory: bypasses the portalocker file system error completely!
        self.db_client = QdrantClient(":memory:")
        self.collection_name = "twin_knowledge"
        self._setup_vector_db()

    def _setup_vector_db(self):
        collections = self.db_client.get_collections().collections
        exists = any(c.name == self.collection_name for c in collections)
        if not exists:
            # Groq's nomic-embed-text-v1.5 model uses 768 dimensions
            self.db_client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=768, distance=Distance.COSINE)
            )

    def ingest_pdf(self, file_path: str):
        """Extracts text from a PDF, splits it natively, and saves vectors to Qdrant."""
        reader = pypdf.PdfReader(file_path)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
        
        # Native Python chunking: splits by paragraphs (~500 characters)
        paragraphs = [p.strip() for p in full_text.split("\n\n") if p.strip()]
        
        for idx, chunk in enumerate(paragraphs):
            # Fetch embeddings directly from Groq
            emb_res = self.ai_client.embeddings.create(
                input=chunk,
                model="nomic-embed-text-v1.5"
            )
            vector = emb_res.data[0].embedding
            
            self.db_client.upsert(
                collection_name=self.collection_name,
                points=[
                    PointStruct(
                        id=idx,
                        vector=vector,
                        payload={"text": chunk, "metadata": os.path.basename(file_path)}
                    )
                ]
            )

    def retrieve_context(self, query: str, top_k: int = 3) -> str:
        """Finds the most relevant context chunks for a given query via Groq."""
        try:
            emb_res = self.ai_client.embeddings.create(
                input=query,
                model="nomic-embed-text-v1.5"
            )
            query_vector = emb_res.data[0].embedding

            search_results = self.db_client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                limit=top_k
            )
            return "\n---\n".join([res.payload["text"] for res in search_results])
        except Exception:
            return ""
