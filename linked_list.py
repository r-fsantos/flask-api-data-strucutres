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

	def add_front(self, data: Any) -> None:
		new_node: Node = Node(data=data, next_node=self.get_head())
		self.set_head(node=new_node)
	
	def add_back(self, data: Any) -> None:
		node: Node = self.get_head()

		if node is None:  # this means that is empty, so
			self.add_front(data=data)  # simply add it at the head
		else:
			new_last_node: Node = Node(data=data, next_node=None)

		last_node: Node = self.get_last_node()
		if last_node is not None:
			last_node.set_next_node(node=new_last_node)

		elif last_node is None:
			print("...Iterating until the end to get the last reference...")
			while node.get_next_node():
				node = node.get_next_node()

			node.set_next_node(node=new_last_node)
			self.set_last_node(node=new_last_node)

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
	print("Creating the very first linked list:")
	linked_list.print()

	print()
	print("Adding a new Head:")
	linked_list.add_front(data="New Head")
	linked_list.print()

	print()
	print("Adding a New Last Node:")
	linked_list.add_back(data="New Last Node")
	linked_list.print()

