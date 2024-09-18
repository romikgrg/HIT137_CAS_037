#Initializing a variable with a value
total = 0

#Nested loop to sum or subtract based on the condition
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

#Initialize a counter for another loop
counter = 0

#While loop with conditions to modify 'total'
while counter < 5:
    if total < 13:         #If total is less than 13, it increases
        total += 1
    elif total > 13:       #If total is more than 13, it decreases
        total -= 1
    else:
        counter += 2        #The counter increments by 2 if total equals 13

#Print the final total and counter values
print("Final total:", total)
print("Final counter:", counter)