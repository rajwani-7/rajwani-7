# scripts/cat_animation.py
import math
from datetime import datetime

frame = f"""
<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="black"/>
  <circle cx="{100 + 50 * math.sin(datetime.now().second)}" cy="200" r="20" fill="orange" />
  <circle cx="{100 + 50 * math.sin(datetime.now().second + 2)}" cy="220" r="10" fill="pink" />
  <text x="50" y="50" fill="white" font-size="24">🐱 Cat chasing wool 🧶</text>
</svg>
"""

with open("assets/cat.svg", "w") as f:
    f.write(frame)
