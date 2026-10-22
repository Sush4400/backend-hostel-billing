from fastapi import APIRouter, Depends
from app.services import auth_service
# from app.schemas.author_schemas import AuthorCreate, AuthorUpdate, AuthorResponse
from app.core.session import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/auth", tags=["Auth"])