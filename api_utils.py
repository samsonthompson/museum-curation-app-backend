import requests

BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

def get_departments():
    """Fetches all departments from The Met API."""
    url = f"{BASE_URL}/departments"
    response = requests.get(url)
    return response.json()

def get_objects_by_department(department_ids):
    """Fetches objects based on department IDs."""
    url = f"{BASE_URL}/objects?departmentIds={department_ids}"
    response = requests.get(url)
    return response.json()

def get_object_details(object_id):
    """Fetches details of a specific object using its ID."""
    url = f"{BASE_URL}/objects/{object_id}"
    response = requests.get(url)
    return response.json()
