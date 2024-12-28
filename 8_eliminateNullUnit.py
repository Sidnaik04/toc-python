def eliminate_null_and_unit_productions(grammar):
    
    # Step 1: Eliminate null (ε) productions
    nullable = set()  # To store nullable non-terminals

    # Identify nullable non-terminals
    for nt, productions in grammar.items():
        if "^" in productions:  # Check if ε is a production
            nullable.add(nt)
            productions.remove("^")  # Remove ε production

    # Update productions to account for nullable non-terminals
    for nt, productions in grammar.items():
        new_productions = set(productions)  # Create a set to avoid duplicates
        for production in productions:
            for nullable_nt in nullable:
                if nullable_nt in production:
                    # Generate new productions by removing the nullable non-terminal
                    new_production = production.replace(nullable_nt, "")
                    new_productions.add(new_production)  # Add the new production
        # Update the grammar with the new productions, excluding empty strings
        grammar[nt] = [p for p in new_productions if p != ""]

    # Step 2: Eliminate unit productions (A → B where B is a non-terminal)
    for nt in list(grammar.keys()):
        unit_productions = [p for p in grammar[nt] if p in grammar]  # Find unit productions
        while unit_productions:
            unit = unit_productions.pop()  # Get a unit production
            grammar[nt].remove(unit)  # Remove the unit production
            
            # Add all productions of the unit non-terminal to the current non-terminal
            for prod in grammar[unit]:
                if prod not in grammar[nt]:  # Avoid duplicates
                    grammar[nt].append(prod)
                    if prod in grammar:  # If prod is also a non-terminal, check for further units
                        unit_productions.append(prod)

    return grammar

# Example Grammar
grammar = {
    "S": ["AB", "ε"],
    "A": ["a", "B"],
    "B": ["b", "A"]
}

# Eliminate null and unit productions
result = eliminate_null_and_unit_productions(grammar)

# Print updated grammar
print("Updated Grammar:")
for nt, productions in result.items():
    print(f"{nt} -> {', '.join(productions)}")

