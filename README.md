# NASA-Rover-Challenge-Expanded
# 🚀 Rover Mapping Project

A pathfinding prototype for rover navigation using real-world road data. This project reads shapefiles (SHP) to construct a road network graph and compute the shortest or fastest route between two points. The long-term goal is to incorporate terrain data (elevation, lidar) and eventually build a full-stack web application.

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
