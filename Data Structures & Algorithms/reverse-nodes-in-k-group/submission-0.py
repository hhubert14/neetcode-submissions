# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        def findKth(node):
            nonlocal k
            for i in range(k):
                node = node.next
                if not node:
                    return None
            return node
        prev = dummy
        prevGroup = prev
        curr = head
        while True:
            kthNode = findKth(prevGroup)
            if not kthNode:
                return dummy.next
            kthNodeAfter = kthNode.next
            for i in range(k):
                after = curr.next
                if i == 0:
                    curr.next = kthNodeAfter
                    nextIt = curr
                else:
                    curr.next = prev
                prev = curr
                curr = after
            prevGroup.next = prev
            prevGroup = nextIt
            prev = prevGroup
            curr = prev.next
        return ListNode(-1)


