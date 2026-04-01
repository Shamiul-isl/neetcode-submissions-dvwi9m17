# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        
        turtle, hare = head.next, head.next.next
        while turtle and hare:
            if turtle == hare:
                return True
            turtle = turtle.next
            if not hare.next or not hare.next.next:
                break
            hare = hare.next.next
        
        return False
        
        