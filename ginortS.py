# Enter your code here. Read input from STDIN. Print output to STDOUT
def sort_string(s):
    lowercase = []
    uppercase = []
    odd_digits = []
    even_digits = []

    for char in s:
        if char.islower():
            lowercase.append(char)
        elif char.isupper():
            uppercase.append(char)
        elif char.isdigit():
            if int(char) % 2 == 0:
                even_digits.append(char)
            else:
                odd_digits.append(char)

    lowercase.sort()
    uppercase.sort()
    odd_digits.sort()
    even_digits.sort()

    # Combine the sorted lists and return the result
    return ''.join(lowercase + uppercase + odd_digits + even_digits)

if __name__ == '__main__':
    input_string = input().strip()
    print(sort_string(input_string))
