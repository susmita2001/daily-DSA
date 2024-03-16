class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class clinklist:
    def __init__(self):
        self.start=None
    def insert_at_biginning(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
            n.link=self.start
        else:
            p=self.start
            self.start=n
            n.link=p
            s=p
            while p.link!=s:
                p=p.link
            p.link=self.start
    def insert_at_end(self,value):
        t=node(value)
        temp=self.start
        s=temp
        while temp.link!=s:
            temp=temp.link
        temp.link=t
        t.link=s
    def delete_start(self):
        p=self.start
        self.start=p.link
        s=p
        while p.link!=s:
            p=p.link
        p.link=self.start
        item=s.info
        del s
        return item
    
    def display(self):
        if self.start==None:
            print("Empty")
        else:
            temp=self.start
        
            while temp!=None and temp.link!=self.start:
                print(temp.info,end=' ')
                temp=temp.link
            print(temp.info)
ob=clinklist()
ob.display()
ob.insert_at_biginning(5)
ob.insert_at_biginning(90)
ob.insert_at_end(78)
ob.delete_start()
ob.display()