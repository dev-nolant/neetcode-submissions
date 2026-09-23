class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def get(self, index: int) -> int:
        curr = self.head

        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next

        if curr is None:
            return -1

        return curr.val



    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode


    def insertTail(self, val: int) -> None:
        newNode = ListNode(val) # make new node with the new val

        # new ll? place tail as first and only node
        if self.head is None:
            self.head = newNode
            return

        # if not new, establish current as head, then search until you reach
        # a None value (tail), place newNode as new tail
        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = newNode


    def remove(self, index: int) -> bool:

        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head

        count = 0

        while curr.next is not None:
            if count + 1 == index:
                curr.next = curr.next.next
                return True

            curr = curr.next
            count += 1

        return False


    def getValues(self) -> List[int]:

        pList = []

        curr = self.head

        while curr is not None:
            pList.append(curr.val)
            curr = curr.next

        return pList

