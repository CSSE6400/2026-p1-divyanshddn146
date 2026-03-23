from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api/v1')

# This is our "Golden Copy"
MOCK_TODO = {
    "id": 1,
    "title": "Watch CSSE6400 Lecture",
    "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
    "completed": True,
    "deadline_at": "2023-02-27T00:00:00",
    "created_at": "2023-02-20T00:00:00",
    "updated_at": "2023-02-20T00:00:00"
}

@api.route('/health')
def health():
    return jsonify({"status": "ok"})

@api.route('/todos', methods=['GET'])
def get_todos():
    # Return a LIST [] because it's a collection
    return jsonify([MOCK_TODO])

@api.route('/todos', methods=['POST'])
def create_todo():
    # Return 201 Created and a single OBJECT {}
    return jsonify(MOCK_TODO), 201

@api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    # Return a single OBJECT {}
    return jsonify(MOCK_TODO)

@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    # Return a single OBJECT {}
    return jsonify(MOCK_TODO)

@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    # Return a single OBJECT {}
    return jsonify(MOCK_TODO)