from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

names: list= ['sabih', 'ali']

class NameRequest(BaseModel):
    data:str

@app.get("/")
def data():
    return names



@app.post("/names")
def add_name(request: NameRequest):
    names.append(request.data)
    return names

# ======================================delete=============

@app.delete("/names/{index}")
def del_name(index:int):
    names.pop(index)
    return names
 
 
#  =================================updatw data================
@app.put("/names/{index}")
def update(index:int, request:NameRequest):
    names[index]= request.data
    return names
    
    
    
    
    
    
    


    