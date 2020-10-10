temp = 40

while temp >28:
    print("The water  is {} normal".format(temp))
    temp -=1
    if temp == 33:
        break
for num in range(1, 20):
    if num == 11:
        print("We're skipping number 11")
        continue
    print("This is the number {}".format(num))


for number in range(20, 40):
    if number == 22:
        pass
    else:
        print("chalty rahoo {}".format(number))