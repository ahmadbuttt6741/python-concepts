from num2words import num2words

print(num2words(15))        # fifteen
print(num2words(1234))      # one thousand, two hundred and thirty-four
print(num2words(1000000))   # one million


number = int(input("Enter a number : "))

print(num2words(number))
