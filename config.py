import os

# API endpoint for fetching cat facts
URL_CAT_FACT = "https://catfact.ninja/fact"

# relative paths
dirname = os.path.dirname(__file__)

# List of available cat avatars
AVATARS = [
    os.path.join(dirname, "cat1.png"),
    os.path.join(dirname, "cat2.png"),
    os.path.join(dirname, "cat3.png"),
    os.path.join(dirname, "cat4.png"),
    os.path.join(dirname, "cat5.png"),
    os.path.join(dirname, "cat6.png"),
    os.path.join(dirname, "cat7.png"),
    os.path.join(dirname, "cat8.png"),
]

# Background color options for the app
BACKGROUND_COLORS = [
  "lightblue",  # Light blue
  "lightgrey",  # Light grey
  "lightgoldenrod", # Light goldenrod
  "pink", # Pink
]