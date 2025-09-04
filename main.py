from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}
