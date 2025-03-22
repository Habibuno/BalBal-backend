from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Middleware CORS : autorise l'accès depuis StackBlitz
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ← autorise toutes les origines (dont StackBlitz)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clé API sécurisée
openai.api_key = os.getenv("OPENAI_API_KEY")

class Prompt(BaseModel):
    user_prompt: str

@app.post("/generate")
async def generate_saas(prompt: Prompt):
    print("Prompt reçu :", prompt.user_prompt)  # pour débug
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu es un assistant qui crée des SaaS complets depuis une description simple."},
            {"role": "user", "content": prompt.user_prompt}
        ]
    )
    return {"result": response.choices[0].message.content}
