def is_isogram(string):  
    
    # my solution
    """data= "".join(sorted([i.upper() for i in string if i.isalpha()])).strip()

    data2= "".join(sorted({i.upper()for i in string if i.isalpha()})).strip()

    return data == data2   """

    # Correction from the mentor (readability is key)                                                                               
    filtered_text = list(filter(str.isalpha, string.upper())) 
                                                            
    sorted_text,isogram_text= filtered_text,set(filtered_text)    
                                                            
    return len(sorted_text) == len(isogram_text)


