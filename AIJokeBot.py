from ai import call_gpt

def main():
    # Add your code here!
    print("Hello! I am an AI joke bot.")
    want_jokes = input("Do you want to hear a joke? Type yes or no: ")

    while want_jokes == "yes":
        ai_response = call_gpt("generate 1 joke question with answer")
        gpt_prompt = call_gpt(f"You already told me: {ai_response} please generate another one, response only question and answer 2 lines and each line separate by 1 enter")
        print(gpt_prompt)
        want_jokes = input("\nDo you want to hear a joke? Type yes or no: ")



if __name__ == "__main__":
    main()