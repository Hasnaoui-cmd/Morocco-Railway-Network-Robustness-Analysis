# Railway Network Analysis - Moroccan Railway System

## Overview

This project provides a comprehensive analysis of the Moroccan railway network using graph theory principles. It models railway stations as nodes and connections as edges, enabling advanced network analysis, optimization, and robustness testing.

## Project Description

The **Railway Network Analysis** project uses graph theory to analyze and optimize the Moroccan railway infrastructure. The analysis includes:

- **Network Modeling**: Representation of railway stations and connections as a graph
- **Shortest Path Algorithms**: Finding optimal routes between stations using Dijkstra's and Floyd-Warshall algorithms
- **Network Centrality**: Identifying critical stations and connections
- **Robustness Analysis**: Testing network resilience to station or connection failures
- **Interactive Visualizations**: Graphical representation of the network with customizable displays

## Features

- ✅ **Data Loading and Preprocessing**: Clean and process railway connection data
- ✅ **Graph Construction**: Build network graph with NetworkX
- ✅ **Network Analysis**: Calculate connectivity, centrality, and network metrics
- ✅ **Shortest Path Computation**: Dijkstra's and Floyd-Warshall algorithms
- ✅ **Adjacency and Incidence Matrices**: Matrix representations of the network
- ✅ **Interactive Visualizations**: Matplotlib-based network visualizations
- ✅ **Robustness Testing**: Analyze network behavior under failures
- ✅ **Interactive Widgets**: IPyWidgets for dynamic station selection

## Dataset

The project uses `projet_reseau_maroc.csv` which contains:

- **Source**: Origin station
- **Target**: Destination station
- **Distance_km**: Distance in kilometers
- **Duree_min**: Travel time in minutes
- **Type_Train**: Train type (Al Boraq, TNR, Al Atlas, etc.)
- **Frequence_par_heure**: Trains per hour

### Railway Network Coverage

The dataset includes major Moroccan cities and stations:
- **North**: Tanger Ville, Asilah
- **Central**: Rabat, Casablanca, Kenitra, Meknes, Fes
- **South**: Marrakech, Benguerir, Safi
- **East**: Oujda, Nador, Taza

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Jupyter Notebook or JupyterLab

### Setup

1. **Clone or download the project**:
   ```bash
   cd railway_structure
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     .venv\\Scripts\\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Analysis

1. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Open the analysis notebook**:
   - Navigate to `Railway_Network_Analysis_v2_Robustness.ipynb`

3. **Run the analysis**:
   - Execute cells sequentially from top to bottom
   - The notebook is organized into sections for easy navigation

### Testing Imports

A test script is provided to verify library installations:

```bash
python test_imports.py
```

This will verify that NetworkX and Matplotlib are correctly installed.

## Project Structure

```
railway_structure/
│
├── Railway_Network_Analysis_v2_Robustness.ipynb  # Main analysis notebook
├── projet_reseau_maroc.csv                        # Railway network data
├── test_imports.py                                 # Import verification script
├── requirements.txt                                # Python dependencies
├── README.md                                       # This file
│
└── .venv/                                          # Virtual environment (ignored)
```

## Key Components

### 1. Data Loading and Preprocessing
- Load CSV data using pandas
- Clean station names and validate connections
- Handle missing or duplicate entries

### 2. Graph Construction
- Create NetworkX graph with stations as nodes
- Add edges with travel time weights
- Store metadata (distance, train type, frequency)

### 3. Network Analysis
- **Connectivity**: Check if network is fully connected
- **Centrality Measures**: 
  - Degree centrality (most connected stations)
  - Betweenness centrality (critical transfer points)
  - Closeness centrality (accessibility)
- **Clustering Coefficient**: Network density analysis

### 4. Shortest Path Algorithms
- **Dijkstra's Algorithm**: Single-source shortest paths
- **Floyd-Warshall Algorithm**: All-pairs shortest paths
- Interactive station selection with IPyWidgets

### 5. Matrix Representations
- **Adjacency Matrix**: Direct connections between stations
- **Incidence Matrix**: Station-edge relationships

### 6. Visualization
- Network graph with stations and connections
- Abbreviated station names for clarity
- Color-coded train types
- Edge weights representing travel times

### 7. Robustness Analysis
- Simulate station or connection failures
- Measure impact on network connectivity
- Identify critical infrastructure points

## Dependencies

All Python dependencies are listed in `requirements.txt`:

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **networkx**: Graph theory and network analysis
- **matplotlib**: Data visualization
- **ipywidgets**: Interactive widgets for Jupyter
- **IPython**: Enhanced interactive Python shell

## Analysis Results

The notebook generates various outputs including:

### Metrics
- Number of stations: 25
- Number of connections: 25 bidirectional routes
- Network connectivity status
- Critical stations and connections

### Visualizations
- Network topology diagram
- Shortest path visualizations
- Centrality heatmaps
- Adjacency matrix displays

### Insights
- Most connected stations (hubs)
- Optimal routes between cities
- Network vulnerability points
- Travel time optimizations

## Technical Details

### Graph Representation
- **Type**: Undirected weighted graph
- **Weight**: Travel time in minutes (primary metric)
- **Additional Attributes**: Distance (km), train type, frequency

### Algorithms Used
- **Dijkstra's Algorithm**: O(E log V) for single-source shortest path
- **Floyd-Warshall**: O(V³) for all-pairs shortest paths
- **Centrality Calculations**: Various NetworkX implementations

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**:
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt`

2. **Jupyter Kernel Issues**:
   - Install ipykernel: `pip install ipykernel`
   - Register kernel: `python -m ipykernel install --user --name=railway_env`

3. **Visualization Not Displaying**:
   - Ensure matplotlib backend is configured
   - For inline plots in Jupyter: `%matplotlib inline`

4. **CSV File Not Found**:
   - Verify `projet_reseau_maroc.csv` is in the same directory
   - Check file path in notebook

## Future Enhancements

Potential improvements and extensions:

- 🔄 **Real-time Data Integration**: Connect to live railway APIs
- 📊 **Advanced Analytics**: Machine learning for demand prediction
- 🗺️ **Geographic Visualization**: Interactive maps with station locations
- ⚡ **Performance Optimization**: Handle larger networks efficiently
- 📱 **Web Interface**: Deploy as an interactive web application
- 🔍 **Capacity Analysis**: Include passenger volume data

## Contributing

Contributions are welcome! Areas for improvement:

- Additional network analysis algorithms
- Enhanced visualizations
- Performance optimizations
- Documentation improvements
- New features and metrics

## License

This project is for educational and research purposes.

## Acknowledgments

- **Data Source**: Moroccan Railway Network (ONCF)
- **Graph Theory**: NetworkX library and community
- **Inspiration**: Graph theory applications in transportation networks

## Contact

For questions, issues, or suggestions, please create an issue in the project repository.

---

**Note**: This project is intended for educational and analytical purposes. Railway network data may not reflect real-time conditions or recent infrastructure changes.
