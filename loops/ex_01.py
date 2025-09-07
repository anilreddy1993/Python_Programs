#print the alphabets from a to z
# to convert numbers to alphabets we have to use chr()
# to convert alphabets to nubers we have to use ord()
# print(ord('C'))
for i in range(65,100):
    print(chr(i))
    if chr(i)=='Z':
       break

