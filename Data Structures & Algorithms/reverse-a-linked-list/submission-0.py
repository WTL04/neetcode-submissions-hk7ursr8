# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse and store tail
        curr = head
        prev = None
        while curr:

            # save current next as temp 
            temp = curr.next

            # by pointing current to previous, we reverse it 
            curr.next = prev

            # move prev forwards
            prev = curr

            # move current forwards
            curr = temp

        # prev is the new head of the reversed list
        return prev
        