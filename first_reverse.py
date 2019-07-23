def FirstReverse(text): 

    # code goes here 
    new_text = ""
    size = len(text)
    i = size -1
    while i >= 0:
        new_text += text[i]
        i -= 1
    return new_text
    
# keep this function call here  
print FirstReverse(raw_input())
