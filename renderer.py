"""
This file provides the Renderer class, which is responsible for rendering graphical elements on a Pygame window.

Key Classes:
- Renderer: Manages screen initialization, background color setup, and drawing lines.

Usage Notes:
- Use the `draw` method to render lines and the `quit` method to close the Pygame window.
"""
import pygame

class Renderer:
    def __init__(self, screen_width, screen_height, background_color=(255, 255, 255), line_color=(0, 0, 0)):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Graph Viewer")
        self.background_color = background_color
        self.line_color = line_color
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, lines):
        self.screen.fill(self.background_color)
        for (start, end) in lines:
            pygame.draw.line(self.screen, self.line_color, start, end, width=1)
        pygame.display.flip()

    def quit(self):
        pygame.quit()