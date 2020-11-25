x=int(input("Enter the distance between any two petrol pumps on the road : "))
y=int(input("Enter the distance where you find your gas is running low : "))
z=int(input("Enter the distance you can travel on the remaining gas : "))
a=y//x
b=x*(a+1)
if (z<=b-y):
    print("NO")
elif (z>b-y):
    print("YES")
else:
    print("Invalid input, please try again")