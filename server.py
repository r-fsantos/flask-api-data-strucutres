#!/usr/bin/env python3

"""
Main file application
"""

from flask import (
	Flask,
	request,
	jsonify,
)

#: import_name: the name of the application package
app = Flask(import_name=__name__)
