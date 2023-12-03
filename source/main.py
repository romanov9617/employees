from routers.api import router

from fastapi import FastAPI

app = FastAPI(
    title="EmployeeTreeAPI",
)

app.include_router(router)
