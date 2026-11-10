def is_palindrome(s):
    left = 0
    right  = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True


assert is_palindrome("racecar") == True
assert is_palindrome("foo") == False
assert is_palindrome("oof") == False
assert is_palindrome("a") == True
assert is_palindrome("ab") == False
assert is_palindrome("aba") == True
assert is_palindrome("abba") == True

        