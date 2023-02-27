def myAtoi(s: str) -> int:
    # Ignore leading whitespace
    s = s.lstrip()

    # Check for sign
    sign = 1
    if s and s[0] in ('-', '+'):
        if s[0] == '-':
            sign = -1
        s = s[1:]

    # Read digits
    digits = []
    for c in s:
        if c.isdigit():
            digits.append(c)
        else:
            break

    # Convert digits to integer
    if not digits:
        return 0
    num = int(''.join(digits)) * sign

    # Clamp integer to range
    if num < -2 ** 31:
        return -2 ** 31
    elif num > 2 ** 31 - 1:
        return 2 ** 31 - 1
    else:
        return num
