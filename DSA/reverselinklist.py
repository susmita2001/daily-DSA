class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class slink:
    def __init__(self):
        self.start=None
    def insert_at_beginning(self,value):
        n1=node(value)
        n1.link=self.start
        self.start=n1
    def insert_at_end(self,value):
        t=node(value)
        temp=self.start
        while temp.link!=None:
            temp=temp.link
        temp.link=t
    def delete_start_node(self):
        temp=self.start
        self.start=temp.link
        item=temp.info
        del temp
        return item
    def delete_last_node(self):
        temp=self.start
        while temp.link!=None:
            previous=temp
            temp=temp.link
        item=temp.info
        del temp
        previous.link=None
        return item
    def insert_at_specifiedposition(self,value):
        self.pos=3
        i=1
        n=node(value)
        temp=self.start
        while i<self.pos:
            previous=temp
            temp=temp.link
            i=i+1
        previous.link=n
        n.link=temp
    def insert_after_specificitem(self,value,item):
        
        temp=self.start
        a=node(value)
        while temp.link!=None and temp.info!=item:
            
            temp=temp.link
        
        a.link=temp.link
        temp.link=a
    def delete_at_specifiedpos(self):
        self.pos=4
        i=1
        temp=self.start
        while i<self.pos:
            previous=temp
            temp=temp.link
            i=i+1
        item=temp.info
        previous.link=temp.link
        del temp
        return item
    def delete_specified_item(self,item):
        temp=self.start
        while temp.link!=None and temp.info!=item:
            previous=temp
            temp=temp.link
        value=temp.info
        previous.link=temp.link
        del temp
        return value
    def reverse(self):
        c=None
        n=self.start
        while n!=None:
            t=n.link
            n.link=c
            c=n
            n=t
        self.start=c

    def display(self):
        temp=self.start
        while temp!=None:

            print(temp.info,end=" ")
            temp=temp.link
    

lst=slink()

lst.insert_at_beginning(35)
lst.insert_at_beginning(45)
lst.insert_at_beginning(75)
lst.insert_at_beginning(89)
lst.insert_at_end(60)
lst.insert_at_end(78)
lst.display()
lst.insert_after_specificitem(67,45)
#lst.display()
print()
#print(lst.delete_specified_item(75))

#lst.delete_at_specifiedpos()
# b=lst.delete_start_node()
# print(b)
lst.display()
print()
lst.reverse() 
lst.display()



    
    

  

