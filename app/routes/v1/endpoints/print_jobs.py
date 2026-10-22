from fastapi import APIRouter, Depends
# from app.services import print_job_service
# from app.schemas.author_schemas import AuthorCreate, AuthorUpdate, AuthorResponse
from app.core.session import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/print_job", tags=["Print Jobs"])