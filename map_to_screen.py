def map_to_screen(self, x, y, screen_width, screen_height):
    bbox = self.get_bounding_box()
    norm_x = (x - bbox['min_x']) / (bbox['max_x'] - bbox['min_x'])
    norm_y = (y - bbox['min_y']) / (bbox['max_y ']- bbox['min_y'])

    screen_x = int(norm_x * screen_width)
    screen_y = int((1 - norm_y) * screen_height)  # Y flip for Pygame
    return screen_x, screen_y
