from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str 
    pincode : int
    landmark: str = "No Landmark"

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_info = {'city' : 'gurgaon', 'state': 'Haryana', 'pincode' : 123456}
patient_info = {'name': 'Sahil', 'gender': 'Male', 'age':25, 'address': address_info}

patient1 = Patient(**patient_info)
print(patient1.address.pincode)
print(type(patient1))

temp = patient1.model_dump()
print(temp)
print(type(temp))

temp_json = patient1.model_dump_json()
print(type(temp_json))

temp_selected = patient1.model_dump(include=['name','gender'])
print(temp_selected)

temp_excluded = patient1.model_dump(exclude=['name','gender'])
print(temp_excluded)

temp_excluded_unset = patient1.model_dump(exclude_unset=True)  # it won't show default values for example landmark in this case
print(temp_excluded_unset)
