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
