from fastapi import FastAPI

app = FastAPI()

names: list= ['sabih', 'ali']

# @app.get("/")
# def data():
#     return names



# @app.post("/names")
# def add_name(name:str):
#     names.append(name)
#     return names

# @app.delete("/names/{name}")
# def del_name(name:str):
#     names.remove(name)
#     return names
    
# @app.put("/names/{index}")
# def update(index:int,name:str):
#     names[index]=name
#     return names
    
    
    
    
    
    
    

@app.get("/")
def data():
    return names

@app.post("/myname")
def add_data(data:str):
    names.append(data)
    return names


@app.delete("/myname/{index}")
def del_finc(index:int):
    names.pop(index)
    return names

@app.put("/myname/{index}")
def update(index:int):
    names[index]= "ascdfer"
    return names

    