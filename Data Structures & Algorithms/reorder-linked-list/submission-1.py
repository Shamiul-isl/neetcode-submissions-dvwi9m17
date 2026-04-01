# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        seen = []
        newcur = head.next
        while newcur:
            seen.append(newcur)
            newcur = newcur.next
        left, right = 0, len(seen) - 1
        cur = head
        while left < right:
            cur.next = seen[right]
            cur = cur.next
            right -= 1
            cur.next = seen[left]
            cur = cur.next
            left += 1
            
        if left == right:
            cur.next = seen[left]
            cur = cur.next
        cur.next = None