def nfa_to_dfa(nfa, start_state, final_states):

    # Initialize DFA components
    dfa = {}  # Dictionary to hold DFA transitions
    queue = [frozenset([start_state])]  # Queue for processing DFA states as sets of NFA states
    processed = set()  # Set to keep track of processed DFA states
    dfa_final_states = set()  # Set to hold DFA final states

    while queue:
        # Get the current DFA state (a set of NFA states)
        current = queue.pop(0)
        
        if current in processed:
            continue  # Skip if this state has already been processed
        
        processed.add(current)  # Mark this state as processed

        # Initialize transitions for this DFA state
        dfa[current] = {}
        
        # Loop through each symbol in the NFA
        for symbol in nfa['symbols']:
            reachable = set()  # Set to hold reachable NFA states

            # Find all reachable NFA states from the current DFA state on this symbol
            for state in current:
                if state in nfa['transitions'] and symbol in nfa['transitions'][state]:
                    reachable.update(nfa['transitions'][state][symbol])  # Add reachable states

            # If there are reachable states, create a new DFA transition
            reachable = frozenset(reachable)  # Convert to frozenset for immutability
            if reachable:
                dfa[current][symbol] = reachable  # Add transition to DFA
                
                if reachable not in processed:
                    queue.append(reachable)  # Add new state to process later

        # Check if this DFA state contains any NFA final state
        if current & set(final_states):
            dfa_final_states.add(current)  # Mark as final state in DFA

    return dfa, dfa_final_states


# Example NFA definition
nfa = {
    'states': {'q0', 'q1', 'q2'},  # Set of NFA states
    'symbols': {'a', 'b'},         # Input symbols for the NFA
    'transitions': {               # Transition function for the NFA
        'q0': {'a': {'q0', 'q1'}, 'b': {'q0'}},  # From q0 on 'a' goes to q0 or q1, on 'b' stays at q0
        'q1': {'b': {'q2'}},                       # From q1 on 'b' goes to q2
        'q2': {}                                  # No transitions from q2
    }
}

start_state = 'q0'  # Starting state of the NFA
final_states = {'q2'}  # Final states of the NFA

# Convert NFA to DFA
dfa, dfa_final_states = nfa_to_dfa(nfa, start_state, final_states)

# Print DFA transitions
print("DFA Transitions:")
for state, transitions in dfa.items():
    state_name = ','.join(state)  # Convert set of states to a readable string format
    print(f"State {state_name}:")
    for symbol, target in transitions.items():
        target_name = ','.join(target)  # Convert target set to a readable string format
        print(f"  On '{symbol}' -> {target_name}")

# Print DFA final states
print("\nDFA Final States:")
for state in dfa_final_states:
    print(','.join(state))  # Print each final state as a string
