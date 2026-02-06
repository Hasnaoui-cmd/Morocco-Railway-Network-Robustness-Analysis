import sys
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Python path: {sys.path}")

try:
    import networkx as nx
    print(f"\n✓ networkx imported successfully! Version: {nx.__version__}")
except ImportError as e:
    print(f"\n✗ networkx import failed: {e}")

try:
    import matplotlib.pyplot as plt
    print(f"✓ matplotlib imported successfully!")
except ImportError as e:
    print(f"✗ matplotlib import failed: {e}")
