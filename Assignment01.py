'''
In the last lesson you built a language practice tool that quizzed the user on a single word. Now use a while loop to keep quizzing them until they want to stop.

Your program should:

Ask the user what language they want to practice.
Ask them for an English word, or done to quit.
As long as the word is not done: ask for their translation, use GPT to translate the same word, compare the two with an if statement, and then ask for the next word.
When they type done, print a goodbye message.


Here is example output from running this program:

What language do you want to practice? Spanish
Type a word in English, or done to quit: apple
Type the word in Spanish: manzana
Wahoo! You and GPT agreed on the translation.
Type a word in English, or done to quit: hello
Type the word in Spanish: Aloha
Oh no! GPT said that the translation is Hola
Type a word in English, or done to quit: done
Nice practicing with you!

Remember to call .lower() on both translations before comparing them, so capitalization does not change the result.
'''

from ai import call_gpt

def main():
    # Add your code here!
    student_res = input("What language do you want to practice? ")
    language = input("Type a word in English, or done to quit: ")
    Translate = input(f"Type the word in {student_res}: ")
    
    while language != "done":
        response = call_gpt(f"Translate {language} into {student_res} in just one word")
        if response.lower() == Translate.lower():
            print("Wahoo! You and GPT agreed on the translation.")
        else: 
            print(f"Oh no! GPT said that the translation is {response}")
        
        language = input("Type a word in English, or done to quit: ")
        Translate = input(f"Type the word in {student_res}: ")
    print("Nice practicing with you!")
if __name__ == "__main__":
    main()
