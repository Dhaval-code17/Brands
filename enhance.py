import os

base_dir = r"c:\Users\Dhaval\OneDrive\Desktop\websites"
# Running on the new 10 brands
brands = ["apple", "ferrari", "gucci", "tesla", "red-bull", "porsche", "under-armour", "louis-vuitton", "sony", "vans"]

newsletter_html = """
        <section id="newsletter" class="newsletter-section" style="padding: 100px 5%; text-align: center; border-top: 1px solid rgba(128,128,128,0.2);">
            <div class="container reveal-up" style="max-width: 600px; margin: 0 auto;">
                <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">JOIN THE EXCLUSIVE</h2>
                <p style="margin-bottom: 2rem; opacity: 0.8;">Subscribe to receive updates, access to exclusive deals, and more.</p>
                <form style="display: flex; gap: 1rem; justify-content: center;">
                    <input type="email" placeholder="Enter your email" style="padding: 1rem; flex: 1; border: 1px solid #ccc; background: transparent; color: inherit;">
                    <button type="submit" style="padding: 1rem 2rem; background: #333; color: #fff; border: none; cursor: pointer; text-transform: uppercase; font-weight: bold;">Subscribe</button>
                </form>
            </div>
        </section>
"""

parallax_js = """
    // Mouse Parallax Effect
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 20;
        const heroImg = document.querySelector('.hero-img, .hero-img-box img, .hero-img-container img, .content img, .neon-frame img, .polaroid img, .grid-item img');
        if (heroImg) {
            heroImg.style.transform = `translate(${x}px, ${y}px) scale(1.05)`;
        }
    });
"""

for brand in brands:
    html_path = os.path.join(base_dir, brand, "index.html")
    js_path = os.path.join(base_dir, brand, "script.js")
    
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if '<section id="newsletter"' not in content:
            content = content.replace("</main>", newsletter_html + "\n    </main>")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(content)
                
    if os.path.exists(js_path):
        with open(js_path, "r", encoding="utf-8") as f:
            js_content = f.read()
            
        if 'Mouse Parallax Effect' not in js_content:
            with open(js_path, "a", encoding="utf-8") as f:
                f.write("\n" + parallax_js)

print("Enhancements applied to the new 10 websites!")
