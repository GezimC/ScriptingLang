# count = 1
#
# print(count)
# print(count+1)
# print(count+2)
# print(count+3)
#
#
#
# count = 0
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print(count + i)
#
#
# count = 0
# for i in range(11,0,-1):
#     print(count+i)
#
#

# 1. Create a list of numbers and print each element using a for loop.
lista_1 = [1,2,3,4,5, 100, 200, 300]
for element in lista_1:
    print(element)


lista_1 = [1,2,3,4,5, 100, 200, 300]
length = len(lista_1)

for index in range(0, length  ):
    print(lista_1[index])

# 2. Given a list of numbers, calculate the sum of all elements using a for loop.

numbers = [1,2,3,4]
sum_numbers = 0

for num in numbers:
    sum_numbers += num

print(sum_numbers)

# v2 with range()
numbers = [1,2,3,4]
sum_numbers = 0

for index in range(0, 4):
     sum_numbers  += numbers[index]

print(sum_numbers)

# 3. Given a list of numbers, count how many numbers are even.

numbers = [1,2,3,4]
count_even = 0

for num in numbers:
    if num%2==0:
        count_even +=1

print(count_even)

# 4. Given a list of numbers, find the largest number without using max().
numbers = [10,2,5,12, 17]

max_of_numbers = numbers[0] #10

for number in numbers:
    if max_of_numbers < number:
        max_of_numbers = number

print(max_of_numbers)


# 5. Given a list of numbers, replace every negative number with 0.

list_of_numbers = [1,2,-3,4,-5]
print(list_of_numbers)

for index in range(0,5):
    if list_of_numbers[index] < 0:
        list_of_numbers[index] = 0

print(list_of_numbers)

# 6. Given a list of boolean values, count how many values are True.