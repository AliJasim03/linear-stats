# Linear Stats Project

## Overview
This project calculates the Linear Regression Line and Pearson Correlation Coefficient from a given dataset.

## Prerequisites
- Python 3.7 or higher
- No external libraries required (uses only standard library)

## Installation
1. Clone the repository
2. Ensure you have Python 3.7+ installed

## Usage
### Running the Program
```bash
# Make the script executable
chmod +x src/linear_stats.py

# Run the script with a data file
./src/linear_stats.py data.txt
```

## Output Format
The program outputs two lines:
1. Linear Regression Line: 
   - Format: `y = <slope>x + <intercept>`
   - Slope and intercept are displayed with 6 decimal places
2. Pearson Correlation Coefficient:
   - Displayed with 10 decimal places

### Example Output
```
Linear Regression Line: y = 1.234567x + -2.345678
Pearson Correlation Coefficient: 0.9876543210
```

## Calculations Explained
- **Linear Regression Line**: Represents the best-fit straight line through the data points
  - Calculated using the least squares method
  - Slope (m) represents the line's steepness
  - Intercept (b) represents the y-value where the line crosses the y-axis

- **Pearson Correlation Coefficient**: Measures the strength and direction of linear relationship
  - Ranges from -1 to 1
  - 1: Perfect positive linear correlation
  - 0: No linear correlation
  - -1: Perfect negative linear correlation

## Error Handling
- Checks for file existence
- Validates numeric input
- Provides clear error messages

## Testing
To test the program:
1. Prepare a text file with numeric values (one per line)
2. Run the script with the file as an argument
3. Verify the output matches expected format

## Troubleshooting
- Ensure input file contains only numeric values
- Check file permissions
- Verify Python version compatibility

## License
[Add your license information]

## Contributing
[Add contribution guidelines if applicable]