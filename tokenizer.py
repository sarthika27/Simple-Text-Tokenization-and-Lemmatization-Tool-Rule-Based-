def tokenize_text(text):
    cleaned_text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    tokens = cleaned_text.split()
    return tokens


