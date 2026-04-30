import os

brands = {
    "nike": {
        "title": "NIKE - Just Do It",
        "colors": {"primary": "#000000", "secondary": "#ff6600", "text": "#ffffff"},
        "font": "'Inter', sans-serif",
        "tagline": "Engineered for the Unstoppable.",
        "description": "Experience the next generation of athletic performance. Our latest innovation combines hyper-responsive cushioning with an impossibly lightweight upper.",
        "button": "Shop Collection",
        "story": "For decades, we have pushed the boundaries of human potential. This isn't just a shoe; it's a statement.",
        "theme_class": "neon-dark"
    },
    "puma": {
        "title": "PUMA - Forever Faster",
        "colors": {"primary": "#1a1a1a", "secondary": "#e60000", "text": "#ffffff"},
        "font": "'Roboto', sans-serif",
        "tagline": "Unleash Your Inner Beast.",
        "description": "Born on the track, built for the streets. Defy gravity with agility and explosive power.",
        "button": "Explore",
        "story": "Speed is in our DNA. We equip the fastest athletes on the planet. Now, it's your turn.",
        "theme_class": "slanted-action"
    },
    "adidas": {
        "title": "ADIDAS - Impossible is Nothing",
        "colors": {"primary": "#ffffff", "secondary": "#000000", "text": "#000000"},
        "font": "'Helvetica Neue', sans-serif",
        "tagline": "Three Stripes. Infinite Possibilities.",
        "description": "Minimalist design meets maximum comfort. Classic silhouettes re-engineered for tomorrow.",
        "button": "Discover",
        "story": "From the stadium to the streets, we unite creators. Join a legacy of champions.",
        "theme_class": "minimal-clean"
    },
    "skechers": {
        "title": "SKECHERS - Comfort That Performs",
        "colors": {"primary": "#0033a0", "secondary": "#ffd100", "text": "#ffffff"},
        "font": "'Outfit', sans-serif",
        "tagline": "Step Into Pure Comfort.",
        "description": "Why choose between style and comfort? Our memory foam technology adapts to your every move.",
        "button": "Find Your Fit",
        "story": "We believe everyone deserves to walk on clouds. Experience the comfort revolution.",
        "theme_class": "vibrant-playful"
    },
    "bugatti": {
        "title": "BUGATTI - Incomparable",
        "colors": {"primary": "#0a0a0a", "secondary": "#0055ff", "text": "#e0e0e0"},
        "font": "'Montserrat', sans-serif",
        "tagline": "Form Follows Performance.",
        "description": "A masterpiece of engineering. The pinnacle of automotive luxury and hyper-speed capability.",
        "button": "Configure",
        "story": "If it is comparable, it is no longer Bugatti. We craft rolling works of art for the uncompromising few.",
        "theme_class": "luxury-speed"
    },
    "titan": {
        "title": "TITAN - Crafted for the Moment",
        "colors": {"primary": "#1f2a44", "secondary": "#d4af37", "text": "#ffffff"},
        "font": "'Playfair Display', serif",
        "tagline": "Your Time. Your Legacy.",
        "description": "Precision engineering meets exquisite craftsmanship. A timepiece that tells more than just time.",
        "button": "View Collection",
        "story": "For over three decades, we have celebrated the spirit of those who dare to dream.",
        "theme_class": "elegant-classic"
    },
    "rolex": {
        "title": "ROLEX - The Crown of Achievement",
        "colors": {"primary": "#006039", "secondary": "#a37e2c", "text": "#ffffff"},
        "font": "'Georgia', serif",
        "tagline": "A Crown for Every Achievement.",
        "description": "The ultimate watch of prestige. Unparalleled reliability, born from a century of relentless innovation.",
        "button": "Discover Rolex",
        "story": "It doesn't just tell time. It tells history. Worn by visionaries, explorers, and leaders.",
        "theme_class": "sophisticated-gold"
    },
    "patek-philippe": {
        "title": "PATEK PHILIPPE - Begin Your Own Tradition",
        "colors": {"primary": "#f8f5f0", "secondary": "#5c4033", "text": "#333333"},
        "font": "'Cinzel', serif",
        "tagline": "For the Next Generation.",
        "description": "Masterpieces of horological complexity. Crafted by hand in Geneva, preserving centuries of tradition.",
        "button": "Explore Timepieces",
        "story": "You never actually own a Patek Philippe. You merely look after it for the next generation.",
        "theme_class": "heritage-sepia"
    },
    "omega": {
        "title": "OMEGA - Exact Time for Life",
        "colors": {"primary": "#002b5c", "secondary": "#c0c0c0", "text": "#ffffff"},
        "font": "'Futura', sans-serif",
        "tagline": "From the Ocean to the Moon.",
        "description": "Pioneering the depths of the sea and the vastness of space. Precision that defies limits.",
        "button": "Explore the Universe",
        "story": "Our legacy is defined by those who push boundaries. The choice of astronauts and deep-sea explorers.",
        "theme_class": "marine-space"
    },
    "cartier": {
        "title": "CARTIER - The Jeweler of Kings",
        "colors": {"primary": "#ffffff", "secondary": "#e3000f", "text": "#1a1a1a"},
        "font": "'Bodoni MT', serif",
        "tagline": "Elegance is an Attitude.",
        "description": "Iconic design characterized by perfect proportions. A harmonious blend of boldness and grace.",
        "button": "Discover the Maison",
        "story": "A story of passion, creativity, and exceptional savoir-faire. Transforming the ordinary into the precious.",
        "theme_class": "romantic-red"
    }
}

base_dir = r"c:\Users\Dhaval\OneDrive\Desktop\websites"

def generate_html(brand, data):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']}</title>
    <meta name="description" content="{data['description']}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;500;800&family=Playfair+Display:wght@400;700&family=Outfit:wght@400;700&family=Montserrat:wght@300;600&family=Cinzel:wght@400;700&family=Roboto:wght@400;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body class="{data['theme_class']}">
    <header>
        <div class="logo">{brand.upper()}</div>
        <nav>
            <a href="#discover">Discover</a>
            <a href="#story">Heritage</a>
            <a href="#collection">Collection</a>
        </nav>
    </header>

    <main>
        <section id="hero" class="hero-section">
            <div class="hero-content">
                <h1 class="reveal-text">{data['tagline']}</h1>
                <p class="fade-in">{data['description']}</p>
                <button class="cta-button slide-up">{data['button']}</button>
            </div>
            <div class="hero-image-container parallax">
                <img src="assets/hero.jpg" alt="{brand} hero product" class="hero-img" id="hero-img">
            </div>
        </section>

        <section id="story" class="story-section">
            <div class="story-container">
                <h2 class="slide-right">The Legacy</h2>
                <p class="slide-left">{data['story']}</p>
            </div>
        </section>

        <section id="collection" class="collection-section">
            <div class="product-showcase zoom-in">
                <img src="assets/product1.jpg" alt="{brand} product showcase" class="product-img" id="prod-img">
                <div class="product-info">
                    <h3>Iconic Design</h3>
                    <p>Experience the culmination of years of research and perfection.</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 {brand.upper()}. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

def generate_css(brand, data):
    return f''':root {{
    --primary: {data['colors']['primary']};
    --secondary: {data['colors']['secondary']};
    --text: {data['colors']['text']};
    --font-main: {data['font']};
}}

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: var(--font-main);
    background-color: var(--primary);
    color: var(--text);
    overflow-x: hidden;
}}

/* Header */
header {{
    position: fixed;
    top: 0;
    width: 100%;
    padding: 2rem 5%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
    mix-blend-mode: difference;
    color: white; /* Forced white for difference blend */
}}

.logo {{
    font-size: 1.5rem;
    font-weight: 800;
    letter-spacing: 2px;
}}

nav a {{
    color: inherit;
    text-decoration: none;
    margin-left: 2rem;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: opacity 0.3s ease;
}}

nav a:hover {{
    opacity: 0.6;
}}

/* Sections */
section {{
    min-height: 100vh;
    padding: 100px 5%;
    display: flex;
    align-items: center;
}}

/* Hero Section */
.hero-section {{
    position: relative;
    justify-content: space-between;
    overflow: hidden;
}}

.hero-content {{
    width: 45%;
    z-index: 2;
}}

h1 {{
    font-size: 4rem;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
}}

.hero-content p {{
    font-size: 1.2rem;
    line-height: 1.6;
    margin-bottom: 2rem;
    opacity: 0.8;
}}

.cta-button {{
    padding: 1rem 2.5rem;
    background-color: var(--secondary);
    color: var(--primary);
    border: none;
    font-size: 1rem;
    font-family: inherit;
    font-weight: 600;
    cursor: pointer;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: transform 0.3s ease, background-color 0.3s ease;
}}

.cta-button:hover {{
    transform: translateY(-5px);
    filter: brightness(1.2);
}}

.hero-image-container {{
    position: absolute;
    top: 50%;
    right: -5%;
    transform: translateY(-50%);
    width: 60%;
    height: 80vh;
    z-index: 1;
}}

.hero-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 20px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
}}

/* Story Section */
.story-section {{
    background-color: var(--secondary);
    color: var(--primary);
    justify-content: center;
    text-align: center;
}}

.story-container {{
    max-width: 800px;
}}

.story-container h2 {{
    font-size: 3rem;
    margin-bottom: 2rem;
}}

.story-container p {{
    font-size: 1.5rem;
    line-height: 1.8;
}}

/* Collection Section */
.collection-section {{
    justify-content: center;
}}

.product-showcase {{
    display: flex;
    align-items: center;
    gap: 4rem;
    background: rgba(255,255,255,0.05);
    padding: 4rem;
    border-radius: 30px;
    backdrop-filter: blur(10px);
}}

.product-img {{
    width: 400px;
    height: 400px;
    object-fit: cover;
    border-radius: 50%;
}}

.product-info h3 {{
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: var(--secondary);
}}

/* Animations */
.reveal-text, .fade-in, .slide-up, .slide-right, .slide-left, .zoom-in {{
    opacity: 0;
    transition: all 1s cubic-bezier(0.16, 1, 0.3, 1);
}}

.reveal-text.active {{ opacity: 1; transform: translateY(0); }}
.reveal-text {{ transform: translateY(50px); }}

.fade-in.active {{ opacity: 1; }}

.slide-up.active {{ opacity: 1; transform: translateY(0); }}
.slide-up {{ transform: translateY(30px); }}

.slide-right.active {{ opacity: 1; transform: translateX(0); }}
.slide-right {{ transform: translateX(-50px); }}

.slide-left.active {{ opacity: 1; transform: translateX(0); }}
.slide-left {{ transform: translateX(50px); }}

.zoom-in.active {{ opacity: 1; transform: scale(1); }}
.zoom-in {{ transform: scale(0.9); }}

/* Thematic Overrides */
.neon-dark .cta-button {{ background: transparent; border: 2px solid var(--secondary); color: var(--secondary); box-shadow: 0 0 15px var(--secondary); }}
.slanted-action section {{ transform: skewY(-3deg); margin-top: -50px; padding: 150px 5%; }}
.slanted-action section > * {{ transform: skewY(3deg); }}
.minimal-clean .hero-img {{ border-radius: 0; box-shadow: none; filter: grayscale(100%); }}
.minimal-clean .hero-img:hover {{ filter: grayscale(0%); transition: filter 1s ease; }}
.luxury-speed .hero-img {{ width: 80%; right: -10%; }}
.elegant-classic .product-showcase {{ background: none; border: 1px solid var(--secondary); border-radius: 0; }}
.sophisticated-gold .cta-button {{ border-radius: 30px; }}
.heritage-sepia .hero-img {{ filter: sepia(0.5); }}
.romantic-red .hero-img {{ border-radius: 100px 100px 0 0; }}

footer {{
    text-align: center;
    padding: 2rem;
    background: #000;
    color: #fff;
}}

@media (max-width: 768px) {{
    .hero-section {{ flex-direction: column; }}
    .hero-content, .hero-image-container {{ width: 100%; position: relative; transform: none; top: 0; right: 0; height: auto; }}
    .hero-image-container {{ margin-top: 2rem; height: 50vh; }}
    .product-showcase {{ flex-direction: column; text-align: center; padding: 2rem; }}
    .product-img {{ width: 100%; height: auto; max-height: 300px; border-radius: 20px; }}
    h1 {{ font-size: 2.5rem; }}
}}
'''

def generate_js():
    return '''document.addEventListener('DOMContentLoaded', () => {
    // Parallax effect
    const heroImg = document.querySelector('.hero-img');
    window.addEventListener('scroll', () => {
        const scroll = window.pageYOffset;
        if(heroImg) {
            heroImg.style.transform = `translateY(${scroll * 0.3}px)`;
        }
    });

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.2,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.reveal-text, .fade-in, .slide-up, .slide-right, .slide-left, .zoom-in');
    animatedElements.forEach(el => observer.observe(el));
    
    // Initial hero animation
    setTimeout(() => {
        document.querySelectorAll('#hero .reveal-text, #hero .fade-in, #hero .slide-up').forEach(el => {
            el.classList.add('active');
        });
    }, 100);
});
'''

for brand, data in brands.items():
    brand_dir = os.path.join(base_dir, brand)
    
    # Write HTML
    with open(os.path.join(brand_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(generate_html(brand, data))
        
    # Write CSS
    with open(os.path.join(brand_dir, 'styles.css'), 'w', encoding='utf-8') as f:
        f.write(generate_css(brand, data))
        
    # Write JS
    with open(os.path.join(brand_dir, 'script.js'), 'w', encoding='utf-8') as f:
        f.write(generate_js())

print("All websites generated successfully!")
