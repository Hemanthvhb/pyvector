from contextlib import asynccontextmanager
from fastapi import FastAPI
from math_engine import euclidean_dist, cosine_similarity
from kdtree import build, search, insert
from models import InsertRequest, SearchRequest, SearchResponse
import asyncio
import uvicorn

@asynccontextmanager
async def lifespan(app):
    app.state.tree=build([])
    app.state.cache = {}
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/insert")
async def insert_vector(request: InsertRequest):
    app.state.tree = insert(app.state.tree, request.vector, request.payload)
    app.state.cache.clear()
    return {"message": "vector inserted successfully"}

@app.post("/search")
async def search_vector(request: SearchRequest):
    cache_key=tuple(request.vector)
    if cache_key in app.state.cache:
        return app.state.cache[cache_key]

    result= await asyncio.to_thread(search,app.state.tree,request.vector)

    if result is None:
        return { "message":"no vectors in the database yet"}
    
    response=SearchResponse(payload=result[1],distance=result[0])

    app.state.cache[cache_key]=response

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)