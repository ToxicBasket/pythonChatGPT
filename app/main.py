from typing import Union
import os
import openai
from fastapi import FastAPI
app = FastAPI()
openai.api_key_path = "/Users/collin/PycharmProjects/pythonChatGPT/app/.env"

@app.get("/")
def read_root():
    return {"Hello": "WWWorld"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




def check_message(user_id: int, message: str):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Decide whether a Tweet's sentiment is positive, neutral, or negative.\n\nTweet: \"{message}\"\nSentiment:",
      temperature=0,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0
    )

    return response["choices"][0]["text"]

@app.post("/text")
def read_text(user_id: int, message: str):
    return check_message(user_id, message)