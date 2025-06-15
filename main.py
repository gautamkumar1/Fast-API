from fastapi import FastAPI
from pydantic import BaseModel
import json
import os
class Patient(BaseModel):
    id: int
    name: str
    age: int
    email: str

app = FastAPI()
POST_FILE = "patient.json"
# Helper functions to read/write JSON
def read_patient():
    if not os.path.exists(POST_FILE):
        return []
    with open(POST_FILE, "r") as f:
        return json.load(f)

def save_patient(posts):
    with open(POST_FILE, "w") as f:
        json.dump(posts, f, indent=2)
@app.get("/")
def hello():
    return {"message":"Hello, World!"}
@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}

# Parameters
@app.get("/greet/{name}")
def greeet(name:str):
    return {"message": f"Hello, {name}!"}

# ---------- CRUD endpoints ----------

@app.post("/create",response_model=Patient)
def create_patient(body: Patient):
    patient = read_patient()
    # Check if patient with the same ID already exists
    for p in patient:
        if p['id'] == body.id:
            return {"message": "Patient with this ID already exists."}
    # Add new patient
    patient.append(body.model_dump())
    save_patient(patient)
    return body
@app.get("/read")
def read_patient_by_id():
    patients = read_patient()
    if patients:
        return patients
@app.get("/read/{id}")
def read_patient_by_id(id: int):
    patients = read_patient()
    for patient in patients:
        if patient['id'] == id:
            return patient
    return {"message": "Patient not found."}
@app.put("/update/{id}",response_model=Patient)
def update_patient(id: int, body: Patient):
    patients = read_patient()
    for i, patient in enumerate(patients):
        if patient['id'] == id:
            patients[i] = body.model_dump()
            save_patient(patients)
            return body
    return {"message": "Patient not found."}
@app.delete("/delete/{id}", response_model=Patient)
def delete_patient(id: int):
    patients = read_patient()
    for i, patient in enumerate(patients):
        if patient['id'] == id:
            del patients[i]
            save_patient(patients)
            return {"message": "Patient deleted successfully."}
    return {"message": "Patient not found."}
