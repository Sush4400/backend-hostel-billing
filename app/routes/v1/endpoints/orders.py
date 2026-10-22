from fastapi import APIRouter, Depends
from app.services import order_service
# from app.schemas.author_schemas import AuthorCreate, AuthorUpdate, AuthorResponse
from app.core.session import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/order", tags=["Orders"])