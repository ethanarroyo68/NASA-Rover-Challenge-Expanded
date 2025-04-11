from renderer import Renderer
from shp_visualizer import get_render_lines
import pygame

class Visualizer:
    def __init__(self, screen_width, screen_height):
        self.renderer = Renderer(screen_width, screen_height)

    def run(self, graph, bounds):
        lines = get_render_lines(graph, bounds, self.renderer.screen_width, self.renderer.screen_height)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.renderer.draw(lines)

        self.renderer.quit()