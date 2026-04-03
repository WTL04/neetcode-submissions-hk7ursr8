# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """
        Goal: create a new linked list with a dummy node, compare the values and append values to this dummy node.
        """
        dummy = ListNode()
        node = dummy 

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next # move list1 pointer
            else:
                node.next = list2
                list2 = list2.next # move list2 pointer

            node = node.next # move node pointer
        
        # add any remaining nodes
        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return dummy.next # head of merged list is dummy.next

      
