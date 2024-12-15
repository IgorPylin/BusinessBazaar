# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from .models import UserType

class UserBase(BaseModel):
    email: EmailStr
    user_type: UserType

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class ProposalBase(BaseModel):
    title: str
    description: str
    price: float
    industry: str
    revenue: float
    profit: float
    employees_count: int
    location: str

class ProposalCreate(ProposalBase):
    seller_id: Optional[int] = None

class Proposal(ProposalBase):
    id: int
    seller_id: Optional[int]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
