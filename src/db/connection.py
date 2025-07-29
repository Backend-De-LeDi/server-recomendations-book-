import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv() 

DB_URI = os.getenv("URL_DB")
if not DB_URI:
    raise ValueError("No se encontró URL_DB en el entorno.")

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)

db_name = "ledi-backend"
db = client[db_name]