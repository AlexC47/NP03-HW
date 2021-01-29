# def my_function(*args, **kwargs):
#     total = 0
#     for x in args:
#         if type(x) is int:
#             total += x
#     return total
#
#
# print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
# print(my_function())
# print(my_function(2, 4, 'abc', param_1=2))


# odd = 0
# even = 0

def my_function(n):
    # odd: int = 0
    # even = 0
    if n == 0 or n == -1:
        return 0
    elif n % 2 == 0:
        even = n
        # even += n
        # print(even)
        return even + my_function(n - 2)
        # return n + my_function(n - 1) as even
    elif n % 2 == 1:
        odd = n
        # odd += n
        print(odd)
        return odd + my_function(n - 2)
        # return n + my_function(n - 1) as odd

    # odd += n
    # print(odd, even)
    return n + my_function(n - 1)
    # return n + my_function(n - 1), odd, even


print(my_function(7))


# user_input = input('int pls: ')
#
#
# try:
#     my_int = int(user_input)
# except ValueError:
#     print('0')
# else:
#     print(f'{user_input} is an integer')

