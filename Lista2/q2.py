def tuple_mean(t_tuple):
    start = ()

    for tuple in t_tuple:
        start += (sum(tuple)/len(tuple),)

    return start