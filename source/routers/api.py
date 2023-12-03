from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["API"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_hello():
    return {"message": "Hello World"}
