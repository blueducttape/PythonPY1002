def palindrome(data):
    data = data.replace(' ', '').lower()
    return 'Палиндром' if data == data[::-1] else 'Не палиндром'


if __name__ == "__main__":
    data = input()
    print (palindrome(data))