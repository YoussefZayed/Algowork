# Write a program to find the node at which the intersection of two singly linked lists begins.

# For example, the following two linked lists:

# begin to intersect at node c1.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA =headA
        curB =headB
        tailA = None
        tailB = None
        
        while curB and curA:
            
            if curA == curB:
                return curA
            
            if not curA.next:
                tailA = curA
                curA = headB
            else:
                curA = curA.next
            if not curB.next:
                tailB = curB
                curB = headA
            else:
                curB = curB.next
            if tailA and tailB and not tailA == tailB:
                return None
            
                