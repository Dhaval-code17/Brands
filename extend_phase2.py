import os

base_dir = r"c:\Users\Dhaval\OneDrive\Desktop\websites"

extensions = {
    "apple": """
        <section class="grid-section" style="margin-top: 40px;">
            <div class="grid-card dark reveal-up">
                <h2>Battery Life.</h2>
                <p>All day battery life. Go further.</p>
            </div>
            <div class="grid-card light reveal-up delay-1">
                <h2>Camera.</h2>
                <p>Photonic engine. Unprecedented detail.</p>
            </div>
        </section>
        <section class="hero-section" style="min-height: 50vh;">
            <h2 class="reveal-up">Carbon Neutral by 2030.</h2>
            <p class="reveal-up delay-1">Innovation that protects the planet.</p>
        </section>
""",
    "ferrari": """
        <section class="heritage" style="background: #111; color: white;">
            <div class="heritage-grid">
                <div class="text-col reveal-left">
                    <h3 style="color: white;">AERODYNAMICS</h3>
                    <p>Carved by the wind. Every curve serves a purpose, generating maximum downforce for unparalleled cornering speeds.</p>
                </div>
                <div class="img-col reveal-right" style="border: 5px solid #ff2800; min-height: 300px; display:flex; align-items:center; justify-content:center; font-family:'Syncopate', sans-serif;">[AERO IMAGE]</div>
            </div>
        </section>
        <section style="padding: 100px 5%; text-align: center; background: #ff2800; color: white;">
            <h2 class="reveal-up" style="font-size: 3rem; font-family:'Syncopate', sans-serif;">THE V12 SYMPHONY</h2>
            <p class="reveal-up delay-1" style="font-size: 1.5rem; margin-top: 20px;">Pure naturally aspirated power.</p>
        </section>
""",
    "gucci": """
        <section class="archive-section" style="background: #fbf9f6;">
            <div class="archive-content">
                <h2 class="reveal-up">THE COLLECTION</h2>
                <div class="archive-grid" style="flex-direction: row-reverse;">
                    <div class="archive-text reveal-up delay-1">
                        <p>Contemporary luxury tailored for the modern era. Accessories that define the silhouette.</p>
                    </div>
                    <div class="archive-image reveal-up delay-2" style="background: #006400; height: 400px;"></div>
                </div>
            </div>
        </section>
        <section style="padding: 100px 5%; text-align: center; background: #8b0000; color: white;">
            <h2 class="reveal-up" style="font-family: 'Playfair Display', serif; font-size: 3rem; font-style: italic;">FIND A BOUTIQUE</h2>
        </section>
""",
    "tesla": """
        <section class="tech snap-section">
            <div class="tech-card fade-in">
                <h2>500 MILE RANGE</h2>
                <p>Go anywhere. Supercharging network included.</p>
            </div>
        </section>
        <section class="hero snap-section" style="background: #111;">
            <h2 class="fade-in">SOLAR ROOF</h2>
            <p class="fade-in delay-1">Power your home and your car.</p>
        </section>
""",
    "red-bull": """
        <section class="action-hero" style="background: #DB0A40;">
            <h2 class="zoom-in" style="font-size: 4rem;">F1 RACING TEAM</h2>
            <p class="zoom-in delay-1" style="font-size: 1.5rem; margin-top: 20px;">World Champions.</p>
        </section>
        <section class="action-hero" style="background: #FFC200; color: #001A35;">
            <h2 class="zoom-in" style="color: #001A35; text-shadow: none;">EVENTS & STUNTS</h2>
            <div class="dynamic-grid" style="margin-top: 40px;">
                <div class="grid-item" style="height: 300px; background: #001A35;"></div>
                <div class="grid-item" style="height: 300px; background: #001A35;"></div>
            </div>
        </section>
""",
    "porsche": """
        <section class="performance">
            <div class="perf-grid" style="flex-direction: row-reverse;">
                <div class="perf-text fade-up">
                    <h2 style="color: white;">E-PERFORMANCE</h2>
                    <p>The soul of a Porsche, electrified. Taycan redefines what an EV can be.</p>
                </div>
                <div class="perf-img fade-up delay-1" style="background: #444; height: 300px;"></div>
            </div>
        </section>
        <section class="hero" style="background: #f1f1f1; color: #191919;">
            <h2 class="fade-up" style="color: #d5001c;">MOTORSPORT HERITAGE</h2>
            <p class="fade-up delay-1" style="font-size: 1.2rem; margin-top: 20px;">Born in Flacht.</p>
        </section>
""",
    "under-armour": """
        <section class="gear" style="background: #111;">
            <div class="gear-content smash-in">
                <h2 style="color: white;">HOVR™ CUSHIONING</h2>
                <p style="font-size: 1.5rem;">Zero gravity feel. Energy return that keeps you running.</p>
            </div>
        </section>
        <section class="gritty-hero" style="min-height: 50vh;">
            <h2 class="smash-in" style="font-size: 5rem; text-shadow: 2px 2px 0 #cc0000;">TRAIN HARDER</h2>
        </section>
""",
    "louis-vuitton": """
        <section class="craftsmanship" style="background: var(--lv-light); color: var(--lv-brown);">
            <div class="craft-grid" style="flex-direction: row-reverse;">
                <div class="text fade">
                    <h2 style="color: var(--lv-brown);">HIGH WATCHMAKING</h2>
                    <p>Timepieces crafted in Geneva, featuring exceptional complications.</p>
                </div>
                <div class="img fade delay-1" style="background: var(--lv-brown); height: 400px;"></div>
            </div>
        </section>
        <section style="padding: 100px 5%; text-align: center; background: var(--lv-gold); color: white;">
            <h2 class="fade" style="font-family: 'Cormorant Garamond', serif; font-size: 3rem;">MEN'S & WOMEN'S COLLECTION</h2>
        </section>
""",
    "sony": """
        <section class="alpha-cam" style="background: #111;">
            <div class="alpha-content glow-in">
                <h2 style="color: var(--neon-blue);">PLAYSTATION 5</h2>
                <p style="font-size: 1.5rem; margin-bottom: 30px;">Play Has No Limits.</p>
                <div class="neon-frame"><div style="width: 600px; height: 300px; background: #000;"></div></div>
            </div>
        </section>
        <section class="tech-hero" style="min-height: 50vh;">
            <h2 class="glow-in" style="font-size: 3rem; text-shadow: 0 0 10px var(--neon-pink);">BRAVIA XR DISPLAY</h2>
        </section>
""",
    "vans": """
        <section class="classics" style="background: var(--red); color: white;">
            <div class="classics-content pop">
                <h2 style="background: white; color: var(--black);">CUSTOMS</h2>
                <p style="font-size: 1.5rem; margin-top: 20px; font-weight: bold;">Make your own shoes. Express yourself.</p>
            </div>
        </section>
        <section class="skate-hero" style="min-height: 50vh; background: var(--black);">
            <h2 class="pop" style="font-size: 4rem; color: white; transform: rotate(2deg);">PRO SKATE TEAM</h2>
        </section>
"""
}

for brand, html_addition in extensions.items():
    html_path = os.path.join(base_dir, brand, "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Insert before the newsletter section
        if '<section id="newsletter"' in content:
            content = content.replace('<section id="newsletter"', html_addition + '\n        <section id="newsletter"')
        else:
            content = content.replace("</main>", html_addition + "\n    </main>")
            
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Extended 10 websites with additional sections!")
