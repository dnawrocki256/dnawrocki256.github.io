import matplotlib.pyplot as plt

# Original data
sizes = [56.6, 18.3, 5.5, 9.8, 0.6, 4.9, 5.6]
colors = ['#5AFFFD', '#E50038', '#00B0EF', '#F2B119', '#00AB5B', '#FEF687', '#808080']

# Add invisible padding to fill the bottom half
# Sum of sizes
total = sum(sizes)
# Padding = total (so the invisible wedge takes the bottom 180°)
sizes_with_padding = sizes + [total]
colors_with_padding = colors + ['white']  # invisible wedge

# Create donut
plt.pie(
    sizes_with_padding,
    colors=colors_with_padding,
    startangle=180,  # start from left
    counterclock=False,
    wedgeprops={'width': 0.7, 'edgecolor': 'white'}
)

plt.gca().set_aspect('equal')
plt.show()
