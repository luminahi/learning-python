
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    upperCaseMessage = ""
    upperCaseMessage = message.upper()

    for currentCharacter in upperCaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = (position + int(cipherKey)) % 26
        if currentCharacter in alphabet:
            encryptedMessage  = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decriptKey = -1 * int(cipherKey)
    return encryptMessage(message, decriptKey, alphabet)

def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
    print(f"my alphabet: {alphabet}")
    msg = encryptMessage("alex", getCipherKey(), alphabet)
    print(msg)
    msg = decryptMessage(msg, getCipherKey(), alphabet)
    print(msg)
    return 0

main()
