# "Декораторы"
def is_prime(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        for i in range(2, int(x ** 0.5 + 1)):
            if x % i == 0:
                print("Составное")
                break
        else:
            if x > 1:
                print("Простое")
        return x

    return inner


@is_prime
def sum_three(one, two, three):
    return sum((one, two, three))


result = sum_three(2, 3, 6)
print(result)

# Результат консоли:
# Простое
# 11
