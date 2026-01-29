import re

def is_palindrome(text: str) -> bool:
    clean = re.sub(r"[^a-zA-Z0-9]", "", text.lower())
    return clean == clean[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
