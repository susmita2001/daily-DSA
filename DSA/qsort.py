
def quicksort(list,l,h):
    if l<h:
        piv=quick(list,l,h)
        quicksort(list,l,piv-1)
        quicksort(list,piv+1,h)
def quick(list,l,h):
    piv=l
    lt=l+1
    rt=h
    while(True):
        while lt<=rt and list[piv]<=list[rt]:
            rt=rt-1
        if lt>rt:
            return piv

        if list[piv]>list[rt]:
            list[piv],list[rt]=list[rt],list[piv]
            piv=rt
            rt=rt-1
        while lt<=rt and list[piv]>=list[lt]:
            lt=lt+1
        if lt>rt:
            return piv

        if list[piv]<list[lt]:
            list[piv],list[lt]=list[lt],list[piv]
            piv=lt
            lt=lt+1

lst=[20,10,28,16,56,6,89,90,67,1,4,5]
p=quicksort(lst,0,len(lst)-1)
print(lst)
            
