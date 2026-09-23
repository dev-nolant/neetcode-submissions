class DynamicArray:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.size = 0

        self.dynArray = [None] * capacity


    def get(self, i: int) -> int:
        return self.dynArray[i]



    def set(self, i: int, n: int) -> None:
        self.dynArray[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.dynArray[self.size] = n
        self.size += 1



    def popback(self) -> int:
        value = self.dynArray[self.size - 1]
        self.dynArray[self.size - 1] = None
        self.size -= 1

        return value



    def resize(self) -> None:
        self.capacity *= 2

        newArray = [None] * self.capacity

        for i in range(self.size):
            newArray[i] = self.dynArray[i]

        self.dynArray = newArray

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
