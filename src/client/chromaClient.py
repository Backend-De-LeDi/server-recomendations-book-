import chromadb
from chromadb.config import Settings

def initClient():
     client = chromadb.PersistentClient(
          path="src/db/chroma",
          settings=Settings(allow_reset=True)
     )

     collection = client.get_or_create_collection(
          name="books",
          metadata={"hnsw":"cosine"}
     )
     return collection

     
     