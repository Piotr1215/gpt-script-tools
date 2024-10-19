#!/usr/bin/env python3
import csv
import sys
import os

def zsh_stats_to_csv(input_file):
    # Print the CSV header
    print("rank,count,percentage,command")

    try:
        with open(input_file, 'r') as file:
            # Process each line of the input file
            for line in file:
                # Skip empty lines
                if line.strip() == "":
                    continue

                # Split the line and extract relevant parts
                parts = line.strip().split()
                if len(parts) >= 4:
                    rank = parts[0]
                    count = parts[1]
                    percentage = parts[2].rstrip('%')
                    command = ' '.join(parts[3:])

                    # Print as CSV
                    print(f"{rank},{count},{percentage},{command}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.", file=sys.stderr)
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_file}'.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Construct the path to the stats.txt file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    input_file = os.path.join(project_root, 'zsh_data', 'stats.txt')
    
    zsh_stats_to_csv(input_file)
