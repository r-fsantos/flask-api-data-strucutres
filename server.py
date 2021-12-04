#!/usr/bin/env python3

"""
Main file application
"""

from datetime import datetime

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
