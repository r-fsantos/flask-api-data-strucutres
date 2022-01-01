#!/usr/bin/env python3

"""
Main file application
"""

from datetime import datetime
from os import name

# ORM imports
from sqlalchemy import event
from sqlalchemy.engine import Engine

# database imports
from sqlite3.dbapi2 import Cursor
from sqlite3 import Connection as SQLite3Connection

from flask import (
	Flask,
	request,
	jsonify,
)
from flask_sqlalchemy import SQLAlchemy

from hash_table import HashTable
from linked_list import LinkedList

#: import_name: the name of the application package
app = Flask(import_name=__name__)


#: configuration

#: database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
#: ? why do not track any modification
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

#: configure sqlite3 to enforce foreign key constraints
@event.listens_for(target=Engine, identifier="connect")
def _set_sqlite_pragma(dbapi_connection, connection_record) -> None:
	if isinstance(dbapi_connection, SQLite3Connection):
		cursor: Cursor = dbapi_connection.cursor()
		cursor.execute("PRAGMA foreign_keys=ON;")
		cursor.close()

#: creating instance database (db)
#: TODO: Ensure that db.Time == UTC
db = SQLAlchemy(app=app)
now = datetime.now()

HASH_TABLE_DEFAULT_SIZE: int = 5

#:=============================================================================
#: Models

class User(db.Model):
	"""
	Defines a user inside the project.

	TODOs:
		- Add the columns:
			- updated_at DateTime,
			- deleted_at: DateTime and
			- deleted: bool
	"""
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	posts = db.relationship("BlogPost", cascade="all, delete")
	name = db.Column(db.String(50))
	email = db.Column(db.String(50))
	address = db.Column(db.String(200))
	phone = db.Column(db.String(50))
	created_at = db.Column(db.Date)


class BlogPost(db.Model):
	"""
	Defines BlogPosts mades by some user, inside the project.

	TODOs:
		- Add the columns:
			- updated_at DateTime,
			- deleted_at: DateTime and
			- deleted: bool
	"""
	__tablename__ = "blog_post"
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	title = db.Column(db.String(50))
	body = db.Column(db.String(200))
	created_at = db.Column(db.Date)

#:=============================================================================
#: Routes

# First of all, one must create the API Skeleton
@app.route(rule="/users/", methods=["POST"])
def create_user() -> dict:
	data: dict = request.get_json()
	# TODO: Apply SRP (SOLID) and MVC architecture by
	#	- Writing a controller and adding the persistence logic to it
	#	- Add validation (has mandatory inputs? data format (email), str_len,)
	new_user: User = User(
		name=data["name"],
		email=data["email"],
		address=data["address"],
		phone=data["phone"],
	)
	# Encapsulate into a Controller as well
	db.session.add(new_user)
	db.session.commit()

	return jsonify(
		{
			"id": new_user.id,
			"result": True,
			"message": "New user created!",
		}
	), 201

@app.route(rule="/users/descending_id", methods=["GET"])
def get_all_users_in_descending_order() -> list:
	users: User = User.query.all()
	users_linked_list: LinkedList = LinkedList()

	for user in users:
		users_linked_list.add_front(
			data={
				"id": user.id,
				"name": user.name,
				"email": user.email,
				"address": user.address,
				"phone": user.phone
			}
		)

	users_list: list = users_linked_list.to_list()

	return jsonify(users_list), 200

@app.route(rule="/users/ascending_id", methods=["GET"])
def get_users_in_ascending_order() -> list:
	users: User = User.query.all()
	users_linked_list: LinkedList = LinkedList()

	for user in users:
		users_linked_list.add_back(
			data={
				"id": user.id,
				"name": user.name,
				"email": user.email,
				"address": user.address,
				"phone": user.phone
			}
		)

	users_list: list = users_linked_list.to_list()

	return jsonify(users_list), 200

@app.route(rule="/users/<id>", methods=["GET"])
def get_user_by_id(id: int) -> list:
	user: User = User.query.filter_by(id=id).first()

	if not user:
		return jsonify(
			{
			"result": False,
			"message": f"There is not user with id: {id} registered!"
			}
		), 400

	user_dict: dict = {
		"id": user.id,
		"name": user.name,
		"email": user.email,
		"address": user.address,
		"phone": user.phone
	}

	return jsonify(user_dict), 200

@app.route(rule="/users/<id>", methods=["DELETE"])
def delete_user(id: int):
	user = User.query.filter_by(id=int(id)).first()
	if not user:
		return jsonify(
			{
			"result": False,
			"message": f"There is not user with id: {id} registered!"
			}
		), 400

	db.session.delete(user)
	db.session.commit()

	return jsonify({}), 200

@app.route(rule="/blog-posts/<user_id>", methods=["POST"])
def create_blog_post(user_id: int):
	user = User.query.filter_by(id=int(user_id)).first()

	if not user:
		return jsonify(
			{
			"result": False,
			"message": f"There is not user with id: {id} registered!"
			}
		), 400

	data: dict = request.get_json()
	# TODO: add lookup validation!

	hash_table: HashTable = HashTable(table_size=HASH_TABLE_DEFAULT_SIZE)
	hash_table.inserting(key="user_id", value=user_id)
	hash_table.inserting(key="title", value=data.get("title"))
	hash_table.inserting(key="body", value=data.get("body"))
	hash_table.inserting(key="created_at", value=datetime.now())

	blog_post: BlogPost = BlogPost(
		user_id=hash_table.get_value(key="user_id"),
		title=hash_table.get_value(key="title"),
		body=hash_table.get_value(key="body"),
		created_at=hash_table.get_value(key="created_at")
	)

	db.session.add(blog_post)
	db.session.commit()

	blog_post_dict: dict = {
		"id": blog_post.id,
		"user_id": blog_post.user_id,
		"title": blog_post.title,
		"body": blog_post.body,
		"created_at": blog_post.created_at
	}

	return jsonify(blog_post_dict), 201

@app.route(rule="/blog-posts/<user_id>", methods=["GET"])
def get_all_blog_posts_by_user(user_id: int):
	pass

@app.route(rule="/blog-posts/<id>", methods=["GET"])
def get_blog_post(id: int):
	pass

@app.route(rule="/blog-posts/<id>", methods=["DELETE"])
def delete_blog_post(id: int):
	pass


if __name__ == "__main__":
	# TODO: Only in local development
	app.run(debug=True)
