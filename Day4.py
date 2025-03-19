#📢 Day 4 – Daily Python Challenge 🐍
#🚀 Challenge:Write a Python program that converts numbers into words! 🔢➡️🔡

#🔥Example:
#📌 Input: 123
#📌 Output: "One Hundred Twenty-Three"

#📌 Input: 5067
#📌 Output: "Five Thousand Sixty-Seven"

def number_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    if n == 0:
        return "Zero"
    
    def convert_chunk(num):
        if num == 0:
            return ""
        elif num < 20:
            return ones[num]
        elif num < 100:
            return tens[num // 10] + ("-" + ones[num % 10] if num % 10 != 0 else "")
        else:
            return ones[num // 100] + " Hundred" + (" " + convert_chunk(num % 100) if num % 100 != 0 else "")
        
    result = ""
    check_index = 0
    while n > 0:
        if n % 1000 != 0:
            result = convert_chunk(n % 1000) + (" " + thousands[check_index] if thousands[check_index] != "" else "") + (" " + result if result != "" else "")
        n //= 1000
        check_index += 1

    return result.strip()

# Test the function
print(number_to_words(123))  # Output: "One Hundred Twenty-Three"
print(number_to_words(5067))  # Output: "Five Thousand Sixty-Seven"
print(number_to_words(0))     # Output: "Zero"
print(number_to_words(1000000)) # Output: "One Million"
print(number_to_words(1234567890)) # Output: "One Billion Two Hundred Thirty-Four Million Five Hundred Sixty-Seven Thousand Eight Hundred Ninety"
