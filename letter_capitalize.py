def LetterCapitalize(text): 

    # code goes here
    words = text.split()
    new_text = ""
    words_size = len(words)
    for i, w in enumerate(words, 1):
        if i != words_size:
            new_text += w.capitalize() + " "
        else:
            new_text += w.capitalize()
    return new_text
    
# keep this function call here  
print LetterCapitalize(raw_input())
