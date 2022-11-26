import numpy as np
import matplotlib.pyplot as plt

categories = ['NEU/CD4', 'NEU/CD3', 'NEU/LYMF', 'NEU/CD8']
categories = [*categories, categories[0]]

results_T = [1.85, 1.14, 0.74, 2.87]
min_T = [3.00, 2.25, 1.67, 9.47]
max_T = [5.00, 3.63, 1.80, 12.30]

results_T = [*results_T, results_T[0]]
min_T = [*min_T, min_T[0]]
max_T = [*max_T, max_T[0]]

label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(results_T), endpoint=True)

plt.figure(figsize=(8, 8))
plt.subplot(polar=True)
plt.plot(label_loc, results_T, label='results_T', color="red")
plt.plot(label_loc, min_T, label='min_T', color="#74B72E")
plt.plot(label_loc, max_T, label='max_T', color="green")
# plt.fill(max_T, 'r')
# plt.fill_betweenx(restaurant_1, restaurant_2)
plt.title('T-клеточное звено', size=20, y=1.05)
for i in range(len(results_T)):
    plt.annotate(max_T[i], (max_T[i], min_T[i]))

lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
plt.legend()
plt.show()
