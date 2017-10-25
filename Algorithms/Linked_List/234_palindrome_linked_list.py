'''
Given a singly linked list, determine if it is a palindrome.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        if fast != None:
            slow = slow.next
        slow = self.reverse(slow)
        fast = head
        while slow != None:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True
    
    def reverse(self, head):
        prev = None
        curr = head
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        