"""
This file provides the Shapefile class, which wraps around GeoPandas for shapefile handling.

Key Classes:
- Shapefile: Reads a shapefile and provides utilities like bounding box computation.

Usage Notes:
- Ensure the shapefile path provided is valid and accessible.
"""
import geopandas as gpd

class Shapefile:
    def __init__(self, shapefile_path):
        self.shapefile_path = shapefile_path
        self.shapefile = gpd.read_file(shapefile_path)  # Read the shapefile into geopandas
        self.bounding_box = self.shapefile.total_bounds


    def get_bounding_box(self, buffer_ratio=0.05):
        min_x, min_y, max_x, max_y = self.bounding_box

        width = max_x - min_x
        height = max_y - min_y

        buffer_x = width * buffer_ratio
        buffer_y = height * buffer_ratio

        return {
            "min_x": min_x - buffer_x,
            "max_x": max_x + buffer_x,
            "min_y": min_y - buffer_y,
            "max_y": max_y + buffer_y,
            "true_width": width,
            "true_height": height,
            "width": (max_x - min_x) + 2 * buffer_x,
            "height": (max_y - min_y) + 2 * buffer_y
        }


    def get_filepath(self):
        return self.shapefile_path  # Returns the filepath of the shapefile