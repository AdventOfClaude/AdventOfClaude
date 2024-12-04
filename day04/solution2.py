import sys
from typing import List, Set, Tuple

def read_puzzle(filename: str) -> List[str]:
    """Read the puzzle from a file and return it as a list of strings."""
    with open(filename) as f:
        return [line.strip() for line in f]

def check_mas(grid: List[str], x: int, y: int, dx: int, dy: int) -> bool:
    """Check if 'MAS' exists starting from (x,y) in direction (dx,dy)."""
    if not (0 <= x + 2*dx < len(grid) and 0 <= y + 2*dy < len(grid[0])):
        return False
    
    word = ""
    for i in range(3):  # MAS is 3 letters
        word += grid[x + i*dx][y + i*dy]
    
    return word in ["MAS", "SAM"]

def find_x_mas_patterns(puzzle: List[str]) -> Set[Tuple[Tuple[int, int, str], Tuple[int, int, str]]]:
    """Find all X-MAS patterns where each diagonal contains MAS (forwards or backwards)."""
    height = len(puzzle)
    width = len(puzzle[0])
    patterns = set()
    
    # For each potential center point of the X
    for i in range(1, height-1):  # Center needs space above and below
        for j in range(1, width-1):  # Center needs space left and right
            # Check all possible combinations of MAS in the diagonals
            # Top-left to bottom-right diagonal
            tlbr_coords = [(i-1, j-1), (i, j), (i+1, j+1)]
            # Top-right to bottom-left diagonal
            trbl_coords = [(i-1, j+1), (i, j), (i+1, j-1)]
            
            # Check if both diagonals form valid MAS patterns (forward or backward)
            tlbr_valid = check_mas(puzzle, i-1, j-1, 1, 1) or check_mas(puzzle, i+1, j+1, -1, -1)
            trbl_valid = check_mas(puzzle, i-1, j+1, 1, -1) or check_mas(puzzle, i+1, j-1, -1, 1)
            
            if tlbr_valid and trbl_valid:
                # Store the pattern with both diagonals
                pattern = (
                    tuple((x, y) for x, y in tlbr_coords),
                    tuple((x, y) for x, y in trbl_coords)
                )
                patterns.add(pattern)
    
    return patterns

def create_visualization(puzzle: List[str], patterns: Set[Tuple[Tuple[int, int, str], Tuple[int, int, str]]]) -> List[str]:
    """Create a visualization where only letters part of X-MAS patterns are shown."""
    height = len(puzzle)
    width = len(puzzle[0])
    
    # Create a grid of dots
    result = [['.' for _ in range(width)] for _ in range(height)]
    
    # Fill in the letters that are part of X-MAS patterns
    for diagonal1, diagonal2 in patterns:
        for x, y in diagonal1:
            result[x][y] = puzzle[x][y]
        for x, y in diagonal2:
            result[x][y] = puzzle[x][y]
    
    # Convert to strings
    return [''.join(row) for row in result]

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <puzzle_file>")
        sys.exit(1)
        
    # Read puzzle
    puzzle = read_puzzle(sys.argv[1])
    
    # Find all X-MAS patterns
    patterns = find_x_mas_patterns(puzzle)
    
    # Print results
    print(f"Found {len(patterns)} X-MAS patterns")
    
    # Create and print visualization
    visualization = create_visualization(puzzle, patterns)
    print("\nVisualization (only showing letters part of X-MAS patterns):")
    for row in visualization:
        print(row)

if __name__ == "__main__":
    main()