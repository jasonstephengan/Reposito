#shift letter
letter = "A"
shift = 33



def shift_letter(letter, shift):
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
    code = list(message)
    decode = ""
    for i in code:
        encoded = chr(ord(i) + shift)
        decode += encoded
    return decode

decode = caesar_cipher(message, shift)
print(decode)

#shift by letter
letter = "I"
letter_shift = "S"


def shift_by_letter(letter, letter_shift):
    numerical = ord(letter) + ord(letter_shift)-65
    alphabetical = chr(numerical)
    
    return alphabetical

alphabetical = shift_by_letter(letter, letter_shift)
print(alphabetical)
    
    
    
#vigenere cipher
message = "I am inevitable"
key = "stones"
repeat = (len(message) // len(key)) + 1
key = key*repeat
key = key[:len(message)]
    

def vigenere_cipher(message, key):
    code = list(message)
    decode = ""
    message = message.upper()
    key = key.upper()
    
    
    for i in range(0,len(message)):
        char_m = message[i]
        char_k = key[i]
    
        code = chr(ord(char_m) + (ord(char_k)-65))
        decode += code
    
    return decode

decode = vigenere_cipher(message, key)
print(decode)


#scytale cipher
message = "HOMELANDER_HAS_FALLEN"
shift = 4
def scytale_cipher(message, shift):
    if len(message) % shift ==0:
        shift = len(message) // shift

    elif len(message) % shift !=0:
        shift = len(message) // shift +1
        
    decode = ""
    zero = 0
    
    while len(message) % shift != 0:
        message += "_"
    
    while zero < shift:
        for i in range (zero,len(message),shift):
            row1 = message[i]
            decode += row1
        zero += 1
    


    
    return decode
    
decode = scytale_cipher(message, shift)  
print(decode)
    
#scytale decipher
message = "HNALODSEME_NERF_L_A_AHL_"
shift = 4


def scytale_decipher(message, shift):
    decode = ""
    zero = 0

    while zero < shift:
        for i in range (zero,len(message),shift):
            row1 = message[i]
            decode += row1
        zero += 1
    
    while decode[-1] == "_":
        decode = decode[:-1]
    

    return decode
    
decode = scytale_decipher(message, shift)  
print(decode)
