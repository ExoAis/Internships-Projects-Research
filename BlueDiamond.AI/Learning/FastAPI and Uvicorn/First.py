from fastapi import FastAPI
from pydantic import BaseModel
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["E-Commerce"]
mycustomers = mydb["Customers"]

app = FastAPI()

class Customer(BaseModel):
    Email: str
    Address: str
    Avatar: str
    Session_Length: float
    Time_on_App: float
    Time_on_Website: float
    Length_of_Membership: float
    Yearly_Amount_Spent: float

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/customer")
def getID(customer: Customer):
    mycustomers.insert_one(customer.dict())
    return customer
