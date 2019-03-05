def str_range(first_str, last_str, step=1):
    if step > 0:
        offset = 1
    else:
        offset = -1
    for i in range(ord(first_str), ord(last_str)+offset, step):
        yield chr(i)


for letter in str_range('c', 'a', -2):
    print(letter, end=' ')
print('\n')

for letter in str_range('א', 'ז'):
    print(letter, end=' ')
print('\n')

for letter in str_range('א',
                        'ז',
                        2):
    print(letter, end=' ')
print('\n')
