from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(prefix="/drugs", tags=["drugs"])


@router.post("/", response_model=schemas.Drug)
def create_drug(drug: schemas.DrugCreate, db: Session = Depends(get_db)):
    db_drug = models.Drug(**drug.model_dump())
    db.add(db_drug)
    db.commit()
    db.refresh(db_drug)
    return db_drug


@router.get("/", response_model=List[schemas.Drug])
def read_drugs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drugs = db.query(models.Drug).offset(skip).limit(limit).all()
    return drugs


@router.get("/{drug_id}", response_model=schemas.Drug)
def read_drug(drug_id: int, db: Session = Depends(get_db)):
    drug = db.query(models.Drug).filter(models.Drug.id == drug_id).first()
    if drug is None:
        raise HTTPException(status_code=404, detail="Drug not found")
    return drug


@router.get("/{drug_id}/feedback", response_model=List[schemas.Feedback])
def read_drug_feedback(drug_id: int, db: Session = Depends(get_db)):
    feedback = db.query(models.Feedback).filter(
        models.Feedback.drug_id == drug_id).all()
    return feedback
