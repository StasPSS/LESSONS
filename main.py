# Home Worc 1

# Task 1
print('Task 1')
int_variable = int(1000) # create int variable
text_variable = "string" # create string variable
print(text_variable) # print value of the text_variable
print(int_variable) # print value of the int_variable
print("input some value: ") # request to input value of the other_variable
other_variable=input() # input value of the other_variable
print("other_variable: {}".format(other_variable))

# Task 2
print('Task 2')
seconds_time = int(input("input time in seconds: ")) # request to input time in seconds
hours_time = str(seconds_time // 3600) # get quantity of hours
seconds_time = seconds_time % 3600 # get remainder in seconds
minutes_time = str(seconds_time//60) # get quantity of minutes
seconds_time = str(seconds_time%60) # get remainder in seconds, this reminder is quantity of seconds
print("standard time is {}:{}:{}".format(hours_time,minutes_time,seconds_time)) # print formed string

# task 3
print('Task 3')
universal_task_variable = input("input int number: ") # request to enter some int number
x1_var = int(universal_task_variable) # create first int variable from int number n
x2_var = int(2 * universal_task_variable) # create second int variable from int number nn
x3_var = int(3 * universal_task_variable) # create third int variable from int number nnn
print("result: {}".format(x1_var+x2_var+x3_var)) # print formed string

# task 4
print('Task 4')
universal_task_variable = input("input some string: ") # request to enter some string
i = len(universal_task_variable) # determine the length of the string and put this value in the cycle counter "i"
maximum_number = universal_task_variable[i-1] # the last element of string assign sa maximum
while i > 0: # cycle will continue until cycle counter gather then zero
    print("iteration: {}, maximum: {}".format(i,maximum_number)) # print the cycle counter and present maximum
    if (maximum_number < universal_task_variable[i-1]): # maximum reassignment condition
        maximum_number = universal_task_variable[i-1] # maximum reassignment
    i = i-1 # decrement i--
print("maximum value is : {}".format(maximum_number)) # output the element of the row with the maximum value

# task 5, 6
print('Task 5,6')
profit = int(input("input profit: "))
expenses = int(input("input expenses: "))
revenue = profit - expenses
if revenue > 0:
    print("enterprise income: {}".format(revenue))
    profitability = float(revenue) / float(profit)
    print("enterprise profitability: {}".format(profitability))
    workers = int(input("input quantity of workers: "))
    print("profit per employee: {}".format(float(revenue/workers)))
else:
    print("enterprise losses: {}".format(revenue))

# task 7
print('Task 7')

start_result = float(input("input start result: "))
final_result = float(input("final result: "))
cycle = 0
growth = 0
while start_result < final_result:
    start_result=start_result+growth
    cycle = cycle + 1
    print(" {} day: {} km".format(cycle,start_result))
    growth=start_result/10
print("final result is: {} rm. on {} day".format(start_result,cycle))
