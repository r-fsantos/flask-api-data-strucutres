#!/usr/bin/env python3

from typing import Any

from node import Node

class ApiQueue:
	"""
	FIFO structure.
	queues adds data to the tail
	dequeues removes node from the head, and pulls it to the next node
	"""
	def __init__(self) -> None:
		self.head: Node = None
		self.tail: Node = None

	def _queue_is_empty(self) -> bool:
		is_empty: bool = (
			self.head is None
			and self.tail is None
		)
		return is_empty

	def enqueue(self, data: Any):
		if self._queue_is_empty():
			self.head = self.tail = Node(data=data, next_node=None)
			return
		
		self.tail._next_node = Node(data=data, next_node=None)
		self.tail = self.tail._next_node

		return
	
	def dequeue(self) -> Node or None:
		if self.head is None:
			return None
		
		# TODO: Although python is garbage-collected,
		# it is interesting to free the memory right now, not
		# leave this to the compiller.
		removed_node: Node = self.head
		self.head = self.head._next_node

		if self.head is None:  # last node was dequeued,
			self.tail = None  # tail must be none, too.

		return removed_node
