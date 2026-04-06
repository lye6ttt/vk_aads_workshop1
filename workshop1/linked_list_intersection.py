class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_intersection(head1: ListNode, head2: ListNode) -> ListNode:
    if not head1 or not head2:
        return None

    p1 = head1
    p2 = head2

    while p1 != p2:
        p1 = p1.next if p1 else head2
        p2 = p2.next if p2 else head1

    return p1

if __name__ == "__main__":
    tail = ListNode(7, ListNode(8, ListNode(9)))
    head1 = ListNode(1, ListNode(2, ListNode(3, tail)))
    head2 = ListNode(4, ListNode(5, tail))
    print(find_intersection(head1, head2).val)

    head3 = ListNode(4, ListNode(5, ListNode(3)))
    print(find_intersection(head1, head3))