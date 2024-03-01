def bubble_sort(data: list[int]) -> list[int]:
    ready = False
    while not ready:
        ready = True
        x = 0
        for i in range(1, len(data) - x):
            if data[i] < data[i - 1]:
                data[i], data[i - 1] = data[i - 1], data[i]
                ready = False
    return data


x = [4, 2, 1, 7, 3, 0]
print(bubble_sort(x))
