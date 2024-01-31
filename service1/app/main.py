from fastapi import FastAPI
from pydantic import BaseModel
from dapr.ext.fastapi import DaprApp

app = FastAPI()
dapr= DaprApp(app)

class Message(BaseModel):
    content: str

@app.post("/publish")
async def publish_message(message: Message):
    # Publishes a message to Dapr pub/sub
    dapr.publish(pubsub_name="messages", topic="new-message", data=message.dict())
    return {"message": "Message published successfully"}
