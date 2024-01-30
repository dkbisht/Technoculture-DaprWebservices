from fastapi import FastAPI
from dapr.ext.fastapi import Dapr

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
