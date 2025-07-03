from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

from lms_api import get_file_from_lms
from intents import detect_intent

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

class Query(BaseModel):
    text: str
    user_id: str

@app.post("/process_query")
async def process_query(query: Query):
    user_input = query.text.lower()
    intent = detect_intent(user_input)

    if intent == "summary":
        response = await generate_summary(user_input)
    elif intent == "lms_file":
        response = await get_file_from_lms(user_input)
    elif intent == "doubt":
        response = await solve_doubt(user_input)
    else:
        response = "Sorry, I couldn't understand your request."

    return {"response": response}

async def generate_summary(text):
    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}]
    )
    return completion.choices[0].message.content.strip()

async def solve_doubt(text):
    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Explain this: {text}"}]
    )
    return completion.choices[0].message.content.strip()