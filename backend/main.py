from fastapi import FastAPI
import uuid

app = FastAPI()

@app.post("/{post}")
def make_post(post: str):
    post_id = uuid.uuid1()

    Post = post
    Post_id = post_id
    return {"post": Post, "post_id": Post_id}
