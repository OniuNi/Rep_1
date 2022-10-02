import timeit
import random


def generate_random_strings(num):
    result = []
    for i in range(num):
        s = ''.join(random.choice([chr(i) for i in range(ord('a'), ord('z'))]) for _ in range(5))
        result.append(s)
    return result


ten = generate_random_strings(10)
hundred = generate_random_strings(100)
thousand = generate_random_strings(1000)

# For eval() statements where input is translated to list names
mapping = {
    10: 'ten',
    100: 'hundred',
    1000: 'thousand'
}


# Based on input, evaluate the expression to sort adequate list
def run_sort(num):
    eval(f'{mapping[num]}.sort()')


# Based on input, evaluate the expression to sort adequate list
def run_sorted(num):
    eval(f'sorted({mapping[num]})')


for index, num_samples in enumerate([10, 100, 1000]):
    result = timeit.timeit(f"run_sorted({num_samples})", number=100000, globals=globals())
    print(f'sorted() on {num_samples} took {result} seconds')

print('____________________________________________________')

for index, num_samples in enumerate([10, 100, 1000]):
    result = timeit.timeit(f"run_sort({num_samples})", number=100000, globals=globals())
    print(f'sort() on {num_samples} took {result} seconds')