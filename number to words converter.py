def number_to_words(num):
    """Convert a number to its English word representation"""

    if num == 0:
        return "zero"

    # Word mappings
    ones = [
        "", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]

    scales = ["", "thousand", "million", "billion", "trillion"]

    def convert_below_thousand(n):
        """Convert a number less than 1000 to words"""
        result = ""

        # Handle hundreds
        if n >= 100:
            result += ones[n // 100] + " hundred"
            n %= 100
            if n > 0:
                result += " "

        # Handle tens and ones
        if n >= 20:
            result += tens[n // 10]
            if n % 10 > 0:
                result += " " + ones[n % 10]
        elif n > 0:
            result += ones[n]

        return result

    # Handle negative numbers
    if num < 0:
        return "negative " + number_to_words(-num)

    result = ""
    scale_index = 0

    # Process number in groups of three digits
    while num > 0:
        if num % 1000 != 0:
            chunk = convert_below_thousand(num % 1000)
            if scales[scale_index]:
                chunk += " " + scales[scale_index]
            if result:
                result = chunk + " " + result
            else:
                result = chunk
        num //= 1000
        scale_index += 1

    return result.strip()


# Main program
if __name__ == "__main__":
    print("=" * 55)
    print("     Number to English Words Converter")
    print("=" * 55)

    # Test examples
    test_numbers = [
        0, 5, 15, 21, 99, 100, 101, 200, 555, 999,
        1000, 1234, 5678, 10000, 100000,
        1000000, 1234567, 1000000000, -42
    ]

    print("\n--- Test Examples ---\n")
    for num in test_numbers:
        words = number_to_words(num)
        print(f"{num:>15} => {words}")

    # Interactive input
    print("\n" + "=" * 55)
    print("--- Try Your Own ---")
    print("=" * 55 + "\n")

    while True:
        user_input = input("Enter a number (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Goodbye! 👋")
            break

        try:
            number = int(user_input)
            result = number_to_words(number)
            print(f"In words: {result}\n")
        except ValueError:
            print("❌ Please enter a valid integer!\n")
