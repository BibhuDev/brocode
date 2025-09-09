from fastapi import FastAPI
import schema

app= FastAPI()

@app.post('/')
def create(req: schema.Blog):
    return req



