from src.client.chromaClient import initClient
from rich import print


collection = initClient()




result = collection.delete(ids=["689b5ac49dbc1a05772ebd45"])

print(result)

result = collection.query(
    query_texts=["¿Qué libro me recomiendas?"],

    )

print(result)

     