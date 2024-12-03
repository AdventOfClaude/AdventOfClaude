def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        # Multiply each left number by its count in the right list
        similarity_score += num * right_counts.get(num, 0)
    
    return similarity_score

def read_location_ids():
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
    
    return left_list, right_list

# Read lists and calculate similarity score
left_list, right_list = read_location_ids()
print(calculate_similarity_score(left_list, right_list))
