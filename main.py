from graph_processor import GraphProcessor
from visualizer import Visualizer

def main():
    # Configuration
    shapefile_path = 'South_Clear_Creek_Roads.shp'
    screen_width = 600 # Works best if this is a multiple of 100
    screen_height = 800 # Works best if this is a multiple of 100

    # Initialize GraphProcessor
    graph_processor = GraphProcessor(shapefile_path)
    graph, bounds = graph_processor.process_graph()

    # Initialize Visualizer
    visualizer = Visualizer(screen_width, screen_height)
    visualizer.run(graph, bounds)

if __name__ == "__main__":
    main()