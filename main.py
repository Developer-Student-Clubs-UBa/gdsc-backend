from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

import models
from database import Base, engine, SessionLocal
from fastapi import FastAPI
import schemas

app = FastAPI()

app = FastAPI()

fake_database = {
    1: {'task': 'clean the house'},
    2: {'task': 'cook dinner'},
    3: {'task': 'go to the gym'},
    4: {'task': 'go to the supermarket'},
}

Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# @app.get("/")
# def getItems(session: Session = Depends(get_session)):
#     items = session.query(models.Item).all()
#     return items
#
#
# @app.get("/get/{id}")
# def getItem(id: int, session: Session = Depends(get_session)):
#     item = session.query(models.Item).get(id)
#     return item
#
#
# @app.post("/addUser")
# def addItem(item: schemas.Item, session: Session = Depends(get_session)):
#     item = models.Item(task=item.task)
#     session.add(item)
#     session.commit()
#     session.refresh(item)
#     return item
#
#
# @app.put("/update/{id}")
# def updateItem(id: int, item: schemas.Item, session: Session = Depends(get_session)):
#     item_obj = session.query(models.Item).get(id)
#     item_obj.task = item.task
#     session.commit()
#     session.refresh(item_obj)
#     return item_obj
#
#
# @app.delete("/delete/{id}")
# def deleteItem(item_id: int, session: Session = Depends(get_session)):
#     itemObject = session.query(models.Item).get(item_id)
#     session.delete(itemObject)
#     session.commit()
#     session.close()
#     return f'Item was {item_id} deleted -- {itemObject.task}'


@app.get("/getAllUsers")
def getUsers(session: Session = Depends(get_session)):
    users = session.query(models.User).all()
    return users


@app.get("/getUser/{id}")
def getUser(user_id, session: Session = Depends(get_session)):
    user = session.query(models.User).get(user_id)
    return user


@app.post("/addUser")
def addUser(user: schemas.User, session: Session = Depends(get_session)):
    user = models.User(name=user.name, email=user.email, password=user.password, username=user.username,
                       avatar_link=user.avatar_link, bio=user.bio)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.put("/updateUser/{id}")
def updateUser(user_id: int, user: schemas.User, session: Session = Depends(get_session)):
    user_obj = session.query(models.User).get(user_id)
    for key, value in user.dict().items():
        if value:
            setattr(user_obj, key, value)
    session.commit()
    session.refresh(user_obj)
    return user_obj
