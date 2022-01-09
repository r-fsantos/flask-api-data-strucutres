#!/usr/bin/env python3

from typing import Any


class Node:
	def __init__(self, data: Any = None) -> None:
		self.data: Any = data
		self.left = None
		self.right = None


class BinarySearchTree:  # BST
	"""
	Values < Root -> left side of the root
	Values > Root -> right side of the root
	Values == Root -> Does nothing. BSY does not
	allow data duplicates
	"""
	def __init__(self) -> None:
		self.root: Node = None
	
	def insert(self, data: Any) -> None:
		if self.root is None:  # empty tree
			self.root = Node(data=data)
		else:  # root is not none. Now, recursively adds data
			self._recursive_insertion(data=data, node=self.root)
	
	def _recursive_insertion(self, data: Any, node: Node) -> None:
		if data["id"] < node.data["id"]:
			if node.left is None:
				node.left = Node(data=data)
			else:
				self._recursive_insertion(data=data, node=node.left)
		elif data["id"] > node.data["id"]:
			if node.right is None:
				node.right = Node(data=data)
			else:
				self._recursive_insertion(data=data, node=node.right)
		else:  # data == node.data
			return
	
	def search(self, id: int) -> dict:
		_id: int = int(id)

		if self.root is None:
			return False
		
		return self._recursive_searching(id=_id, node=self.root)
	
	def _recursive_searching(self, id: int, node: Node) -> dict:		
		if id == node.data["id"]:
			return node.data
		
		if id < node.data["id"] and node.left is not None:
			if id == node.left.data["id"]:
				return node.left.data
			return self._recursive_searching(id=id, node=node.left)

		if id > node.data["id"] and node.right is not None:
			if id == node.right.data["id"]:
				return node.right.data
			return self._recursive_searching(id=id, node=node.right)

		return {}

