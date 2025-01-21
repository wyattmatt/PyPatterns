n = int(input("Input Number: "))
for i in range(0, n + 1):
    if i == 0:
        print(" " * (n - i) + "*")
    elif i < n:
        print(" " * (n - i) + "*" + " " * (2 * i - 1) + "*")
    else:
        print("* " * (n + 1))