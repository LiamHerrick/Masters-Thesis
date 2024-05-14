import numpy as np
import matplotlib.pyplot as plt

# Parameters
gamma = 1.4  # Adiabatic index
L = 10.0  # Length of the domain
Nx = 1000  # Number of grid points
dx = L / (Nx - 1)  # Grid spacing
dt = 0.001  # Time step
T_final = 0.1  # Final simulation time

# Initialize arrays
x = np.linspace(0, L, Nx)
rho = np.ones(Nx)  # Initial density
u = np.zeros(Nx)  # Initial x-velocity
p = np.ones(Nx)  # Initial pressure

# Left BCs
rho[0] = 0.8
u[0] = 0.5
p[0] = 0.1

# Simulation loop
for t in np.arange(1, T_final, dt):
    # Forward Euler updates
    rho[1:] -= dt / dx * (rho[1:] * u[1:] - rho[:-1] * u[:-1])  # Update density
    u[1:] -= dt / dx * (u[1:] * u[1:] - u[:-1] * u[:-1] + p[1:] - p[:-1])  # Update x-velocity
    p = (gamma - 1) * (rho * (0.5 * u**2) - 0.5 * rho * u[0]**2)  # Update pressure

# Right BCs
rho[Nx-2] = -1.0
rho[Nx-1] = 1.0
u[Nx-2] = -0.1
u[Nx-1] = 0.1
p[Nx-2] = 0.0
p[Nx-1] = 0.0

# Plot the final state
plt.plot(x, rho, label='Density')
plt.plot(x, u, label='Velocity')
plt.plot(x, p, label='Pressure')
plt.xlabel('Position')
plt.ylabel('Values')
plt.legend()
plt.show()
