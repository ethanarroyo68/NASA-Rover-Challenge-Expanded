import networkx as nx
import matplotlib.pyplot as plt

def shp_to_graph(shapefile):
    """
    Convert a Shapefile instance into a NetworkX graph.
    
    Parameters:
        shapefile: An instance of the Shapefile class (which contains a GeoDataFrame as `shapefile.shapefile`).
        
    Returns:
        G: A NetworkX graph where nodes are start and end coordinates of each geometry,
           and edges are added with a weight equal to the length of the geometry.
    """
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

def visualize_graph(G):
    """Visualize the provided NetworkX graph."""
    nx.draw(G, with_labels=True)
    plt.show()
