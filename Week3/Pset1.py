from words import get_random_word

NUM_ATTEMPTS = 6

def main():
    # Delete pass and start writing your solution here.
    print("Welcome to Wordle!")
    secret = "candy"
    guess_word = input("Enter your guess: ")
    results = []

    for i in range(len(guess_word)):
        if  guess_word[i] == secret[i]:
            results.append("G")
        else:
            results.append("B")

    #for item in results:
    print("Result:", *results)



if __name__ == "__main__":
    main()
