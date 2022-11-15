import plotly.graph_objects as go


results_Bf = [0.50, 5.00, 0.74, 0.78, 0.50]
categories_Bf = ["CD19/CD4", "LYMF/CD19", "NEU/LYMF", "CD19/CD8", "CD19/CD4"]
# x = categories_B[0]
# s = categories_B.extend(x[0])
# i =0
# print(s)
min_B = [0.16, 9.60, 1.67, 0.53,  0.16]
max_B = [0.31, 10.00, 1.80, 0.77, 0.31]

v = max(max_B)
s = max(results_Bf)
if v > s:
    g = v
else:
    g = s

fig_B = go.Figure()
# min_B
fig_B.add_trace(go.Scatterpolar(
      r=min_B,
      theta=categories_Bf,
      fill='none',
      name='min_B'
))
# max_B
fig_B.add_trace(go.Scatterpolar(
      r=max_B,
      theta=categories_Bf,
      fill='tonext',
      name='max_B'
))
# results_B
fig_B.add_trace(go.Scatterpolar(
      r=results_Bf,
      theta=categories_Bf,
      fill='none',
      name='results_B'
))


fig_B.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, g+2]
    )),
  showlegend=False
)

fig_B.show()