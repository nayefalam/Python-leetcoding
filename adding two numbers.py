#adding two numbers

class Solution(object):
    def addTwoNumberstest(self, l1, l2):
        l1 = []
        l2 = []
        lfinal = l1 + l2
        return lfinal
    
    def addTwoNumbers1(self, l1, l2):
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(l1, l2):
            #here we will be using a completely different approach
            #because we also have take in consideration carry, which is either 0 or 1
            # when there is a 9 + 1 it need to be 10 -> [9,5] + [1,2] = 59 + 21 = 80 = [0, 8] 
            #the range of the node should be [1,100] - 0 <= node.val <= 9
            #also to keep some points in mind we are going to loop this shit with some crazy socialnetwork maain character energy
            #we are looping since we are taking each number and adding like how we add numbers in min remember we are breaking each bit by bit and adding from scratch and whatever we do in brain step by step we
            #are implementing that in rhis algorithm

        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2:
            # Get the values of the current nodes (if available)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum of current digits and the carry from the previous step
            _sum = x + y + carry

            # Update carry for the next calculation
            carry = _sum // 10

            # Create a new node with the sum % 10 as its value and move the current pointer
            current.next = ListNode(_sum % 10)
            current = current.next

            # Move to the next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # If there's a carry left after the loop, create an additional node
        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next


    
def main():
    sol = ListNode()
    l1 = [1,2,3]
    l2 = [2,5,7]

    result = sol.addTwoNumbers(l1, l2)
    print(result)
