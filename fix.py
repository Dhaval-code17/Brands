import os

missing_images = [
    (r'c:\Users\Dhaval\OneDrive\Desktop\websites\skechers\assets', 'product1.jpg'),
    (r'c:\Users\Dhaval\OneDrive\Desktop\websites\patek-philippe\assets', 'product1.jpg'),
    (r'c:\Users\Dhaval\OneDrive\Desktop\websites\omega\assets', 'hero.jpg'),
    (r'c:\Users\Dhaval\OneDrive\Desktop\websites\omega\assets', 'product1.jpg'),
    (r'c:\Users\Dhaval\OneDrive\Desktop\websites\cartier\assets', 'hero.jpg'),
    (r'c:\Users\Dhaval\OneDrive\Desktop\websites\cartier\assets', 'product1.jpg')
]
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800" viewBox="0 0 800 800">
  <rect width="800" height="800" fill="#222" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="#fff" font-size="30" font-family="sans-serif">Image Generation Limit Reached</text>
</svg>"""

for dir_path, filename in missing_images:
    svg_filename = filename.replace('.jpg', '.svg')
    with open(os.path.join(dir_path, svg_filename), 'w') as f:
        f.write(svg_content)
    
    # Update HTML
    html_path = os.path.join(os.path.dirname(dir_path), 'index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(f'assets/{filename}', f'assets/{svg_filename}')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
print("Placeholders generated and HTML updated.")
