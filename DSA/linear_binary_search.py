# class linear_search:
#     def __init__(self,a,n):
#         self.list=a
#         self.item=n
#     def result(self):
#         i=0
#         while i<len(self.list):
#             if self.item==self.list[i]:
#                 print("the position:",i)
#                 break
#             i+=1
#         if i==len(self.list):
#             return -1
# l=[1,6,8,5]
# input=8
# ob=linear_search(l,input)
# ob.result()
                   

# class linearsearch:
#     def create_list(self):
#         st=input('Enter list of integers: ')    
#         l=st.split()
#         self.l= [int(i)for i in l]
#     def search(self):
#         n=int(input("Enter the number: "))
#         i=0
#         while i<len(self.l):
#             if n==self.l[i]:
#                 print('position: ',i)
#                 break
#             i=i+1
#         if i==len(self.l):
#             return -1
# ob=linearsearch()
# ob.create_list()
# b=ob.search()
# print(b)


class binary_search:
    def __init__(self,l,n):
         self.list=l
         self.item=n
     
    def search(self):
        
        l=0
        h=len(self.list)-1
        while l<=h:
            mid=(l+h)//2
            if self.item==self.list[mid]:
                print('position',mid)
                break
            if self.item<self.list[mid]:
                h=mid-1
            elif self.item>self.list[mid]:
                l=mid+1
        if l>h:
                print('-1')

    def display(self):
         print(self.list)
         
l=[20,28,30,40,48,59,60,78,82,98,99]
ob=binary_search(l,59)

ob.display()
ob.search()



