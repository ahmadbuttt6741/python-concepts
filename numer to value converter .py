def words_to_number(text):
    """Convert number words to numeric value"""

    # Define word-to-number mappings
    ones = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19
    }

    tens = {
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90
    }

    scales = {
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000,
        'billion': 1000000000,
        'trillion': 1000000000000
    }

    # Clean and split the input text
    text = text.lower().replace('-', ' ').replace(' and ', ' ')
    words = text.split()

    current = 0
    result = 0

    for word in words:
        if word in ones:
            current += ones[word]
        elif word in tens:
            current += tens[word]
        elif word == 'hundred':
            current *= 100
        elif word in scales:
            current *= scales[word]
            result += current
            current = 0

    return result + current


# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("  Number Words to Value Converter")
    print("=" * 50)

    # Test examples
    test_cases = [
        "two hundred",
        "fifty five",
        "one thousand two hundred thirty four",
        "nine hundred ninety nine",
        "one million",
        "three thousand five hundred",
        "twenty one",
        "fifteen",
        "one hundred and one"
    ]

    print("\n--- Test Examples ---\n")
    for test in test_cases:
        value = words_to_number(test)
        print(f'"{test}" => {value}')

    # Interactive input
    print("\n--- Try Your Own ---\n")
    while True:
        user_input = input("Enter a number in words (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            result = words_to_number(user_input)
            print(f"Numeric value: {result}\n")
        except Exception as e:
            print(f"Error: Could not convert. Please try again.\n")
