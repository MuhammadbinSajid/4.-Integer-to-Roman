class RomanConverter:
    """
    A class to convert an integer to a Roman numeral.
    """

    def __init__(self, number):
        """
        Initializes the RomanConverter instance with a number.
        :param number: Integer to be converted to Roman numeral
        """
        if not isinstance(number, int) or number <= 0 or number > 3999:
            raise ValueError("Number must be an integer between 1 and 3999.")
        self.number = number

    def to_roman(self):
        """
        Converts the integer to a Roman numeral.
        :return: Roman numeral as a string
        """
        value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        result = ""
        number = self.number
        for value, numeral in value_map:
            while number >= value:
                result += numeral
                number -= value
        return result


# Example Usage
try:
    number = int(input("Enter an integer between 1 and 3999: "))
    converter = RomanConverter(number)
    print(f"The Roman numeral for {number} is: {converter.to_roman()}")
except ValueError as e:
    print(e)
