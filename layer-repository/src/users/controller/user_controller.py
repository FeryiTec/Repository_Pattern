from flask import Blueprint, jsonify, request
from users.model.user_model import User
from users.repository.memory_repository import UserRepository


blueprint = Blueprint('user_controller', __name__)
repository = UserRepository()


# Endpoint to insert users
@blueprint.route("/users", methods=["POST"])
def insert_user():
    # Get the user data from the request
    user_data = request.get_json()

    # Create a new user
    user = User(
        id=len(repository.users) + 1,
        name=user_data["name"],
        email=user_data["email"]
    )

    # Add the new user to the list of users
    repository.add(user)

    # Return the newly inserted user
    return jsonify(user)


# Endpoint to retrieve users based on user_id
@blueprint.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    # Find the user with the given user_id
    user = repository.get(user_id)

    # If the user is not found, return a 404 error
    if user is None:
        return jsonify({"message": "User not found"}), 404

    # Return the retrieved user
    return jsonify(user)