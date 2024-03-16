class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class stack:
    def __init__(self):
        self.start=None
        self.top=None
    def push(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
            self.top=n
        
        else:
            self.top.link=n
            self.top=n
    def pop(self):
        if self.start==None:
            print("stack is empty")
        elif self.start==self.top:
            p=self.top
            item=self.top.info
            self.start=None
            self.top=None
            del p
            return item
        else:
            temp=self.start         
            while temp.link!=self.top:
                    temp=temp.link
            temp.link=None
            q=self.top
            self.top=temp
            item=q.info
            del q
            return item
    def display(self):
        if self.top==None:
            print("stack is empty")
        temp=self.start
        while temp!=self.top:
            print(temp.info,end=" ")
            temp=temp.link
        print(temp.info)
ob=stack()
ob.push(9)
ob.push(23)
ob.push(34)
ob.push(67)
ob.display()
print()
ob.pop()
ob.display()