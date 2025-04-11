"""
This file provides functions for converting shapefiles into NetworkX graphs and visualizing them.

Key Functions:
- shp_to_graph: Converts a shapefile into a NetworkX graph.

Usage Notes:
- Ensure the input shapefile is properly formatted and contains geometry data.
"""
import networkx as nx
import matplotlib.pyplot as plt

def shp_to_graph(shapefile):
    # Get the GeoDataFrame from the shapefile instance
    gdf = shapefile.shapefile.copy()
    
    # Extract start and end coordinates using vectorized operations
    gdf['start'] = gdf.geometry.apply(lambda line: (line.coords[0][0], line.coords[0][1]))
    gdf['end'] = gdf.geometry.apply(lambda line: (line.coords[-1][0], line.coords[-1][1]))
    
    # Create an empty graph and add edges (nodes are automatically added)
    G = nx.Graph()
    G.add_edges_from(
        (row.start, row.end, {
            "weight": row.geometry.length,
            "geometry": list(row.geometry.coords)  # This stores all intermediate points
        })
        for row in gdf.itertuples(index=False)
    )
    return G