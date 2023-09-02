from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class WalletBase(BaseModel):
    user_id: int

class WalletCreate(WalletBase):
    pass

class Wallet(WalletBase):
    id: int
    balance: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    sender_wallet_id: int
    receiver_wallet_id: int
    amount: float

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
