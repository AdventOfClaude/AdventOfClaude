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

def count_safe_reports(input_data):
    """
    Count the number of safe reports in the input data.
    
    Args:
        input_data (str): Multi-line string containing reports
        
    Returns:
        int: Number of safe reports
    """
    # Split input into lines and convert each line to list of integers
    reports = [list(map(int, line.strip().split())) for line in input_data.splitlines() if line.strip()]
    
    # Count safe reports
    return sum(1 for report in reports if is_safe_report(report))

# Test with the example data
example_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

result = count_safe_reports(example_data)
print(f"Number of safe reports: {result}")  # Should output 2

# Verify individual reports
test_reports = [
    [7, 6, 4, 2, 1],  # Should be True
    [1, 2, 7, 8, 9],  # Should be False
    [9, 7, 6, 2, 1],  # Should be False
    [1, 3, 2, 4, 5],  # Should be False
    [8, 6, 4, 4, 1],  # Should be False
    [1, 3, 6, 7, 9],  # Should be True
]

# Test each report individually
for i, report in enumerate(test_reports):
    print(f"Report {i+1}: {report} is {'safe' if is_safe_report(report) else 'unsafe'}")
