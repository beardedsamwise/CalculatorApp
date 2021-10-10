from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/multiply/")
def multiply(num1: int, num2: int):
    total = num1 * num2
    return {"total": total}

