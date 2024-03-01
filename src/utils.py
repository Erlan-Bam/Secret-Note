from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def check_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def hash_id(text: str, password: str) -> str:
    return pwd_context.hash(text+password)