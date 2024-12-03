import re
import sys

def parse_multiplications(filename):
    """
    Parse a file containing corrupted multiplication instructions and calculate the sum
    of all valid and enabled multiplications.
    
    Args:
        filename (str): Path to the input file
        
    Returns:
        tuple: (sum of multiplications, list of individual results, list of disabled results)
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return 0, [], []
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0, [], []

    # Find all control instructions and multiplications with their positions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Find all instances with their positions
    muls = [(m.start(), int(m.group(1)), int(m.group(2))) 
            for m in re.finditer(mul_pattern, content)]
    dos = [m.start() for m in re.finditer(do_pattern, content)]
    donts = [m.start() for m in re.finditer(dont_pattern, content)]
    
    # Combine all control instructions and sort by position
    controls = [(pos, True) for pos in dos] + [(pos, False) for pos in donts]
    controls.sort()
    
    # Start enabled
    currently_enabled = True
    if controls:
        # Find the most recent control instruction before each multiplication
        for i in range(len(controls)-1, -1, -1):
            if controls[i][1] != currently_enabled:
                currently_enabled = controls[i][1]
                break
    
    enabled_results = []
    disabled_results = []
    
    for pos, x, y in muls:
        # Find the last control instruction before this multiplication
        current_state = currently_enabled
        for control_pos, enabled in controls:
            if control_pos > pos:
                break
            current_state = enabled
        
        result = x * y
        if current_state:
            enabled_results.append(result)
        else:
            disabled_results.append(result)
    
    return sum(enabled_results), enabled_results, disabled_results

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        return

    total, enabled_muls, disabled_muls = parse_multiplications(sys.argv[1])
    
    print(f"Enabled multiplications: {enabled_muls}")
    print(f"Disabled multiplications: {disabled_muls}")
    print(f"Sum of enabled multiplications: {total}")

if __name__ == "__main__":
    main()
