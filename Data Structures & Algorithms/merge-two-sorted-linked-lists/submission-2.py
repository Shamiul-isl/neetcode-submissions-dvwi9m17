# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = list1, list2
        if not list1 and not list2:
            return None
        # elif list1 and not list2:
        #     return list1
        # elif not list1 and list2:
        #     return list2
        # else:
        #     head = list1 if list1.val <= list2.val else list2
        
        res = ListNode()
        cur = res
        while left and right:
            temp = None
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left != None:
            cur.next = left
        if right != None:
            cur.next = right
        return res.next
            
        
