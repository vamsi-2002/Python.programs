def binary_convert(dec_1):
    number=int(dec_1)
    print("decimal number-",number,"binary number-",bin(number))
    
def hexa_convert(dec_1):  
    number=int(dec_1)
    print("decimal number-",number,"hexa number-",hex(number))

def octa_convert(dec_1):
    number=int(dec_1)
    print("decimal number-",number,"octal number-",oct(number))

dec_1=int(input("enter a decimal number"))
binary_convert(dec_1)
hexa_convert(dec_1)
octa_convert(dec_1)
