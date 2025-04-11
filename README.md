> REST API для бронирования столиков в ресторане. Сервис позволяет создавать, просматривать 
> и удалять брони, а также управлять столиками и временными слотами.

# Документация по развертыванию сервиса

- Проверить .env файл, настроить под себя.

- Зайти в папку проекта, написать следующую команду:
```sh
docker-compose up -d
```

# Swagger docs url

`localhost/docs`

# Endpoints

## Table
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`table` | GET | READ | Список всех столиков
`table`| POST | CREATE | Создать новый столик
`table/{id}` | DELETE | DELETE | Удалить столик

### Reservation
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`reservation` | GET | READ | Список всех броней
`reservation`| POST | CREATE | Создать новую бронь
`reservation/{id}` | DELETE | DELETE | Удалить бронь


