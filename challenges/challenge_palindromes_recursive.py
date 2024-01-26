def is_palindrome_recursive(word, low_index, high_index):
    # se nao houver palavra
    if not word:
        return False

    # coloca todas as letras em minusculo
    word = word.lower()

    # caso base
    if low_index > high_index:
        return True

    # se a letra da posicao low_index for igual a letra da posicao high_index
    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
