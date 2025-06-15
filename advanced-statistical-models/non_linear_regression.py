import numpy as np
import plotly.graph_objects as go
import numpy.polynomial.polynomial as poly

np.random.seed(42)
x = np.linspace(0, 30, 100)
noise_scale = 4  # Increased noise

# Define nonlinear functions with noise
def nonlinear_log(x):
    return 10 * np.log(x + 1) + 0.1 * x**2 + np.random.normal(scale=noise_scale, size=len(x))

def nonlinear_cubic(x):
    return 0.01 * x**3 - 0.4 * x**2 + 3 * x + 5 + np.random.normal(scale=noise_scale, size=len(x))

def nonlinear_quadratic(x):
    return -0.5 * x**2 + 5 * x + 10 + np.random.normal(scale=noise_scale, size=len(x))

# Prepare functions and titles
functions = {
    "Logarithmic + Quadratic": nonlinear_log,
    "Cubic Polynomial": nonlinear_cubic,
    "Quadratic Polynomial": nonlinear_quadratic,
}

for name, func in functions.items():
    y = func(x)
    coefs = poly.Polynomial.fit(x, y, deg=3)
    x_ext = np.linspace(-5, 35, 500)
    y_poly_ext = coefs(x_ext)

    fig = go.Figure()

    # Raw noisy data
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers',
        name='Data',
        marker=dict(color='blue', size=6)
    ))

    # Cubic polynomial fit
    fig.add_trace(go.Scatter(
        x=x_ext, y=y_poly_ext,
        mode='lines',
        name='Cubic Polynomial Fit',
        line=dict(color='red', width=2)
    ))

    fig.update_layout(
        template="simple_white",
        font=dict(size=15),
        title_text=f"{name} with Cubic Polynomial Fit",
        width=900,
        height=500,
        title_x=0.5,
        xaxis_title="t",
        yaxis_title="y",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    fig.show()
