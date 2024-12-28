# Define Turing Machine components
transitions = [
    [1, 5, 4, 5, 3],  # State 0 transitions
    [1, 2, 5, 5, 1],  # State 1 transitions
    [2, 5, 5, 0, 2],  # State 2 transitions
    [5, 5, 4, 5, 3],  # State 3 transitions
    [4, 4, 4, 4, 4],  # State 4 transitions (accepting state)
    [5, 5, 5, 5, 5]   # State 5 transitions (rejecting state)
]

# Symbols that can appear on tape
symbols = ["0", "1", " ", "x", "y"]

# Head movement for each transition (0 = left, 1 = right)
pointer = [
    [1, 1, 0, 1, 1],  # State 0 movements
    [1, 0, 1, 1, 1],  # State 1 movements
    [0, 1, 1, 1, 0],  # State 2 movements
    [1, 1, 0, 1, 1],  # State 3 movements
    [1, 1, 1, 1, 1],  # State 4 movements
    [1, 1, 1, 1, 1]   # State 5 movements
]

# Symbol to write for each transition
replace = [
    [3, 3, 3, 3, 4],  # State 0 replacements
    [0, 4, 3, 3, 4],  # State 1 replacements
    [0, 3, 3, 3, 4],  # State 2 replacements
    [0, 1, 2, 3, 4],  # State 3 replacements
    [0, 1, 2, 3, 4],  # State 4 replacements
    [0, 1, 2, 3, 4]   # State 5 replacements
]

def run_turing_machine(input_string):
    # Initialize machine
    state = 0
    tape = list(input_string + " ")  # Add blank space at end
    head = 0
    
    print("\nStarting Turing Machine...")
    print(f"Initial tape: {tape}")
    
    # Run until reaching accept (4) or reject (5) state
    while state < 4:
        current_state = state
        
        # Get current symbol's index from symbols list
        current_symbol = symbols.index(tape[head])
        
        # Process current state and symbol
        # 1. Write new symbol
        tape[head] = symbols[replace[current_state][current_symbol]]
        
        # 2. Change state
        state = transitions[current_state][current_symbol]
        
        # 3. Move head (0 = left, 1 = right)
        if pointer[current_state][current_symbol] == 0:
            head -= 1
        else:
            head += 1
        
        # Print current configuration
        print(f"\nTape: {tape}")
        print(f"State: {state}, Head position: {head}")
        
        # Check if accepted
        if state == 4:
            print("\nString ACCEPTED!")
        else:
            print("\nString not accepted yet...")

# Run the machine
input_string = input("Enter input string: ")
run_turing_machine(input_string)