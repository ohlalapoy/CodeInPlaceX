from ai import call_gpt

def main():
    # Add your code here!
    language = input("What language do you want to practice?")
    eng_word = input("Type the word in English: ")
    translate = input("Type the word in" + {language} +":")

    get_translation  = call_gpt(f"Translate the word {eng_word} to {language}. Return the translation only.")
    gpt_answer = gpt_translation.lower()
    user_answer = user_translation.lower()
    if gpt_answer == user_answer:
        print("Wahoo! You and GPT agreed on the translation.")
    else:
        print(f"Oh no! GPT said that the translation is {gpt_translation}")
    

    

if __name__ == "__main__":
    main()
