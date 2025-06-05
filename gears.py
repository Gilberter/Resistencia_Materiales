def generar_gif_engranajes(teeth1, teeth2, filename="gears.gif", frame_count=60):
    import pygame
    import math
    import imageio

    WIDTH, HEIGHT = 800, 400
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    gear1 = {
        "pos": (250, HEIGHT // 2),
        "radius": 60,
        "teeth": teeth1,
        "angle": 0,
        "color": (0, 150, 255)
    }
    gear2 = {
        "pos": (550, HEIGHT // 2),
        "radius": 100,
        "teeth": teeth2,
        "angle": 0,
        "color": (255, 180, 0)
    }

    def draw_gear(surface, gear, angle):
        cx, cy = gear["pos"]
        radius = gear["radius"]
        teeth = gear["teeth"]
        color = gear["color"]
        tooth_width = 6
        tooth_height = 12
        pygame.draw.circle(surface, color, (cx, cy), radius, 2)
        for i in range(teeth):
            theta = angle + i * (2 * math.pi / teeth)
            x = cx + (radius + tooth_height / 2) * math.cos(theta)
            y = cy + (radius + tooth_height / 2) * math.sin(theta)
            rect = pygame.Rect(0, 0, tooth_width, tooth_height)
            rect.center = (x, y)
            rotated_rect = pygame.transform.rotate(
                pygame.Surface((tooth_width, tooth_height), pygame.SRCALPHA), 
                -math.degrees(theta)
            )
            rotated_rect.fill(color)
            blit_pos = (x - rotated_rect.get_width() // 2, y - rotated_rect.get_height() // 2)
            surface.blit(rotated_rect, blit_pos)

    frames = []
    speed1 = 0.02  # radians/frame

    for _ in range(frame_count):
        screen.fill((30, 30, 30))
        gear1["angle"] += speed1
        gear2["angle"] -= speed1 * gear1["teeth"] / gear2["teeth"]
        draw_gear(screen, gear1, gear1["angle"])
        draw_gear(screen, gear2, gear2["angle"])
        pygame.draw.line(screen, (200, 200, 200), gear1["pos"], gear2["pos"], 2)
        pygame.display.flip()
        clock.tick(60)
        frame = pygame.surfarray.array3d(screen)
        frame = frame.transpose([1, 0, 2])
        frames.append(frame)

    pygame.quit()
    imageio.mimsave(filename, frames, duration=0.05)