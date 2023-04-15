import random

words = ["tiger", "lion", "rocket", "cat", "dog", "subway", "lucky", "funny", "matrix", "rickshaw", "python", "berry"]
def hangman():
    word = random.choice(words)
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guesses = ''

    while turns>=0:
        main = ''
        failed = 0

        for char in word:
            if char in guesses:
                main += char
            else:
                main = main + "_" + ""

        if main == word:
            print(main)
            print("You Won! the word was", word)
            break
        print("Guess the word:", main)
        guess = input()

        if guess in validletters:
            guesses += guess
        else:
            print("Please enter a valid letter")
            guess = input()

        if guess not in word:
            turns -= 1
            if turns == 9:
                print("9 turns left.")
                print(" -------- ")

            if turns == 8:
                print("8 turns left.")
                print(" -------- ")
                print("       0     ")

            if turns == 7:
                print("7 turns left.")
                print(" -------- ")
                print("       0     ")
                print("       |     ")

            if turns == 6:
                print("6 turns left.")
                print(" -------- ")
                print("       0     ")
                print("       |     ")
                print("      /      ")

            if turns == 5:
                print("5 turns left.")
                print(" -------- ")
                print("       0     ")
                print("       |     ")
                print("      / \    ")

            if turns == 4:
                print("4 turns left.")
                print(" -------- ")
                print("     \ 0     ")
                print("       |     ")
                print("      / \    ")

            if turns == 3:
                print("3 turns left.")
                print(" -------- ")
                print("     \ 0 /   ")
                print("       |     ")
                print("      / \    ")

            if turns == 2:
                print("2 turns left.")
                print(" -------- ")
                print("              ")
                print("|             ")
                print("|    \ 0 /    ")
                print("|      |      ")
                print("|     / \     ")
                print("|             ")

            if turns == 1:
                print("1 turns left.")
                print(" -------- ")
                print("________      ")
                print("|             ")
                print("|    \ 0 /    ")
                print("|      |      ")
                print("|     / \     ")
                print("|             ")

            if turns == 0:
                print("You loose")
                print("Better luck next time")
                print(" -------- ")
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|\     ")
                print("|     / \     ")
                print("|             ")
                break



name = input("What is your name?\n")
print("Welcome", name, ",Time to play the game!")
print("---------------")
print("Try to guess the word in less than 10 attempts")
hangman()




