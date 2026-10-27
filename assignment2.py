
def logical_left_shift(binary, positions):
    print("Original 8-bit number:", binary)

    for i in range(positions):
        binary = binary[1:] + "0"
        print(f"After left shift {i + 1}:", binary)

    return binary


def logical_right_shift(binary, positions):
    print("Original 8-bit number:", binary)

    for i in range(positions):
        binary = "0" + binary[:-1]
        print(f"After right shift {i + 1}:", binary)

    return binary


# Part (a): Logical left shift
print("Logical Left Shift")
num1 = "11110110"
result1 = logical_left_shift(num1, 2)
print("Final 8-bit result:", result1)

print()

# Part (b): Logical right shift
print("Logical Right Shift")
num2 = "10010100"
result2 = logical_right_shift(num2, 2)
print("Final 8-bit result:", result2)
