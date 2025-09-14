def insert_patient_name(name: str, age: int):
    print(name)
    print(age)
    print('insert into database')

#insert_patient_name('nitish','thirty')

""" 
    Problem 1 :-
    We wanted age as a integer

    we can use type hinting here as === insert_patient_name(name: str, age: int):

    but type hinting is only for giving information, it won't generate error  if someone send by mistake

    to fix this we'll have to add type conditions

    def insert_patient_name(name: str, age: int):
        if type(name) == str and type(age) == int:
            print....
        else raise TypeError('Incorrect  data type)
    
    this will solve our problem but it is not scalable, we can't write this again and again , 
    and if I introduce new variable, I'll have to change in every function.

    Problem 2:-

    if let's say we wanted data validation for age, age shouldn't be less than 0. 
    To do this, we again have to write code, not just for age, but for all the varibales that wwe wanna validate.

"""

''' Here Comes Pydantic  '''

''' 
    1. In Pydantic we can define class with a schema
'''

from typing import Annotated
from pydantic import BaseModel, EmailStr, AnyUrl, Field

# always call BaseModel in class, they define variables
class Patient(BaseModel):

    name : Annotated[ str , Field(max_length= 50, title= "name of the patient", description= 'give string value with max length 50 here') ]
    age: int = Field(ge = 19, lt = 30)
    email: EmailStr
    linkedin_url: AnyUrl
    

def insert_patient_name_v2(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print('insert into database')

patient_info = { 'name' :'Sahil', 'age': 20, 'email': 'abc@gmail.com', 'linkedin_url' : 'https://linkedin.com' }

patient1 = Patient(**patient_info)

insert_patient_name_v2(patient1)

# if in my business usecase, age of my patient should be between 20-30
# for this Pydantic have Field
