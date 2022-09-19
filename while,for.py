##i = 1
##while i < 6:
##    print(i)
##    if i == 3:
##     break
##    i += 1


i = 1
while i < 6:
    i += 1
    if i == 3:
     continue
    print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


for x in range(2, 6):
  print(x)

#specifying increment value by addidng parameter: increment by 3
for x in range(2, 30, 3):
  print(x) 

#nested loops
colour = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry", "lemon"]
size = ["1kg", "2kg", "3kg"]

for x in colour:
  for y in fruits:
    for z in size:
     print(x, y, z)

for x in [0, 1, 2]:
  pass
