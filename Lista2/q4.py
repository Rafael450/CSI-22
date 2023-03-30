def alpha_contains(letters, has):
    for letter in letters:
        if has.find(letter) == -1:
            return False
    return True