# A single node of a singly linked list
class Node:
    #constructor
    def __init__(self, data, next=None):
        self.data=data
        self.next= next
        
        
# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head= None
        
#linkedlist node
LL= LinkedList()
LL.head= Node("Jack")

print(LL.head.data)