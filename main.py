import random

global hidden_word, word, guessed_letters, counter, drawing


def pick_word():
    global word, guessed_letters, counter, drawing
    guessed_letters = []
    with open('sowpods.txt', 'r') as f:
        words = f.readlines()
    word = random.choice(words)
    word = word.strip()
    word = word.upper()
    counter = 6
    drawing = ["r------------\n|           |\n|           O\n|          /|\\\n|          / \\\n|",  # right leg
               "r------------\n|           |\n|           O\n|          /|\\\n|          /\n|",  # left leg
               "r------------\n|           |\n|           O\n|          /|\\\n|\n|",  # right hand
               "r------------\n|           |\n|           O\n|          /|\n|\n|",  # left hand
               "r------------\n|           |\n|           O\n|           |\n|\n|",  # body
               "r------------\n|           |\n|           O\n|\n|\n|",  # head
               "r------------\n|           |\n|\n|\n|\n|"]  # only rope
    return word


def enter_letter():
    global guessed_letters
    flag = True
    while flag:
        print_word()
        letter = input("Enter a single letter: ")
        letter = letter.upper()
        if len(letter) == 1 and letter.isalpha():
            flag = False
            for char in guessed_letters:
                if char == letter:
                    print("Letter already used.")
                    print()
                    flag = True

            if not flag:
                guessed_letters.append(letter)
        else:
            print("Invalid input.")
    return letter


def word_structure():
    global hidden_word
    hidden_word = []

    for i in range(len(word)):
        hidden_word.append("_")


def print_word():
    global hidden_word, guessed_letters
    for i in range(len(hidden_word)):
        print(hidden_word[i], end="")
    print("\n")

    if guessed_letters:
        print("previously guessed letters: ", end="")

        for i in range(len(guessed_letters) - 1):
            print(guessed_letters[i] + ", ", end="")
        print(guessed_letters[-1])
    print()


def check_word():
    global word, hidden_word, counter, drawing
    letter = enter_letter()
    flag = False
    for i in range(len(word)):
        if letter == word[i]:
            hidden_word[i] = letter
            flag = True
    if not flag:
        counter = counter - 1

    print(drawing[counter])
    print("remaining guesses: " + str(counter))
    return flag


def has_won():
    global hidden_word, word
    temp = ''.join(hidden_word)
    if temp == word:
        return True
    return False


def has_lost():
    global counter
    return counter <= 0


def again():
    while True:
        answer = input("Would you like to play again(Y/N): ")
        answer = answer.lower()
        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Invalid answer, try again.\n")


def game():
    global word
    pick_word()
    word_structure()
    print("\nGame by Nevo & Oren Kaplan\n")
    flag = True
    while flag:
        print("==================================================")
        if check_word():
            flag = not has_won()
            if not flag:
                print("You Won!!")
                print("The word was:", word)
        elif has_lost():
            print("You Died\nGAME OVER")
            print("The word was:", word)
            flag = False


if __name__ == '__main__':
    play = True
    while play:
        game()
        play = again()
