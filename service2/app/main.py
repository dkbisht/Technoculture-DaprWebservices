from fastapi import FastAPI
from dapr.ext.fastapi import DaprApp

app = FastAPI()
dapr= DaprApp(app)

# Subscribe to the "new-message" topic from the "messages" pub/sub
@dapr.subscribe(pubsub_name="messages", topic="new-message")
async def handle_new_message(message_data: dict):
    # Handle the received message (e.g., log it)
    print("Received message:", message_data)
    return {"message": "Message processed successfully"}
