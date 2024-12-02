def is_safe_report(levels):
    """
    Check if a report's levels are safe according to the original rules.
    """
    if len(levels) < 2:
        return True
    
    # Get the differences between adjacent levels
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    # Check if all differences are within the valid range (-3 to -1 or 1 to 3)
    for diff in differences:
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    
    # Check if direction changes (mixing increasing and decreasing)
    if any(diff > 0 for diff in differences) and any(diff < 0 for diff in differences):
        return False
    
    return True

def is_safe_with_dampener(levels):
    """
    Check if a report is safe, considering the Problem Dampener's ability
    to remove one level.
    
    Args:
        levels (list): List of integers representing the levels
        
    Returns:
        bool: True if the report is safe (either naturally or with one level removed)
    """
    # First check if it's safe without removing any level
    if is_safe_report(levels):
        return True
    
    # If not safe, try removing each level one at a time
    for i in range(len(levels)):
        # Create new list without the current level
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe_report(dampened_levels):
            return True
    
    return False

def process_input_file(filepath):
    """
    Read and process the input file containing reports.
    
    Args:
        filepath (str): Path to the input file
        
    Returns:
        tuple: (Number of safe reports, Total number of reports)
    """
    try:
        with open(filepath, 'r') as file:
            # Read lines and convert each line to list of integers
            reports = [list(map(int, line.strip().split())) 
                      for line in file 
                      if line.strip()]
            
        # Count reports that are safe with the Problem Dampener
        safe_count = sum(1 for report in reports if is_safe_with_dampener(report))
        return safe_count, len(reports)
    
    except FileNotFoundError:
        print(f"Error: Could not find file {filepath}")
        return None
    except ValueError:
        print(f"Error: File contains invalid data. All values must be integers.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main(input_filepath):
    """
    Main function to process reactor safety reports.
    
    Args:
        input_filepath (str): Path to the input file
    """
    result = process_input_file(input_filepath)
    
    if result:
        safe_count, total_count = result
        print(f"Processed {total_count} reports.")
        print(f"Number of safe reports (with Problem Dampener): {safe_count}")
        print(f"Percentage safe: {(safe_count/total_count)*100:.1f}%")

if __name__ == "__main__":
    import sys
    
    # Verify example data
    example_data = [
        [7, 6, 4, 2, 1],  # Safe without dampener
        [1, 2, 7, 8, 9],  # Unsafe even with dampener
        [9, 7, 6, 2, 1],  # Unsafe even with dampener
        [1, 3, 2, 4, 5],  # Safe with dampener (remove 3)
        [8, 6, 4, 4, 1],  # Safe with dampener (remove second 4)
        [1, 3, 6, 7, 9],  # Safe without dampener
    ]
    
    print("Testing example data:")
    safe_count = sum(1 for report in example_data if is_safe_with_dampener(report))
    print(f"Safe reports in example: {safe_count}")  # Should output 4
    
    # Check if filepath was provided as command line argument
    if len(sys.argv) != 2:
        print("\nUsage: python script.py <input_file_path>")
        sys.exit(1)
    
    print("\nProcessing input file:")
    input_filepath = sys.argv[1]
    main(input_filepath)
