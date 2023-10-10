from fastapi import FastAPI
from typing import Optional
#request body model
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data' : f'{limit} published blogs from the db'}
    else:
        return {'data' : f'{limit} unpublished blogs from the db: {sort}'}

    

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'app unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    #fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    #fetch blog with id = id
    return limit

class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool] = False

@app.post('/blog')
def create_blog(blog: Blog):
    return({'data': f"Blog is created with title as {blog.title}"})