def find_pairs(list):
    return [*filter(lambda num : True if num % 2 == 0 else False, list)]