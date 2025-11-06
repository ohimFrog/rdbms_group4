from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(prefix="/languages", tags=["languages"])


@router.post("/", response_model=schemas.Lang)
def create_language(lang: schemas.LangCreate, db: Session = Depends(get_db)):
    db_lang = models.Lang(**lang.model_dump())
    db.add(db_lang)
    db.commit()
    db.refresh(db_lang)
    return db_lang


@router.get("/", response_model=List[schemas.Lang])
def read_languages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    languages = db.query(models.Lang).offset(skip).limit(limit).all()
    return languages


@router.get("/{lang_id}", response_model=schemas.Lang)
def read_language(lang_id: int, db: Session = Depends(get_db)):
    lang = db.query(models.Lang).filter(models.Lang.id == lang_id).first()
    if lang is None:
        raise HTTPException(status_code=404, detail="Language not found")
    return lang
