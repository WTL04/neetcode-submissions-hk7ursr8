# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of linked list
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        # determine index of node to remove (0th indexed)
        position = length - n

        # remove head
        if position == 0:
            return head.next

        # go to middle nodes
        curr = head
        for _ in range(position - 1):
            curr = curr.next

        # remove node
        curr.next = curr.next.next

        return head



