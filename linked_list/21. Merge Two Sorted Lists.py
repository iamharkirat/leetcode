from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                # pointer l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                # pointer l2
            tail = tail.next

        # once out of loop pointers l1 & l2 are pointing at the remaining list
        tail.next = l1 if l1 else l2

        return dummy.next