from fastapi import FastAPI, Request
from mockData import products 
from dtos import ProductDTO

app = FastAPI()


@app.get("/") # get is the http method 
def home():
  return "Welcome to fastapi tutorial"

@app.get("/connect")
def contact():
  return "You can connect us any time on this email id"

# Chap1: path and querry parameters

@app.get("/products")
def get_products():
  return products

# Path params
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
  # if product avaialable with the id, return product else return error message
  for oneProduct in products:
    if oneProduct.get("id") == product_id:
      return oneProduct
    

  return {
    "error": "Product not found"
  }

# Querry params
# @app.get("/greet")
# def greet_user(name:str, age:int):
#   return {
#     "greet": f"Hello {name}, you are {age} years old!"
#   }


@app.get("/greet")
def greet_user(request: Request):
  name = request.query_params.get("name")
  age = request.query_params.get("age")
  query_params = dict(request.query_params)
  print(query_params)
  return {
    "greet": f"Hello {name}, you are {age} years old!"
  }

# we can send data to the servr in an api
# 1. body 2. headers (request headers) 3. query params 

# different http methods
@app.post("/create_product")
def create_product(product_data: ProductDTO):
  product_data = product_data.model_dump()  # pydantic is a module which can imlement data validation
   # this model dump helps to convert the data into dictionary format
  products.append(product_data)

  return {"status": "Product created successfully", "data": product_data}

# update product
@app.put("/update_product/{product_id}")
def update_product(product_data: ProductDTO, product_id:int):
  for index, oneProduct in enumerate(products):
    if oneProduct.get("id") == product_id:
      products[index] = product_data.model_dump()
      return {"status": "Product updated successfully", "product": product_data}

  return {
    "status": "Product not found"
  }

# delete

@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):

  for index, oneProduct in enumerate(products):
    if oneProduct.get("id") == product_id:
      deleted_product = products.pop(index)
      return {
        "status": "product deleted successfully",
        "deleted_product": deleted_product
      }

  return {
    "status": "Product not found"
  }

# How to call different http methods - Any Tool (postman)




# How to validate data. -> DTOS (Data transfer object)


