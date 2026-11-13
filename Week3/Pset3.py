from words import get_random_word

NUM_ATTEMPTS = 6

def main():
    print("Welcome to Wordle!")
    secret = "candy"
    guess_word = input("Enter your guess: ")
    results = []
    remaining_letters = list(secret)

    # First loop: Check G
    for i in range(len(guess_word)):
        if guess_word[i] == secret[i]:
            results.append("G")
            remaining_letters.remove(guess_word[i])
        else:
            results.append("B")

    # Second loop: Check Y
    for i in range(len(guess_word)):
        if results[i] == "B":
            if guess_word[i] in remaining_letters:
                results[i] = "Y"
                remaining_letters.remove(guess_word[i])

    # Third loop: Format output
    output = []

    for i in range(len(guess_word)):
        if results[i] == "G":
            output.append("[" + guess_word[i] + "]")
        elif results[i] == "Y":
            output.append("(" + guess_word[i] + ")")
        else:
            output.append(guess_word[i])

    print("Result:", *output)


if __name__ == "__main__":
    main()