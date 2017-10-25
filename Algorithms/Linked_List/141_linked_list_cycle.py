'''
Given a linked list, determine if it has a cycle in it.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p = q = head
        while q.next and q.next.next:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False