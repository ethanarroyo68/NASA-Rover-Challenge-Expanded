import geopandas as gpd

class Shapefile:
    def __init__(self, shapefile_path):
        self.shapefile_path = shapefile_path
        self.shapefile = gpd.read_file(shapefile_path)  # Read the shapefile into geopandas
        self.bounding_box = self.shapefile.total_bounds


    def get_bounding_box(self):
        min_x, min_y, max_x, max_y = self.bounding_box # Uses stored value
        return {
            "min_x": min_x,
            "max_x": max_x,
            "min_y": min_y,
            "max_y": max_y,
            "width": max_x - min_x,
            "height": max_y - min_y
        }

    def get_filepath(self):
        return self.shapefile_path  # Returns the filepath of the shapefile
