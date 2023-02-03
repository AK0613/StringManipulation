# Given two strings S and T, return if they are equal when both are typed out. Any # in the string count as a backspace

def check_strings(s, t):
    p1 = len(s) - 1
    p2 = len(t) - 1
    equal = True

    while p1 >= 0 or p2 >= 0:
        if s[p1] == '#':
            count = 2
            while count > 0:
                p1 -= 1
                count -= 1
                if s[p1] == '#':
                    count += 2
        if t[p2] == '#':
            count = 2
            while count > 0:
                p2 -= 1
                count -= 1
                if t[p2] == '#':
                    count += 2
        else:
            if s[p1] == t[p2]:
                p1 -= 1
                p2 -= 1
            else:
                equal = False
                return equal

    return equal


s = 'abc##d'
t = 'abz##d'

print(check_strings(s, t))

# OLD Solution
# def trim_string(input):
#     temp = []
#     for x in range(len(input)):
#         if not input[x] == '#':
#             temp.append(input[x])
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
