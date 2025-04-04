# Pygame Asteroids

A simple Python game built using Pygame where the player controls a spaceship and attempts to avoid or destroy asteroids.

## Requirements

To run this project, you need to have Python installed on your system. You also need to install Pygame.

You can install the required dependencies by running:

```bash
pip install -r requirements.txt

Game Description
The player controls a spaceship that can move around the screen and shoot lasers to destroy asteroids. The objective is to avoid colliding with asteroids and destroy as many as possible.

Files
asteroid.py: Handles asteroid mechanics.

asteroidfield.py: Generates the field and positions asteroids.

circleshape.py: Defines circular objects used in the game.

constants.py: Contains the constants like screen dimensions, colors, and other configurations.

main.py: The main game loop and the core of the game.

player.py: Handles the player spaceship mechanics.

shot.py: Defines the laser shot objects and their behavior.

requirements.txt: Lists the Python dependencies (e.g., Pygame).

How to Play
Run the game by executing main.py.

Use the arrow keys or WASD to move your spaceship.

Press space to shoot lasers at the asteroids.

Avoid colliding with asteroids to keep your spaceship alive.
