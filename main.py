def encode(data):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    code = "zyxwvutsrqponmlkjihgfedcba"
    
    #Here will be encode text
    output = ""
    words = []

    #Here is create or open file with your encode text
    file_with_encode = open("ecnode_msg.txt", "w")
    
    #Here is encoding 
    for word in data:                       #For every word in your input text
        for i in range(len(word)):          #For every letter in word from input
            idx = alphabet.index(word[i])   #eg. for a is z
            output += code[idx]             
            i += 1
            
        words.append(output)                #Here is add first encode word
        file_with_encode.write(output + " ")#Here is add encode word to file
        output = ""                         #Clear "output" for next word

    file_with_encode.close()                
    return words
    

print("Don't use special characters, numbers or letters other than (abcdefghijklmnopqrstuvwxyz).")
input_text = input("Enter text to encode >>>> ")

result = encode(input_text.lower().split()) 

print(result)
