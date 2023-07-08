from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from tools import get_person, remove_person, calcular_imc, add_attribute_first


data_people = []

app = FastAPI()

class Person(BaseModel):
    id: Optional[float] = None
    name: str
    weight: float
    height: float
    imc: Optional[float] = None


@app.get("/")
async def get_people():
    return data_people

@app.get("/people/{person_id}")
async def read_item(person_id: int):
    data = get_person(person_id, data_people)
    return data

@app.post("/person/")
async def create_person(person: Person):
    person_dict = person.model_dump()
    person_imc = calcular_imc(person.weight, person.height)
    person_new_id = len(data_people) + 1
    # person_dict['id'] = person_new_id
    person_dict['imc'] = person_imc
    person_dict = add_attribute_first(person_dict, 'id', person_new_id)
    data_people.append(person_dict)
    
    return person_dict