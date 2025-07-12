import os

def save_cleaned_output(tokens):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    with open("logs/cleaned_output.txt", "w") as file:
        for token in tokens:
            file.write(token + '\n')
    print("\n✅ Cleaned tokens saved to logs/cleaned_output.txt")
