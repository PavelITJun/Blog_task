from fastapi import APIRouter, Query
from fastapi_pagination import Page, paginate
from app.posts.schemas import SPutPost, SPost
from app.posts.dao import PostDAO


router = APIRouter(
    prefix='/posts',
    tags=['posts'],
)


# @router.get("/posts/search")
# async def find_by_substr(substr: str = Query(None, min_length=3)):
#     return await PostDAO.find_posts_by_substr(substr)


# GET /posts: Возвращает список всех сообщений блога.
@router.get('/', response_model=Page[SPost])
async def get_all_messages():
    result = await PostDAO.find_all()
    return paginate(result)


# GET /posts/{id}: Возвращает одну запись блога по идентификатору.
@router.get('/{id}', response_model=SPost)
async def get_post_by_id(id: int):
    return await PostDAO.find_by_id(id)


# POST /posts: Создать новую запись в блоге.
@router.post("/", response_model=SPost)
async def create_post(post: SPost):
    return await PostDAO.create_new_post(post)


# PUT /posts/{id}: Обновить существующую запись в блоге.
@router.put('/{id}')
async def update_note_by_id(id: int, post_update: SPutPost):
    return await PostDAO.update_post_by_id(id, post_update)


# DELETE /posts/{id}: Удалить запись в блоге.
@router.delete('/{id}')
async def delete_post_by_id(id: int):
    return await PostDAO.delete_by_id(id)
    