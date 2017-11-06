# this is a D&D dice rolling program still in R&D
import random
a = True
print("1. again")
print("2. quit")
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

    print("D10-%: int: total: ", end = '')
    e = [00, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    f = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_d1 = random.choice(e)
    num_d2 = random.choice(f)
    num_d3 = num_d1
    num_d4 = num_d2
    num_d5 = num_d3 + num_d4
    print(num_d3, num_d4, num_d5)
    
    print("")
    print("D12: ")
    print("d20: ")
 
if chs == "2":
    print("seeya sweetcheeks")
    #break
