class Node ():
  def __init__( self,val=0, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    return str(self.val) +"->"+ str(self.next)


# "Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# Example:
# 1->2->3->4 -> 5
# 2->1->4->3 -> 5.
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# "


head1 = Node(1,Node(2,Node(3,Node(4,Node(5)))))
head2 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))


def swapPairsRecursive(head):
  '''Made by Halley Ding in a very quick mannor'''
  if not head or not head.next:
    return head
  
  n1, n2 = head, head.next
  n1.next = swapPairsRecursive(n2.next)
  n2.next = n1
  return n2

def swapPairsIterative(head):
  ''' This method uses the multiple pointer method Made by Youssef'''
  if not head or not head.next:
    return head
  newhead = head.next
  prev = Node(0,head)
  cur = head
  
  while (cur and cur.next): 
    temp = cur.next
    cur.next = cur.next.next
    temp.next = cur
    prev.next = temp
    prev = cur 
    cur = cur.next
    
  return newhead




#Tests
print("input",head1)
print("result swapPairsRecursive:",swapPairsRecursive(head1))

print("input",head2)
print("result swapPairsRecursive:",swapPairsRecursive(head2))

head1 = Node(1,Node(2,Node(3,Node(4))))
head2 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))

print("input",head1)
print("result swapPairsIterative:",swapPairsIterative(head1))

print("input",head2)
print("result swapPairsIterative:",swapPairsIterative(head2))

