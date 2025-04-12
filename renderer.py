"""
This file provides the Renderer class, which is responsible for rendering graphical elements on a Pygame window.

Key Classes:
- Renderer: Manages screen initialization, background color setup, drawing lines, and rendering coordinate rulers.

Usage Notes:
- Use the `draw` method to render lines, `draw_rulers` to render axis rulers with coordinate labels, and `quit` to close the Pygame window.
"""

import pygame
from render_utils import screen_to_map

class Renderer:
    def __init__(self, screen_width, screen_height, background_color=(255, 255, 255), line_color=(0, 0, 0)):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Graph Viewer")
        self.background_color = background_color
        self.line_color = line_color
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw_paths(self, lines):
        for (start, end) in lines:
            pygame.draw.line(self.screen, self.line_color, start, end, width=1)
        pygame.display.flip()
    """
    def draw_rulers(self, bounds, tick_spacing=100):
        font = pygame.font.SysFont(None, 16)
        ruler_color = (0, 0, 0)
        text_color = (0, 0, 0)

        # X-axis (top)
        for x in range(0, self.screen_width, tick_spacing):
            pygame.draw.line(self.screen, ruler_color, (x, 0), (x, 5), width=1)
            map_x, _ = screen_to_map(bounds, x, 0, self.screen_width, self.screen_height)
            label = font.render(str(int(map_x)), True, text_color)
            self.screen.blit(label, (x + 2, 6))  # slight offset below tick

        # Y-axis (left)
        for y in range(0, self.screen_height, tick_spacing):
            pygame.draw.line(self.screen, ruler_color, (0, y), (5, y), width=1)
            _, map_y = screen_to_map(bounds, 0, y, self.screen_width, self.screen_height)
            label = font.render(str(int(map_y)), True, text_color)
            self.screen.blit(label, (6, y - 6))  # offset right of tick
    """

    def quit(self):
        pygame.quit()