def multiply_all (*args: int) -> int:
    result = 1
    for number in args:
        result *= number
    return result
pass
print(multiply_all(2, 3, 4))
print(multiply_all(5, 6))