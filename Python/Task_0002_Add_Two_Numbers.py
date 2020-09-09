# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_s = ''
        while l1:
            l1_s += str(l1.val)
            l1 = l1.next
        l2_s = ''
        while l2:
            l2_s += str(l2.val)
            l2 = l2.next
        l1_n = int(l1_s[::-1])
        l2_n = int(l2_s[::-1])
        sum = list(map(int, str(l1_n + l2_n)[::-1]))
        pn = None
        sll = None
        for ch in sum:
            cn = ListNode(ch)
            if sll is None:
                sll = cn
            if pn is not None:
                pn.next = cn
                pn = cn
        return sll