"""
This file provides the GraphProcessor class, which integrates the Shapefile and graph processing logic.

Key Classes:
- GraphProcessor: Handles the conversion of shapefiles into graphs and computes bounding boxes.

Usage Notes:
- Use the `process_graph` method to generate the graph and its bounds.
"""
from shapefile_class import Shapefile
from shp_to_graph import shp_to_graph

class GraphProcessor:
    def __init__(self, shapefile_path):
        self.shapefile = Shapefile(shapefile_path)
        self.graph = None
        self.bounds = None

    def process_graph(self):
        if not self.graph:
            self.graph = shp_to_graph(self.shapefile)
        if not self.bounds:
            self.bounds = self.shapefile.get_bounding_box(buffer_ratio=0.05)
        return self.graph, self.bounds