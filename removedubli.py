lt=[]
print("enter the limit of list")
n=int(input())
for i in range(0,n):
    d=int(input())
    lt.append(d)

print(lt)
print(list(set(lt)))
