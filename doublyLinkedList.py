from gettext import npgettext
from tkinter.messagebox import NO

from torch import true_divide


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None
    
    def __repr__(self) -> str:
        return f"Node({self.data})"
    

class DoublyLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length =  1  
        

    def __iter__(self):
        """Iterate through the list and yield the nodes"""
        temp = self.head
        while temp:
            yield temp
            temp = temp.next
            
    
    def __repr__(self) -> str:
        return '<=>'.join([str(item) for item in iter(self)])
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
            
    
    def append(self,value):
        """Append to the end of the list"""
        temp = Node(value)
        if self.head:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
        else:
            self.head = temp
            self.tail = temp
        self.length+=1
        return True
        
    def pop(self):
        """Pop out the last item from the list"""
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev= None
        self.length -= 1
        return temp
    
    def prepend(self,value):
        """Add nodes to the start of the list"""
        temp = Node(value)
        if self.head:
            self.head.prev = temp
            temp.next = self.head
            self.head = temp
            
        else:
            self.head = temp
            self.tail = temp
        self.length +=1
        return True
    
    def pop_first(self):
        """Pop nodes from the start of the list"""
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None 
        self.length -= 1  
        
    def get(self,index):
        """Get nodes based on the index supplied"""
        if not 0 <= index <= self.length  :
            raise ValueError('Index out of range')
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        return temp   
             
    
    def set_value(self,index,value):
        """Set the given value at given index"""
        if not 0 <= index <= self.length  :
            raise ValueError('Index out of range')
        temp = self.get(index)
        if temp:
            temp.data = value
            return True
        return False
            
    
    def insert(self,index,value):
        """Insert a new node at given index with given value"""
        if not 0 < index <=self.length:
            raise ValueError('Index out of Range')
        if index == 0:
            self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index-1)
        after  = before.next
        
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
                 
        self.length += 1
        return True    
    
    
    def remove(self,index):
        """Remove an item from a given index"""
        if not 0 < index <=self.length:
            raise ValueError('Index out of Range')
        if index == 0:
            self.pop_first()
        if index == self.length:
            self.pop()
            
        node_removed = self.get(index)
        node_removed.next.prev = node_removed.prev
        node_removed.prev.next = node_removed.next
        
        node_removed.next = None
        node_removed.prev = None
        
        
        self.length -= 1
        return True
          
    def reverse(self):
        before = None
        temp = self.head
        self.tail  = temp        
        while temp:
            after = temp.next
            temp.next = before
            temp.prev =after
            before = temp
            temp = after
        self.head = before
        return self
        
def main():
    double_list = [Node('Toronto'),
                    Node('Scarborough'),
                    Node('North York')]

    new_double = DoublyLinkedList('Toronto')
    # new_double.print_list()

    print(new_double)
    new_double.append('Scarborough')
    print(new_double)
    new_double.pop()
    print(new_double)
    # print(new_double.head)
    # print(new_double.tail)
    new_double.prepend('Scarborough')
    print(new_double)
    print(new_double.head)
    print(new_double.tail)
    print(new_double.get(0))
    new_double.set_value(0,'Peel')
    print(new_double)
    new_double.insert(1,'Durham')
    print(new_double)
    print(new_double.reverse())
    print(new_double.head)
    print(new_double.tail)
    


if __name__ == "__main__":
    main()
    