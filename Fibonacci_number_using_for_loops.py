n=int(input("Enter nth positon: "))
x=0
y=1
for i in range(0,n):
    print(x,end=" ")
    t=x
    x=y
    y=t+x
    
