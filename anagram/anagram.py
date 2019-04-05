def find_anagrams(word, candidates):
    anagrams=[]
    for i in candidates:
        if i.upper() == word.upper():
            #return anagrams
            break

        if sorted(i.upper()) == sorted(word.upper()):
            anagrams.append(i)        

    return anagrams
