from modules.input_module import get_input_text
from modules.tokenizer import tokenize_text
from modules.stemmer import stem_tokens
from modules.cleaner_viewer import show_cleaned_output
from modules.log_exporter import save_cleaned_output

def main():
    sentence = get_input_text()
    tokens = tokenize_text(sentence)
    cleaned_tokens = stem_tokens(tokens)
    show_cleaned_output(tokens,cleaned_tokens)
    save_cleaned_output(tokens)

if __name__ == "__main__":
    main()
