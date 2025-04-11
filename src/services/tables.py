from schemas.tables import TableSchemaAdd
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from sqlalchemy import insert, select, delete
from models.models import Table

from fastapi import Depends, HTTPException


class TablesService:
    async def get_tables(self, session : AsyncSession = Depends(get_async_session)):
        """
        Возвращает все столики из БД.
        """
        query = select(Table)
        result = await session.execute(query)
        return result.scalars().all()
    
    async def add_table(self, table: TableSchemaAdd, session : AsyncSession = Depends(get_async_session)):
        """
        Добавление нового столика в БД.

        -**table** - схема столика
        """
        query = insert(Table).values(**table.model_dump())
        await session.execute(query)
        await session.commit()
        return {"status": "success"}

    async def delete_table(self, id: int, session : AsyncSession = Depends(get_async_session)):
        """
        Удаляет столик из БД по id.

        -**id**: id столика, который нужно удалить
        """
        query = delete(Table).where(Table.id == id)
        result = await session.execute(query)
        await session.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Столик не найден")
        
        return {"status": "success"}
    