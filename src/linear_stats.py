#!/usr/bin/env python3
import sys
import math


def read_data(filename):
    """Read data from the input file."""
    try:
        with open(filename, 'r') as file:
            # Convert lines to floats, stripping whitespace
            return [float(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid data in the file. Ensure all lines contain numeric values.")
        sys.exit(1)


def calculate_statistics(y_values):
    """
    Calculate linear regression line and Pearson correlation coefficient.

    Args:
        y_values (list): List of y-values

    Returns:
        tuple: (slope, intercept, pearson_correlation)
    """
    # Generate x-values (line numbers starting from 0)
    x_values = list(range(len(y_values)))

    # Calculate means
    x_mean = sum(x_values) / len(x_values)
    y_mean = sum(y_values) / len(y_values)

    # Calculate necessary sums for regression and correlation
    sum_xy = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
    sum_x_squared = sum((x - x_mean) ** 2 for x in x_values)
    sum_y_squared = sum((y - y_mean) ** 2 for y in y_values)

    # Calculate slope (m) and intercept (b)
    slope = sum_xy / sum_x_squared
    intercept = y_mean - slope * x_mean

    # Calculate Pearson correlation coefficient
    pearson_r = sum_xy / math.sqrt(sum_x_squared * sum_y_squared)

    return slope, intercept, pearson_r


def main():
    # Check if filename is provided
    if len(sys.argv) < 2:
        print("Usage: python linear_stats.py <data_file>")
        sys.exit(1)

    # Read data from file
    data = read_data(sys.argv[1])

    # Calculate statistics
    slope, intercept, pearson_r = calculate_statistics(data)

    # Print results with specified decimal precision
    print(f"Linear Regression Line: y = {slope:.6f}x + {intercept:.6f}")
    print(f"Pearson Correlation Coefficient: {pearson_r:.10f}")


if __name__ == "__main__":
    main()