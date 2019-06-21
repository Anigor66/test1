l=[5,3,8,4,7,2]
n=int(input("Enter a number: "))
try:
    s=[]
    for i in range(len(l)-(n-1)):
        sum=l[i]
        for j in range(1,n):
            sum+=l[i+j]
        #print(sum)
        s.append(sum)
    print(max(s))
except (ValueError):
    print("Value Error. Reduce n!")

    
