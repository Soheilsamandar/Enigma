import pickle
#==============================================================================================
#global variable
alphabet = "abcdefghijklmnopqrstuvwxyz"
state_rotor=0
#==============================================================================================
# reading the rotors alphabet file
def read_file(filename):
    with open(filename,'rb') as f:
        return pickle.load(f)
filename="rotor_state"
rotor1,rotor2,rotor3=read_file(filename)
#==============================================================================================
# reflector alphabet
def reflector(c):
    global alphabet
    return alphabet[len(alphabet)-alphabet.find(c)-1]
#==============================================================================================
# state rotor
def Enigma(c):
    global alphabet
    char1=rotor1[alphabet.find(c)]
    char2=rotor2[alphabet.find(char1)]
    char3=rotor3[alphabet.find(char2)]
    reflected=reflector(char3)
    char3=alphabet[rotor3.find(reflected)]
    char2=alphabet[rotor2.find(char3)]
    char1=alphabet[rotor1.find(char2)]
    return char1
#==============================================================================================
# rotate rotor every 26 time                 
def rotate_rotor():                         
    global rotor1,rotor2,rotor3 , state_rotor
    rotor1=rotor1[1:]+rotor1[0]
    if state_rotor%26:
        rotor2=rotor2[1:]+rotor2[0]
    if state_rotor%26*26:
        rotor3 = rotor3[1:]+rotor3[0]
#==============================================================================================
# code and decode enigma 
def decode_enigma(code):
    global state_rotor
    code = str(code)
    decode = ''
    for c in code:
        state_rotor+=1
        decode+=Enigma(c)
        rotate_rotor()
    return decode
#==============================================================================================
# OUTPUT
print(decode_enigma("hi"))