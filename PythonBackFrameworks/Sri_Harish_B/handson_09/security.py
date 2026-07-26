from datetime import timedelta
from datetime import datetime
from passlib.context import CryptContext
from jose import jwt,JWTError

# bcrypt context used to hash and verify user passwords (never store plaintext)
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_password_hash(password:str) -> str:
    # One-way hash — the raw password is never persisted, only this hash.
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str) -> bool:
    # Compares a login attempt against the stored hash without ever decrypting it.
    return pwd_context.verify(plain_password,hashed_password)

# JWT signing config.
# NOTE: SECRET_KEY is hard-coded here for hands-on/demo purposes only —
# in a real deployment this must come from an environment variable / secrets manager.
SECRET_KEY = "aufbyvgfyvyiVFLIVvwRv@YRv2yrv2FVFVfVGYVyfvHKFVYfv2qyVR1EV1828RH3U7T48TurfHVDS48407E8WQ45E6R"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    # Build the token payload (e.g. {"sub": user_email}) and attach an expiry claim.
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp":expire})

    # Sign the payload with our secret so the server can later verify it wasn't tampered with.
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def decode_access_token(token:str):
    # Validates the token's signature and expiry, then extracts the user identity ("sub").
    # Any failure (bad signature, expired, malformed) is treated as "not authenticated".
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str = payload.get("sub")
        if email is None:
            return None
        return email
    except JWTError:
        return None
