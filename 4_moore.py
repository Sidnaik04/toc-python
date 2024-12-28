# Moore machine

# transitions: what state to go to on each input
# state_outputs: what output to produce in each state
transitions = {
    'q0': {'a': 'q0', 'b': 'q1'},  # From q0: 'a' keeps in q0, 'b' goes to q1
    'q1': {'a': 'q0', 'b': 'q1'}   # From q1: 'a' goes to q0, 'b' keeps in q1
}

# Define output for each state
state_outputs = {
    'q0': '1',  # State q0 produces output '1'
    'q1': '0'   # State q1 produces output '0'
}

def process_string(input_string, transitions, state_outputs, start_state = 'q0'):
    
    current_state = start_state
    output = state_outputs[current_state] # Initial state output
    
    print(f"\nStarting in state: {current_state} ")
    
    # Process each input symbol
    for symbol in input_string:
        # Check if input symbol is valid
        if symbol not in transitions[current_state]:
            print(f"Invalid input:{symbol}")
            return None
        
        # Get next state
        next_state = transitions[current_state][symbol]
        
        # Print transition
        print(f"State {current_state} --({symbol})--> State {next_state} (output: {state_outputs[next_state]})")

        # Update state and add its output
        current_state = next_state
        output += state_outputs[current_state]
        
    return output

# Main loop to process input strings
while True:
    # Get input from user
    user_input =  input("\nEnter string (or 'exit' to quit): ")
    
    # Check for exit
    if user_input.lower() == 'exit':
        break
    
    # Process string and get output
    print(f"\nProcessing: {user_input}")
    output = process_string(user_input,transitions,state_outputs)
    
    # Print final output if valid
    if output:
        print(f"Final output sequence: {output}")    