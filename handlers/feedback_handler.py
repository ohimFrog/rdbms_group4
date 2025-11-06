from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(prefix="/feedback", tags=["feedback"])


@router.post("/", response_model=schemas.Feedback)
def create_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = models.Feedback(**feedback.model_dump())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback


@router.get("/", response_model=List[schemas.Feedback])
def read_feedback(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    feedback = db.query(models.Feedback).offset(skip).limit(limit).all()
    return feedback
