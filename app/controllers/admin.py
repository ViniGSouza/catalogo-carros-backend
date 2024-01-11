from fastapi import APIRouter, HTTPException
from app.services.admin_service import create_admin

router = APIRouter()

@router.post("/create-user")
async def create_admin_endpoint(username: str, password: str):
    try:
        create_admin(username, password)
        return {"message": "Admin criado com sucesso"}
    except HTTPException as err:
        return err
