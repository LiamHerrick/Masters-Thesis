import numpy as np
import matplotlib.pyplot as plt

# Define the number of particles
num_particles = 100

# Define the simulation parameters
time_step = 0.01
time_end = 10

# Define the particle positions and velocities
particle_positions = np.random.rand(num_particles, 2)
particle_velocities = np.random.rand(num_particles, 2)

# Define the force field
def force_field(positions):
    return -positions

# Define the equations of motion
def equations_of_motion(positions, velocities, force_field):
    return velocities + time_step * force_field(positions) / num_particles

# Define the Runge-Kutta method
def runge_kutta(positions, velocities, force_field, time_step):
    k1 = time_step * equations_of_motion(positions, velocities, force_field)
    k2 = time_step * equations_of_motion(positions + 0.5 * k1, velocities, force_field)
    k3 = time_step * equations_of_motion(positions + 0.5 * k2, velocities, force_field)
    k4 = time_step * equations_of_motion(positions + k3, velocities, force_field)
    
    return (positions + (k1 + 2 * k2 + 2 * k3 + k4) / 6,
            velocities + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

# Run the simulation
for t in np.arange(0, time_end, time_step):
    particle_positions, particle_velocities = runge_kutta(particle_positions, particle_velocities, force_field, time_step)
    
# Visualize the results

plt.plot(particle_positions[:, 0], particle_positions[:, 1], 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()