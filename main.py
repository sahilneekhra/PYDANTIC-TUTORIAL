from typing import Annotated, Optional, Dict
from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field, field_validator, model_validator


# always call BaseModel in class, they define variables
class Patient(BaseModel):

    name : Annotated[ str , Field(max_length= 50, title= "name of the patient", description= 'give string value with max length 50 here') ]
    age: Annotated[int, Field(default = 1, title='Age of patient', gt=0, lt=150 )]
    email: EmailStr
    company_email : EmailStr
    linkedin_url: AnyUrl
    weight : Annotated [Optional[float], Field(gt=0, strict=True)]      #kgs
    height : Optional[float]                                            #Meters
    contact: Optional[Dict[str,str]]

    @field_validator('company_email')
    @classmethod
    def email_validatore(cls,value):
        valid_domains = ['hdfc.com','icici.com']
        r=value
        domain_name = r.split('@')[-1]
        if domain_name not in valid_domains:
            print("value = " , value)
            raise ValueError("Not a valid domain")
        return value
    
    @field_validator('name')
    @classmethod
    def capitalize_name ( cls,value):
        return value.capitalize()
    
    @field_validator('age',mode = 'before')  # mdoe is after by default
    @classmethod
    def validate_age(cls,value):
        if 0< value<100:
            return value
        else:
            raise ValueError('Age should be within 0 to 100')

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact:
            raise ValueError("Paitents older than 60 must have emergency contact number")

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(((self.weight/self.height)**2),2)
        return bmi




def insert_patient_name_v2(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.company_email)
    print(patient.weight)
    print(patient.height)
    print(patient.contact)
    print(patient.bmi)

    print('inserted into database')
# from pprint import pprint 
# patient_info = { 'name' :'sahil', 'age': 62, 'email': 'abc@gmail.com','company_email' : 'abc@icici.com', 'linkedin_url' : 'https://linkedin.com', 'weight' : 45, "contact" : {'emergency' : "7338973598"} }
patient_info = { 'name': 'sahil',
 'age': 62,
 'email': 'abc@gmail.com',
 'company_email': 'abc@icici.com',
 'linkedin_url': 'https://linkedin.com',
 'weight': 75.2,
 'height' : 1.72,
 'contact': {
    'emergency': '7338973598'
    }
 }

patient1 = Patient(**patient_info)

insert_patient_name_v2(patient1)

# if in my business usecase, age of my patient should be between 20-30
# for this Pydantic have Field
