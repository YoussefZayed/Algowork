# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val <= l2.val:
            head = l1
            node = l1
            l1 = l1.next
        else:
            head = l2
            node = l2
            l2 = l2.next
        startnode = node
        while l1 and l2:
            print(l1, l2)
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
            
        while l1:
            node.next = l1
            l1 = l1.next
            node = node.next
        while l2:
            node.next = l2
            l2 = l2.next
            node = node.next
        return head
                    
                    
        
        