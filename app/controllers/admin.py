from fastapi import APIRouter, HTTPException
from app.services.admin_service import create_admin
from app.models.user import CreateUser

router = APIRouter()

@router.post("/create-user")
async def create_admin_endpoint(user: CreateUser):
    try:
        create_admin(username=user.username, password=user.password)
        return {"message": "Admin criado com sucesso"}
    except HTTPException as err:
        return err
