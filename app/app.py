from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate 

app = FastAPI()

text_posts = {
    1: {
        "title":"New Post",
        "content":"Cool testi post"
    },
    2: {
        "title":"Another Post",
        "content":"This is another cool post."
    },
    3: {
        "title":"Third Post",
        "content":"Content for the third post."
    },
    4: {
        "title":"Fourth Post",
        "content":"Yet another interesting post."
    },
    5: {
        "title":"Fifth Post",
        "content":"The fifth post's content."
    },
    6: {
        "title":"Sixth Post",
        "content":"More content for the sixth post."
    },
    7: {
        "title":"Seventh Post",
        "content":"A post about nothing in particular."
    },
    8: {
        "title":"Eighth Post",
        "content":"This is the eighth post."
    },
    9: {
        "title":"Ninth Post",
        "content":"Content for the ninth entry."
    },
    10: {
        "title":"Tenth Post",
        "content":"The final post in this set."
    }
}
@app.get("/posts")
def get_posts(limit:int = None):
    if limit: 
            return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{post_id}")
def get_post(post_id: int) -> PostCreate:
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(post_id)  

@app.post("/posts")
def create_post(post: PostCreate) -> PostCreate: 
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post 
    return new_post



