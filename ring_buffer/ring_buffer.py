class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.pointer = 0

    def append(self, item):
        if len(self.storage) < self.pointer + 1:
           self.storage.append(item)
        else:
           self.storage[self.pointer] = item
    
        self.pointer = (self.pointer + 1) % self.capacity

    def get(self):
        return self.storage


