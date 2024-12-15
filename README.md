# 2D Physics Simulation Project

This project is a simple 2D physics simulation written in Python using the Pygame library. It demonstrates basic physics concepts such as gravity, collisions, and damping effects in a visual and interactive way.

## Features

- Realistic gravity simulation.
- Collision detection with boundaries (top, bottom, left, and right walls).
- Interactive controls to manipulate the particle's velocity.
- Adjustable damping factor based on particle mass.
- Smooth animations with customizable frame rates.

## Installation

To run this project, you need Python installed on your system along with the Pygame library. Follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/stigsec/2d-physics.git
   cd 2d-physics
   ```

2. Install the required library:

   ```bash
   pip install pygame
   ```

3. Run the script:

   ```bash
   python 2d-physics.py
   ```

## Controls

- **Arrow Keys**:
  - **Up**: Increase upward velocity.
  - **Down**: Increase downward velocity.
  - **Right**: Increase rightward velocity.
  - **Left**: Increase leftward velocity.
- **`W`**: Add a large upward velocity.
- **`S`**: Add a large downward velocity.
- **`D`**: Add a large rightward velocity.
- **`A`**: Add a large leftward velocity.
- **`R`**: Reset the particle's velocity to 0.

## How It Works

### Physics

The simulation calculates the particle's position and velocity based on gravity and time step updates:

- Gravity is a constant force applied in the downward direction.
- Collisions with walls are detected, and the particle's velocity is adjusted with a damping factor to simulate energy loss.

### Rendering

Pygame is used to render the simulation:

- The particle is drawn as a circle with customizable mass, radius, and color.
- The screen updates at a fixed frame rate

## Customization

You can customize various parameters in the code:

- **`GRAVITY`**: Change the gravity value to simulate different environments.
- **`TIME_STEP`**: Adjust the time step for finer or coarser updates.
- **Particle Attributes**: Modify the initial position, mass, radius, and color of the particle.
- **Screen Dimensions**: Adjust the width and height of the simulation window.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) for more details.

---

Developed by stigsec

