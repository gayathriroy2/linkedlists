class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_front(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print("prev_node not in list")
            return
        new_node=Node(new_data)
        new_node.next =prev_node.next
        prev_node.next=new_node

    def last_append(self,new_data):
        #new_node=Node(new_data)
        #if self.head is None:
        #    new_node=self.head
        #last=self.head
        #while last.next: #can be avoided if a empty node created at end
        #    last=last.next
        #last.next=new_node
        forth.data=new_data
    def delete(self,delete_node):
        tmp=self.head
        if tmp==delete_node:
            self.head=tmp.next
            tmp=None

        
        while tmp:
            if tmp.next==delete_node:
                tmp.next=delete_node.next
            tmp=tmp.next


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
    forth=Node(None)
    llist.head.next=second
    second.next=third
    third.next=forth
    #llist.printlist()
    #llist.insert_front(0)
    #llist.printlist()
    #llist.insert_after(second,4)
    #llist.insert_after(second.next,5)
    #llist.printlist()
    #llist.last_append(6)
    #llist.printlist()
    llist.delete(llist.head)
    llist.delete(second)
    llist.printlist()