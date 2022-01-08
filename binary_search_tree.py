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
	
	def insert(self, value: Any) -> None:
		if self.root is None:  # empty tree
			self.root = Node(data=value)
		else:  # root is not none. Now, recursively adds data
			self._recursive_insertion(value=value, node=self.root)
	
	def _recursive_insertion(self, value: Any, node: Node) -> None:
		if value < node.data:
			if node.left is None:
				node.left = Node(data=value)
			else:
				self._recursive_insertion(value=value, node=node.left)
		elif value > node.data:
			if node.right is None:
				node.right = Node(data=value)
			else:
				self._recursive_insertion(value=value, node=node.right)
		else:  # value == node.data.
			return
	
