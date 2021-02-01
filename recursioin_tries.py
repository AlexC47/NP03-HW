# even = 0
# odd = 0
#
#
# def my_function(n):
#     if n <= 0:
#         return 0
#     elif n % 2 == 0 and n > 0:
#         global even
#         even += n
#     elif n % 2 == 1 and n > 0:
#         global odd
#         odd += n
#
#     return (n + my_function(n - 1), even, odd)
#
#
# print(my_function(7))


# def my_sum(n):
#     if n <= 0:
#         return 0
#     elif n % 2 == 0:
#         even = n
#         return even + my_sum(n - 1)
#         # return even
#     elif n % 2 == 1:
#         odd = n
#         return odd + my_sum(n - 1)
#         # return odd
#
#     return even + my_sum(n - 1)
#
#     return (3, 1, 2)
#
# print(my_sum(7))


# def my_sum(n):
#     if n <= 0:
#         return (0, 0, 0)
#     elif n % 2 == 1:
#         def odd(n):
#             if n <= 0:
#                 return 0
#
#             return n + odd(n - 2)
#
#     elif n % 2 == 0:
#         def even(n):
#             if n <= 0:
#                 return 0
#
#             return n + even(n - 2)
#
#
#     return (n + my_sum(n - 1), n + odd(n - 1), n + even(n - 1))
#
# print(my_sum(7))


# def my_function(n):
#     def my_sum(n):
#         if n <= 0: return 0
#         return n + my_sum(n - 1)
#
#     def even(n):
#         if n <= 0 and n % 2 == 1: return 0
#
#         return n + even(n - 1)
#
#     def odd(n):
#         if not n >= 0 or n % 2 == 0: return 0
#         return n + odd(n - 1)
#
#
#     return (my_sum(n), even(n), odd(n))
#
# print(my_function(7))



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