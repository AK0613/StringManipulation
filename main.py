# Given two strings S and T, return if they are equal when both are typed out. Any # in the string count as a backspace

# Optimal solution to check if strings are equal
def check_strings(s, t):
    # Pointers initialized at the end of the string
    p1 = len(s) - 1
    p2 = len(t) - 1
    # Assume that the strings are equal
    equal = True
    # While loop ensures that we traverse the entire string and stop at index = 0
    while p1 >= 0 or p2 >= 0:
        # If # is found at position p1, ignore the current value as well as the next value.
        if s[p1] == '#':
            # Count = 2 to skip the # character and the following char as well
            count = 2
            # Then we check if the characters to be skipped happen to be #
            while count > 0:
                # Move the pointer to the left by one and the counter
                p1 -= 1
                count -= 1
                # If the current value at index p1 happens to be another #, then reset the count to 2.
                # This repeats as long as we keep finding # in the string
                if s[p1] == '#':
                    count += 2
        # Repeat process for string 2
        if t[p2] == '#':
            count = 2
            while count > 0:
                p2 -= 1
                count -= 1
                if t[p2] == '#':
                    count += 2
        # If the current value of the strings is not #, then evaluate them to see if they are equal
        else:
            if s[p1] == t[p2]:
                # If equal move the pointers to the left
                p1 -= 1
                p2 -= 1
            # Else the strings are not equal and we can set equal to false
            else:
                equal = False

    return equal


s = 'abc##d'
t = 'abz##d'

print(check_strings(s, t))

# Brute-force solution that uses a stack to hold each character in the string.
# As we iterate through it, letters are added to the stack and they are also removed when encountering a #
# OLD Solution
# def trim_string(input):
#     #temp list to hold letters as we iterate through the string
#     temp = []
#     for x in range(len(input)):
# If the current letter is not a # add it to the temp list
#         if not input[x] == '#':
#             temp.append(input[x])
# Remove the last letter added if the current value is #
#         else:
#             temp.pop()
#     return temp
#
#
# s = 'ab#z'
# t = 'az#z'
#
# str1 = trim_string(s)
# str2 = trim_string(t)
#
# if (str1 == str2):
#     print('Yeah nice they is equal')
# else:
#     print('You fucked up')
