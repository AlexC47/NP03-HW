def my_function(*args, **kwargs):
    total = 0
    for x in args:
        if type(x) is int or type(x) is float:
            total += x
    return total


print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2))


def my_function(n):
    if n == 0:
        return 0, 0, 0

    sum_temp, even_temp, odd_temp = my_function(n - 1)

    if n % 2 == 0:
        even_sum = n + even_temp
        odd_sum = odd_temp
    else:
        even_sum = even_temp
        odd_sum = n + odd_temp

    tot_sum = n + sum_temp

    return (tot_sum, even_sum, odd_sum)


print(my_function(7))


user_input = input('int pls: ')


try:
    my_int = int(user_input) or float(user_input)
except ValueError:
    print('0')
else:
    print(f'{user_input} is an integer/float')

