# .github/workflows/cat_animation.py

import math
import os
from datetime import datetime

# ✅ Create folder if not exists
os.makedirs("assets", exist_ok=True)

second = datetime.now().second
cat_x = 100 + 40 * math.sin(second)
ball_x = 100 + 60 * math.sin(second + 1)

svg_content = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400">
  <rect width="100%" height="100%" fill="black"/>
  <text x="{cat_x+20}" y="250" font-size="60">🐱</text>
  <circle cx="{ball_x+150}" cy="270" r="12" fill="pink"/>
  <text x="20" y="50" fill="white" font-size="22">🐾 Cat chasing wool ball 🧶</text>
</svg>
"""

with open("assets/cat.svg", "w") as f:
    f.write(svg_content)

print("✅ Cat animation SVG generated successfully!")
