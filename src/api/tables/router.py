from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

from services.tables import TablesService
from schemas.tables import TableSchemaAdd, TableSchema


router = APIRouter()


@router.get("/", summary="Список всех столиков", response_model=List[TableSchema])
async def get_tables(session : AsyncSession = Depends(get_async_session)):
    """
    Получить все столики, находящиеся в БД.
    """
    return await TablesService().get_tables(session)

@router.post("/", summary="Создать новый столик")
async def get_tables(table: TableSchemaAdd, session : AsyncSession = Depends(get_async_session)):
    """
    Добавить новый столик в БД.
    """
    return await TablesService().add_table(table, session)

@router.delete("/{id}", summary="Удалить столик")
async def get_tables(id: int, session : AsyncSession = Depends(get_async_session)):
    """
    Удалить столик с указанным id из БД.

    - **id**: id столика
    """
    return await TablesService().delete_table(id, session)