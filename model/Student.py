from pydantic import BaseModel, EmailStr

class Student(BaseModel):
    name: str
    description: str | None = None
    email: EmailStr
    rollnumber: int
    standard: str


#optional create getters and setters

def set_name(self, name):
    self.name = name

def get_name(self):
    return self.name