class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self) -> int:
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self) -> str or None:
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def peek(self) -> str or None:
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    def size(self) -> int:
        return len(self.items)
    
    
    def clear(self):
        while not self.is_empty():
            self.pop()