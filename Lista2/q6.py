def rev_list(_list):
    for i in range(len(_list)):
        yield _list[len(_list)-i-1]