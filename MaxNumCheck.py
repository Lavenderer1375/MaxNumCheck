max = 0

while True:
    value =  input("Pleas enter a number: \n")
    if value == "stop":
        break
    else:
        num = int(value)
        if num > max:
            max = num

print("Max number is %d" %(max))
