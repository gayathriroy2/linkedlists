#using tortoise and hare algo
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circular:
    def __init__(self):
        self.head=None
    def split(self):
        fast=self.head
        slow=self.head
        pre=self.head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            pre=slow
            slow=slow.next
        if fast==None:
            print("MEDIAN:",slow.data)
        else:
            print("MEDIAN:",(slow.data+pre.data)/2)

