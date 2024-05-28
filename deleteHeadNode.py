def deleteHeadNode(head):
    if head == None:
        return head
    secondNode = head.next
    head.next = None
    return secondNode