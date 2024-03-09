n=int(input("enter"))
a=n
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if a == sum1:
    print("The given number", a, "is armstrong number")
else:
    print("The given number", a, "is not armstrong number")