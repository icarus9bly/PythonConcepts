# https://realpython.com/python-itertools/#what-is-itertools-and-why-should-you-use-it

numbers = [1,3,4,5,6,7]
it_obj = iter(numbers)
print(next(it_obj))
print(next(it_obj))
print(next(it_obj))
print(next(it_obj))
print(next(it_obj))
print(next(it_obj))

# Under the hood, the zip() function works, in essence, by calling iter() on each of its arguments, then advancing each iterator returned by iter() with next() and aggregating the results into tuples. The iterator returned by zip() iterates over these tuples.
a = zip([1,3,2],["adi","wad","hjk"])
print(next(a))
print(next(a))
print(next(a))

# The map() built-in function is another “iterator operator” that, in its simplest form, applies a single-parameter function to each element of an iterable one element at a time:
mapped = map(len, ["eee","ceccce", "ecckkekec"])
print(list(mapped))
def my_func(x):
    return x * len(x)
mapped_outi = map(my_func,["beem","boom","bhoosh"])
print(list(mapped_outi))

# Since iterators are iterable, you can compose zip() and map() to produce an iterator over combinations of elements in more than one iterable.
sum_of_all_nums = map(sum,zip([43,56,23], [90,33,899]))
print(list(sum_of_all_nums))

inputs = [1, 2, 3, 4, 5, 6]
n = 2
# Expected: [(1, 2), (3, 4), (5, 6)]
def divider(inputs, n):
    group = len(inputs) // n
    result = []
    for idx, elem in enumerate(inputs):
        if idx % n == 0:
            result.append(tuple(inputs[idx:idx+2]))
    return result
out = divider(inputs, n)
print(out)