import re
import sys

def parse_multiplications(filename):
    """
    Parse a file containing corrupted multiplication instructions and calculate the sum
    of all valid multiplications.
    
    Args:
        filename (str): Path to the input file
        
    Returns:
        tuple: (sum of multiplications, list of individual results)
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return 0, []
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0, []

    # Regular expression to match valid mul(X,Y) instructions
    # Where X and Y are 1-3 digit numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all valid matches
    matches = re.finditer(pattern, content)
    
    results = []
    for match in matches:
        x, y = int(match.group(1)), int(match.group(2))
        results.append(x * y)
    
    return sum(results), results

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        return

    total, multiplications = parse_multiplications(sys.argv[1])
    
    print(f"Individual multiplications: {multiplications}")
    print(f"Sum of all multiplications: {total}")

if __name__ == "__main__":
    main()
