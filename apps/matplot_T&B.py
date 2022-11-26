import matplotlib.pyplot as plt
from matplotlib import gridspec


''' 
Тут принимем знач. из др. файлов и тд.
Порядок принимаемых значений звена Т
max_T_input, min_T_input, results_T_input = [NEU/CD4, NEU/CD3, NEU/LYMF, NEU/CD8]

'''
# принимаемые данные
max_T_input = [5.00, 3.63, 1.80, 12.30]
max_T_input = [*max_T_input, max_T_input[0]]
min_T_input = [3.00, 2.25, 1.67, 9.47]
min_T_input = [*min_T_input, min_T_input[0]]
results_T_input = [1.85, 1.14, 0.74, 2.87]
results_T_input = [*results_T_input, results_T_input[0]]

# данные ниже используются для отрисовки графиков
max_T = [[max_T_input[0], 0, -max_T_input[2], 0, max_T_input[0]], [0, max_T_input[1], 0, -max_T_input[3], 0]]
min_T = [[min_T_input[0], 0, -min_T_input[2], 0, min_T_input[0]], [0, min_T_input[1], 0, -min_T_input[3], 0]]
results_T = [[results_T_input[0], 0, -results_T_input[2], 0, results_T_input[0]], [0, results_T_input[1], 0,
                                                                                   -results_T_input[3], 0]]

''' 
Тут принимем знач. из др. файлов и тд.
Порядок принимаемых значений звена В
max_B_input, min_B_input, results_B_input = [NEU/CD4, NEU/CD3, NEU/LYMF, CD19/CD8]

'''
# принимаемые данные
max_B_input = [-1.8, 10, 0.31, -0.77, -1.8]
max_B_input = [*max_B_input, max_B_input[0]]
min_B_input = [-1.67, 9.6, 0.16, -0.53]
min_B_input = [*min_B_input, min_B_input[0]]
results_B_input = [-0.7, 5, 0.5, -0.78]
results_B_input = [*results_B_input, results_B_input[0]]

# данные ниже используются для отрисовки графиков
max_B = [[max_B_input[0], 0, max_B_input[2], 0, max_B_input[0]], [0, max_B_input[1], 0, max_B_input[3], 0]]
min_B = [[min_B_input[0], 0, min_B_input[2], 0, min_B_input[0]], [0, min_B_input[1], 0, min_B_input[3], 0]]
results_B = [[results_B_input[0], 0, results_B_input[2], 0, results_B_input[0]], [0, results_B_input[1], 0,
                                                                                  results_B_input[3], 0]]


# figsize разрешение области для отрисовки графиков вместе
fg = plt.figure(figsize=(20, 11.25), constrained_layout=True)
# размер зоны для вывода графиков
gs = gridspec.GridSpec(ncols=2, nrows=1, figure=fg)
plt.suptitle('T- и B- клеточные звенья')

# График Т
fig_ax_1 = fg.add_subplot(gs[0, 0])
# подписываем оси
plt.title("NEU/CD3")
fig_ax_1.text(5.1, -4.86, "NEU/CD4", rotation='vertical')
plt.xlabel("NEU/CD8")
plt.ylabel("NEU/LYMF")

# рисуем график верхних реф. значений звена T
plt.plot(max_T[0], max_T[1], linewidth=2, color='green', label='Верхние референтные значения звена T')
plt.scatter(max_T[0], max_T[1], color='green')  # рисуем точки
for i in range(len(max_T[0])):  # подписываем значения точек
    plt.annotate(max_T_input[i], (max_T[0][i] - 0.17, max_T[1][i] - 0.3))

plt.plot(min_T[0], min_T[1], linewidth=1, color="lightgreen", label='Нижние референтные значения звена T')
plt.scatter(min_T[0], min_T[1], color='lightgreen')
for i in range(len(min_T[0])):
    plt.annotate(min_T_input[i], (min_T[0][i], min_T[1][i] + 0.2))

plt.plot(results_T[0], results_T[1], linewidth=2, color='red', label='Результаты звена T')
plt.scatter(results_T[0], results_T[1], color='red')
for i in range(len(results_T[0])):
    plt.annotate(results_T_input[i], (results_T[0][i], results_T[1][i] - 0.4))

plt.legend()  # отображает легенду

# График В
fig_ax_2 = fg.add_subplot(gs[0, 1])

plt.title("LYMF/CD19")
fig_ax_2.text(0.55, 4.86, "CD19/CD4", rotation='vertical')
plt.xlabel("CD19/CD8")
plt.ylabel("NEU/LYMF")

plt.plot(max_B[0], max_B[1], linewidth=2, color="green", label='Верхние референтные значения звена В')
plt.scatter(max_B[0], max_B[1], color="green")
for i in range(len(max_B[0])):
    plt.annotate(max_B_input[i], (max_B[0][i], max_B[1][i] + 0.08))

plt.plot(min_B[0], min_B[1], linewidth=1, color="lightgreen", label='Нижние референтные значения звена В')
plt.scatter(min_B[0], min_B[1], color="lightgreen")
for i in range(len(min_B[0])):
    plt.annotate(min_B_input[i], (min_B[0][i] + 0.01, min_B[1][i] + 0.05))

plt.plot(results_B[0], results_B[1], linewidth=2, color='red', label='Результаты звена B')
plt.scatter(results_B[0], results_B[1], color="red")
for i in range(len(results_B[0])):
    plt.annotate(results_B_input[i], (results_B[0][i] - 0.05, results_B[1][i] - 0.3))

plt.legend()


#plt.savefig('p.png')
plt.show()
