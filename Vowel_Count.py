def get_count(sentence):
    sentence = [*sentence]
    count= [x for x in sentence if  x in ["a", "e", "i", "o", "u"]]
    count = len(count)
    return count 