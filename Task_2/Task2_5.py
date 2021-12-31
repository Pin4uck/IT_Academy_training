str_one = str()
while len(str_one) == 0:
    str_one = input('Enter the first string:')


str_two = str()
while len(str_two) == 0:
    str_two = input('Enter the second string:')


if len(str_one) != len(str_two):  # string equality check
    print('Strings are not equal')
if len(str_one) == len(str_two):
    for i in range(len(str_one)):
        if str_one[i] != str_two[i]:
            print('Strings are not equal')
            break
        if i == len(str_one) - 1:
            print('Strings are equal')


if f'{str_one}'.find(f'{str_two}') != -1:  # checking substring
    print("The second string is a substring of the first string")
else:
    print("The second string is not a substring of the first string")


r_str_one = str_one[::-1]
for i in range(len(str_one)):  # checking if a string is a palindrome
    if str_one[i] != r_str_one[i]:
        print('The first string is not palindrome')
        break
    if i == len(str_one) - 1:
        print('The first string is palindrome')
