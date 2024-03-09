#zero division error

def reciprocal(num1):
    try:
        reci=1/num1
    except ZeroDivisionError:
        print("can not be divided by zero")

    else:
        print(reci)
reciprocal(3)
reciprocal(0)            

