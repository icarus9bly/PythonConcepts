# https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/

# In Python 3.0, the * operator was added to the multiple assignment syntax, allowing us to capture remaining items after an unpacking into a list
numbers = [1,2,4,56,434,22]
first, *rest = numbers
print(first)
print(rest)
*begining, last = numbers
print(last)