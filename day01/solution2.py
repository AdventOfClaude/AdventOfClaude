def calculate_location_distance():
    # Read the lists from stdin
    left_list = []
    right_list = []
    
    # Read input until EOF or empty line
    while True:
        try:
            line = input().strip()
            if not line:
                break
            
            # Split the line and convert to integers
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
        except EOFError:
            break
    
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate distances between paired elements
    distances = [abs(left - right) for left, right in zip(left_sorted, right_sorted)]
    
    # Return total distance
    return sum(distances)

# Run the function and print the result
print(calculate_location_distance())
