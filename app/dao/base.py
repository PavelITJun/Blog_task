from fastapi import HTTPException
from app.posts.models import Posts
from app.posts.schemas import SPost
from app.database import async_session_maker
from sqlalchemy import delete, select
from sqlalchemy.exc import NoResultFound



class BaseDAO:
    model = None


    @classmethod
    async def delete_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(cls.model).where(cls.model.id==id)
            after_query = await session.execute(query)

            try:
                item = after_query.scalar_one()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="Post isn't found")
            
            query = delete(cls.model).where(cls.model.id==id)
            await session.execute(query)
            await session.commit()
            return item


    @classmethod
    async def find_by_id(cls, post_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=post_id)
            after_query = await session.execute(query)
            try:
                item = after_query.scalar_one()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="Post isn't found")
            return item
        
    
    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            after_query = await session.execute(query)
            try:
                items = after_query.mappings().all()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="Posts aren't found")
            return items
        