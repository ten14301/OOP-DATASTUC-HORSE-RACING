class queue:
    def __init__(self):
        self.items = []

    def is_empty(self) -> int:
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self) -> str or None:
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self) -> int:
        return len(self.items)
    
    def clear(self):
        while not self.is_empty():
            self.dequeue()
class typequeue(queue):
    def __init__(self):
        super().__init__() 


