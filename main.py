from typing import Union
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
mongo_connection_string = ""
client = MongoClient(mongo_connection_string)

db = client["Notes"]
collection = db["mynotes"]
@app.get("/",response_class=HTMLResponse)
def home_page(request:Request):
    result = collection.find({})
    newdoc = []
    for results in result:
        newdoc.append({
            "id": results["_id"],
            "note": results["note"]
        })
    print(result)
    return templates.TemplateResponse("index.html", {"request": request,"newdoc": newdoc})