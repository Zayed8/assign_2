# For Arithmetic Operator =>
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
print(f"Addition of {num1} and {num2} is: ", num1 + num2)
print(f"Subtraction of {num1} and {num2} is: ", num1 - num2)
print(f"Multiplication of {num1} and {num2} is: ", num1 * num2)
print(f"Exponentation of {num1} and {num2} is: ", num1 ** num2)
print(f"Division of {num1} and {num2} is: ", num1 / num2)
print(f"floor division of {num1} and {num2} is: ", num1 // num2)
print(f"Modulus of {num1} and {num2} is: ", num1 % num2)

# For Assigment Operator =>
num = int(input("Enter first Number: "))
num+=2
print(" += : ", num)
num-=2
print(" -= : ", num)
num*=2
print(" *= : ", num)
num**=2
print(" **= : ", num)
num/=2
print(" /= : ", num)
num//=2
print(" //= : ", num)
num%=2
print(" %= : ", num)

# For Comparison Operator =>
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
print(" == ", num1 == num2)
print(" != ", num1 != num2)
print(" >= ", num1 >= num2)
print(" <= ", num1 <= num2)
print(" > ", num1 > num2)
print(" < ", num1 < num2)

# For Logical Operator =>
n1 = True
n2 = False
print(" and ", n1 and n2)
print(" and ", n1 or n2)
print(" not ", not n1)

# For Bitwise Operator =>
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
print(" & ", num1 & num2)
print(" | ", num1 | num2)
print(" ^ ", num1 ^ num2)
print(" << ", num1 << num2)
print(" >> ", num1 >> num2)

# For Identity Operator =>
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
print(" is ", num1 is num2)
print(" is not ", num1 is not num2)

# For Membership Operator =>
x = "HelloWorld"
print(" in ","W" in x)
print(" not in ","W" not in x)