import matplotlib.pyplot as plt
import numpy as np
theta = np.linspace(0, 4 * np.pi, 200)
r = theta
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.plot(x, y, '*')
plt.title("Spiral Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()