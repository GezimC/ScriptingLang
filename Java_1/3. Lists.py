# lists - []

notat = [10,8,10,9,7]

print(notat[-5])

# modify list elements
notat[-1] = 10
print(notat)


# mixed types lists
# mixed_list = [1,2,3, 'a', 'b', 'c', 4,5,6, [7,8.5,9] ]
#
# print( "Length of mixed list", len(mixed_list))
# print(mixed_list[-1][1] , [-1][0])
# lista_1 = [-1]
#
# nested_lists = [ [1,2,3] , ['a','b','c'] , [4,5,6], "Test123" ]
# print(nested_lists[1])
#
# simple_list = [1, 2, 3, 4]
#
# nested_lists_1 = [ ['a','b','c'] , 10, 20, 'Test456' ]
# print(nested_lists_1[-1][2])



lista_2 = [1,2,3,'a','b','c', 4,5,6]

# slice

print(lista_2[3 : 6])

print(lista_2[3:-1])

notat = [10,9,8,10,8]

notat.append(10)

print("After append()",notat)

notat.insert(1,6)



print("After insert", notat)

notat_2 = [10,9,8,7,6]

notat.extend(notat_2)

print(notat)
print(notat_2)


print(notat)

notat.remove(6)

notat.pop()

print(notat)

print(notat.index(9))

print(notat.count(10))

# ------------------------------------------

new_list = [5,1,7,8,10,3]

# sort list and apply changes
new_list.sort(reverse=True)
print(new_list)

#sort list and create new list
print(sorted(new_list))



number = 8

if number%2==0 and number>5:
    print(f'Number {number} is even and bigger then 5!')
elif number%2==0 and number<5:
    print(f'Number {number} is even and less then 5!')
else:
    print('Number is odd!')




