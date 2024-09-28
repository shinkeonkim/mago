# Mago

## DB Migration

> alembic revision -m "이름"
> docker-compose exec mago_app alembic upgrade head
> docker-compose exec mago_app alembic downgrade -1
