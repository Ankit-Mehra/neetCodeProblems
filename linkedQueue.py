from queue import Empty


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    # ------ Nested Node Class------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, data) -> None:
            """Lightweight, nonpublic class for storing a singly linked node."""
            self._data = data
            self._next = None

    def __init__(self) -> None:
        """Create an empty Queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self) -> int:
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self) -> bool:
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._data

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        temp = self._head._data
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # if only one item in the queue and after removal head becomes none
            self._tail = None
        return temp

    def enqueue(self, e):
        """Add an element to the back of queue."""
        new_node = self._Node(e)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1
