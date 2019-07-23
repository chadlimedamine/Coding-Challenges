def TimeConvert(num): 

    # code goes here 
    hours = num / 60
    minutes = num % 60
    return str(hours) + ":" + str(minutes)
    
# keep this function call here  
print TimeConvert(raw_input())
