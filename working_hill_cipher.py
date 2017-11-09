# keyword
print("Type in your word:")
word = input()

# plaintext
print("enter second word:")
word2 = input()

print(word)
print(word2)
mod = 26

alpha2numeric = {
      "A": 0, "a": 0, "B": 1, "b": 1, "C": 2, "c": 2, "D": 3, "d": 3, "E": 4,
      "e": 4, "F": 5, "f": 5, "G": 6, "g": 6, "H": 7, "h": 7, "I": 8, "i": 8,  
      "J": 9, "j": 9, "K": 10, "k": 10, "L": 11, "l": 11, "M": 12, "m": 12, 
      "N": 13, "n": 13, "O": 14, "o": 14, "P": 15, "p": 15, "Q": 16, "q": 16,
      "R": 17, "r": 17, "S": 18, "s": 18, "T": 19, "t": 19, "U": 20, "u": 20,
      "V": 21, "v": 21, "W": 22, "w": 22, "X": 23, "x": 23, "Y": 24, "y": 24, 
      "Z": 25, "z": 25
     }
keytxt = []
plaintxt = []


for letter in word:
   keytxt.append(alpha2numeric[letter])
print(keytxt)

for letter in word2:
    plaintxt.append(alpha2numeric[letter])
print(plaintxt)


a1 = keytxt[0] * plaintxt[0]
a2 = keytxt[1] * plaintxt[1]
a3 = keytxt[2] * plaintxt[0]
a4 = keytxt[3] * plaintxt[1]
a5 = a1 + a2
a6 = a3 + a4 
a7 = a5 % mod
a8 = a6 % mod
print("""
     """)
print("this output of group A")
print(a1, a2, a3, a4, a5, a6, a7, a8)


b1 = keytxt[0] * plaintxt[2]
b2 = keytxt[1] * plaintxt[3]
b3 = keytxt[2] * plaintxt[2]
b4 = keytxt[3] * plaintxt[3]
b5 = b1 + b2
b6 = b3 + b4
b7 = b5 % mod
b8 = b6 % mod
print("""
    """)
print("this output of group B")
print(b1, b2, b3, b4, b5, b6, b7, b8)


c1 = keytxt[0] * plaintxt[4]
c2 = keytxt[1] * plaintxt[5]
c3 = keytxt[2] * plaintxt[4]
c4 = keytxt[3] * plaintxt[5]
c5 = c1 + c2
c6 = c3 + c4
c7 = c5 % mod
c8 = c6 % mod
print("""
    """)
print("this is the output of group C")
print(c1, c2, c3, c4, c5, c6, c7, c8)


d1 = keytxt[0] * plaintxt[6]
d2 = keytxt[1] * plaintxt[7]
d3 = keytxt[2] * plaintxt[6]
d4 = keytxt[3] * plaintxt[7]
d5 = d1 + d2
d6 = d3 + d4
d7 = d5 % mod
d8 = d6 % mod
print("""
    """)
print("this is the output group D")
print(d1, d2, d3, d4, d5, d6, d7, d8)


e1 = keytxt[0] * plaintxt[8]
e2 = keytxt[1] * plaintxt[9]
e3 = keytxt[2] * plaintxt[8]
e4 = keytxt[3] * plaintxt[9]
e5 = e1 + e2
e6 = e3 + e4
e7 = e6 % mod
e8 = e7 % mod
print("""
    """)
print("this is the output group E")
print(e1, e2, e3, e4, e5, e6, e7, e8)


f1 = keytxt[0] * plaintxt[10]
f2 = keytxt[1] * plaintxt[11]
f3 = keytxt[2] * plaintxt[10]
f4 = keytxt[3] * plaintxt[11]
f5 = f1 + f2
f6 = f3 + f4
f7 = f5 % mod
f8 = f6 % mod 
print("""
    """)
print("this is the output group F")
print(f1, f2, f3, f4, f5, f6, f7, f8)
