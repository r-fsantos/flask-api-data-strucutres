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
		self._head: Node = None
		self._last_node: Node = None

	def get_head(self) -> Node:
		return self._head

	def get_last_node(self) -> Node:
		return self._last_node
	
	def list_is_empty(self) -> bool:
		return self._head is None

	def add_front(self, data: Any) -> None:
		if self.list_is_empty():
			self._head = Node(data=data, next_node=None)
			self._last_node = self._head
		else:
			self._head = Node(data=data, next_node=self._head)

	def add_back(self, data: Any) -> None:
		if self.list_is_empty():
			self.add_front(data=data)
		else:
			self._last_node._next_node = Node(data=data, next_node=None)
			self._last_node = self._last_node._next_node

	def print(self) -> None:
		ll_string: str = ""
		node: Node = self.get_head()

		while node:
			data: Any = node.get_data()
			ll_string += f"{str(data)} -> "
			node = node.get_next_node()

		ll_string += "None"
		print(ll_string)
	
	def to_list(self) -> list:
		if self.list_is_empty():
			return []
		
		array: list = []
		node: Node = self.get_head()

		while node:
			array.append(node.get_data())
			node = node.get_next_node()

		return array
	
	def get_user_by_id(self, id: int) -> dict:
		node: None = self.get_head()

		while node:
			data: dict = node.get_data()
			if data["id"] == id:
				return data
			node = node.get_next_node()

		return None


if __name__ == "__main__":
	node4 = Node(data="4", next_node=None)
	node3 = Node(data="3", next_node=node4)
	node2 = Node(data="2", next_node=node3)
	node1 = Node(data="1", next_node=node2)
	node0 = Node(data="0", next_node=node1)

	linked_list: LinkedList = LinkedList()
	print("Creating the very first linked list:")
	linked_list.print()

	print()
	print("Adding in the front:")
	linked_list.add_front(data="New Head")
	linked_list.print()

	print()
	print("Adding in the front:")
	linked_list.add_front(data="New Head, Again!")
	linked_list.print()

	print()
	print("Adding in the back:")
	linked_list.add_back(data="New Last Node")
	linked_list.print()
