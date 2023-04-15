import random

roll = "y"
while roll == "y":
    num = random.randint(1, 6)
    print("*Press y to roll the dice\n*Press q to exit")
    roll = input("INPUT:")
    if (roll == "y"):
        if num == 1:
            print("-----------")
            print("|         |")
            print("|    0    |")
            print("|         |")
            print("-----------")

        if num == 2:
            print("-----------")
            print("|       0 |")
            print("|         |")
            print("| 0       |")
            print("-----------")

        if num == 3:
            print("-----------")
            print("|       0 |")
            print("|    0    |")
            print("| 0       |")
            print("-----------")

        if num == 4:
            print("-----------")
            print("| 0     0 |")
            print("|         |")
            print("| 0     0 |")
            print("-----------")

        if num == 5:
            print("-----------")
            print("| 0     0 |")
            print("|    0    |")
            print("| 0     0 |")
            print("-----------")

        if num == 6:
            print("-----------")
            print("| 0     0 |")
            print("| 0     0 |")
            print("| 0     0 |")
            print("-----------")
