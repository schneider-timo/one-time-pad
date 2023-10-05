def decode(code, cipher, clear):
    for i in range(0,len(code)):
        code_num    = alphabet_to_numbers[code[i].upper()]
        cipher_num  = alphabet_to_numbers[cipher[i].upper()]
        clear_num   = 0
        if cipher_num < code_num:
            for j in range (code_num, code_num+26):
             if j%26 == cipher_num:
                clear_num = j-code_num
                clear+=numbers_to_alphabet[clear_num]
                break
        else:   
            for j in range (0,26):
                if j%26 == cipher_num:
                    clear_num = j-code_num
                    clear+=numbers_to_alphabet[clear_num]
                    break
    return clear

def encode(code, clear, cipher):
    for i in range(0,len(code)):
       code_num  = alphabet_to_numbers[code[i].upper()]
       clear_num = alphabet_to_numbers[clear[i].upper()]
       cipher_num = (clear_num + code_num)%26
       cipher_let = numbers_to_alphabet[cipher_num]
       cipher +=cipher_let
    return cipher

banner = """
 _____                 _____ _                      ______         _ 
|  _  |               |_   _(_)                     | ___ \       | |
| | | |_ __   ___ ______| |  _ _ __ ___   ___ ______| |_/ /_ _  __| |
| | | | '_ \ / _ \______| | | | '_ ` _ \ / _ \______|  __/ _` |/ _` |
\ \_/ / | | |  __/      | | | | | | | | |  __/      | | | (_| | (_| |
 \___/|_| |_|\___|      \_/ |_|_| |_| |_|\___|      \_|  \__,_|\__,_|
                                                                     
                                                                     """
alphabet_to_numbers = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
    "F" : 5,
    "G" : 6,
    "H" : 7,
    "I" : 8,
    "J" : 9,
    "K" : 10,
    "L" : 11,
    "M" : 12,
    "N" : 13,
    "O" : 14,
    "P" : 15,
    "Q" : 16,
    "R" : 17,
    "S" : 18,
    "T" : 19,
    "U" : 20,
    "V" : 21,
    "W" : 22,
    "X" : 23,
    "Y" : 24,
    "Z" : 25
}

numbers_to_alphabet = {
    0 : "A",
    1 : "B",
    2 : "C",
    3 : "D",
    4 : "E",
    5 : "F",
    6 : "G",
    7 : "H",
    8 : "I",
    9 : "J",
    10 : "K",
    11 : "L",
    12 : "M",
    13 : "N",
    14 : "O",
    15 : "P",
    16 : "Q",
    17 : "R",
    18 : "S",
    19 : "T",
    20 : "U",
    21 : "V",
    22 : "W",
    23 : "X",
    24 : "Y",
    25 : "Z"
}  
print(banner)
encode_decode = input("would you like to decode(1) or encode(2) a phrase?: ")
    
if encode_decode == "1":
    code    = input("please Enter the codephrase: ").replace(" ", "")
    cipher  = input("please Enter ciphertext to decode: ").replace(" ", "")
    clear   = ""
    if len(code)!=len(cipher):
        raise Exception("codephrase and ciphertext must have the same length!")
    clear   = decode(code,cipher, clear)
    
elif encode_decode == "2":
    code    = input("please Enter the codephrase: ").replace(" ", "")
    clear   = input("please enter the cleartext to encode: ").replace(" ", "")
    cipher  = ""
    if len(code)!=len(clear):
        raise Exception("codephrase and ciphertext must have the same length!")
    cipher = encode(code, clear, cipher)
    
else:
    raise Exception("please choose an option!")
    
print("the decoded text is:\t", clear)
print("the codephrase is:\t", code)
print("the encoded text is:\t", cipher)
