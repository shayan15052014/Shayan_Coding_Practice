n = int(input("Enter a number: "))

if n % 5 == 0:
    print("Divisible by 5")
    print("result: ", n // 5)
else:
    print("Sorry, not divisible by 5. Try an other number.")
    print("result: ", n / 5)
    