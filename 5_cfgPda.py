#cfg to pda
# Function to get a list of items from the user
def get_input_list(prompt, count):
    items = []
    print(f"\n{prompt}")
    for i in range(count):
        item = input(f"Enter item {i+1}: ")
        items.append(item)
    return items

# Function to get production rules
def get_productions(symbols):
    productions = {}
    print("\nEnter productions (e.g., A->aB):")
    for symbol in symbols:
        productions[symbol] = input(f"Production for {symbol}: ")
    return productions

# Input: Non-terminals (uppercase letters)
num_non_terminals = int(input("Enter number of non-terminals: "))
non_terminals = get_input_list("Enter non-terminals (e.g., A, B, C):", num_non_terminals)

# Input: Terminals (lowercase letters)
num_terminals = int(input("Enter number of terminals: "))
terminals = get_input_list("Enter terminals (e.g., a, b, c):", num_terminals)

# Input: Production symbols (left-hand side of productions)
num_productions = int(input("Enter number of production symbols: "))
prod_symbols = get_input_list("Enter production symbols:", num_productions)

# Input: Production rules (right-hand side of productions)
productions = get_productions(prod_symbols)

# Output: Transitions for CFG to PDA
print("\nTransitions for CFG to PDA:")
# Initial transition: Starting production added to the stack
print(f"δ(q0,ε,Z0) = (q1,{prod_symbols[0]}Z0)")

# Transitions for replacing non-terminals based on production rules
for symbol in prod_symbols:
    print(f"δ(q1,ε,{symbol}) = (q1,{productions[symbol]})")

# Transitions for matching terminals (consume terminal from input and stack)
for terminal in terminals:
    print(f"δ(q1,{terminal},{terminal}) = (q1,ε)")

# Final transition: Reach the accepting state
print("δ(q1,ε,Z0) = (q2,Z0)")
