import random
from hangmanWrongStep import steps
from words_for_hangman import words


def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


picked_words = get_valid_words(words)


print(f"The word has {len(picked_words)} Letters")
# print(picked_words)
for i in range(len(picked_words)):
    print('-', ' ', end='')
print()

right = ['_'] * len(picked_words)
wrong = []


def right_letters():
    for i in right:
        print(i, ' ', end='')
    print()


def wrong_letters():
    print("Wrong Letter:", end='')
    for i in wrong:
        print(i, ' ', end='')
    print()


while True:
    guess = input("Guess a letter: ").upper()

    if guess in picked_words:

        index = 0
        for i in picked_words:
            if i == guess:
                right[index] = guess
            index = index + 1

        right_letters()
        wrong_letters()
        steps(len(wrong))

    elif guess not in picked_words:
        if guess in wrong:
            print("You already guessed!", guess)
            wrong_letters()
        else:
            print(guess, "is not in my word")
            wrong.append(guess)
            right_letters()
            wrong_letters()
            steps(len(wrong))

    if len(wrong) > 8:
        print("Game Over")
        print("I picked", picked_words)
        break

    if '_' not in right:
        print("Congratulations!!! You have won the Game")
        print("I picked", picked_words)
        break

