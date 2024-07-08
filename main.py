from fastapi import FastAPI
import uvicorn
from app.posts.router import router as posts_router
from fastapi_pagination import add_pagination


app = FastAPI()
app.include_router(posts_router)
add_pagination(app)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)