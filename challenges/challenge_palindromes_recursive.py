def is_palindrome_recursive(word, low_index, high_index):
    try:
        if word[low_index] == word[high_index]:
            if high_index - low_index <= 1:
                return True
            next = word[low_index + 1: high_index]
            return is_palindrome_recursive(next, 0, len(next) - 1)
        return False
    except Exception:
        return False


teste = 'aaa'

print(is_palindrome_recursive(teste, 0, len(teste) - 1))
