# .github/workflows/cat_animation.py
import os
from datetime import datetime

# ✅ Ensure folder exists
os.makedirs("assets", exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400">
  <rect width="100%" height="100%" fill="#0a0a0a"/>
  
  <!-- Ground -->
  <rect y="320" width="800" height="80" fill="#333"/>

  <!-- 🐱 Cat -->
  <text x="50" y="300" font-size="60">
    🐈
    <animateTransform attributeName="transform"
                      type="translate"
                      values="0,0; 600,0; 0,0"
                      dur="10s"
                      repeatCount="indefinite"/>
  </text>

  <!-- 🧶 Wool Ball -->
  <circle cx="120" cy="310" r="15" fill="pink">
    <animateTransform attributeName="transform"
                      type="translate"
                      values="0,0; 600,0; 0,0"
                      dur="10s"
                      begin="0.5s"
                      repeatCount="indefinite"/>
    <animateTransform attributeName="transform"
                      additive="sum"
                      type="rotate"
                      from="0 120 310" to="360 120 310"
                      dur="1s"
                      repeatCount="indefinite"/>
  </circle>

  <text x="20" y="50" fill="white" font-size="22">
    🐾 Meow (last updated {timestamp})
    <animate attributeName="opacity"
             values="1;0.7;1"
             dur="3s"
             repeatCount="indefinite"/>
  </text>
</svg>
"""

with open("assets/cat.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("✅ Animated cat and wool ball SVG generated successfully!")
