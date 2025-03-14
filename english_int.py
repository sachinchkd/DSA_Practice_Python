def english_int(number):
        number = int(number)
        count = 0

        while (number<=0):
            number = number / 10
            count += 1

def decimal_count(number):
    number = int(number)
    count = 0
    while (number != 0):
        count += 1
        number = int( number / 10)
        # print(number)
        
    return count

# print("unit place",decimal_count(1111))
def number_to_words(n):
    if n == 0:
        return "Zero"

    # Dictionaries for number mappings
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def num_to_words(num):
        """Convert a number (1-999) into words."""
        if num == 0:
            return ""
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
        else:
            return ones[num // 100] + " Hundred" + (" " + num_to_words(num % 100) if num % 100 != 0 else "")

    result = ""
    chunk_count = 0

    while n > 0:
        chunk = n % 1000  # Extract last 3 digits
        if chunk != 0:
            result = num_to_words(chunk) + " " + thousands[chunk_count] + " " + result
        n //= 1000  # Remove last 3 digits
        chunk_count += 1

    return result.strip()

# Test cases
print(number_to_words(123))      # Output: "One Hundred Twenty Three"
print(number_to_words(1005))     # Output: "One Thousand Five"
print(number_to_words(1000000))  # Output: "One Million"
print(number_to_words(999999999))# Output: "Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine"
print(number_to_words(0))        # Output: "Zero"



