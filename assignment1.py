
def to_binary(n, bits=8):
    return format(n & ((1 << bits) - 1), f'0{bits}b')


def to_decimal(binary):
    bits = len(binary)
    value = int(binary, 2)

    if binary[0] == '1':
        value -= (1 << bits)

    return value


def signed_binary_add(a, b):
    bits = 8

    bin_a = to_binary(a, bits)
    bin_b = to_binary(b, bits)

    result = (int(bin_a, 2) + int(bin_b, 2)) & 0xFF
    bin_result = format(result, '08b')
    decimal_result = to_decimal(bin_result)

    # Overflow occurs when operands have the same sign
    # but the result has a different sign.
    overflow = (
        bin_a[0] == bin_b[0]
        and bin_result[0] != bin_a[0]
    )

    print("First Operand  :", bin_a, "(", a, ")")
    print("Second Operand :", bin_b, "(", b, ")")
    print("Binary Result  :", bin_result)
    print("Decimal Result :", decimal_result)
    print("Overflow       :", "Yes" if overflow else "No")
    print("-" * 40)


print("a) (24 + (+17))")
signed_binary_add(24, 17)

print("b) ((-25) + (-18))")
signed_binary_add(-25, -18)
