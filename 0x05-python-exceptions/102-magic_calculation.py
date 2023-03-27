#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for pi in range(1, 3):
        try:
            if pi > a:
                raise Exception('Too far')
            result += a ** b / pi
        except Exception:
            result = b + a
            break
    return result
