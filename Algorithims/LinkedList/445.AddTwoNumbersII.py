# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len1 = self.getLen(l1)
        len2 = self.getLen(l2)
        
        if len1 > len2:
            a = l1
            b = l2
            dif = len1-len2
            maxlen = len1
        else:
            a = l2
            b = l1
            dif = len2-len1
            maxlen = len2
        
        head = ListNode(0,a)
        prev = head
        for i in range(maxlen):
            if i >= dif:
                a.val += b.val
                if a.val >= 10:
                    a.val -= 10
                    prev.val += 1
                    
                b = b.next
            a = a.next
            prev =prev.next

        while self.has10(head):
            self.remove10(head)
        
        return head.next if head.val == 0 else head
    
    def getLen(self,head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    def has10(self,head):
        while head:
            if head.val == 10:
                return True
            head = head.next
        return False
    
    def remove10(self,head):
        prev = head
        head = head.next
        while head:
            if head.val >= 10:
                head.val -= 10
                prev.val += 1
            prev = head
            head =head.next
    