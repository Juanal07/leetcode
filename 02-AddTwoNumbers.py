from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
         return str(self.val)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lSol=ListNode()
        mellevo=0
        while l1.next!=None and l2.next!=None:
            lAux=l1.val+l2.val
            lNodeAux=ListNode(lAux)
            lSol.next(lNodeAux)
        print(lSol)








        
Solution.addTwoNumbers('hi',ListNode(),ListNode())
