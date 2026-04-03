# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        """
        two pointer: one fast, one slow

        i iterates once
        j iterates every other
        if i and j meet, then there is a cycle
        
        if j reaches the tail, then there is no cycle
            this is because j is the fast pointer, it can get to the end of the list faster and determine if there is an end
        """
        i = head
        j = head

        while j and j.next: 
            i = i.next
            j = j.next.next

            if i == j:
                return True

        return False

