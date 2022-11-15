import plotly.graph_objects as go


# params =
results_B = [0.74, 5.00, 0.50, 0.78, 0.74]
categories_B = ["CD19/CD4", "LYMF/CD19", "NEU/LYMF", "CD19/CD8", "CD19/CD4"]
#categories = [*categories, categories[0]]
results_T = [1.85, 1.14, 0.74, 2.87, 1.85]
min_T = [3.00, 2.25, 1.67, 9.47, 3.00]
max_T = [5.00, 3.63,1.80, 12.30, 5.00]
min_B = [1.67, 9.60, 0.16, 0.53]
max_B = [1.80, 10.00, 0.31, 0.77]
d = max(max_T)
s = max(results_T)
if d > s:
    f = d
else:
    f = s
categories_T = ['NEU/CD4', 'NEU/CD3', 'NEU/LYMF', 'NEU/CD8', 'NEU/CD4']

fig_T = go.Figure()
# min_T
fig_T.add_trace(go.Scatterpolar(
      r=min_T,
      theta=categories_T,
      fill='none',
      name='min_T'
))
# max_T
fig_T.add_trace(go.Scatterpolar(
      r=max_T,
      theta=categories_T,
      fill='tonext',
      name='max_T'
))
# results_T
fig_T.add_trace(go.Scatterpolar(
      r=results_T,
      theta=categories_T,
      fill='none',
      name='results_T'
))


fig_T.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, f+2]
    )),
  showlegend=False
)

fig_T.show()


# from math import pi
# import matplotlib.pyplot as plt
#
# # Вносим данные - какие скиллы хотим видеть в веб-разработчике
# params = ['NEU/CD3', 'NEU/LYMF', 'NEU/CD8', 'NEU/CD4']
# min_T = [1.67, 2.25, 3.00, 9.47]
#
# results = [6.08, 3.60, 9.12, 25.83]
#
# max_T = [1.80, 3.63, 5.00, 12.30]
# min_B = [1.67, 9.60, 0.16, 0.53]
# max_B = [1.80, 10.00, 0.31, 0.77]
#
#
# N = len(params)
#
# x_as = [n / float(N) * 2 * pi for n in range(N)]
#
# # Связываем последнее значение с первым чтобы построить радиальный график
# min_T += min_T[:1]
# x_as += x_as[:1]
#
# # Устанавливаем цвет и толщину линий
# plt.rc('axes', linewidth=0.5, edgecolor="#888888")
#
# # Создаем диаграмму
# ax = plt.subplot(111, polar=True)
#
# # Устанавливаем стили для сетки
# ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
# ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
# ax.set_theta_offset(pi / 2)
# ax.set_theta_direction(-1)
# ax.set_rlabel_position(0)
#
# # Убираем стандартные метки
# plt.xticks(x_as[:-1], [])
#
# # Выводим шаг значения на графAик
# plt.yticks([2, 4, 6, 8, 10, 12, 14], ["2", "4", "6", "8", "10", "12", "14"])
#
# # Берем данные для диаграммы
# ax.plot(x_as, min_T, linewidth=0, linestyle='solid', zorder=3)
#
# # Заполняем область под значениями
# ax.fill(x_as, min_T, 'b', alpha=0.3)
#
# # Ограничиваем области
# plt.ylim(0, 50)
#
# # Отрисовываем все элементы
# for i in range(N):
#     angle_rad = i / float(N) * 2 * pi
#
#     if angle_rad == 0:
#         ha, distance_ax = "center", 10
#     elif 0 < angle_rad < pi:
#         ha, distance_ax = "left", 1
#     elif angle_rad == pi:
#         ha, distance_ax = "center", 1
#     else:
#         ha, distance_ax = "right", 1
#
#     ax.text(angle_rad, 50 + distance_ax, params[i], size=10, horizontalalignment=ha, verticalalignment="center")
#
#
# # Показываем итоговую диаграмму
# plt.show()