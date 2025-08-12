from src.client.chromaClient import initClient
from rich import print


collection = initClient()




result = collection.query(
    query_texts=["¿Qué libro me recomiendas?"],
    n_results=5,
    
)

print(result)
     
     