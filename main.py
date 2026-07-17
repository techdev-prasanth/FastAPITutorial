from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List
from models import Products
app = FastAPI()

from database import session,engine
import schemas

schemas.Base.metadata.create_all(bind=engine)


###

"""
Without Db
"""

###



@app.get("/")
def home():
    return {"message":"welcom"} 


@app.get("/name/")
def name():
    return {"message":"name is prasanth"} 



products = [
    Products(id=1,name="macbook",pku=111,desc="its laptop",price=100.22),
    Products(id=2,name="asus",pku=222,desc="its laptop",price=1100.22)
]
@app.get("/products")
def get_all_products():
    return products


@app.get("/products/{id}")
def get_all_products(id: int):
    for product in products:
        if product.id == id:
            return product
    return "No product"


@app.post("/products")
def add_product(product: Products):
    products.append(product)
    return product


@app.put("/products")
def update_product(id: int , product: Products):

    print("Produc",product)
    for items in range(len(products)):
        if products[items].id == id:
            products[items] = product 
            return "Added"
    
    return "No update No id"


@app.delete("/products")
def delete_product(id: int):

    for i in range(len(products)):
        if products[i].id == id:
            del products[i].id
            return "deleted success"
        
    return "Error, no deletd"



