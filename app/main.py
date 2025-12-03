from fastapi import FastAPI 
from routers import user, post, message 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(message.router)

origin = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"hello": "world"}