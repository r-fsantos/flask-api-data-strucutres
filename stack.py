#!/usr/bin/env python3

from typing import Any

from node import Node


class Stack:
	"""
	FILO structure.
	"""
	def __init__(self) -> None:
		self._top: Node = None
	
	def get_peek(self) -> Node or None:
		return self._top

	def push(self, data: Any):
		next_node: Node = self._top

		new_top: Node = Node(data=data, next_node=next_node)

		self._top = new_top
	
	def stack_is_empty(self) -> bool:
		return self._top is None

	def pop(self) -> Node or None:
		if self.stack_is_empty():
			return None

		removed_node: Node = self._top

		self._top = self._top._next_node

		return removed_node
