#!/usr/bin/env python3

from typing import Any


class Node:
	"""
	Add Doc Strings
	"""

	_data: Any
	_next_node: None  # can be Node as well

	def __init__(
		self,
		data: Any,
		next_node: None  # can be Node as well
	) -> None:
		self._data = data
		self._next_node = next_node
	
	def set_data(self, data: Any) -> None:
		self._data = data
	
	def get_data(self) -> Any:
		return self._data
	
	def set_next_node(self, node: None) -> None:
		self._next_node = node
	
	def get_next_node(self):
		return self._next_node
