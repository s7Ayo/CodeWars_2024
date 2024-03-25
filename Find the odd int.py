def find_it(seq):
    count = {}

    for i in seq:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1 

    for key, value in count.items():
        if value % 2 != 0: 
            return key 
    return None
