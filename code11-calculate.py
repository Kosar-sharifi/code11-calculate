n = int(input('enter number: '))
o = 0
s = 0
for i in range (n+1):
    if i % 2 == 1:
        o = o + i
    if i % 5 == 0 :
        s = s + i
print( o * s)