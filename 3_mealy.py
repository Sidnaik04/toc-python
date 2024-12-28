# Define the transitions for Mealy Machine
# Format: 'current_state': {'input': ('next_state', 'output')}
transitions = {
    'q0': {'a': ('q0', '1'), 'b': ('q1', '0')},
    'q1': {'a': ('q0', '1'), 'b': ('q1', '0')}
}

def process_string(input_string, transitions, start_state='q0'):

    current_state = start_state
    output = ""
    
    # Process each symbol in input string
    for symbol in input_string:
        # Check if input symbol is valid for current state
        if symbol not in transitions[current_state]:
            print(f"Invalid input: {symbol}")
            return None
            
        # Get next state and output for current transition
        next_state, out = transitions[current_state][symbol]
        
        # Print the transition
        print(f"State {current_state} --({symbol}/{out})--> State {next_state}")
        
        # Update state and add to output
        current_state = next_state
        output += out
        
    return output

# Main loop to process input strings
while True:
    # Get input from user
    user_input = input("\nEnter string (or 'exit' to quit): ")
    
    # Check if user wants to exit
    if user_input.lower() == 'exit':
        break
    
    # Process the string and get output
    print(f"\nProcessing: {user_input}")
    output = process_string(user_input, transitions)
    
    # Print final output if valid
    if output:
        print(f"Final output: {output}")