NO_SOLUTION = 'No solution for selected parameters'


def get_binary_scheme(n):
    """Функция для построения списка всех вариантов
    расстановки знака +"""
    # Функция возвращает список схем расстановки.
    # В схеме '1' - наличие знака '+' между цифрами
    # '0' - отсутствие
    binary_scheme = []
    i = 1
    limit = 2**(n) - 1
    while i <= limit:
        binary_scheme.append(bin(i)[2:].zfill(n))
        i += 1
    return binary_scheme


def get_num_expression(n, m):
    nums = [i for i in range(1, n + 1)]
    binary_scheme = get_binary_scheme(n - 1)
    # Проверим случай, когда знак плюс стоит между всеми цифрами числа
    # Если полученная сумма больше m, то решения нет,
    # т.к. во всех остальных случаях расстановки мы получим сумму еще больше
    if sum(nums) > m:
        return print(NO_SOLUTION)
    for scheme in binary_scheme:
        result = 0
        full_exp = ''
        j = 0
        exp = str(nums[0])
        for i, elem in enumerate(scheme):
            if elem == '0':
                exp = (''.join(map(str, nums[j:i+2])))
            if elem == '1':
                result += int(exp)
                if full_exp:
                    full_exp += '+' + exp
                else:
                    full_exp += exp
                exp = str(nums[i+1])
                j = i + 1
        result += int(exp)
        full_exp += '+' + exp
        if result == m:
            return print(f'{full_exp}={result}')
    return print(NO_SOLUTION)


n, m = tuple(map(int, input().split(",")))
get_num_expression(n, m)
