from collections import ChainMap

def get_person(id, data):
    for person in data:
        if person['id'] == int(id):
            return person
    return 'person not found'

def remove_person(id, data):
    for person in data:
        if person['id'] == id:
            data.remove(person)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

def add_attribute_first(dictionary, key, value):
    new_dict = {key: value}
    updated_dict = ChainMap(new_dict, dictionary)
    return dict(updated_dict)