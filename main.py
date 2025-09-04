from fastapi import FastAPI
import random

app = FastAPI()

# List of random messages
MESSAGES = [
    "The future belongs to those who believe in the beauty of their dreams.",
    "It is during our darkest moments that we must focus to see the light.",
    "The only way to do great work is to love what you do.",
    "Innovation distinguishes between a leader and a follower.",
    "Your limitation—it's only your imagination.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn't just find you. You have to go out and get it.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Don't stop when you're tired. Stop when you're done."
]

@app.get("/hello")
def read_hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}

@app.get("/messages")
def get_random_message():
    return {"message": random.choice(MESSAGES)}
