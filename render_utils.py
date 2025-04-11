"""
This file provides utility functions for translating graph elements into visual renderings.

Key Functions:
- map_to_screen: Maps spatial coordinates to screen coordinates based on bounds and screen dimensions.
- screen_to_map: Maps screen coordinates to spatial coordinates based on bounds and screen dimensions.
- get_render_lines: Converts graph edges into drawable screen lines.

Usage Notes:
- Use the `map_to_screen` function for individual point mappings and `get_render_lines` for bulk edge conversions.
"""
# Functions for the translation of graph elements to visual renderings

def map_to_screen(bounds, x, y, screen_width, screen_height):
    bbox = bounds
    norm_x = (x - bbox['min_x']) / (bbox['max_x'] - bbox['min_x'])
    norm_y = (y - bbox['min_y']) / (bbox['max_y'] - bbox['min_y'])

    screen_x = int(norm_x * screen_width)
    screen_y = int((1 - norm_y) * screen_height)  # Y flip for Pygame
    return screen_x, screen_y

def screen_to_map(bounds, screen_x, screen_y, screen_width, screen_height):
    bbox = bounds
    norm_x = screen_x / screen_width
    norm_y = 1 - (screen_y / screen_height)  # Undo Y flip

    x = norm_x * (bbox['max_x'] - bbox['min_x']) + bbox['min_x']
    y = norm_y * (bbox['max_y'] - bbox['min_y']) + bbox['min_y']
    return x, y

def get_render_lines(G, bounds, screen_width, screen_height):
    lines = []
    for u, v, data in G.edges(data=True):
        polyline = data["geometry"]  # guaranteed to exist now

        for i in range(len(polyline) - 1):
            start, end = polyline[i], polyline[i + 1]
            sx1, sy1 = map_to_screen(bounds, start[0], start[1], screen_width, screen_height)
            sx2, sy2 = map_to_screen(bounds, end[0], end[1], screen_width, screen_height)
            lines.append(((sx1, sy1), (sx2, sy2)))

    return lines