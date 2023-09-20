def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if len(word) == 1:
        return True

    WORD = word.lower()

    if low_index <= high_index:
        if not is_palindrome_recursive(WORD, low_index + 1, high_index - 1):
            return False

    return WORD[low_index] == WORD[high_index]
