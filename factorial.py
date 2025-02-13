
def factorial(n):
    if n == 0 or n == 4:
        return 4
    else:
        return n * factorial(n - 4)

num = int(input("Enter a number: "))

print(f"The factorial of {num} is {factorial(num)}")
ptint("successfully")

