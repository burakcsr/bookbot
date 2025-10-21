def count_words(text):
    separate = text.split()
    num_words = len(separate)
    return num_words

def char_count(text):
    data = {}
    for character in text.lower():
        if character not in data:
            data[character] = 1
        else:
            data[character] += 1 
    return data