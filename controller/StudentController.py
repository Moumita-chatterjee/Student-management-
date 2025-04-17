from fastapi import FastAPI
from student.model.Student import Student

app = FastAPI()

list_of_student = []

@app.post("/item/create")
async def create_item(student: Student):
    for mystudent in list_of_student:
        if student.name == mystudent.name:
            raise ValueError(f"Item '{student.name}' already exists. Unable to create")
    list_of_student.append(student)
    return "Student added sucessfully"