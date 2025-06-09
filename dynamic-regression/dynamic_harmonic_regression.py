import numpy as np
import plotly.graph_objects as go

# Create x values from 0 to 3π
x = np.linspace(0, 3 * np.pi, 500)

# Compute sine(2x), cos(3x), and their sum
y1 = np.sin(2 * x)
y2 = np.cos(3 * x)
y_sum = y1 + y2

# Define x-ticks and labels
xticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi]
xtick_labels = ['0', 'π/2', 'π', '3π/2', '2π', '5π/2', '3π']

# Create Plotly figure
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='sine(2x)', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(3x)', line=dict(color='green')))
fig.add_trace(go.Scatter(x=x, y=y_sum, mode='lines', name='sum', line=dict(color='red')))

# Customize layout for transparency
fig.update_layout(
    template="simple_white",
    font=dict(size=15),
    title_text="Example Sum of Sinusoidal Waves",
    title_x=0.5,
    width=900,
    height=500,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        title='x',
        tickmode='array',
        tickvals=xticks,
        ticktext=xtick_labels
    ),
    yaxis_title='y'
)

fig.show()


# Create x values from 0 to 3π
x = np.linspace(0, 3 * np.pi, 500)

# Number of odd harmonics to include
N = 100

# Initialize square wave approximation
square_wave = np.zeros_like(x)

# Sum odd harmonics: k = 1, 3, 5, ..., N (odd only)
for k in range(1, N + 1, 2):
    square_wave += (4 / (np.pi * k)) * np.sin(k * x)

# Define x-ticks and labels
xticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi]
xtick_labels = ['0', 'π/2', 'π', '3π/2', '2π', '5π/2', '3π']

# Create Plotly figure
fig = go.Figure()

# Add the square wave approximation trace
fig.add_trace(go.Scatter(x=x, y=square_wave, mode='lines', name='Square wave approx.', line=dict(color='blue')))

# Customize layout for transparency and ticks
fig.update_layout(
    template="simple_white",
    font=dict(size=15),
    title_text="Square Wave Approximation Using Sum of Sines",
    title_x=0.5,
    width=900,
    height=500,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        title='x',
        tickmode='array',
        tickvals=xticks,
        ticktext=xtick_labels
    ),
    yaxis_title='Amplitude'
)

fig.show()

