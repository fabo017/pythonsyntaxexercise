def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase

        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN
    """

    for word in words:
        print(word.upper())


def print_upper_e_words(words):
    """only prints words that start with the letter ‘e’ (either upper or lowercase). print each word on seperate line.



        >>> print_upper_e_words(["eggs", "Envelope", "EASY", "Fried"])
        EGGS
        ENVELOPE
        EASY
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


