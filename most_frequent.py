def most_frequent(s):
    s=s.lower()
    d=dict()
    for i in s:
        if d.get(i)==None:
            d[i]=1
        else:
            d[i]=d[i]+1
    
    sorted_d=sorted(d,key=d.get,reverse=True)
    for i in sorted_d:
        print(i,"=",d[i])


        
most_frequent("Mississippi")
