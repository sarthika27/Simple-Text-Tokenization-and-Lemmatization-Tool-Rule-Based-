def show_cleaned_output(original, cleaned):
    print("\nOriginal vs Cleaned Tokens:")
    for o, c in zip(original, cleaned):
        print(f"{o} → {c}")