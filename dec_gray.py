def decimal_to_gray(n):
    """
    Converts a decimal number to Gray code.
    
    Parameters:
    n (int): decimal number to convert.
    
    Returns:
    int: Number in Gray code.
    """
    return n ^ (n >> 1)

# Example
decimal_number = 7
gray_code = decimal_to_gray(decimal_number)
print(f"Decimal: {decimal_number} -> Gray Code: {bin(gray_code)[2:].zfill(4)}")

