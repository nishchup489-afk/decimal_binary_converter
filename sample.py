print("""
1) Decimal to binary
2) Binary to decimal
""")

choice = int(input("Choose any(1/2) :  "))



def DtB(number):
    binary_digits = []

    if number == 0:
        print("number should be greater than 0")
    
    while number > 0:
        remainder = number % 2
        binary_digits.append(str(remainder))
        number //= 2

    return binary_digits

def BtD(n):
    binary_n = n 
    decimal = 0

    if n == 0:
        print("Binary : 0")
    
    if not all(bit in '01' for bit in binary_n):
        raise ValueError("Input must be a binary string containing only 0s and 1s.")
    
    binary_n = binary_n[::-1]


    for i , bit in enumerate(binary_n):
        decimal += int(bit) * (2 ** i)
    

    return decimal


if __name__ == '__main__':
    if (choice == 1):
        number = int(input("Enter your Decimal number :  "))
        binary = DtB(number)
        print(binary)
    elif (choice == 2):
        try:
            number = input("Enter your Binary number : ")
        except ValueError:
            print("you jerk binary only contains 0 and 1")
        decimal = BtD(number)
        print(decimal)
    else:
        print("shit (0/1)")
    

    

    
