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
	posts = db.relationship("BlogPost")
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
def create_user():
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
def get_users_in_descending_order():
	pass

@app.route(rule="/users/ascending_id", methods=["GET"])
def get_users_in_ascending_order():
	pass

@app.route(rule="/users/<id>", methods=["GET"])
def get_user_by_id(id: int ):
	return {"id": id}

@app.route(rule="/users/<id>", methods=["DELETE"])
def delete_user(id: int):
	pass

@app.route(rule="/blog-posts/<user_id>", methods=["POST"])
def create_blog_post(user_id: int):
	pass

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
