
import argparse
from learning_pypi.core import sum_numbers

def main():
    parser = argparse.ArgumentParser(description="Sum an array of numbers")
    parser.add_argument('numbers', nargs='+', type=int, help="List of numbers to sum")
    args = parser.parse_args()
    
    result = sum_numbers(args.numbers)
    print(result)
    
if __name__ == "__main__":
    main()