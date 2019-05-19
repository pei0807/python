# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Definition for singly-linked list.

from list_node import ListNode

def main():
    w=ListNode(1)
    x=ListNode(2)
    y =ListNode(3)
    z = ListNode(4)
    w.next = x
    x.next = y
    y.next = z
    print(w.val)
    print(w.next.val)
    print(w.next.next.val)
    print(w.next.next.next.val)

    swap(w)
    print(w.val)
    print(w.next.val)
    print(w.next.next.val)
    print(w.next.next.next.val)

def swap(x):

    temp = x.val
    temp2 = x.next.val
    x.val = temp2
    x.next.val = temp

    if x.next.next== None:
        return x
    else:
        swap(x.next.next)
        return x

main()

