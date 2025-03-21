from fastapi import FastAPI
import openai
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

openai.api_key = "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"

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
