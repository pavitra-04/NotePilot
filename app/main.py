from typing import Annotated
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/greet/")
async def greet_user(name: str):
    return {"message": f"Hello {name}, welcome to NotePilot!"}

class Note:
    def __init__(self, id: int, title: str, description: str = None):
        self.id = id
        self.title = title
        self.description = description
Notes = [
    {"id": 123, "title": "Note 1", "description": "My note 1"},
    {"id": 124, "title": "Note 2", "description": "My note 2"},
]
@app.get("/notes")
def get_notes():
    return Notes

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in Notes:
        if note["id"] == note_id:
            return note
    return {"message": "Note not found"}

@app.post("/note")
def create_note(id: int, title: str, description: str = None):
    for note in Notes:
        if note["id"] == id:
            return {"message": "Note with this ID already exists"}
    new_note = {"id": id, "title": title, "description": description}
    Notes.append(new_note)
    return {"message": "Note added successfully", "note": new_note}

@app.put("/notes/{note_id}")
def update_note(note_id: int, title: str = None, description: str = None):
    for note in Notes:
        if note["id"]==note_id:
            if title:
                note["title"]=title
            if description:
                note["description"]=description
            return {"message": "Note updated sucessfully","note":note}
        return {"message": "Note not found"}
    
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for idx, note in enumerate(Notes):
        if note["id"] == note_id:
            deleted = Notes.pop(idx)
            return {"message": "Note deleted successfully", "note": deleted}
    return {"message": "Note not found"}