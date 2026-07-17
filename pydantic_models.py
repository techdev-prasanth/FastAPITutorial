from pydantic import BaseModel, EmailStr ,StrictBool

class CreateUser(BaseModel):
    username : str
    email : EmailStr
    password : str
    full_name : str
    phone : int
    is_active : bool = True 


class ResponseUser(BaseModel):
    username : str
    email : EmailStr
    password : str
    full_name : str
    phone : int
    is_active : bool = True 