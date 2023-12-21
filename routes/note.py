from fastapi import APIRouter,Form
from models.note import Note
from config.db import client
from schemas.note import notesEntity,NoteEntity
from typing import Union
from bson import *
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse,RedirectResponse 
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

note = APIRouter()
templates = Jinja2Templates(directory="templates")

db = client["Notes"]
collection = db["mynotes"]
@note.get("/",response_class=HTMLResponse)
async def home_page(request:Request):
    result = collection.find({})
    newdoc = []
    for results in result:
        newdoc.append({
            "id": results["_id"],
            "title": results["title"],
            "desc": results["desc"],
        })
    print(result)
    return templates.TemplateResponse("index.html", {"request": request,"newdoc": newdoc})

@note.post("/")
async def new_note(request:Request):
    form = await request.form()
    note = collection.insert_one(dict(form))
    return RedirectResponse("/", status_code=302)

@note.post("/delete")
async def delete_note(request: Request):
    form = await request.form()
    note_id = form.get("note_id")
    if note_id:
        result = collection.delete_one({"_id": ObjectId(note_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Note not found")
    return RedirectResponse("/", status_code=302)

@note.post("/edit/{note_id}")
async def edit_note(note_id: str, title: str = Form(...), desc: str = Form(...)):
    result = collection.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": {"title": title, "desc": desc}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return RedirectResponse("/", status_code=302)