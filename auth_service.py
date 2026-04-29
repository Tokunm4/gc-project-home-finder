

import hashlib
import random
import string
from datetime import datetime, timedelta
from typing import Optional, Dict
from models import User




class AuthService:
    

    TOKEN_EXPIRY_SECONDS = 30  


    def __init__(self):
       
        self._users: Dict[str, User] = {}       
        self._tokens: Dict[str, dict] = {}     
        self._active_sessions: Dict[int, str] = {}  


    
    def hash_password(password: str) -> str:
       
        return hashlib.sha256(password.encode()).hexdigest()


    def register(self, name: str, email: str, password: str) -> User:
        
        if email in self._users:
            raise ValueError('Email already registered.')
        user_id = len(self._users) + 1
        user = User(user_id, name, email, self.hash_password(password))
        self._users[email] = user
        return user


    def validate_password(self, email: str, password: str) -> bool:
       
        user = self._users.get(email)
        if not user:
            return False
        return user.password_hash == self.hash_password(password)


    def generate_2fa_token(self, email: str) -> str:
        
        token = ''.join(random.choices(string.digits, k=6))
        expiry = datetime.now() + timedelta(seconds=self.TOKEN_EXPIRY_SECONDS)
        self._tokens[email] = {'token': token, 'expiry': expiry}
       
        return token


    def validate_2fa_token(self, email: str, token: str) -> bool:
        
        stored = self._tokens.get(email)
        if not stored:
            return False
        if datetime.now() > stored['expiry']:
            return False  # Token expired
        return stored['token'] == token


    def enforce_one_session(self, user_id: int, session_token: str):
        
        self._active_sessions[user_id] = session_token


    def login(self, email: str, password: str, token: str) -> Optional[str]:
       
        if not self.validate_password(email, password):
            return None
        if not self.validate_2fa_token(email, token):
            return None
        user = self._users[email]
        session_token = self.hash_password(email + str(datetime.now()))
        self.enforce_one_session(user.user_id, session_token)
        user.session_token = session_token
        return session_token



