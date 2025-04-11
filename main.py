from shapefile_class import Shapefile
from shp_to_graph import shp_to_graph
from renderer import Renderer
import pygame
from shp_visualizer import get_render_lines  # assuming your line-prep logic is here

def main():
    # Path to shapefile
    shapefile_path = 'South_Clear_Creek_Roads.shp'
    screen_width = 600
    screen_height = 800

    # Initialize the shapefile class and load the shapefile
    shapefile = Shapefile(shapefile_path)

    # Use the shp_to_graph method to convert the shapefile to a graph
    graph = shp_to_graph(shapefile)
    bounds = shapefile.get_bounding_box(buffer_ratio=0.05)  # tweak % if needed

    lines = get_render_lines(graph, bounds, screen_width, screen_height)

    renderer = Renderer(screen_width, screen_height)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        renderer.draw(lines)

    renderer.quit()

if __name__ == "__main__":
    main()