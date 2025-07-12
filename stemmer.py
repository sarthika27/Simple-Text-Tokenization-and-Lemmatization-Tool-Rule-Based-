def stem_tokens(tokens):
    suffixes = ['ing', 'ed', 'ly', 'es', 's']
    stemmed = []
    for word in tokens:
        for suffix in suffixes:
            if word.endswith(suffix) and len(word) > len(suffix) + 2:
                word = word[: -len(suffix)]
                break
        stemmed.append(word)
    return stemmed