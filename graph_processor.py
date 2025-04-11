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