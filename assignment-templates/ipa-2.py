#shift letter
letter = "A"
shift = 27



def shift_letter(letter, shift):
    letter = letter.upper()
    numerical = ord(letter) + shift
    numerical = (numerical - 65) % 26 + 65
    alphabetical = chr(numerical)
    
    return alphabetical

alphabetical = shift_letter(letter, shift)
print(alphabetical)
    



#caesar cipher
message = "Hello World"
shift = 5

def caesar_cipher(message, shift):
    code = list(message.upper())
    decode = ""
    for i in code:
        if i == " ":
            decode += " "
        else:
            encoded = (ord(i) + shift)
            encoded = chr((encoded - 65) % 26 + 65)
            decode += encoded
    return decode

decode = caesar_cipher(message, shift)
print(decode)




#shift by letter
letter = ""
letter_shift = "B"


def shift_by_letter(letter, letter_shift):
    letter = letter.upper()
    letter_shift = letter_shift.upper()
    if letter == "" or letter == " " or letter == "_" or letter_shift == "_" or letter_shift == "" or letter_shift == " " or ord(letter) == 32:
        return(" ")
    else:
        numerical = ord(letter) + ord(letter_shift)-65
        numerical = (numerical - 65) % 26 + 65
        alphabetical = chr(numerical)
    
    return alphabetical

alphabetical = shift_by_letter(letter, letter_shift)
print(alphabetical)
    
    
    
    
    
    
#vigenere cipher
message = "I am inevitable"
key = "stones"

    

def vigenere_cipher(message, key):
    repeat = (len(message) // len(key)) + 1
    key = key*repeat
    key = key[:len(message)]
    code = list(message)
    decode = ""
    message = message.upper()
    key = key.upper()
    
    
    for i in range(0,len(message)):
        if message[i] == " ":
            decode += " "
        else:
            char_m = message[i]
            char_k = key[i]
            
            code = ord(char_m) + (ord(char_k)-65)
            code = chr((code - 65) % 26 + 65)
            decode += code
    
    return decode

decode = vigenere_cipher(message, key)
print(decode)





message = "ALGORITHMS_ARE_IMPORTANT"
shift = 8

def scytale_cipher(message, shift):
    code = ""
    while len(message) % shift != 0:
        message += "_"
        
    for i in range(len(message)):
        x = (i // shift) + (len(message) // shift) * (i % shift)
        if x < len(message):
            code += message[x]
    
    return code


code = scytale_cipher(message, shift)  
print(code)    



    

#scytale decipher
message = "HA_FNONHA_MDAL_EESL_LR_E_"
shift = 5


def scytale_decipher(message, shift):
    message = message.upper()
    decode = ""
    zero = 0

    while zero < shift:
        for i in range (zero,len(message),shift):
            row1 = message[i]
            decode += row1
        zero += 1

    return decode
    
decode = scytale_decipher(message, shift)  
print(decode)
    

