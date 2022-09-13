from fastapi import Depends, APIRouter
from ..database import get_db
from sqlmodel import Session

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.get('/me')
def get_me(db: Session = Depends(get_db)):
    return {"user": "me"}