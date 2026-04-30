import os
import glob

base_dir = r"c:\Users\Dhaval\OneDrive\Desktop\websites"
folders_with_images = ["apple", "ferrari", "gucci", "tesla"]

for folder in folders_with_images:
    assets_dir = os.path.join(base_dir, folder, "assets")
    png_files = glob.glob(os.path.join(assets_dir, "ChatGPT*.png"))
    
    if len(png_files) >= 2:
        png_files.sort()
        hero_path = os.path.join(assets_dir, "hero.png")
        product_path = os.path.join(assets_dir, "product1.png")
        
        if os.path.exists(hero_path): os.remove(hero_path)
        if os.path.exists(product_path): os.remove(product_path)
        
        os.rename(png_files[0], hero_path)
        os.rename(png_files[1], product_path)
        
        # Update HTML to point to the new PNGs
        html_path = os.path.join(base_dir, folder, "index.html")
        if os.path.exists(html_path):
            with open(html_path, "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace("hero.svg", "hero.png").replace("product1.svg", "product1.png")
            content = content.replace("hero.jpg", "hero.png").replace("product1.jpg", "product1.png")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(content)

print("Images linked correctly!")
