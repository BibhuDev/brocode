from fastapi import FastAPI
from . import schema

app= FastAPI()



@app.post('/blog')
def create(req: schema.Blog):
    return req 