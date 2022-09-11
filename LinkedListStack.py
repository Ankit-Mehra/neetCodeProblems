from pandas import value_counts


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None