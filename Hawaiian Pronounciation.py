#dictionaries
hawaiianChar = ['a', 'e', 'i', 'o', 'u', 'p', 'k', 'h', 'l', 'm', 'n', 'w', ' ', "'"]
vowelPronounciations ={
        'a': 'ah',
        'e': 'eh',
        'i': 'ee',
        'o': 'oh',
        'u': 'oo',
        'ai': 'eye',
        'ae': 'eye',
        'ao': 'ow',
        'au': 'ow',
        'ei': 'ay',
        'eu': 'eh-oo',
        'iu': 'ew',
        'oi': 'oyo',
        'ou': 'ow',
        'ui': 'ooey'
}

#making a function that wil generate the pronounciation for the input that is given

def givePronounciation(givenWord):
    pronounciationGuide = " "
    i = 0
    while i < len(givenWord):
        char = givenWord[i]

        if char in "pmnk":
            pronounciationGuide += char
        elif char == "w":
                if i == 0 or word[i - 1] ==  ' a ' :
                    pronounciationGuide +=  ' w ' #this is if w is by itself or after "a"
                elif word[i-1] in "ie": 
                    pronounciationGuide += ' v ' #after i or e it would sound like v
                else:
                    pronounciationGuide += ' w ' #this leaves u and o which makes it sound like w
        elif char == " ' ":
                pronounciationGuide += " ' " # this would give it a stop
        else:
                for legnth in range(2, 0, -1): #this is for vowel combinations
                        substring = givenWord[i:i + legnth]
                        if substring in vowelPronounciations:
                            pronounciationGuide += vowelPronounciations[substring]
                            i+= legnth - 1 #to move it forward by the length of the substring it matches
                            break
                    
                else: #if it does not find a pronounciation then it will assume to be by itself
                    pronounciationGuide += vowelPronounciations.get(char,char)
        i += 1

    return pronounciationGuide

    
  #doing the input here so i can determine if it is valid or not and ask for other word if user wants  
while True:
    givenWord = input("Enter a Hawaiian word to pronounce: ").strip().lower()
    
    validInput = all(char in hawaiianChar for char in givenWord)
    
    if validInput:
        pronunciation = givePronounciation(givenWord)
        print(f"{givenWord.upper()} is pronounced {pronunciation.capitalize()}")
    else:
        print("Please enter a valid Hawaiian word :)")
    
    response = input("Do you want learn to pronounce another word?? Y/YES/N/NO: ").strip().lower()
    
    if response not in ('y', 'yes'):
        print("bye! bye!")
        break      
                        
                
                
        




    
    
