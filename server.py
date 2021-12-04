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
db = SQLAlchemy(app=app)
