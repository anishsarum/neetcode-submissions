
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev