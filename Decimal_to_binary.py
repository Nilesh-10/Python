def Decimaltobin(num):
    if num > 1:
        Decimaltobin(num//2)
    print(num%2,end="")    

a=int(input("Enter a number: "))
Decimaltobin(a)   
