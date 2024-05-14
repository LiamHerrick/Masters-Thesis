import numpy as np
import matplotlib.pyplot as plt

def forward_euler(ode_func, y0, t_start, t_end, step_size):
    num_steps = int((t_end - t_start) / step_size) + 1
    t_values = np.linspace(t_start, t_end, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0

    for i in range(1, num_steps):
        t = t_values[i - 1]
        y = y_values[i - 1]
        dydt = ode_func(y, t)
        y_values[i] = y + step_size * dydt

    return t_values, y_values

def example_ode(y, t):
    return -10 * y

# Set up initial conditions and integration parameters
initial_value = 1.0
start_time = 0.0
end_time = 2.0
time_step = 0.01

# Solve the ODE using Forward Euler
time_values, solution_values = forward_euler(example_ode, initial_value, start_time, end_time, time_step)

# Plot the results
plt.plot(time_values, solution_values, label='Forward Euler')
plt.xlabel('Time')
plt.ylabel('Solution')
plt.legend()
plt.show()

