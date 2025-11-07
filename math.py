print("MATH UTILITY TOOL")

while True:
    print("\n1. Factorial")
    print("2. Check Prime Number")
    print("3. Sum of Digits")
    print("4. Even/Odd")
    print("5. Exit")

    n = input("Enter your choice: ")

    if n == "1":
        # factorial logic
        num = int(input("Enter number: "))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print("Factorial of number is", fact)

    elif n == "2":
        # prime logic
        num = int(input("Enter number: "))
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print("Number is NOT prime")
                    break
            else:
                print("Number is prime")
        else:
            print("Number is NOT prime")

    elif n == "3":
        # sum of digits logic
        num = int(input("Enter number: "))
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        print("Sum of digits =", total)

    elif n == "4":
        # even/odd logic
        num = int(input("Enter number: "))
        if num % 2 == 0:
            print("Number is even")
        else:
            print("Number is odd")

    elif n == "5":
        # exit
        print("Exitinggg.....")
        break

    else:
        print("Invalid choice! Try again.")
