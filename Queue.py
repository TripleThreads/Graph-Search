class Queue:
    def __init__(self):
        self.__elements = []

    def peek(self):
        if not self.is_empty():
            return self.__elements[0]
        return None

    def enqueue(self, *val):
        for v in val:
            self.__elements.append(v)
    
    def deque(self):
        if not self.is_empty():
            value = self.__elements[0]
            self.__elements.remove(self.__elements[0])
            return value
        return None

    def clear(self):
        self.__elements = []

    def is_empty(self):
        if len(self.__elements) == 0:
            return True
        return False

    def length(self):
        return len(self.__elements)


