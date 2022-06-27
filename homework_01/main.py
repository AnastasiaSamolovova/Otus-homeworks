"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    list_of_squares = []
    
    for n in nums:
        list_of_squares.append(n*n)
    
    return list_of_squares


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False

def filter_numbers(nums, nums_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    results = []
    
    if nums_type == ODD:
        for n in nums:
            if n % 2 != 0:
                results.append(n)
    
    if nums_type == EVEN:
        for n in nums:
            if n % 2 == 0:
                results.append(n)
                     
    if nums_type == PRIME:
        for n in nums:
            if is_prime(n):
                results.append(n)
    
    return results