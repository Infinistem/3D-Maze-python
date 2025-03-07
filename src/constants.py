import math

class Constants:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FOV = math.pi / 2  # 60 degrees field of view
    HALF_FOV = FOV / 2
    NUM_RAYS = 320  # Number of rays for raycasting
    MAX_DEPTH = 800  # Maximum distance the ray can travel
    MOVE_SPEED = 4  # Player movement speed
    ROTATE_SPEED = 0.07  # Player rotation speed

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (169, 169, 169)
    FLOOR_COLOR = (30, 30, 220)
    CEIL_COLOR = (0, 200, 200)
    WALL_COLOR = (22, 200, 50)

    # Item mapping & texture mapping