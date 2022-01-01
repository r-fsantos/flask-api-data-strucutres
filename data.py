#!/usr/bin/env python3

from typing import Any

# TODO: This really could be an NamedTuple?
class Data:
	"""
	TODO: Add DocStrings
	"""
	key: str
	value: Any

	def __init__(self, key: str, value: Any) -> None:
		self.key = key
		self.value = value

