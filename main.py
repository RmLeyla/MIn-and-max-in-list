list = [5, 1, 14, 27]
min = list[0]
max = list[0]

for i in range(len(list)):
  if min > list[i]:
    min = list[i]
  if max < list[i]:
    max = list[i]


print (f"min is {min}")
print (f"max is {max}")