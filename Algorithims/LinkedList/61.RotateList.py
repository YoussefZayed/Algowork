# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:

# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# Example 2:

# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL


class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)



def listLength(head):
  ''' helper method to get list Length '''
  cur = head
  count = 0
  while (cur):
      count += 1
      cur = cur.next
  return count


def rotateIterative(head, k):
  ''' main method, used multipass technique By Youssef '''

  if not head or k == 0  or not head.next :
    return head
  length = listLength(head)
  cur = head
  #finds new head
  for i in range(length- k%length):
    if cur.next:
      cur = cur.next
    else:
      cur = head
  newhead = cur

  #sets rest of list to after new head
  while (cur.next != newhead):
    if not cur.next:
      cur.next = head  
    cur = cur.next
  cur.next = None
  return newhead
    

head0 = Node(0, Node(1, Node(2)))
head1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
print(rotateIterative(head1, 2))
print(rotateIterative(head0, 4))
print(rotateIterative(head2, 5))