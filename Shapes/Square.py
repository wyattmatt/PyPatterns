n = int(input("Input Number: "))
for i in range(1, n + 1):
    if i == 1:
        print("*" * (n))
    elif i < n:
        print("*" + " " * (n - i + i - 2) + "*")
    else:
        print("*" * (n))