from datetime import timedelta
from schemas.reservations import ReservationSchema, ReservationSchemaAdd
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from sqlalchemy import insert, select, delete
from models.models import Reservation

from fastapi import Depends, HTTPException

class ReservationsService:
    async def get_reservations(self, session : AsyncSession = Depends(get_async_session)):
        """
        Возвращает все брони из БД.
        """
        query = select(Reservation)
        result = await session.execute(query)
        return result.scalars().all()
    
    async def add_reservation(self, reservation: ReservationSchemaAdd, session : AsyncSession = Depends(get_async_session)):
        """
        Добавление новой брони в БД. Проверяет, можно ли забронировать столик на указанное время.

        """
        # reservation_data = reservation.model_dump()
        
        #   Проверяем, можно ли создать бронь в указанное время
        if await self.check_reservation_time(reservation.model_dump(), session):
            query_insert = insert(Reservation).values(**reservation.model_dump())
            await session.execute(query_insert)
            await session.commit()
            return {"status": "success"}
        else:
            return {"error": "Невозможно забронировать столик, пересечение по дате и времени с другой бронью"}
    
    async def check_reservation_time(self, reservation_data, session: AsyncSession):
        """
        Проверка на доступность столика в указанное время

        -**reservation_data**: dict данных (model_dump());
        
        -**session**
        """
        #   Получаем все брони на указанный столик
        query = select(Reservation).where(Reservation.table_id == reservation_data['table_id'])
        result = await session.execute(query)
        reservations = result.scalars().all()

        #   Переменные с новой датой брони и её окончанием
        new_start = reservation_data['reservation_time']
        new_end = new_start + timedelta(minutes=reservation_data['duration_minutes'])

        #   Проверяем, доступен ли столик
        for r in reservations:
            existing_start = r.reservation_time
            existing_end = r.reservation_time + timedelta(minutes=r.duration_minutes)
            
            if new_start < existing_end and existing_start < new_end:
                print(f"Невозможно создать бронь, есть столик: {existing_start} - {existing_end}")
                return False
        return True

    async def delete_reservation(self, id: int, session : AsyncSession = Depends(get_async_session)):
        """
        Удаляет бронь из БД по id.

        -**id**: id брони
        """
        query = delete(Reservation).where(Reservation.id == id)
        result = await session.execute(query)
        await session.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Бронь не найдена")
        return {"status": "success"}
