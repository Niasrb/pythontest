from flask import Blueprint, jsonify, request
from .models import User
from .database import db

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return {"message": "Welcome to the API"}


@main.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@main.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or 'username' not in data or 'email' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        user = User(username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400