if __name__ == '__main__':
    print("ABC")
    first_list = [2,3,4]
    print(list(map(lambda x:x**2, first_list)))

def squareit(n):
    return n**2

print(list(map(squareit,first_list)))

input = ['San Jose', 'San Francisco', 'Santa Fe', 'Houston']
def count_s(input):
    n = 0
    if(input[0].lower() == 's'):
        n+=1
    return n
n=0
count = sum(list(map(count_s,input)))
print(count)
# Output is 3

#Python program to put sum of two lists in an array
first = [2,3,4]
second = [6,2,1]
print(list(map(lambda x,y:x+y,first,second)))
## Output is [8, 5, 5]

#Python Program to combine the first name and Last name of two lists
first_name = ['nikola','james','albert']
second_name = ['tesla','watt','einstein']
proper = lambda x,y:x[0].upper()+x[1:] + ' ' + y[0].upper()+y[1:]
print(list(map(proper,first_name,second_name)))
## Output is ['Nikola Tesla', 'James Watt', 'Albert Einstein']

##Lambda Filter function to filter out the numbers divisible by 3
my_list = [1,2,3,5,6,9,12,13,14,15]
div3 = lambda x:x%3==0
result = filter(div3,my_list)
print(list(result))
## Output of the function is [3, 6, 9, 12, 15]

## Combine the firstname and last name from two list inside the arrays
## Input array is in form [ ['Ankur', 'Avik', 'Kiran', 'Nitin'], ['Narang', 'Sarkar', 'R', 'Sareen']]
intial_arr = [ ['Ankur', 'Avik', 'Kiran', 'Nitin'], ['Narang', 'Sarkar', 'R', 'Sareen']]
list1 = intial_arr[0]
list2 = intial_arr[1]
var2 = list(map(lambda x,y:x+' '+y,list1,list2))
print(var2)
##Output of the program is ['Ankur Narang', 'Avik Sarkar', 'Kiran R', 'Nitin Sareen']

from functools import reduce
q = reduce(lambda x,y:x+y,range(1,4))
print(q)
## 6

##If the current number is greater than the next number then retain it
list_of_nums = [22,45,32,20,87,94,30]
print(reduce(lambda x,y: x if x>y else y,list_of_nums))

##Filter function example:
# You are given a list of strings such as input_list =  ['hdjk', 'salsap', 'sherpa'].
#
# Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.
input_list =  ['hdjk', 'salsap', 'sherpa']
filter_func = filter(lambda x:x[0].lower() == 's' and x[-1].lower() == 'p',input_list)
print(list(filter_func))
## Output of the program ['salsap']

##Use of Map Function
# Count the number of words that starts with s
input_list1 = ['San Jose', 'San Francisco', 'Santa Fe', 'Houston']
print(sum(list(map(lambda x:x[0].lower() == 's',input_list1))))
# output 3

#Using the Reduce function, concatenate a list of words in input_list, and print the output as a string.
#If input_list = ['I','Love','Python'], the output should be the string 'I Love Python'.
input_list = ['I','Love','Python']
user_list = reduce(lambda x,y:x+y,input_list)
print(list(user_list))

#You are given a list of numbers such as input_list = [31, 63, 76, 89].
# Find and print the largest number in input_list using the reduce() function.
input_list = [31, 63, 76, 89]
print(reduce(lambda x,y:x if x>y else y,input_list))
