
def process_numbers(numbers):
    """Process numbers by multiplying even values by 2 and odd values by 3.

    Args:
        numbers: A list of integers to process.

    Returns:
        A list containing the processed integers.
    """
    return [
        number * 2 if number % 2 == 0 else number * 3
        for number in numbers
    ]


def process_strings(strings):
    """Change string case based on the length of each string.

    Args:
        strings: A list of strings to process.

    Returns:
        A space-separated string with the processed values.
    """
    # Preserve the original rule: five or more characters means uppercase.
    processed_strings = [
        value.upper() if len(value) >= 5 else value.lower()
        for value in strings
    ]
    return " ".join(processed_strings)


def main():
    """Run the program and display the processed numbers and strings."""
    numbers = [1, 2, 3, 4, 5, 6, 7]
    fruits = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(numbers)
    processed_strings = process_strings(fruits)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()

