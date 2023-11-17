print("test")

for i in range(1, 16 + 1):
    if i % 15 == 0:
        print("izzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
