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

## Tables
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`tables` | GET | READ | Список всех столиков
`tables`| POST | CREATE | Создать новый столик
`tables/{id}` | DELETE | DELETE | Удалить столик

### Reservations
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`reservations` | GET | READ | Список всех броней
`reservations`| POST | CREATE | Создать новую бронь
`reservations/{id}` | DELETE | DELETE | Удалить бронь


