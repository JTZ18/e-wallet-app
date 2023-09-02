## tasks.py
from celery import Celery
from secure_ewallet.config import settings
from secure_ewallet.utils import update_wallet_balance
from secure_ewallet.exceptions import WalletNotFoundException
from sqlalchemy.orm import Session

celery_app = Celery("tasks", broker=settings.CELERY_BROKER_URL)

@celery_app.task
def update_wallet_balance_task(wallet_id: int, amount: float, transaction_type: str, db: Session):
    try:
        update_wallet_balance(db, wallet_id, amount, transaction_type)
    except WalletNotFoundException as e:
        print(f"Error: {e.detail}")
