# reparte as strings
def quick_sort(string, start, end):
    if start < end:
        pivot = partition(string, start, end)
        quick_sort(string, start, pivot - 1)   # < elementos a esq do pivot
        quick_sort(string, pivot + 1, end)  # > elementos a direita do pivot


def partition(string, start, end):
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):  # o index passa por todos os elementos
        if string[index] <= pivot:  # elem index for menor ou igual ao pivot
            delimiter = delimiter + 1  # o delimiter aumenta
            string[index], string[delimiter] = string[delimiter], string[index]
            # o elemento no index é trocado pelo elemento no delimiter
    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]
    # o elemento no delimiter + 1 é trocado pelo elemento final
    return delimiter + 1


# ordena e junta a string
def ordened(string, start, end):
    new_string = list(string.lower())  # transforma a string em lista e min
    quick_sort(new_string, start, end)  # ordena a lista
    return "".join(new_string)  # transforma a lista em string


def is_anagram(first_string, second_string):
    if (len(first_string) == 0) or (len(second_string) == 0):  # string vazia
        return tuple([first_string, second_string, False])

    ordered_first = ordened(first_string, 0, len(first_string) - 1)  # ordena
    ordered_second = ordened(second_string, 0, len(second_string) - 1)

    if ordered_first == ordered_second:  # compara as strings ordenadas
        return tuple([ordered_first, ordered_second, True])

    else:
        return tuple([ordered_first, ordered_second, False])
