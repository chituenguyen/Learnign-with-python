import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.title("Sports Watch Data")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xpoints, ypoints)
plt.show()

### Draw without line
plt.plot(xpoints, ypoints,'o')
plt.show()
### Marker

plt.plot(xpoints, ypoints, marker='o')
plt.show()

#### Short cut marker:line:color
plt.plot(ypoints, '*:r')
plt.show()