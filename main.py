from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

# @app.get("/")
# def get_func():
#     return {
#         "data": "Hello World"
#     }

# ===========================================post data======================
# class Item(BaseModel):
#     name: str
#     age: int
#     city: str
# @app.post("/data")
# def add_data(mydata:Item):
#     return{
#         "name": mydata.name,
#         "age": mydata.age,
#         "city": mydata.city
#     }

# =======================================delete data=============================

# @app.delete("/data{item_id}")
# def del_func(item_id:int):
#     return{
#         "item_id": f"your id no.{item_id} is deleted"
#     }
    
    
# ===================================updata==================================
# class update(BaseModel):
#     name: str
#     age: int


# @app.put("/update/{id}")
# def update_func(id:int, data: update):
#     return{
#         "id": id,
#         "name": data
#     }
    