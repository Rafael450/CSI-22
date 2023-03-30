def has_num(string):
    for letter in string:
        if letter.isdigit(): return True
    return False

def has_alpha(string):
    for letter in string:
        if letter.isalpha(): return True
    return False

def has_alpha_and_num(list):
    return [x for x in list if has_alpha(x) and has_num(x)]