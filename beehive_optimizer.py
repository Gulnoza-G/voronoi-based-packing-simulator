import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

np.random.seed(42)
num_points = 30
points = np.random.rand(num_points, 2) * 10  

def optimize_packing(points, strength=0.2):
    center = np.mean(points, axis=0)  
    return points + (center - points) * strength 

vor_initial = Voronoi(points)
optimized_points = optimize_packing(points)
vor_optimized = Voronoi(optimized_points)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

voronoi_plot_2d(vor_initial, ax=ax1, show_vertices=False, line_colors='black')
ax1.scatter(points[:,0], points[:,1], c='gold', s=50, edgecolor='black')
ax1.set_title("🐝 Initial Random Beehive")
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

voronoi_plot_2d(vor_optimized, ax=ax2, show_vertices=False, line_colors='black')
ax2.scatter(optimized_points[:,0], optimized_points[:,1], c='gold', s=50, edgecolor='black')
ax2.set_title("🍯 Optimized Beehive (After Evolution)")
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

plt.savefig('beehive_results.png')  
plt.show()