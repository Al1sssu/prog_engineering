def is_palindrome(data):
    return data == data[::-1]


def test_is_palindrome():
    test_cases = ["radar", "level", "hello", "12321", "racecar"]

    for test_case in test_cases:
        if is_palindrome(test_case):
            continue
        else:
            print("NO")
            return

    print("YES")


test_is_palindrome()

import sys

def main():
    data = sys.stdin.readline().strip()

    if is_palindrome(data):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
