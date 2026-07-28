# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current_node = result
        total = 0
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            total = num1 + num2 + carry
            carry = total // 10 
            total = total % 10

            current_node.next = ListNode()
            current_node = current_node.next
            current_node.val = total

            if l1 is not None:
                l1 = l1.next
            
            if l2 is not None:
                l2 = l2.next

        return result.next

