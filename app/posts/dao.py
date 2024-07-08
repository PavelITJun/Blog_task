from datetime import datetime, timezone
from fastapi import HTTPException, Query
from app.posts.schemas import SPutPost
from app.posts.models import Posts
from app.dao.base import *
from sqlalchemy.exc import NoResultFound
# from sqlalchemy_searchable import search


class PostDAO(BaseDAO):
    model = Posts

    # @classmethod
    # async def find_posts_by_substr(cls, substr):
    #     async with async_session_maker() as session:
    #         if substr is None:
    #             raise HTTPException(status_code=400, detail="Query parameter is required")
    #         query = select(cls.model)
    #         search_query = search(query, substr)
    #         posts = await session.execute(search_query)
    #         return posts.scalars().all()


    @classmethod
    async def update_post_by_id(cls, id: int, post_update: SPutPost):
        update_data = post_update.__dict__
        async with async_session_maker() as session:
            query = select(cls.model).where(cls.model.id == id)
            after_query = await session.execute(query)

            try:
                post = after_query.scalar_one()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="Post isn't found")

            for key, value in update_data.items():
                setattr(post, key, value)
            
            session.add(post)
            await session.commit()
            return post


    @classmethod
    async def create_new_post(cls, post: SPost):
        post = Posts(**post.__dict__)
        async with async_session_maker() as session:
            session.add(post)
            await session.commit()
            await session.refresh(post)
        return post
    