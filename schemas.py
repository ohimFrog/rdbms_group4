from pydantic import BaseModel
from typing import Optional, List

# Lang schemas


class LangBase(BaseModel):
    code: str
    name: str


class LangCreate(LangBase):
    pass


class Lang(LangBase):
    id: int

    class Config:
        from_attributes = True

# Company schemas


class CompanyBase(BaseModel):
    name: str


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int

    class Config:
        from_attributes = True

# Drug schemas


class DrugBase(BaseModel):
    product_name: str
    lang_id: Optional[int] = None
    company_id: Optional[int] = None
    effect: Optional[str] = None
    dosage: Optional[str] = None
    dprecaution: Optional[str] = None
    interaction: Optional[str] = None
    side_effect: Optional[str] = None
    storage: Optional[str] = None


class DrugCreate(DrugBase):
    pass


class Drug(DrugBase):
    id: int

    class Config:
        from_attributes = True

# User schemas


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True

# Feedback schemas


class FeedbackBase(BaseModel):
    drug_id: int
    user_name: Optional[str] = None
    comments: Optional[str] = None
    positive: Optional[bool] = None


class FeedbackCreate(FeedbackBase):
    pass


class Feedback(FeedbackBase):
    id: int

    class Config:
        from_attributes = True
