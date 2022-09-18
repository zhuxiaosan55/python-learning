'''for i in range(1, 21):
    print(i)

numbers = list(range(1, 1000001))
# print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
'''
numbers = list(range(1, 21, 2))
for i in range(0, 10):
    print(numbers[i])
print("the first three items in the list are")
print(numbers[0:3])

threes = [value**3 for value in range(1, 11)]
print(threes)
