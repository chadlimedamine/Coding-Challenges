from string import punctuation


def LongestWord(sen):
    text = ""
    for c in sen:
        if c not in punctuation:
            text += c
    words = text.split()
    big = ""
    for w in words:
        if len(w) > len(big):
            big = w
    return big
    
# keep this function call here  
print LongestWord(raw_input())
