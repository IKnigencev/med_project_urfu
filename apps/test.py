import numpy as np
#from PyQt5 import uic
import matplotlib.pyplot as plt


params = ['NEU/CD3', 'NEU/LYMF', 'NEU/CD8', 'NEU/CD4']
results = [6.08, 3.60, 9.12, 25.83]
min_T = [1.67, 2.25, 3.00, 9.47]
max_T = [1.80, 3.63, 5.00, 12.30]
min_B = [1.67, 9.60, 0.16, 0.53]
max_B = [1.80, 10.00, 0.31, 0.77]

theta = np.linspace(start=0, stop=2*np.pi, num=len(min_T), endpoint=False)
theta = np.concatenate((theta, [theta[0]]))
min_T = np.append(min_T, min_T[0])
fig = plt.figure(figsize=(5, 5), facecolor='#f3f3f3')
ax = fig.add_subplot(111, projection='polar')
ax.plot(theta, min_T, linewidth=2, color="green")
ax.set_thetagrids(range(0, 360, int(360 / len(params))), (params))
plt.yticks(np.arange(0, 32, 2.0), fontsize=8)
ax.set(facecolor='#f3f3f3')
ax.set_theta_offset(np.pi / 2)

pl = ax.yaxis.get_gridlines()

#for line in pl:
    #line.get_path()._interpolation_steps = 4

plt.show()