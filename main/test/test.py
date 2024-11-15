import matplotlib.pyplot as plt
import numpy as np

# Generate random data for the example
np.random.seed(42)
x = np.random.normal(50, 10, 100)  # X values (e.g., hours studied)
y = x * 1.5 + np.random.normal(0, 10, 100)  # Y values (e.g., test scores)

# Create the scatter plot
plt.scatter(x, y, color='blue', alpha=0.7, edgecolor='black')

# Add labels and title
plt.title("Scatter Plot of Hours Studied vs. Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Test Scores")

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Show the plot
plt.show()
