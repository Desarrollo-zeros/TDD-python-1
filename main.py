from fastapi import FastAPI

app = FastAPI()

@app.get("/IsPrime/{number}")
async def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            return False
    return True
