# NASA-Rover-Challenge-Expanded
# 🚀 Rover Mapping Project

A pathfinding prototype for rover navigation using real-world road data. This project reads shapefiles (SHP) to construct a road network graph and compute the shortest or fastest route between two points.

---

## 🎯 Goals

- Parse shapefiles into usable graph structures
- Visualize the road network with a Pygame-based prototype
- Calculate shortest paths using NetworkX
- Structure the project modularly for future web integration

---

## 🛣️ Project Roadmap

1. **Shapefile Parsing**  
   Use a `shp_to_graph` class to build graph structures from SHP data.

2. **Coordinate Normalization**  
   Compute bounding boxes and scale coordinates — handled outside core graph logic.

3. **Pygame Visualization**  
   Display roads and paths interactively, while keeping logic modular and decoupled from UI.

4. **Pathfinding Engine**  
   Compute optimal paths using filters (e.g. shortest, fastest), powered by NetworkX.

5. **Future Additions**  
   - Integrate elevation data or lidar scans  
   - Support terrain-based cost heuristics  

6. **Full-Stack Web Prototype**  
   Convert backend logic to serve a frontend app with map display and route planning.

---

## 🛠️ Installation / Setup

### Dependencies

Ensure you have the following Python libraries installed:
- `pygame`
- `networkx`
- `pyshp`
- `geopandas`
- `matplotlib`

### Environment

- Python 3.8 or higher is recommended.

### How to Install and Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ethanarroyo68/NASA-Rover-Challenge-Expanded.git
   cd NASA-Rover-Challenge-Expanded
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## 🚀 Usage Instructions

1. Run `main.py` using Python.
2. Use the graphical interface to select starting and ending points on the road network.
3. The application will calculate and display the optimal route based on the selected filter (e.g., shortest distance, fastest time).

### Optional CLI Arguments

- `--filter`: Specify the pathfinding filter (`shortest`, `fastest`).

Example:
```bash
python main.py --filter shortest
```

---

## 📁 File/Module Descriptions

- `main.py`: The entry point for the application; initializes graph processing and visualization.
- `graph_processor.py`: Processes shapefiles into graphs and computes bounding boxes.
- `shp_to_graph.py`: Converts shapefiles into NetworkX graphs with detailed geometry data.
- `shapefile_class.py`: Handles shapefile reading and provides bounding box utilities.
- `visualizer.py`: Integrates the Renderer and visualization logic to display graph data.
- `renderer.py`: Manages screen rendering, including drawing lines and handling the Pygame window.
- `render_utils.py`: Provides utilities for mapping graph data to screen coordinates and renderable lines.

---

## 🏛️ Architecture / Design Notes

- **Separation of Concerns**: Graph logic is fully decoupled from the visualization layer, allowing future integration with other frontends (e.g., web apps).
- **Modularity**: Each component (shapefile parsing, visualization, pathfinding) is designed as an independent module, making the project easier to extend and maintain.