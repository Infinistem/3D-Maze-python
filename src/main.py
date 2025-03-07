import pygame
import math
from constants import Constants as C

# Initialize Pygame
pygame.init()
pygame.font.init()
hud_font = pygame.font.Font("comicsans.ttf", 30)
screen = pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Player class
class Player:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, da):
        self.angle += da

world_map = [
    "1111111111111111111111111111",
    "1000010000000000000000000001",
    "1000010000000000001000000001",
    "1000000000000000000000000001",
    "1000000000000000111000000001",
    "1000000000000000000000000001",
    "1000000000000000000000000001",
    "1000000000000000000000000001",
    "1111111111111111111111111111"
]

def cast_ray(player, angle):
    # Raycasting loop
    ray_x = player.x
    ray_y = player.y
    sin_a = math.sin(angle)
    cos_a = math.cos(angle)

    # Ray step increments
    step_size = 1

    # Avoid division by zero when checking for map bounds
    for depth in range(C.MAX_DEPTH):
        ray_x += cos_a * step_size
        ray_y += sin_a * step_size

        map_x = int(ray_x // 64)
        map_y = int(ray_y // 64)

        # Ensure we don't go out of bounds in the world map
        if map_x < 0 or map_x >= len(world_map[0]) or map_y < 0 or map_y >= len(world_map):
            return C.MAX_DEPTH

        # Check if we hit a wall
        if world_map[map_y][map_x] == '1':
            return depth
    return C.MAX_DEPTH

def render_3d(player):
    for ray in range(C.NUM_RAYS):
        ray_angle = player.angle - C.HALF_FOV + (ray / C.NUM_RAYS) * C.FOV
        depth = cast_ray(player, ray_angle)
        line_height = C.SCREEN_HEIGHT / (depth / 100)
        x_pos = ray * (C.SCREEN_WIDTH / C.NUM_RAYS)
        y_pos = (C.SCREEN_HEIGHT - line_height) / 2
        pygame.draw.rect(screen, C.WALL_COLOR, (x_pos, y_pos, C.SCREEN_WIDTH / C.NUM_RAYS, line_height))
def render_hud(player):
    return
    text_Health = hud_font.render('Health: ', True, green, blue)
    screen.blit(text, rect)


def init():
    player = Player(100, 100, math.pi / 4)  # Starting position and angle
    running = True

    while running:
        screen.fill(C.FLOOR_COLOR)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player controls (WASD for movement, Arrow keys for rotation)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.move(math.cos(player.angle) * C.MOVE_SPEED, math.sin(player.angle) * C.MOVE_SPEED)
        if keys[pygame.K_s]:
            player.move(-math.cos(player.angle) * C.MOVE_SPEED, -math.sin(player.angle) * C.MOVE_SPEED)
        if keys[pygame.K_LEFT]:
            player.rotate(-C.ROTATE_SPEED)
        if keys[pygame.K_RIGHT]:
            player.rotate(C.ROTATE_SPEED)

        # Raycasting and 3D rendering
        render_3d(player)
        render_hud(player)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    init()
