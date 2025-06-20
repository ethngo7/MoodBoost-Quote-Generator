



'''
Next Steps:

include quotes, AND which celebrity said it

....

'''






from emotion_analysis import detect_emotions
from quote_selector import get_quotes_for_emotions

raw_yes = ['yes', 'y', 'ye', 'yeah', 'yep']
raw_no = ['no', 'n', 'nope', 'nah', 'naw']

YES_RESPONSES = set(word.lower() for word in raw_yes) | set(word.capitalize() for word in raw_yes)
NO_RESPONSES = set(word.lower() for word in raw_no) | set(word.capitalize() for word in raw_no)

# Emotion input + confirmation loop
while True:
    print("Type how you're feeling, or type 'quit' to exit.")
    user_input = input("Tell me how you're feeling right now:\n> ").strip().lower()

    if user_input in ['quit', 'exit', 'q', 'Q', 'e', 'E']:
        print("👋 Take care. See you next time.")
        exit()

    emotions = detect_emotions(user_input)

    print(f"\nI think you're feeling: {', '.join(emotions)}. Does that sound right?")
    confirm = input("Type 'yes' to continue or 'no' to retype:\n> ").strip().lower()

    if confirm in YES_RESPONSES:
        break
    elif confirm in NO_RESPONSES:
        print("\nLet's try again.\n")
    else:
        print("❓ I didn't catch that. Please type 'yes' or 'no'.\n")

# Quote loop
while True:
    quotes = get_quotes_for_emotions(emotions)
    print("\n🌟 Here are some quotes that might help:\n")
    for q in quotes:
        print(f"💬 \"{q}\"\n")

    more = input("Would you like more quotes? (yes/no): ").strip().lower()
    if more not in YES_RESPONSES:
        print("❤️ Glad I could help. Take care!")
        break
