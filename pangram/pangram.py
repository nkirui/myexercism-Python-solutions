import string

def is_pangram(sentence):

    alphabet = string.ascii_letters
 
    for set(alphabet).issubset(alphabet):
        return True
        else:
            pass



