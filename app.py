from flask import Flask, jsonify
from api_utils import get_departments, get_objects_by_department, get_object_details

app = Flask(__name__)

@app.route('/departments', methods=['GET'])
def departments():
    """Endpoint to get all departments."""
    departments_data = get_departments()
    return jsonify(departments_data)

@app.route('/objects/<department_ids>', methods=['GET'])
def objects(department_ids):
    """Endpoint to get objects by department IDs."""
    objects_data = get_objects_by_department(department_ids)
    return jsonify(objects_data)

@app.route('/object/<int:object_id>', methods=['GET'])
def object_details(object_id):
    """Endpoint to get object details by object ID."""
    object_data = get_object_details(object_id)
    return jsonify(object_data)

if __name__ == '__main__':
    app.run(debug=True)
