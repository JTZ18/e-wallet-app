## Required Python third-party packages
```python
"""
fastapi==0.63.0
sqlalchemy==1.3.23
pydantic==1.8.1
asyncio==3.4.3
websockets==8.1
stripe==2.55.0
pytest==6.2.2
tox==3.23.0
docker==4.4.4
kubernetes==12.0.1
flower==0.9.7
sentry-sdk==1.0.0
redis==3.5.3
celery==5.0.5
mkdocs==1.1.2
bcrypt==3.2.0
"""
```

## Required Other language third-party packages
```python
"""
No third-party packages required in other languages.
"""
```

## Full API spec
```python
"""
openapi: 3.0.0
info:
  title: Secure eWallet API
  version: 1.0.0
paths:
  /users:
    post:
      summary: Create a new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
      responses:
        '200':
          description: User created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
  /wallets:
    post:
      summary: Create a new wallet
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wallet'
      responses:
        '200':
          description: Wallet created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wallet'
  /transactions:
    post:
      summary: Create a new transaction
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Transaction'
      responses:
        '200':
          description: Transaction created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Transaction'
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        email:
          type: string
        password:
          type: string
        first_name:
          type: string
        last_name:
          type: string
        phone_number:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        is_active:
          type: boolean
        is_superuser:
          type: boolean
    Wallet:
      type: object
      properties:
        id:
          type: integer
        user_id:
          type: integer
        balance:
          type: number
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
    Transaction:
      type: object
      properties:
        id:
          type: integer
        sender_wallet_id:
          type: integer
        receiver_wallet_id:
          type: integer
        amount:
          type: number
        created_at:
          type: string
          format: date-time
"""
```

## Logic Analysis
```python
[
    ("main.py", "Contains the main entry point for the application. Initializes FastAPI application and includes routers."),
    ("models.py", "Contains SQLAlchemy models for User, Wallet and Transaction."),
    ("schemas.py", "Contains Pydantic models for User, Wallet and Transaction."),
    ("routers.py", "Contains FastAPI routers for User, Wallet and Transaction."),
    ("tests.py", "Contains PyTest tests for all the APIs."),
    ("config.py", "Contains configuration variables for the application."),
    ("auth.py", "Contains authentication related utilities."),
    ("utils.py", "Contains utility functions."),
    ("database.py", "Contains database connection and session management utilities."),
    ("exceptions.py", "Contains custom exceptions."),
    ("middlewares.py", "Contains custom middlewares."),
    ("tasks.py", "Contains Celery tasks.")
]
```

## Task list
```python
[
    "config.py",
    "database.py",
    "models.py",
    "schemas.py",
    "auth.py",
    "utils.py",
    "exceptions.py",
    "middlewares.py",
    "routers.py",
    "tasks.py",
    "tests.py",
    "main.py"
]
```

## Shared Knowledge
```python
"""
'config.py' contains configuration variables for the application. These variables are loaded from environment variables and have default values.

'database.py' contains utilities for connecting to the database and managing database sessions. It uses SQLAlchemy for ORM.

'auth.py' contains utilities for handling user authentication. It uses bcrypt for password hashing.

'utils.py' contains utility functions that can be used throughout the application.

'middlewares.py' contains custom middlewares. Middlewares are used to process requests and responses globally before they reach route handlers or after they leave route handlers.

'tasks.py' contains Celery tasks. These tasks are asynchronous and can be used for long running operations.
"""
```

## Anything UNCLEAR
The requirement is clear to me.