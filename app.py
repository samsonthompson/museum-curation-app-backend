from flask import Flask, jsonify
from api_utils import (
    get_met_departments, get_met_objects_by_department, get_met_object_details,
    get_harvard_objects, get_harvard_object_details
)

app = Flask(__name__)

# The Met API 
@app.route('/met/departments', methods=['GET'])
def met_departments():
    """Endpoint to get all departments from The Met."""
    departments_data = get_met_departments()
    return jsonify(departments_data)

@app.route('/met/objects/<department_ids>', methods=['GET'])
def met_objects(department_ids):
    """Endpoint to get objects by department IDs from The Met."""
    objects_data = get_met_objects_by_department(department_ids)
    return jsonify(objects_data)

@app.route('/met/object/<int:object_id>', methods=['GET'])
def met_object_details(object_id):
    """Endpoint to get object details by object ID from The Met."""
    object_data = get_met_object_details(object_id)
    return jsonify(object_data)

# Harvard Art Museums API 
@app.route('/harvard/objects', methods=['GET'])
def harvard_objects():
    """Endpoint to get objects from Harvard Art Museums."""
    harvard_data = get_harvard_objects()
    return jsonify(harvard_data)

@app.route('/harvard/object/<int:object_id>', methods=['GET'])
def harvard_object_details(object_id):
    """Fetches and returns details of a specific object from Harvard Art Museums."""
    object_data = get_harvard_object_details(object_id)
    
    if 'error' in object_data:
        return jsonify(object_data), 404 
    return jsonify(object_data)

if __name__ == '__main__':
    app.run(debug=True)
