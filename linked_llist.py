class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def length(self):
        len=0
        tmp=self.head
        
        while tmp:
            len+=1
            tmp=tmp.next
        print(len)

#recursive
        def getCountRec(self, node):
            if (not node): # Base case
                return 0
            else:
                return 1 + self.getCountRec(node.next)
 
    # A wrapper over getCountRec()
        def getCount(self):
            return self.getCountRec(self.head)
if __name__=='__main__':
    llist=Linkedlist()
    llist.head=Node(1)
    sec=Node(2)
    third=Node(3)
    llist.head.next=sec
    sec.next=third
    llist.length()
         
