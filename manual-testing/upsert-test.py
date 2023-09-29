import requests

url = "http://localhost:3000/dogs"

dogs = [
    {"name": "Buddy", "age": 3, "breed": "Labrador", "owner": "Dave"},
    {"name": "Lucy", "age": 2, "breed": "Bulldog", "owner": "Jenna"},
    {"name": "Max", "age": 1, "breed": "German Shepherd", "owner": "Will"},
]

def get_all_dog_ids(url):
    response = requests.get(url)
    if response.status_code == 200:
        dogs = response.json()
        return [dog['id'] for dog in dogs]
    else:
        print(f"Failed to fetch dogs. Status Code: {response.status_code}")
        return []

def delete_dog_by_id(url, dog_id):
    response = requests.delete(f"{url}/{dog_id}")
    if response.status_code == 200:
        print(f"Dog with ID {dog_id} deleted successfully.")
    else:
        print(f"Failed to delete dog with ID {dog_id}. Status Code: {response.status_code}")

def clear_database(url):
    dog_ids = get_all_dog_ids(url)
    for dog_id in dog_ids:
        delete_dog_by_id(url, dog_id)

def upsert_dogs(url, dogs):
    print(dogs)
    dogs_with_ids = []
    for dog in dogs:
        response = requests.post(url + '/upsert', json=dog)
        if response.status_code == 201:
            id = response.json()['identifiers'][0]['id']  # {'identifiers': [{'id': 131}], 'generatedMaps': [{'id': 131}], 'raw': [{'id': 131}]}
            dog["id"] = id
            dogs_with_ids.append(dog)
            print(f"Upsert successful for {dog['name']}. Response: {response.status_code}: {response.json()}")
        else:
            print(f"Upsert failed for {dog['name']}. Status Code: {response.status_code}")
    return dogs_with_ids


clear_database(url)
print("All dogs: ", get_all_dog_ids(url))
dogs_with_ids = upsert_dogs(url, dogs)
upsert_dogs(url, dogs_with_ids)
# upsert_dogs(url, dogs)
print("All dogs: ", get_all_dog_ids(url))

