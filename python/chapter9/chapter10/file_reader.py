with open('python/chapter9/chapter10/pi_digits.txt') as file_object:
   # contents = file_object.read()
    lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()

birthday = input('enter your birthday,in the form mmddyy:')
if birthday in pi_string:
    print('your birthday appears in the first million digits of pi')
else:
    print('your birthday does not appear in the first million digits of pi')

print(pi_string[:20])
print(len(pi_string))
