def reverse_string(input_string):
    # Create tape as a list of characters with a blank symbol at the end
    tape = list(input_string) + ['_']
    head = 0  # Start at leftmost position
    
    # Step 1: Move to end of string
    while tape[head] != '_':
        head += 1
    head -= 1  # Move back to last character
    
    # Step 2: Read characters from right to left
    reversed_chars = []
    while head >= 0:
        reversed_chars.append(tape[head])
        head -= 1
        
    # Return the reversed string
    return ''.join(reversed_chars)

# Test the program
test_string = "hello"
result = reverse_string(test_string)
print(f"Original string: {test_string}")
print(f"Reversed string: {result}")
