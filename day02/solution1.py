def is_safe_report(levels):
    """
    Check if a report's levels are safe according to the rules:
    1. All levels must be either increasing or decreasing
    2. Adjacent levels must differ by at least 1 and at most 3
    
    Args:
        levels (list): List of integers representing the levels
        
    Returns:
        bool: True if the report is safe, False otherwise
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

def process_input_file(filepath):
    """
    Read and process the input file containing reports.
    
    Args:
        filepath (str): Path to the input file
        
    Returns:
        int: Number of safe reports
    """
    try:
        with open(filepath, 'r') as file:
            # Read lines and convert each line to list of integers
            reports = [list(map(int, line.strip().split())) 
                      for line in file 
                      if line.strip()]
            
        # Count and return safe reports
        safe_count = sum(1 for report in reports if is_safe_report(report))
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
        print(f"Number of safe reports: {safe_count}")
        print(f"Percentage safe: {(safe_count/total_count)*100:.1f}%")

if __name__ == "__main__":
    import sys
    
    # Check if filepath was provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
        sys.exit(1)
    
    input_filepath = sys.argv[1]
    main(input_filepath)
