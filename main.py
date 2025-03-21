from fastapi import FastAPI
import openai
import os
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Récupération sécurisée de la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    user_prompt: str

@app.post("/generate")
async def generate_saas(prompt: Prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu es un assistant qui crée des SaaS complets depuis une description simple."},
            {"role": "user", "content": prompt.user_prompt}
        ]
    )
    return {"result": response.choices[0].message.content}
