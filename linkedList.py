class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return f"Node({self.data})"
    
class LinkedList:
    def __init__(self,nodes=None) -> None:
        self.head  = None
        self.tail = None
        if nodes:
            node =nodes[0]
            self.head = nodes[0]
            for obj in nodes[1:]:
                node.next = obj
                node = obj
            self.tail = node
    
    
    
    def __repr__(self) -> str:
        return '->'.join([str(item) for item in iter(self)])

    def __len__(self):
        return len(tuple(iter(self)))

    def append(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            self.tail = temp  
        else:
            self.tail.next = temp
            self.tail = temp
            
    def pop(self):
        temp = self.head
        if len(self) == 0:
            return None
        else:
            pre = self.head
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        if len(self)< 2:
                self.head = None
                self.tail = None
        return temp
    
    def prepend(self,value):
        temp = Node(value)
        if len(self) == 0:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
        
    def pop_first(self):
        if len(self) == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next  = None
        if len(self) == 0:
            self.tail = None
        return temp
    
    def get(self,index:int):
        if not 0 <= index <= len(self):
            raise ValueError('Index out of range')
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
                
                
    def set_value(self,index,value):
        if not 0 <= index <= len(self):
            raise ValueError('Index out of range')
        temp = self.get(index)
        if temp:
            temp.data = value
            return True
        return False

    def insert(self,index,value):
        if not 0 <= index <= len(self):
            raise ValueError('Index out of range')
        if index == 0:
            return self.prepend(value)
        elif index == len(self):
            return self.append(value)
        temp = self.get(index-1)
        new_node = Node(value)

        new_node.next = temp.next
        temp.next = new_node
        return True
            
    def remove(self, index):
        if not 0 <= index <= len(self):
            raise ValueError('Index out of range')
        if index == 0:
            return self.pop_first()
        elif index == len(self)-1:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        return temp
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(len(self)):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
    def reverse2(self) -> None:
        """
        This reverses the linked list order.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first->second->third
        >>> linked_list.reverse()
        >>> linked_list
        third->second->first
        """
        prev = None
        current = self.head
        self.tail = current

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev
            
def main():
    some_nodes = [Node('Toronto'),
                  Node('Scarborough'),
                  Node('North York')]
    
    first_LL = LinkedList(some_nodes)
    
    print(first_LL)
    print(first_LL.head)
    print(first_LL.tail)
    first_LL.append('Markham')
    print(first_LL)
    poped = first_LL.pop()
    print(poped)
    print(first_LL)
    print(first_LL.head)
    print(first_LL.tail)
    first_LL.prepend('Markham')
    print(first_LL)
    print(first_LL.pop_first())
    print(first_LL)
    print(first_LL.get(1))
    first_LL.set_value(1,'Peel')
    print(first_LL)
    first_LL.insert(3,'Scarborough')
    print(first_LL)
    first_LL.remove(1)
    print(first_LL)
    first_LL.reverse2()
    print(first_LL)
    print(first_LL.tail)
    
    
if __name__ == "__main__":
    main()