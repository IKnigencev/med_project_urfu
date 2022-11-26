import os

import plotly.io as pio
import plotly.graph_objects as go
from datetime import datetime
from plotly.subplots import make_subplots


categories_T = ['NEU/CD4', 'NEU/CD3', 'NEU/LYMF', 'NEU/CD8']
categories_T = [*categories_T, categories_T[0]]

results_T = [1.85, 1.14, 0.74, 2.87]
results_T = [*results_T, results_T[0]]

min_T = [3.00, 2.25, 1.67, 9.47]
min_T = [*min_T, min_T[0]]

max_T = [5.00, 3.63, 1.80, 12.30]
max_T = [*max_T, max_T[0]]

categories_B = ["CD19/CD4", "LYMF/CD19", "NEU/LYMF", "CD19/CD8"]
categories_B = [*categories_B, categories_B[0]]

results_B = [0.50, 5.00, 0.74, 0.78]
results_B = [*results_B, results_B[0]]

min_B = [0.16, 9.60, 1.67, 0.53]
min_B = [*min_B, min_B[0]]

max_B = [0.31, 10.00, 1.80, 0.77]
max_B = [*max_B, max_B[0]]

d = max(max_T)
s = max(results_T)
if d > s:
    f = d
else:
    f = s

v = max(max_B)
z = max(results_B)
if v > z:
    g = v
else:
    g = z

# кол-во областей диаграм
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'polar'}] * 2])

# max_T
fig.add_trace(go.Scatterpolar(
    r=max_T,
    theta=categories_T,
    line=dict(color="green"),
    fill='none',
    legendgroup="group2",
    legendgrouptitle_text="<b>T-клеточное звено</b>",
    name='Верхние референтные значения звена T',
    mode="lines+markers+text",
    textposition='top left',
    text=max_T
), 1, 1)

# min_T
fig.add_trace(go.Scatterpolar(
    r=min_T,
    theta=categories_T,
    line=dict(color="seagreen"),
    fill='tonext',
    fillcolor="lightgreen",
    legendgroup="group2",
    name='Нижние референтные значения звена Т',
    mode="text+lines+markers",
    textposition='bottom center',
    text=min_T
), 1, 1)

# results_T
fig.add_trace(go.Scatterpolar(
    r=results_T,
    theta=categories_T,
    line=dict(color="crimson"),
    fill='none',
    legendgroup="group2",
    name='Результаты звена T',
    mode="lines+markers+text",
    textposition='middle right',
    text=results_T
), 1, 1)

# max_B
fig.add_trace(go.Scatterpolar(
    r=max_B,
    theta=categories_B,
    line=dict(color="mediumblue"),
    fill='none',
    legendgroup="group",
    legendgrouptitle_text="<b>B-клеточное звено</b>",
    name='Верхние референтные значения звена В',
    mode="text+lines+markers",
    textposition='top right',
    text=max_B
), 1, 2)

# min_B
fig.add_trace(go.Scatterpolar(
    r=min_B,
    theta=categories_B,
    line=dict(color="royalblue"),
    fill='tonext',
    fillcolor="lightblue",
    legendgroup="group",
    name='Нижние референтные значения звена В',
    mode="text+lines+markers",
    textposition='bottom left',
    text=min_B
), 1, 2)

# results_B
fig.add_trace(go.Scatterpolar(
    r=results_B,
    theta=categories_B,
    line=dict(color="red"),
    fill='none',
    legendgroup="group",
    name='Результаты звена B',
    mode="text+lines+markers",
    textposition='middle right',
    text=results_B
), 1, 2)

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, f + 1]
        )),
    polar2=dict(
        radialaxis=dict(
            visible=True,
            range=[0, g + 1],
        )),
    showlegend=True,
    legend_orientation='h',
    legend=dict(borderwidth=1, yanchor="bottom", y=-0.08,
                xanchor="center", x=0.5),
    title='T-клеточное звено и B-клеточное звено',
    title_x=0.5
)

curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

path = 'med_project_urfu/diagrams'
filename = f'{curr_datetime} result.png'
filename = os.path.join(path, filename)
pio.write_image(fig, filename, width=1980, height=1080)

