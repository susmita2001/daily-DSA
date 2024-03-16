class node:
    def __init__(self,value):
        self.info=value
        self.prev=None
        self.link=None
class doubllylink:
    def __init__(self):
        self.start=None
    def insert_at_beginning(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
        else:  
            t=self.start
            self.start=n
            n.link=t
            t.prev=n
    def insert_at_end(self,value):
        t=node(value)
        temp=self.start
        while temp.link!=None:
            temp=temp.link
        t.prev=temp
        temp.link=t
        # t.link=None
    def insert_at_specifiedpos(self,value,pos):
        t=node(value)
        temp=self.start
        i=1
        while i<pos-1:
            temp=temp.link
            i=i+1
        a=temp.link
        t.link=a
        temp.link=t
        t.prev=temp

    def delete_at_start(self):
        temp=self.start
        self.start=temp.link
        item=temp.info
        temp.prev=None
        return item
    def delete_at_end(self):
        temp=self.start
        while temp.link!=None:

            temp=temp.link
       
        a=temp.prev
    
        a.link=None
        item=temp.info
        return item
    def delete_from_specificpos(self,pos):
        self.p=pos
        temp=self.start
        i=1
        while i<pos-1:
            temp=temp.link
            i=i+1
        item=temp.link.info
        a=temp.link.link
        temp.link=a
        a.prev=temp
        return item

    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.info,end=' ')
            # print(temp.prev,end=' ')
            temp=temp.link
ob=doubllylink()
ob.insert_at_beginning(3)
ob.insert_at_beginning(0)
ob.insert_at_beginning(4)
ob.insert_at_beginning(7)
ob.insert_at_beginning(6)
ob.insert_at_beginning(5)
ob.insert_at_specifiedpos(45,2)
ob.display()
print()
#ob.delete_from_specificpos(3)
#ob.delete_at_start()
ob.delete_at_end()
ob.display()


    