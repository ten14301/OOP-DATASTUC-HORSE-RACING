class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return self.head    
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            return current
        
    def get_link_list(self, node):
        current = self.head
        count = 1
        while current and count < node:
            current = current.next
            count += 1
        if current:
            return current.data
        else:
            return None
        

    
