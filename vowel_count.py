def vowel_count(string):
    #list of vowels
    vowels= {"a":0,"e":0,"i":0,"o":0,"u":0}

    #loops through vowels
    #appends value if key appears more than once

    for key, value in vowels.items():
        for i in string:
            if i == key:
                vowels[key]+= 1

    return vowels


print(vowel_count("mike tyson can fight"))
