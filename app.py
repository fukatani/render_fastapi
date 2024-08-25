from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Instantiate the app.
app = FastAPI()

# Define a GET on the specified endpoint.
@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}
    
class Body(BaseModel):
    name: str
    item_id: int
    
@app.post("/exercise/{path}")
async def exercise_function(path: str, query: str, body: Body):
  return {"path": path, "query": query, "body": body}

@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}

class Data(BaseModel):
    feature_1: float
    feature_2: str

@app.post("/exercise_data/")
async def exercise_function(body: Data):
    if body.feature_1 < 0:
        raise HTTPException(status_code=404, detail="feature_1 must not be negative")
    if len(body.feature_2) > 128:
        raise HTTPException(status_code=404, detail="length of feature_2 must be smaller than 129")
    return {"feature_1": body.feature_1, "feature_2": body.feature_2}

