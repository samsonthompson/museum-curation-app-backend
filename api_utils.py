import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# The Met API setup
MET_BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

# Harvard API setup
HARVARD_API_KEY = os.getenv("HARVARD_API_KEY")
HARVARD_BASE_URL = "https://api.harvardartmuseums.org"


# The Met API functions

def get_met_departments():
    """Fetches all departments from The Met API."""
    url = f"{MET_BASE_URL}/departments"
    response = requests.get(url)
    return response.json()

def get_met_objects_by_department(department_ids):
    """Fetches objects based on department IDs from The Met API."""
    url = f"{MET_BASE_URL}/objects?departmentIds={department_ids}"
    response = requests.get(url)
    return response.json()

def get_met_object_details(object_id):
    """Fetches details of a specific object using its ID from The Met API."""
    url = f"{MET_BASE_URL}/objects/{object_id}"
    response = requests.get(url)
    return response.json()


# Harvard Art Museums API functions

def get_harvard_objects():
    """Fetches objects from Harvard Art Museums."""
    url = f"{HARVARD_BASE_URL}/object"
    params = {
        "apikey": HARVARD_API_KEY,
        "size": 10  
    }
    response = requests.get(url, params=params)
    return response.json()

def get_harvard_object_details(object_id):
    """Fetches details of a specific object using its ID from Harvard Art Museums."""
    url = f"{HARVARD_BASE_URL}/object/{object_id}"
    params = {
        "apikey": HARVARD_API_KEY
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("objectid"):
            return data
        else:
            return {"error": "Object not found or not available"}
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
