import os

base_dir = r"c:\Users\Dhaval\OneDrive\Desktop\websites"
brands = ["apple", "ferrari", "gucci", "tesla", "red-bull", "porsche", "under-armour", "louis-vuitton", "sony", "vans"]

svg_hero = """<svg width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#333333;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#111111;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" />
  <text x="50%" y="50%" font-family="Arial" font-size="40" fill="#666666" text-anchor="middle" dominant-baseline="middle">HERO IMAGE PLACEHOLDER</text>
  <text x="50%" y="58%" font-family="Arial" font-size="20" fill="#555555" text-anchor="middle" dominant-baseline="middle">(Replace with your own image)</text>
</svg>"""

svg_product = """<svg width="800" height="800" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#222222;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#000000;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad2)" />
  <text x="50%" y="50%" font-family="Arial" font-size="30" fill="#666666" text-anchor="middle" dominant-baseline="middle">PRODUCT IMAGE PLACEHOLDER</text>
</svg>"""

for brand in brands:
    assets_dir = os.path.join(base_dir, brand, "assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    with open(os.path.join(assets_dir, "hero.svg"), "w", encoding="utf-8") as f:
        f.write(svg_hero)
        
    with open(os.path.join(assets_dir, "product1.svg"), "w", encoding="utf-8") as f:
        f.write(svg_product)
        
    # Update HTML to point to SVG
    html_path = os.path.join(base_dir, brand, "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        content = content.replace("hero.jpg", "hero.svg")
        content = content.replace("product1.jpg", "product1.svg")
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Placeholders created and HTML updated!")
