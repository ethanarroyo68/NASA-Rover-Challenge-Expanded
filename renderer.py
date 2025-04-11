import pygame
import networkx as nx
from shapefile_class import Shapefile
from shp_to_graph import shp_to_graph
import map_to_screen

class PygameRenderer:
    def __init__(self, screen_width, screen_height, shapefile_path):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shapefile = Shapefile(shapefile_path)  # Initialize shapefile class
        self.graph = shp_to_graph(shapefile_path)  # Convert shapefile to graph
        self.bbox = self.shapefile.get_bounding_box()  # Get the bounding box
        self.screen = pygame.display.set_mode((screen_width, screen_height))

    def create_graph(self):
        return shp_to_graph(self.shapefile)  # Convert shapefile to graph

    def render_edges(self):
        for edge in self.graph.edges():
            # Get coordinates of the two nodes (assumes nodes have 'pos' attributes)
            x1, y1 = self.graph.nodes[edge[0]]['pos']  # For node 1
            x2, y2 = self.graph.nodes[edge[1]]['pos']  # For node 2

            # Use map_to_screen directly with bbox
            screen_x1, screen_y1 = map_to_screen(x1, y1, self.screen_width, self.screen_height, self.bbox)
            screen_x2, screen_y2 = map_to_screen(x2, y2, self.screen_width, self.screen_height, self.bbox)

            pygame.draw.line(self.screen, (0, 0, 0), (screen_x1, screen_y1), (screen_x2, screen_y2))

    def update(self):
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))  # Clear screen (white)
            self.render_edges()  # Render edges of the graph
            self.update()  # Update the display

        pygame.quit()
