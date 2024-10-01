from fastapi import FastAPI
from backend.routes import router
from backend.db import MysqlConnector

MysqlConnector._create_database()
connector = MysqlConnector()
connector._create_table()

app = FastAPI()
app.include_router(router)
