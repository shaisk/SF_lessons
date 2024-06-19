# Проверка корректности ввода
def is_valid_input(sequence):
    try:
        list(map(float, sequence.split()))
        return True
    except ValueError:
        return False


# Сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Двоичный поиск
def binary_search_position(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def main():
    sequence = input("Введите последовательность чисел через пробел: ")

    if not is_valid_input(sequence):
        print("Некорректный ввод. Пожалуйста, введите последовательность чисел через пробел.")
        return

    num_str_list = sequence.split()
    num_list = list(map(float, num_str_list))

    user_number_str = input("Введите число: ")

    try:
        user_number = float(user_number_str)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")
        return

    sorted_list = bubble_sort(num_list)
    print("Отсортированный список:", sorted_list)

    position = binary_search_position(sorted_list, user_number)
    print(
        f"Номер позиции элемента, который меньше {user_number}, а следующий за ним больше или равен этому числу: {position}")


if __name__ == "__main__":
    main()
