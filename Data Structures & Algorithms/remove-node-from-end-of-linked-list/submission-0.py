# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur, prev = head, None
        count = 0
        while cur:
            cur = cur.next
            count += 1
        
        remove_index = count - n
        curindex = 0
        cur = head
        while cur:
            if curindex < remove_index:
                curindex += 1
                prev = cur
                cur = cur.next
            else:
                temp = cur.next
                if prev != None:
                    prev.next = temp
                    break
                else:
                    return temp
        return head

