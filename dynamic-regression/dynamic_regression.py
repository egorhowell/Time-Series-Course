import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# Generate sample data
np.random.seed(0)
time = np.arange(100)
series1 = np.cumsum(np.random.randn(100))
series2 = 0.5 * series1 + np.random.randn(100) * 0.5

# Plot 1: Time series
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=time, y=series1, mode='lines', name='X', line=dict(color='blue')))
fig1.add_trace(go.Scatter(x=time, y=series2, mode='lines', name='Y', line=dict(color='red')))
fig1.update_layout(
    title='Two Time Series Over Time',
    xaxis_title='t',
    template="simple_white",
    font=dict(size=15),
    yaxis_title='Value',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    width=900,
    height=500
)

# Regression for plot 2
X = series1.reshape(-1, 1)
y = series2
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Plot 2: Scatter + regression line
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=series1, y=series2, mode='markers', name='Data points', marker=dict(color='blue')))
fig2.add_trace(go.Scatter(x=series1, y=y_pred, mode='lines', name='Best fit line', line=dict(color='red')))
fig2.update_layout(
    title='Regression of Y against X',
    template="simple_white",
    font=dict(size=15),
    xaxis_title='X',
    yaxis_title='Y',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    width=900,
    height=500
)

fig1.show()
fig2.show()
