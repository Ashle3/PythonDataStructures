#Counting Down Solution

#create an empty queue
countdown = []

#enqueue each number starting from 10 on down
countdown.append(10)
countdown.append(9)
countdown.append(8)
countdown.append(7)
countdown.append(6)
countdown.append(5)
countdown.append(4)
countdown.append(3)
countdown.append(2)
countdown.append(1)

#create a recursive function that counts down 
def new_years_countdown(list):
    #base case
    if len(list) == 0:
        print("Happy New Year!")
    else:
        current_number = list.pop(0)
        print(current_number)
        new_years_countdown(list)

new_years_countdown(countdown)