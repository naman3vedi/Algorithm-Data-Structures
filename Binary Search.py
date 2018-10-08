a=[23,45,56,98,125,571]
val=int(input("Enter the value you want to search : "))
"Algorithm for Binary search"
mid=int(len(a)//2)
for i in range(mid):
    if val==a[mid]:
         print(mid)
         break
    elif val>a[mid]:
        mid+=1
    elif val<a[mid]:
        mid-=1
    