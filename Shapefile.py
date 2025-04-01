import geopandas as gpd

class Shapefile:
    def __init__(self, shapefile_path):
        self.shapefile_path = shapefile_path
        self.shapefile = gpd.read_file(shapefile_path)  # Read the shapefile into geopandas

    def get_bounding_box(self):
        return self.shapefile.total_bounds  # Returns [min_x, min_y, max_x, max_y]

    def get_filepath(self):
        return self.shapefile_path  # Returns the filepath of the shapefile
