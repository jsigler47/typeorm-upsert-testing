import requests

url = "http://localhost:3000/dogs"

dogs = [
    {"name": "Buddy", "age": 3, "breed": "Labrador", "owner": "Dave"},
    {"name": "Lucy", "age": 2, "breed": "Bulldog", "owner": "Jenna"},
    {"name": "Max", "age": 1, "breed": "German Shepherd", "owner": "Will"},
    {"name": "Max", "age": 1, "breed": "German Shepherd", "owner": "Will"} # Should NOT call the database
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
    for dog in dogs:
        response = requests.post(url + '/upsert', json=dog)
        if response.status_code == 201:
            print(f"Upsert successful for {dog['name']}. Response: {response.json()}")
        else:
            print(f"Upsert failed for {dog['name']}. Status Code: {response.status_code}")



clear_database(url)
upsert_dogs(url, dogs)

