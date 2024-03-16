class graph:
    def __init__(self,row,col):
        self.adj=[]
        self.row=row
        self.column=col

    def creatematrix(self):
        for i in range(self.row):
            a=[]
            for j in range(self.column):
        #a.append(f"{row}{column}")
                a.append(0)
            self.adj.append(a)
    def adjmatrix(self,list):
         for i in list:
              self.adj[i[0]][i[1]]=1
    def outdegree(self):
         outdegree_lst=[]
         for i in self.adj:
              k=0
              for j in i:
                   k=k+j
              outdegree_lst.append(k)
         print(outdegree_lst)
    def indegree(self):
         indegree_lst=[]
         for i in range(len(self.adj)):
            k=0
            for j in range(len(self.adj)):
                if self.adj[j][i]==1:
                     k=k+1
            indegree_lst.append(k)
         print(indegree_lst)      
    def display(self):
                for row in range(6):
                    for col in range(6):
                        print(self.adj[row][col],end=' ')
                    print()
l=[(0,1),(0,2),(1,2),(1,3),(2,4),(3,5),(4,5)]
ob=graph(6,6)
ob.creatematrix()
ob.adjmatrix(l)
ob.display()
ob.outdegree()
ob.indegree()