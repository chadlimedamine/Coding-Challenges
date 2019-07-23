def SimpleAdding(num): 

    # code goes here 
    if num == 1:
        return 1
    return num + SimpleAdding(num - 1)
    
# keep this function call here  
print SimpleAdding(raw_input())
