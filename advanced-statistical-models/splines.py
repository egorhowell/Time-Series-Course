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
x_ext = np.linspace(-5, 35, 500)
y_poly_ext = coefs(x_ext)

# Define knot positions for spline
breakpoints = np.linspace(x.min(), x.max(), 4)
indices = [np.abs(x - bp).argmin() for bp in breakpoints]
x_knots = x[indices]
y_knots = y[indices]

# Prepare arrays for spline with extrapolation
x_spline_ext = []
y_spline_ext = []

# Extrapolate before first knot (x < 0)
x1, x2 = x_knots[0], x_knots[1]
y1, y2 = y_knots[0], y_knots[1]
slope = (y2 - y1) / (x2 - x1)
intercept = y1 - slope * x1
x_seg = np.linspace(-5, x1, 100)
y_seg = slope * x_seg + intercept
x_spline_ext.extend(x_seg)
y_spline_ext.extend(y_seg)

# Segment 1: [0, 10]
x_seg = np.linspace(x1, x2, 200)
y_seg = slope * x_seg + intercept
x_spline_ext.extend(x_seg)
y_spline_ext.extend(y_seg)

# Segment 2: [10, 20]
x1, x2 = x_knots[1], x_knots[2]
y1, y2 = y_knots[1], y_knots[2]
slope = (y2 - y1) / (x2 - x1)
intercept = y1 - slope * x1
x_seg = np.linspace(x1, x2, 200)
y_seg = slope * x_seg + intercept
x_spline_ext.extend(x_seg)
y_spline_ext.extend(y_seg)

# Segment 3: [20, 30]
x1, x2 = x_knots[2], x_knots[3]
y1, y2 = y_knots[2], y_knots[3]
slope = (y2 - y1) / (x2 - x1)
intercept = y1 - slope * x1
x_seg = np.linspace(x1, x2, 200)
y_seg = slope * x_seg + intercept
x_spline_ext.extend(x_seg)
y_spline_ext.extend(y_seg)

# Extrapolate after last knot (x > 30)
x_seg = np.linspace(x2, 35, 100)
y_seg = slope * x_seg + intercept
x_spline_ext.extend(x_seg)
y_spline_ext.extend(y_seg)

# Create Plotly figure
fig = go.Figure()

# Raw data
fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Data', marker=dict(color='blue')))

# Polynomial fit (3rd degree) over extended domain
fig.add_trace(go.Scatter(x=x_ext, y=y_poly_ext, mode='lines', name='Polynomial Fit (deg=3)', line=dict(color='red')))

# Piecewise linear spline with extrapolation
fig.add_trace(go.Scatter(x=x_spline_ext, y=y_spline_ext, mode='lines', name='Extrapolated Linear Spline', line=dict(color='orange', dash='dash')))

# Layout with transparent background
fig.update_layout(
    template="simple_white",
    font=dict(size=15),
    title_text="Piecewise Linear vs Cubic Polynomial Fit (Extrapolated)",
    width=900,
    height=500,
    title_x=0.5,
    xaxis_title="t",
    yaxis_title="y",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

fig.show()
