my_list = []
while True:
    x = int(input("Enter an integer, press 0 to stop  "))
    if x == 0:
        break
    else:
        my_list.append(x)
my_list = sorted(my_list)
for x in range(len(my_list)):
    print(my_list[x])
