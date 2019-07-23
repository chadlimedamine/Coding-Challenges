import string


def SimpleSymbols(text): 

    # code goes here 
    result = "true"
    size = len(text)
    for i, c in enumerate(text, 1):
        if i == 1:
            if c.isalpha():
                result = "false"
                break
        elif (i + 1) <= size:
            if c.isalpha():
                if not ((text[i-2] == "+") and (text[i-1].isalpha()) and (text[i] == "+")):
                    result = "false"
    return result
    
# keep this function call here  
print SimpleSymbols(raw_input())
