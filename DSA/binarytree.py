class node:
    def __init__(self,value):
        self.key=value
        self.left=None
        self.right=None
class binary_tree:
        def __init__(self):
            self.root=None
        def createbst(self,lst):
            for item in lst:
                n=node(item)
                if self.root==None:
                    self.root=n
                else:
                    temp=self.root
                    par=None
                    while temp!=None:
                        if item<temp.key:
                            par=temp
                            temp=temp.left
                        else:
                            par=temp
                            temp=temp.right
                    if item<par.key:
                        par.left=n
                    else:
                        par.right=n
        def search(self,item):
            temp=self.root
            par=None
            while temp!=None:
                if item==temp.key:
                    print("item found")
                    return temp ,par
                
                else:
                    if(item<temp.key):
                        par=temp
                        temp=temp.left
                    else:
                        par=temp
                        temp=temp.right
            print("item not found")
        
        def height(self,T):
            if T==None:
                return 0
            else:
                return max(self.height(T.left),self.height(T.right))+1
            
        def delete(self,item):
            t,n=self.search(item)
            temp=t
            par=n
            while temp!=None:
                if t.left==None and t.right ==None:
                    print("no child")
                    par.left=None
                    par.right=None
                    del temp
                    return
                elif t.left==None and t.right !=None:
                    print("one child exist")
                    child=t.right
                    print(child.key)
                    if par.key>child.key:
                        par.left=child
                        del temp
                        return
                    else:
                        par.right=child
                        del temp
                        return
                elif t.left!=None and t.right ==None:
                    print ("one child exits") 
                    child=t.left
                    print(child.key)
                    if par.key>child.key:
                        par.left=child
                        del temp
                        return
                    else:
                        par.right=child
                        del temp
                        return
                else:
                    print("2 child")
                    parinuscc=temp
                    insucc=temp.right
                    while insucc.left!=None:
                        parinuscc = insucc
                        insucc = insucc.left
                    key1=insucc.key
                    if insucc==parinuscc.left:
                        parinuscc.left=None
                    else:
                        parinuscc.right=None
                        del insucc.key
                        temp.key=key1
        

        def preorder(self,T):
            if T!=None:
                print(T.key)
                self.preorder(T.left)
                self.preorder(T.right)
        def inorder(self,T):
            if T!=None:
                self.inorder(T.left)
                print(T.key)
                self.inorder(T.right)
        def postorder(self,T):
            if T!=None:
                self.postorder(T.left)
                self.postorder(T.right)
                print(T.key)

l=[100,50,90,130,110,150,120,30,20,45,131,140,115,105]
ob=binary_tree()
ob.createbst(l)
# print(ob.search(50))
# # print(ob.root.left.key)
# print("preorder of the tree: ")
# ob.preorder(ob.root)
# print("postorder of the tree:")
# ob.postorder(ob.root)
# print("inorder of the tree: ")
# ob.inorder(ob.root)
# print("height of the tree: ")
# print(ob.height(ob.root))
ob.delete(50)
print("inorder of the tree: ")
ob.inorder(ob.root)


