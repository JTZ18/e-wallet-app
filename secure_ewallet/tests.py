## tests.py
import pytest
from fastapi.testclient import TestClient
from secure_ewallet.main import app
from secure_ewallet.schemas import UserCreate, WalletCreate, TransactionCreate
from secure_ewallet.models import User, Wallet, Transaction
from sqlalchemy.orm import Session
from secure_ewallet.database import SessionLocal, engine
from secure_ewallet.utils import get_user_by_email
from secure_ewallet.auth import authenticate_user, create_access_token

client = TestClient(app)

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    Base.metadata.drop_all(bind=engine)

def test_create_user(db: Session):
    user = UserCreate(email="test@example.com", password="password", first_name="Test", last_name="User", phone_number="1234567890")
    response = client.post("/users", json=user.dict())
    assert response.status_code == 201
    db_user = get_user_by_email(db, user.email)
    assert db_user is not None

def test_authenticate_user(db: Session):
    user = UserCreate(email="test@example.com", password="password", first_name="Test", last_name="User", phone_number="1234567890")
    response = client.post("/users", json=user.dict())
    assert response.status_code == 201
    db_user = authenticate_user(db, user.email, user.password)
    assert db_user is not None

def test_create_access_token(db: Session):
    user = UserCreate(email="test@example.com", password="password", first_name="Test", last_name="User", phone_number="1234567890")
    response = client.post("/users", json=user.dict())
    assert response.status_code == 201
    db_user = authenticate_user(db, user.email, user.password)
    assert db_user is not None
    access_token = create_access_token(data={"sub": db_user.email})
    assert access_token is not None

def test_create_wallet(db: Session):
    user = UserCreate(email="test@example.com", password="password", first_name="Test", last_name="User", phone_number="1234567890")
    response = client.post("/users", json=user.dict())
    assert response.status_code == 201
    db_user = get_user_by_email(db, user.email)
    assert db_user is not None
    wallet = WalletCreate(user_id=db_user.id)
    response = client.post("/wallets", json=wallet.dict())
    assert response.status_code == 201
    db_wallet = db.query(Wallet).filter(Wallet.user_id == db_user.id).first()
    assert db_wallet is not None

def test_create_transaction(db: Session):
    user1 = UserCreate(email="test1@example.com", password="password", first_name="Test", last_name="User", phone_number="1234567890")
    response = client.post("/users", json=user1.dict())
    assert response.status_code == 201
    db_user1 = get_user_by_email(db, user1.email)
    assert db_user1 is not None
    wallet1 = WalletCreate(user_id=db_user1.id)
    response = client.post("/wallets", json=wallet1.dict())
    assert response.status_code == 201
    db_wallet1 = db.query(Wallet).filter(Wallet.user_id == db_user1.id).first()
    assert db_wallet1 is not None

    user2 = UserCreate(email="test2@example.com", password="password", first_name="Test", last_name="User", phone_number="1234567890")
    response = client.post("/users", json=user2.dict())
    assert response.status_code == 201
    db_user2 = get_user_by_email(db, user2.email)
    assert db_user2 is not None
    wallet2 = WalletCreate(user_id=db_user2.id)
    response = client.post("/wallets", json=wallet2.dict())
    assert response.status_code == 201
    db_wallet2 = db.query(Wallet).filter(Wallet.user_id == db_user2.id).first()
    assert db_wallet2 is not None

    transaction = TransactionCreate(sender_wallet_id=db_wallet1.id, receiver_wallet_id=db_wallet2.id, amount=100)
    response = client.post("/transactions", json=transaction.dict())
    assert response.status_code == 201
    db_transaction = db.query(Transaction).filter(Transaction.sender_wallet_id == db_wallet1.id, Transaction.receiver_wallet_id == db_wallet2.id).first()
    assert db_transaction is not None
