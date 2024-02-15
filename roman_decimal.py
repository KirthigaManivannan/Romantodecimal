def roman_to_decimal(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in reversed(roman):
        current_value = roman_dict[char]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total

# Example of usage
roman_numeral = input("Enter a Roman numeral: ")
decimal_equivalent = roman_to_decimal(roman_numeral)
print(f"Decimal equivalent: {decimal_equivalent}")
