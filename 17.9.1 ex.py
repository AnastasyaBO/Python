array = list(map(int, input("Введите последовательность цифр через пробел: ").split()))
#Полученный массив преобразуем в список
element = int(input("Введите число: "))
array.append(element)
#Новое чило добавляем в список array
print(array)


def sorting_list():
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array = sorting_list()
print(array)


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        if array[0] == element:
            return "Введенное число является наименьшим в списке, число больше имеет индекс - 0"
        if array[-1] == element:
            return f"Введенное число является самым большим, наименьшее имеет индекс - {len(array) - 1}"
        else:
            a = 1
            while array[middle] == array[middle - a]:
                a += 1
            return f"Индекс предыдущего элемента - {middle - a}\nИндекс следующего элемента - {middle + a}"
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
print(binary_search(array, element, 0, len(array)))
