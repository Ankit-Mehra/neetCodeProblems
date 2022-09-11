from queue import Empty


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    
    def __init__(self) -> None:
        """Create an empty Stack"""
        self._data = []
        
    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)
    
    def is_Empty(self):
        """Return true if the stack is empty"""
        return len(self._data) == 0
    
    def push(self,e):
        """Add element e at the top of the stack"""
        self._data.append(e)
        
    def top(self,e):
        """Retrun but not remove the top of the stack
        Raise empty exception if the stack is empty"""
        
        if self.is_Empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        """Remove and return the element from the top of the stack
        Raise empty exception if the stack is empty"""
        
        if self.is_Empty():
            raise Empty('Stack is empty')
        return self._data.pop()
        
        
        