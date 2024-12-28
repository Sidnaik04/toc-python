# Example: DFA that accepts strings ending with '01'

# Function to check if the input string is accepted by the DFA
def check_string(transition_table, accepting_states, start_state, input_string):
    current_state = start_state  # Start from the initial state
    
    # Process each character in the input string
    for char in input_string:
        # If the character is not in the transition table for the current state, reject the string
        if char not in transition_table[current_state]:
            return False
        # Move to the next state based on the transition table
        current_state = transition_table[current_state][char]
        
    # After processing all characters, check if the current state is an accepting state
    return current_state in accepting_states

# Define the transition table for the DFA
transition = {
    'q0': {'0':'q1','1':'q0'},
    'q1': {'0':'q1','1':'q2'},
    'q2': {'0':'q1','1':'q0'}
}

# Define the set of accepting states
accepting_states = {'q2'}
# Define the start state
start_state = 'q0'

# List of test strings to check
test_string = ['01','1001','1000101','100','111']

# Check each test string and print whether it is accepted or rejected
for string in test_string:
    result = check_string(transition, accepting_states, start_state, string)
    print(f"String '{string}': {'Accepted' if result else 'Rejected'}")
    
    
    


# DFA that accepts strings ending with '10'
# transition = {
#     'q0': {'0':'q0','1':'q1'},
#     'q1': {'0':'q2','1':'q1'},
#     'q2': {'0':'q2','1':'q1'}
# }