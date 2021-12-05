#!/usr/bin/env python3

from typing import Any
from datetime import datetime


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
		self._data: Any = data
		self._next_node: Node = next_node
	
	def set_data(self, data: Any) -> None:
		self._data = data
	
	def get_data(self) -> Any:
		return self._data
	
	def set_next_node(self, node: None) -> None:
		self._next_node = node
	
	def get_next_node(self):
		return self._next_node


class LinkedList:
	"""
	Add Doc Strings
	"""

	_head: Node
	_last_node: Node

	def __init__(self) -> None:
		self._head: Node or None = None
		self._last_node: Node or None = None

	def set_head(self, node: Node) -> None:
		self._head = node

	def get_head(self) -> Node:
		return self._head
	
	def set_last_node(self, node: Node) -> None:
		self._last_node = node
	
	def get_last_node(self) -> Node:
		return self._last_node

	def print(self) -> None:
		ll_string: str = ""
		node: Node = self.get_head()

		while node:
			data: Any = node.get_data()
			ll_string += f"{str(data)} -> "
			node = node.get_next_node()

		ll_string += "None"
		print(ll_string)


if __name__ == "__main__":
	node4 = Node(data="4", next_node=None)
	node3 = Node(data="3", next_node=node4)
	node2 = Node(data="2", next_node=node3)
	node1 = Node(data="1", next_node=node2)
	node0 = Node(data="0", next_node=node1)

	linked_list: LinkedList = LinkedList()
	linked_list.set_head(node=node0)
	linked_list.set_last_node(node=node4)
	linked_list.print()