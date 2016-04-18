def break_words(stuff):
    """Break up words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort words"""
    return sorted(words)

def print_first_word(words):
    """Pop it off and prints the first word"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Pop it off and prints the last word"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Sorted words in a sentence"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print first and last"""
    
