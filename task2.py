n=int(input("Enter length of string "))
k=int(input("Enter number of characters "))
s=input("Enter string ")
listc=[]
c=input("Enter characters ")
listc=c.split()
#Define factorial function
def fact(z):
    factorial=1
    for i in range(1, z+1):
        factorial=factorial*i
    return factorial

count=0
count2=0
sum1=0
for i in range(n):
    if s[i] in listc:
        count=count+1
        count2=0
        if i==n-1:
            #Factorial of count
            sum1=sum1+fact(count)
    else:
        count2=count2+1
        #Factorial of count
        if count2<2:
            sum1=sum1+fact(count)
            count=0
print("Required number of subsets =", sum1)