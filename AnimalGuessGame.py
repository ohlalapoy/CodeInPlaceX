from animal import get_random_animal
from ai import call_gpt


def main():
    animal = get_random_animal()
    #print(animal)
    # TODO: your code here!
    print('''I am thinking of an animal. \nCan you guess what animal it is? ''')
    guess = input("Ask me a yes or no question: ")

    while guess != animal:
        #if guess == "give up":
        #    print(f"It is {animal}")
        #    return
        response = call_gpt(f"response only yes/no if the user's input {guess} is {animal}")
        print(response)
        guess = input("Ask me a yes or no question: ")
        
    print("Correct!")
    pass


if __name__ == "__main__":
    main()