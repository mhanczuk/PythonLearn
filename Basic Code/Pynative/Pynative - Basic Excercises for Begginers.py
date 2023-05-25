

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

# Exercise 3: Print characters from a string that are present at an even index number
def ex3(v_str:str):
    v_size = len(v_str)
    if (v_size % 2) == 1: v_size -=1
    [print(v_str[i]) for i in range(0,v_size,2)]

    #fancier way to do this in reverse order
    #stringObject[ start : stop : interval]
    [print(v_str[i:i+1:1]) for i in range(v_size,0-1,-2)]

# Exercise 4: Remove first n characters from a string
def ex4(v_str:str, v_pos:int):
    if v_pos < len(v_str):
        return(v_str[v_pos:])
    else: 
        return('Err: position exceeded length of the string')
    
#Exercise 5: Check if the first and last number of a list is the same
def ex5(list_1:list):
    return(list_1[0]==list_1[-1])

#Exercise 6: Display numbers divisible by 5 from a list
def ex6(list_1:list):
    for i in range(len(list_1)):
        if list_1[i]%5 == 0:
            print(list_1[i])

# Exercise 7: Return the count of a given substring from a string
def ex7(in_str:str, val:str):
    cnt = in_str.count(val)
    print('String ',val,' appears in ',in_str,' ',cnt,' times.' )

# Exercise 8: Print the following pattern
def ex8(size:int):
    for i in range(size+1):
        for y in range(i):
            print(i,end=' ')
        print('')
# Exercise 9: Check Palindrome Number
def ex9(val):
    v_str = str(val)
    v_nstr= v_str[::-1]
        
    if v_str == v_nstr:
        print("Given number is palindrome")
    else:
        print("Given number is not palindrome")

ex9(545)