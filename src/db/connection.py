import motor.motor_asyncio
import os 

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get('URL_DB'))
db = client["ledi-backend"]

