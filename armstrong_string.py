def is_armstrong(num):
	num_str = str(num)
	n = len(num_str)
	sum = 0
	for digit in num_str:
		sum += int(digit)**n
	if sum == num:
		return True
	else:
		return False
num=int(input("enter a number"))
print("number entered is",is_armstrong(num))
