from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Lang(Base):
    __tablename__ = "lang"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10), nullable=False)
    name = Column(String(100), nullable=False)

    drugs = relationship("Drug", back_populates="language")


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    drugs = relationship("Drug", back_populates="company")


class Drug(Base):
    __tablename__ = "drug"

    id = Column(Integer, primary_key=True, index=True)
    lang_id = Column(Integer, ForeignKey("lang.id"))
    product_name = Column(String(700), nullable=False)
    company_id = Column(Integer, ForeignKey("company.id"))
    effect = Column(String(500))
    dosage = Column(String(1000))
    dprecaution = Column(String(1500))
    interaction = Column(String(1000))
    side_effect = Column(String(1200))
    storage = Column(String(300))

    language = relationship("Lang", back_populates="drugs")
    company = relationship("Company", back_populates="drugs")
    feedbacks = relationship("Feedback", back_populates="drug")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    drug_id = Column(Integer, ForeignKey("drug.id"))
    user_name = Column(String(255))
    comments = Column(Text)
    positive = Column(Boolean)

    drug = relationship("Drug", back_populates="feedbacks")
