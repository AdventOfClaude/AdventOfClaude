import sys
from typing import List, Set, Tuple

def read_puzzle(filename: str) -> List[str]:
    """Read the puzzle from a file and return it as a list of strings."""
    with open(filename) as f:
        return [line.strip() for line in f]

def find_xmas(puzzle: List[str]) -> Set[Tuple[int, int, int, int]]:
    """Find all instances of 'XMAS' in the puzzle in all directions."""
    height = len(puzzle)
    width = len(puzzle[0])
    target = "XMAS"
    found = set()
    
    # All possible directions: right, down-right, down, down-left, left, up-left, up, up-right
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    def is_valid(x: int, y: int) -> bool:
        """Check if coordinates are within puzzle bounds."""
        return 0 <= x < height and 0 <= y < width
    
    def check_direction(start_x: int, start_y: int, dx: int, dy: int) -> bool:
        """Check if 'XMAS' exists starting from (start_x, start_y) in direction (dx, dy)."""
        word = ""
        x, y = start_x, start_y
        
        for _ in range(4):  # XMAS is 4 letters
            if not is_valid(x, y):
                return False
            word += puzzle[x][y]
            x += dx
            y += dy
            
        return word == target
    
    # Check every starting position and direction
    for i in range(height):
        for j in range(width):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    # Store coordinates of all four letters
                    coords = tuple((i + dx*k, j + dy*k) for k in range(4))
                    found.add(coords)
    
    return found

def create_visualization(puzzle: List[str], found: Set[Tuple[int, int, int, int]]) -> List[str]:
    """Create a visualization where only letters part of XMAS instances are shown."""
    height = len(puzzle)
    width = len(puzzle[0])
    
    # Create a grid of dots
    result = [['.' for _ in range(width)] for _ in range(height)]
    
    # Fill in the letters that are part of XMAS instances
    for coords in found:
        for x, y in coords:
            result[x][y] = puzzle[x][y]
    
    # Convert to strings
    return [''.join(row) for row in result]

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <puzzle_file>")
        sys.exit(1)
        
    # Read puzzle
    puzzle = read_puzzle(sys.argv[1])
    
    # Find all XMAS instances
    found = find_xmas(puzzle)
    
    # Print results
    print(f"Found {len(found)} instances of XMAS")
    
    # Create and print visualization
    visualization = create_visualization(puzzle, found)
    print("\nVisualization (only showing letters part of XMAS):")
    for row in visualization:
        print(row)

if __name__ == "__main__":
    main()