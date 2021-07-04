class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def delete(self,pos):
        tmp=self.head
        if pos==0:
            self.head=tmp.next
            tmp=None

        po=1
        
        while (tmp):
            
            prev=tmp    
            tmp=tmp.next
            
            if po==pos:
                prev.next=tmp.next
                tmp=None
            po+=1
    def printlist(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next
if __name__=='__main__':
    llist=Linkedlist()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    llist.head.next=second
    second.next=third
    #llist.delete(2)
    llist.printlist()

