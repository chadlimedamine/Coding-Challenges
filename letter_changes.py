from string import maketrans


def LetterChanges(text):
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "bcdefghijklmnopqrstuvwxyza"
    c = "eaiou"
    d = "EAIOU"
    translation_01 = maketrans(a, b)
    new_str = text.translate(translation_01)
    translation_02 = maketrans(c, d)
    new_str = new_str.translate(translation_02)
    return new_str
    
# keep this function call here  
print LetterChanges(raw_input())
