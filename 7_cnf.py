# Function to convert CFG to CNF
def cfg_to_cnf(cfg):
    cnf = {}  # Dictionary to store the CNF rules
    counter = 1  # Counter for generating new non-terminal symbols

    # Function to generate a new non-terminal symbol
    def new_nonterminal():
        nonlocal counter
        nt = f"X{counter}"  # Format: X1, X2, X3, ...
        counter += 1
        return nt

    # Step 1: Convert CFG to CNF
    for nt, productions in cfg.items():
        cnf[nt] = []  # Initialize CNF productions for each non-terminal
        for prod in productions:
            if len(prod) > 2:  # Break long productions into smaller parts
                while len(prod) > 2:
                    new_nt = new_nonterminal()  # Create a new non-terminal
                    cnf[new_nt] = [prod[:2]]  # Add the first two symbols
                    prod = new_nt + prod[2:]  # Replace with the new non-terminal
                cnf[nt].append(prod)
            elif len(prod) == 1 or (len(prod) == 2 and prod.isupper()):  
                # If already in CNF form
                cnf[nt].append(prod)
            else:  # Replace terminals in mixed productions
                new_prod = []
                for char in prod:
                    if char.islower():  # Terminal symbol
                        new_nt = new_nonterminal()  # Create a new non-terminal
                        cnf[new_nt] = [char]  # Map terminal to non-terminal
                        new_prod.append(new_nt)
                    else:
                        new_prod.append(char)
                cnf[nt].append(''.join(new_prod))

    return cnf

# Example CFG
cfg = {
    'S': ['AB', 'aB', 'Aa'],
    'A': ['a', 'aS'],
    'B': ['b', 'Sb']
}

# Convert CFG to CNF
cnf = cfg_to_cnf(cfg)

# Print CNF
print("Chomsky Normal Form (CNF):")
for nt, productions in cnf.items():
    print(f"{nt} -> {', '.join(productions)}")