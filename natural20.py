# This is a roll the dice program but it's a D&D dice base. It works but still can be be improved. 
import random
a = True
print("1. Roll The Dice")
print("2. Quit")
chs = input("choose: ")


if chs == "1":
    print("")
    print("D4: ", end = '')
    num1 = 1
    num2 = 5
    num3 = random.randrange(num1, num2)
    print(num3)
    print("")
        
    print("D6: ", end = '')
    num_b1 = 1
    num_b2 = 7
    num_b3 = random.randrange(num_b1, num_b2)
    print(num_b3)
    print("")

    print("D8: ", end = '')
    num_c1 = 1
    num_c2 = 9
    num_c3 = random.randrange(num_c1, num_c2)
    print(num_c3)
    print("")

    # D-10 dice
    e = [00, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    f = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_d1 = random.choice(e)
    num_d2 = random.choice(f)
    num_d3 = num_d1
    num_d4 = num_d2
    num_d5 = num_d3 + num_d4
    print("D10 %:", num_d3, "int:", num_d4, "total:", num_d5)
    
    print("")
    print("D12: ", end = '')
    num_e1 = 1
    num_e2 = 13
    num_e3 = random.randrange(num_e1, num_e2)
    print(num_e3)
    print("")

    print("D20: ", end = '')
    num_f1 = 1
    num_f2 = 21
    num_f3 = random.randrange(num_f1, num_f2)
    print(num_f3)
 
if chs == "2":
    print("seeya sweetcheeks")
    #break
