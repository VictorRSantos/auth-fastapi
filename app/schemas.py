import re
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    
    def validate_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError("Username format invalid")
        return value
