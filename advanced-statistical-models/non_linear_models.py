import numpy as np
import plotly.graph_objects as go
import numpy.polynomial.polynomial as poly

# Generate synthetic data
np.random.seed(42)
x = np.linspace(0, 30, 100)
y = np.piecewise(x,
                 [x < 10, (x >= 10) & (x < 20), x >= 20],
                 [lambda x: 2 * x + 1 + np.random.normal(scale=2, size=len(x)),
                  lambda x: -1 * x + 30 + np.random.normal(scale=2, size=len(x)),
                  lambda x: 0.5 * x + 5 + np.random.normal(scale=2, size=len(x))])

# Polynomial fit (3rd degree)
coefs = poly.Polynomial.fit(x, y, deg=3)
y_poly = coefs(x)

# Define 4 breakpoints (for 3 linear segments)
breakpoints = np.linspace(x.min(), x.max(), 4)
indices = [np.abs(x - bp).argmin() for bp in breakpoints]
x_knots = x[indices]
y_knots = y[indices]

# Create Plotly figure
fig = go.Figure()

# Raw data
fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Data', marker=dict(color='blue')))

# # Polynomial fit
# fig.add_trace(go.Scatter(x=x, y=y_poly, mode='lines', name='Polynomial Fit (deg=3)', line=dict(color='red')))
#
# # Piecewise linear spline (3 segments)
# fig.add_trace(go.Scatter(x=x_knots, y=y_knots, mode='lines+markers',
#                          name='Piecewise Linear Spline (3 segs)', line=dict(color='orange')))

# Layout
fig.update_layout(
    template="simple_white",
    font=dict(size=15),
    title_text="Piece Wise Data Example",
    width=900,
    title_x=0.5,
    height=400,
    xaxis_title="X",
    yaxis_title="Y"
)

fig.show()
