class stack:
    def __init__(self):
        self.top=-1
        self.lst=[]
        self.size=5


    def push(self,item):
        if self.top==self.size-1:
            print('stack is full')
            return
        self.top=self.top+1
        self.lst.append(item)
    def pop(self):
        if self.top==-1:
            print('stack is empty')
            return
        item=self.lst[self.top]
        self.top=self.top-1
        return item
    def display(self):
        if self.top==-1:
            print('stack is empty')
        else:
            i=0
            while i<=self.top:
                print(self.lst[i],end=" ")
                i=i+1
    def peek(self):
        return self.lst[-1]
        
st=stack()
st.push(10)
st.push(20)
st.push(100)
st.display()
print()
print(st.pop())
print()
st.display()

