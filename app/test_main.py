from fastapi.testclient import TestClient

from .main import app
import re

client = TestClient(app)

def test_greet_valid_input():
    response=client.get("/greet/?name=Pavitra")
    assert response.status_code ==200
    assert response.json()=={"message":"Hello Pavitra, welcome to NotePilot!"}

def test_greet_missing():
    response=client.get("/greet/")
    assert response.status_code ==422

def test_greet_multiple():
    response=client.get("/greet/?name=Abc xyz")
    assert response.status_code ==200
    assert response.json()=={"message":"Hello Abc xyz, welcome to NotePilot!"}

def test_greet_special_char():
    response = client.get("/greet/?name=Abc@123")
    assert response.status_code == 200
    assert response.json() == {"message":"Invalid name. Special characters are not allowed."}


def test_greet_multiple_param():
    response=client.get("/greet/?name=Abc&age=12")
    assert response.status_code ==200
    assert response.json()=={"message":"Hello Abc, welcome to NotePilot!"}


