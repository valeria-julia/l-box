"""
L-Box Logic: A Binary-Ternary Hybrid Collatz Engine
Created by: The Signal Architect & AI Assistant
License: MIT
"""

def to_ternary(n):
    """Converts a decimal integer to its base-3 (ternary) string representation."""
    if n == 0: return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //= 3
    return "".join(reversed(digits))

def l_box_packing(binary_str, mode='A'):
    """
    Applies the L-Box Local Bit-Reduction.
    Processes the binary string in pairs to simulate hardware-level 
    signal collapse (Half-Adder logic).
    """
    new_bits = ""
    # Process the string in pairs (2nd bit is XOR sum, 1st bit is AND carry)
    for i in range(0, len(binary_str) - 1, 2):
        pair = binary_str[i:i+2]
        if pair == "11": 
            new_bits += "10"  # Carry generated
        elif pair == "01" and mode == "AI_PARADOX":
            new_bits += "10"  # AI Paradox: Artificial energy push to the left
        else:
            new_bits += "1"   # Simplified signal reduction
            
    # Handle the remaining single bit (The Remainder Rule)
    if len(binary_str) % 2 != 0:
        if mode == 'B':
            new_bits += "10"  # Mode B: Force parity (Zero generator)
        else:
            new_bits += binary_str[-1] # Mode A: Keep as is
            
    return new_bits

def ultimate_hybrid_collatz(x, max_steps=1000):
    """
    The core execution engine. Switches between Binary Truncation, 
    L-Box Packing, and Ternary String Appending.
    """
    history = set()
    steps = 0
    print(f"--- STARTING L-BOX ENGINE WITH: {x} ---")
    
    while x > 1 and steps < max_steps:
        binary = bin(x)[2:]
        
        # PHASE 1: BINARY TRUNCATION (Zero Exhaust)
        if binary.endswith('0'):
            # Rapidly remove all trailing zeros (Division by 2^k)
            x = int(binary.rstrip('0'), 2)
            print(f"Step {steps+1}: [TRUNCATION] -> {x}")
        
        else:
            # PHASE 2: STRATEGY SELECTION
            # If the number is repeating, switch to Mode B to break the loop
            current_mode = 'B' if x in history else 'A'
            
            # PHASE 3: L-BOX PACKING (Bit-level compression)
            packed_bin = l_box_packing(binary, mode=current_mode)
            x = int(packed_bin, 2)
            print(f"Step {steps+1}: [L-BOX {current_mode}] -> {x}")
            
            history.add(x)
            
            # PHASE 4: TERNARY APPEND (The Growth Pump)
            # Only if still odd and greater than 1
            if x > 1 and x % 2 != 0:
                ternary_str = to_ternary(x)
                ternary_str += "1"  # Symbolic shift-append
                x = int(ternary_str, 3)
                print(f"           [TERNARY +1] -> {x}")
        
        steps += 1
        
    if x == 1:
        print(f"--- SUCCESS: Stabilized to 1 in {steps} steps ---")
    else:
        print(f"--- HALTED: Limit reached or system diverging ---")

# EXAMPLE RUN:
# You can test with large numbers like 3**40 or 10031980
if __name__ == "__main__":
    test_val = 10031980
    ultimate_hybrid_collatz(test_val)
