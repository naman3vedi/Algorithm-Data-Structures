x=[2,25,34,56,72,34,54]
val=int(input("Enter the value you want to get searched : "))
for i in x:
    if i==val:
        print(x.index(i))
        break
    elif x.index(i)==(len(x)-1) and i!=val:
        print("The Val u want to search is not there in the list")





