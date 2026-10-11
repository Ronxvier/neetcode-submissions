# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        aux = ListNode()
        curraux = aux
        while curr1 is not None and curr2 is not None:
            if curr1.val >= curr2.val:
                curraux.next = curr2
                curraux = curraux.next
                curr2 = curr2.next
            elif curr1.val < curr2.val:
                curraux.next = curr1
                curraux = curraux.next
                curr1 = curr1.next
        curraux.next = curr1 if curr1 is not None else curr2
        return aux.next