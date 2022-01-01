#!/usr/bin/env python3

from typing import Any

from data import Data

from node import Node


class HashTable:
	_table_size: int
	_hash_table: list

	def __init__(self, table_size: int) -> None:
		self._table_size = table_size
		self._hash_table = [None] * table_size

	def inserting(self, key: str, value: Any) -> None:
		"""
		todo:
			- Apply Single Responsability Principle and
			- rename method name to improve readability
			- If there are more than one Node per key,
			a linked list could be implemented
		"""
		hashed_key: str = self._get_hash(key=key)

		data: Data = Data(key=key, value=value)
		node: Node = Node(data=data, next_node=None)

		if self._hash_table[hashed_key] is None:
			self._hash_table[hashed_key] = node
			return

		previous_node: Node = self._hash_table[hashed_key]
		
		while previous_node._next_node:
			previous_node = previous_node._next_node

		previous_node._next_node = node


	def get_value(self, key: str) -> Any:
		hashed_key: str = self._get_hash(key=key)

		if self._hash_table[hashed_key] is not None:
			node: Node = self._hash_table[hashed_key]
			
			if node.get_next_node() is None:
				return node._data.value

			while node:
				if key == node._data.key:
					return node._data.value
				node = node.get_next_node()

			if key == node._data.key:
					return node._data.value

		return None

	def _get_hash(self, key: str) -> str:
		hash: int = 0
		
		for i in str(key):
			# TODO: Improve this "hashing" method
			hash += self._get_unicode_char(char=i)
			hash = (hash ** 2) % self._table_size

		return hash

	def _get_unicode_char(self, char: str) -> str:
		"""Returns the unicode point from a single-char (char) string"""
		return ord(char)
	
	def	print_table(self) -> None:
		print("{")
		for i, val in enumerate(self._hash_table):
			if val is None:
				print(f"    [{i}] {val}")
			else:
				llist_string: str = ""
				node: Node = val
				if node._next_node:
					while node._next_node:
						llist_string += str(
							str(node._data.key) + ": " + str(node._data.value) + " --> "
						)
						node = node._next_node
					llist_string += str(
						str(node._data.key) + ": " + str(node._data.value) + " --> None"
					)
					print(f"    [{i}] {llist_string}")
				else:
					print(f"    [{i}] {val._data.key}: {val._data.value}")
		print("}")


if __name__ == "__main__":
	test_table_size: int = 5
	ht: HashTable = HashTable(table_size=test_table_size)
	ht.inserting(key="Meu nome", value="Renato")
	ht.inserting(key="Meu nome", value="Felicio")
	ht.inserting(key="Meu nome", value="dos")
	ht.inserting(key="Meu nome", value="Santos")
	ht.inserting(key="Meu nome", value="Junior")
	ht.print_table()
