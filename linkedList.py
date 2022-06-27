class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return f"Node({self.data})"
    
class LinkedList:
    def __init__(self,nodes:list[Node]) -> None:
        self.head  = None
        self.tail = None
        if nodes:
            node =nodes[0]
            self.head = nodes[0]
            for obj in nodes[1:]:
                node.next = obj
                node = obj
            self.tail = node
    
    def __iter__(self):
        
        temp = self.head
        while temp:
            yield temp
            temp = temp.next
    
    def __repr__(self) -> str:
        return '->'.join([str(item) for item in iter(self)])

    def __len__(self):
        return tuple(self)

    def append(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            self.tail = temp  
        else:
            self.tail.next = temp
            self.tail = temp
            
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
    
if __name__ == "__main__":
    main()