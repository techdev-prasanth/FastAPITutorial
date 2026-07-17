from fastapi import FastAPI , Depends

app = FastAPI()
from database import session, engine , get_db , Base
from models import User
from pydantic_models import CreateUser , ResponseUser
from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)


@app.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    try:
        users = db.query(User).all()
        return {
            "message":"Fetched all data",
            "data":users
        }
    except:
        return {
            "message":"Fetched all data",
            "data":[]
        }


@app.post("/users",response_model=ResponseUser)
def create_users(user: CreateUser, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        full_name=user.full_name,
        phone=user.phone,
        is_active=user.is_active
    )
    print("----------")
    print(new_user)
    print(user)
    print("----------")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.get("/users/{id}/")
def get_user(id: int ,  db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()
    return user


@app.put("/users/{id}")
def update_user(id:int,user_update: CreateUser, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).update(
        user_update.model_dump()
    )

    db.commit()
    return {
        "messages":"updated",
    }        


@app.delete("/users/{id}")
def delete_user(id:int,db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()
    db.delete(user)
    db.commit()
    return {
        "message":"deleted successfully"
    }