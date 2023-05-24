

# Exercise 1: Calculate the multiplication and sum of two numbers
def ex1(num1:int, num2:int):
    if num1*num2<=1000:
        return num1*num2
    else:
        return num1+num2
# Exercise 2: Print the sum of the current number and the previous number
def ex2(v_rng:int):
    for i in range(v_rng):
        v_rng+= i
        print('Current number ',i,' Previous Number ',v_rng-i,' Sum: ', v_rng)

######
ex2(5)
