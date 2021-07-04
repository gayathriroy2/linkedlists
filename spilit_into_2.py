class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circular:
    def __init__(self):
        self.head=None
    
    def split(self,head1,head2):
        fast=self.head
        slow=self.head
        
        while fast.next!=self.head and fast.next.next!=self.head:
            fast=fast.next.next
            slow=slow.next
        if fast.next.next==self.head:  #even
            fast=fast.next
        head1.head=self.head
        if self.head.next != self.head:
            head2.head=slow.next
        fast.next=slow.next
        slow.next=self.head


