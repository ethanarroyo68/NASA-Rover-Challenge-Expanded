from shapefile_class import Shapefile
from shp_to_graph import shp_to_graph

def main():
    # Path to shapefile
    shapefile_path = 'South_Clear_Creek_Roads.shp'

    # Initialize the shapefile class and load the shapefile
    shapefile = Shapefile(shapefile_path)

    # Use the shp_to_graph method to convert the shapefile to a graph
    graph = shp_to_graph(shapefile)

if __name__ == "__main__":
    main()
