from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

@app.get("/compute")
def compute():
    start = time.time()
    total = sum(i * i for i in range(1000000))
    elapsed = time.time() - start
    return {
        "result": total,
        "time": elapsed
    }
