class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,value):
        n=node(value)
        if self.front==None:
            self.front=n
            self.rear=n
        else:
            self.rear.link=n
            self.rear=n
    def dequeue(self):
        if self.front==None and self.rear==None:
            print("queue is empty")
        elif self.front==self.rear:
            q=self.front
            item=self.front.info
            del q
            self.front=None
            self.rear=None
            return item
        else:
            p=self.front
            item=p.info
            self.front=p.link
            del p
            return item
    def display(self):
        if self.front==None and self.rear==None:
            print("empty")
        else:
            temp=self.front
            while temp!=self.rear:
                print(temp.info,end=' ')
                temp=temp.link
            print(temp.info)
ob=queue()
# ob.enqueue(34)
# ob.enqueue(90)
# ob.enqueue(6)
ob.enqueue(4)
ob.display()
ob.dequeue()
ob.display()

 
 
