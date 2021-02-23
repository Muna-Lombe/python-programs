
#checks if a string is a sentence
def is_sentence(s):
    h=0
    for i in s.split():
        h+=1
    if h>1:
        return True
    else:
        return False
            


#using recursion
#String is passed as argument recursively
#until it is reversed
def rev_str(get_str):

    #if string length is 0 then it is returned
    if len(get_str) == 0:
          return get_str 
    else:
        if is_sentence(get_str)==True:
            get_str=get_str.rstrip()
        #the string is sliced without 1st character
        #1st character is added to end of string
        return rev_str(get_str[1:]) + get_str[0] 



s=str(input("enter sumn:"))
print("reversed string:",rev_str(s))


            
