l1 = [2, 4, 3]
l2 = [5, 6, 4]
outList = []

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy

        strL1 = ""
        strL2 = ""
        while l1:
            strL1 = str(l1.val) + strL1
            l1=l1.next


        while l2:
            strL2 = str(l2.val) + strL2
            l2=l2.next

        nitls = str(int(strL2) + int(strL1))

        llol = [int((nitls[char])) for char in range(len(str(nitls)) - 1, -1, -1)]

        for char in range(len(str(nitls)) - 1, -1, -1):
            dummy.next = ListNode(char)
            dummy = dummy.next
        return dummy
