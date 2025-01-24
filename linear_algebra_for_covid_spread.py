import numpy as np
import matplotlib.pyplot as plt 

# Adjacency matrix: Connections between regions (A, B, C)

# Rows = Destination regions (A, B, C)  
# Columns = Source regions (A, B, C)  

A = np.array([
    [0.0, 0.3, 0.1],  # Region A
    [0.2, 0.0, 0.4],  # Region B
    [0.1, 0.2, 0.0],  # Region C
])

# Initial infections: [A, B, C]
v = np.array([1.0, 0.0, 0.0])  # Day 0

# Lists to track infections over days
days = [0]          # Days 0, 1, 2, 3
infections_A = [1.0] # Day 0: A has 1 infection
infections_B = [0.0] # Day 0: B and C have 0
infections_C = [0.0]

# Simulate spread over 3 days (Days 1-3)
for day in range(1, 4):
    A_power = np.linalg.matrix_power(A, day)
    new_infections = v @ A_power
    infections_A.append(new_infections[0])
    infections_B.append(new_infections[1])
    infections_C.append(new_infections[2])
    days.append(day)

# Step 2: Plot the Data
plt.figure(figsize=(10, 6))  # Set graph size

# Plot lines for each region
plt.plot(days, infections_A, marker='o', label='Region A', color='red')
plt.plot(days, infections_B, marker='o', label='Region B', color='blue')
plt.plot(days, infections_C, marker='o', label='Region C', color='green')

# Add labels and title
plt.xlabel("Days", fontsize=12)
plt.ylabel("Infections", fontsize=12)
plt.title("COVID-19 Spread Simulation", fontsize=14)
plt.xticks(days)  # Show all days (0, 1, 2, 3)

# Add grid and legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Save and show the plot
plt.savefig("covid_spread.png")  # Save as an image
plt.show()