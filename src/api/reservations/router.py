from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

from services.reservations import ReservationsService
from schemas.reservations import ReservationSchema, ReservationSchemaAdd


router = APIRouter()

@router.get("/", summary="Список всех броней", response_model=List[ReservationSchema])
async def get_tables(session : AsyncSession = Depends(get_async_session)):
    """
    Получить все брони, находящиеся в БД.
    """
    return await ReservationsService().get_reservations(session)

@router.post("/", summary="Создать новую бронь")
async def get_tables(reservation: ReservationSchemaAdd, session : AsyncSession = Depends(get_async_session)):
    """
    Добавить новую бронь в БД.
    """
    return await ReservationsService().add_reservation(reservation, session)

@router.delete("/{id}", summary="Удалить бронь")
async def get_tables(id: int, session : AsyncSession = Depends(get_async_session)):
    """
    Удалить бронь с указанным id из БД.

    - **id**: id брони
    """
    return await ReservationsService().delete_reservation(id, session)