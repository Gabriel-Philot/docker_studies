from faker import Faker
from dataclasses import dataclass
import json
import timeit

fake = Faker()

# Classes de dados sem e com __slots__
@dataclass
class DataClassWithoutSlots:
    name: str
    age: int
    email: str
    city: str
    # Função para processar os dados sem slots e retornar JSON
    def ingest_data_Class(data):
        processed_data = [DataClassWithoutSlots(**row) for row in data]
        json_data = {'data': [{'name': row.name, 'age': row.age, 'email': row.email, 'city': row.city} for row in processed_data]}
        return json.dumps(json_data)

@dataclass
class DataClassWithSlots:
    __slots__ = ['name', 'age', 'email', 'city']
    name: str
    age: int
    email: str
    city: str
    # Função para processar os dados com slots e retornar JSON
    def ingest_data_ClassSlot(data):
        processed_data = [DataClassWithSlots(**row) for row in data]
        json_data = {'data': [{'name': row.name, 'age': row.age, 'email': row.email, 'city': row.city} for row in processed_data]}
        return json.dumps(json_data)


# Função para gerar dados fictícios usando Faker a partir de uma fonte de API
def simu_data_api(num_rows):
    fake_data = []
    for _ in range(num_rows):
        fake_name = fake.name()
        fake_age = fake.random_int(min=18, max=90)
        fake_email = fake.email()
        fake_city = fake.city()
        fake_data.append({'name': fake_name, 'age': fake_age, 'email': fake_email, 'city': fake_city})
    return fake_data



def ingest_data_noClass(data):
    json_data = {'data': []}
    for row in data:
        processed_row = {'name': row['name'], 'age': row['age'], 'email': row['email'], 'city': row['city']}
        json_data['data'].append(processed_row)
    return json.dumps(json_data)