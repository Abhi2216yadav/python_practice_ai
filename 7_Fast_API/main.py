from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome" : "Kaise hai aap?"}

@app.get("/margin")
def margin(revenue: float, expences: float):
    profit = revenue - expences
    margin_persect = (profit / revenue) * 100
    return {"profit": profit, "margin_persect": margin_persect}

#what the user must sent us (the request body) 

class Review(BaseModel):
    text: str

#what gemini must give back, and what we send to the user(the responce)

class Sentiment(BaseModel):
    label: str # possitive / negetive
    score: int # 1 very bad / 5 very good

@app.post("/sentiment")
def analyzer_sentiment(review: Review):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=(
            "Find the sentimate of this customer review."
            "Lable must be 'positive', 'negetive', or 'natural'. "
            "score must be a number from 1 (very bad) to 5 (very good)."
            f"Review : {review.text}"
        ),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Sentiment,
        ),
    )

    return response.parsed