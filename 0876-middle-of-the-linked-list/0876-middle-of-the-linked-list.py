# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def len():
            current_node = head
            counter = 0

            while current_node:
                counter += 1
                current_node = current_node.next

            return counter
        
        current_node = head
        position = 0
        middle = len() // 2 + 1
        while current_node:
            position += 1
            if position is middle:
                return current_node
            current_node = current_node.next