# With this little code you type in a letter and number in you get the ord and chr output back. 
fgh = True
while fgh:
    
    print("1. enter letter and number")
    print("2. Kill Program")

    chs =("+> ")

    if chs == "1":
        q = input("enter a letter: ")
        w = int(input("enter a number: "))

        print(ord(q))
        print(chr(w))

    if chs == "2":
        print("later homes smell you later")
        break
