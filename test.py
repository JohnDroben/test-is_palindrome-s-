# Пошаговый алгоритм для проверки строки на палиндром:
# 1. Привести строку к нижнему регистру (чтобы игнорировать регистр букв).
# 2. Удалить все небуквенно-цифровые символы (пробелы, знаки препинания и т.д.).
# 3. Использовать два указателя:
#                        - left начинает с первого символа строки.
#                        - right начинает с последнего символа строки.
# 4. Сравнивать символы на позициях left и right:
# 5. Если символы не совпадают — строка не палиндром (вернуть False).
# 6. Если совпадают — сдвинуть left вправо, right влево.
# 7. Повторять сравнение, пока left меньше right.
# 8. Если все пары символов совпали — строка палиндром (вернуть True).


def is_palindrome(s):
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Примеры использования
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("maddam"))  # True
print(is_palindrome("Hello"))  # False