import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the plot
plt.plot(x, y, marker="o")

# Add titles and labels
plt.title("My First Matplotlib Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Add a grid
plt.grid(True)

# Display the graph
plt.show()