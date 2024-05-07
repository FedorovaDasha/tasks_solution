def get_monotonic_segments(numbers):
    start_index = 0
    end_index = 0
    sign = numbers[0] < numbers[1]
    result = dict()
    for i in range(len(numbers) - 1):
        if (numbers[i] < numbers[i + 1] and sign) or (
            numbers[i] > numbers[i + 1] and not sign
        ):
            end_index = i + 1
        else:
            sign = not sign
            result[end_index - start_index + 1] = (start_index, end_index)
            if numbers[i] == numbers[i + 1]:
                start_index = i + 1
            else:
                start_index = i
            end_index = i + 1
    # Добавим границы в результат для случая, когда у нас на входе
    # монотонный список, либо последние элементы списка образуют
    # монотонный подотрезок.
    result[end_index - start_index + 1] = (start_index, end_index)
    return result[max(result)]


numbers = list(map(int, input().split(",")))
print(*get_monotonic_segments(numbers), sep=", ")
