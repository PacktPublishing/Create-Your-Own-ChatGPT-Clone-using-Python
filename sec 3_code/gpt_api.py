import os
import openai
import fastapi
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
openai.api_key = os.getenv("API_KEY")

app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this based on your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
def chat_gpt_handler(user_data: dict):
    prompt = user_data.get("prompt")

    if prompt is None:
        return {
            "error": "Please, send your prompt"
        }

    response = openai.Completion.create(
        prompt=prompt,
        model="ada:ft-personal-2023-06-14-18-36-54",
        temperature=0.1,
        frequency_penalty=1.6,
        max_tokens=80,
    )

    return {
        "answer": response['choices'][0]['text'],
    }
