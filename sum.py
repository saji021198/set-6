N=int(input())
sum=0
i=0
while(N>0):
    i=N%10
    sum=sum+i
    N=N//10
print(sum)
