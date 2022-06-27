# ______________________________________________________________________________________________________________________
# timsort, insertion sort for timsort, merge for timsort пока не понял
# ______________________________________________________________________________________________________________________
def insertion_sort(nums, left=0, right=None):
    if right is None:
        right = len(nums) - 1
    # Цикл от элемента, обозначенного
    # `left` до элемента, обозначенного` right`
    for i in range(left + 1, right + 1):
        # Это элемент, который мы хотим разместить в
        # правильное место
        key_item = nums[i]
        # Инициализировать переменную, которая будет использоваться для
        # найти правильную позицию указанного элемента
        # by `key_item`
        j = i - 1
        # Просмотрите список элементов (слева
        # часть массива) и найдите правильную позицию
        # элемента, на который ссылается `key_item`. Сделай это только
        # если `key_item` меньше, чем соседние значения.
        while j >= left and nums[j] > key_item:
            # Сдвинуть значение на одну позицию влево
            # и переместите `j`, чтобы указать на следующий элемент
            # (справа налево)
            nums[j + 1] = nums[j]
            j -= 1
        # Когда вы закончите сдвигать элементы, установите
        # `key_item` в правильном месте
        nums[j + 1] = key_item
    return nums


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result[k] = left[i]
            k += 1
            i += 1
        else:
            result[k] = right[j]
            k += 1
            j += 1

    # checking if anything left in lists
    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1
    # while len(result) < len(left) + len(right):
    #     if left[i] <= right[j]:
    #         result[k] = left[i]
    #         i += 1
    #         k += 1
    #     else:
    #         result[k] = right[j]
    #         j += 1
    #         k += 1
    #     if j == len(right):
    #         result += left[i:]
    #         break
    #     if i == len(left):
    #         result += right[j:]
    #         break
    return result


def timsort(nums):
    min_run = 32
    n = len(nums)
    # Начните с нарезки и сортировки небольших порций
    # входной массив. Размер этих срезов определяется
    # размер вашего `min_run`.
    for i in range(0, n, min_run):
        insertion_sort(nums, i, min((i + min_run - 1), n - 1))
    # Теперь вы можете начать объединение отсортированных фрагментов.
    # Начать с min_run, увеличивая размер вдвое
    # каждую итерацию, пока вы не превысите длину
    # массив.
    size = min_run
    while size < n:
        # Определить массивы, которые будут
        # быть объединенными
        for start in range(0, n, size * 2):
            # Вычислить среднюю точку (где заканчивается первый массив
            # и второй запуск) и ʻendpoint` (где
            # второй массив заканчивается)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            # Объединить два подмассива.
            # Массив `left` должен идти от` start` до
            # `midpoint + 1`, а массив` right` должен
            # перейти от `midpoint + 1` к ʻend + 1`.
            merged_array = merge(
                left=nums[start:midpoint + 1],
                right=nums[midpoint + 1:end + 1])
            # Наконец, поместите объединенный массив обратно в
            # ваш массив
            nums[start:start + len(merged_array)] = merged_array
        # Каждая итерация должна удваивать размер ваших массивов
        size *= 2
    return nums
