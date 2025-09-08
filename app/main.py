from fastapi import FastAPI

app = FastAPI()

# Homepage route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI! 🎉"}

# Notes route
@app.get("/notes")
def get_notes():
    notes = [
        {"id": 1, "title": "First Note", "content": "This is your first note"},
        {"id": 2, "title": "Second Note", "content": "This is your second note"}
    ]
    return {"notes": notes}
