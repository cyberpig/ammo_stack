# this is a caesar cipher program

print("e for encrption or d for decryption")

print("Chose what you what: ", end = '')
chs = input().lower
# this to ensure a lower case letter for the chosing
#chs = chs.lower()



def lox():
    if chs == "e":
        print("enter the text to be encrypted:")
        ina = input().lower()
        key1 = int(input("enter the key for encryption (1-26): "))

        inaA = ""
        for clg in ina:
            ina = chr(ord(clg) + key1)
            inaA = (inaA + ina)
        print(inaA)


def Bil_e_gen():
    in chs == "d":
        print("enter the encrypted text: ")
        inb = input().lower()
        #inb = inb.lower()
        key2 = int(input("enter the key for decryption (1-26): "))
        inbB = ""
        for olp in inb:
            inb = chr(ord(olp) - key2)
            inbB = (inbB + inb)
        print(inbB)
    

lox()
bil_e_gen()
