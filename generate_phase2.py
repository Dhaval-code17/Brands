import os

base_dir = r"c:\Users\Dhaval\OneDrive\Desktop\websites"

data = {
    "tesla": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tesla</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="navbar">
        <div class="logo">TESLA</div>
        <nav><a href="#">Vehicles</a><a href="#">Energy</a><a href="#">Charging</a></nav>
    </header>
    <main>
        <section class="hero snap-section">
            <h1 class="fade-in">CYBERTRUCK</h1>
            <p class="fade-in delay-1">Better utility than a truck with more performance than a sports car.</p>
            <div class="hero-img-box fade-in delay-2"><img src="assets/hero.jpg" alt="Tesla Hero"></div>
            <div class="cta-btns fade-in delay-3"><a href="#" class="btn-solid">ORDER NOW</a></div>
        </section>
        <section class="tech snap-section">
            <div class="tech-card fade-in">
                <h2>AUTOPILOT</h2>
                <p>Future of driving.</p>
                <img src="assets/product1.jpg" alt="Tesla Interior">
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>""",
        "styles.css": """:root { --bg: #000; --text: #fff; --accent: #e82127; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Montserrat', sans-serif; background: var(--bg); color: var(--text); overflow-x: hidden; scroll-snap-type: y mandatory; }
.navbar { position: fixed; width: 100%; top: 0; padding: 1.5rem 5%; display: flex; justify-content: space-between; z-index: 100; background: rgba(0,0,0,0.5); backdrop-filter: blur(10px); }
.logo { font-weight: 700; letter-spacing: 5px; }
nav a { color: var(--text); text-decoration: none; margin-left: 2rem; font-size: 0.9rem; font-weight: 500; }
.snap-section { height: 100vh; scroll-snap-align: start; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; position: relative; padding-top: 80px; }
.hero h1 { font-size: 5rem; letter-spacing: 10px; margin-bottom: 1rem; }
.hero p { font-size: 1.2rem; color: #ccc; margin-bottom: 2rem; }
.hero-img-box { width: 80%; max-width: 1000px; }
.hero-img-box img { width: 100%; border-radius: 10px; }
.btn-solid { padding: 1rem 3rem; background: var(--text); color: var(--bg); text-decoration: none; font-weight: 700; border-radius: 4px; display: inline-block; margin-top: 2rem; }
.tech-card { text-align: center; }
.tech-card h2 { font-size: 3rem; margin-bottom: 1rem; }
.tech-card img { width: 100%; max-width: 800px; margin-top: 2rem; border-radius: 10px; }
.fade-in { opacity: 0; transform: translateY(30px); transition: all 1s ease; }
.fade-in.active { opacity: 1; transform: translateY(0); }
.delay-1 { transition-delay: 0.2s; }
.delay-2 { transition-delay: 0.4s; }
.delay-3 { transition-delay: 0.6s; }""",
        "script.js": """document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('active'); });
    }, { threshold: 0.5 });
    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
    setTimeout(() => { document.querySelectorAll('.hero .fade-in').forEach(el => el.classList.add('active')); }, 100);
});"""
    },
    "red-bull": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Red Bull</title>
    <link href="https://fonts.googleapis.com/css2?family=Anton&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="navbar"><div class="logo">RED BULL</div></header>
    <main>
        <section class="action-hero">
            <h1 class="zoom-in">GIVES YOU WINGS</h1>
            <div class="dynamic-grid">
                <div class="grid-item item-main zoom-in delay-1"><img src="assets/hero.jpg" alt="Action"></div>
                <div class="grid-item item-sub zoom-in delay-2"><img src="assets/product1.jpg" alt="Can"></div>
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>""",
        "styles.css": """:root { --rb-blue: #001A35; --rb-silver: #C0C0C0; --rb-red: #DB0A40; --rb-yellow: #FFC200; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Roboto', sans-serif; background: var(--rb-blue); color: white; overflow-x: hidden; }
h1, .logo { font-family: 'Anton', sans-serif; }
.navbar { padding: 1.5rem 5%; background: var(--rb-blue); position: sticky; top: 0; z-index: 100; border-bottom: 2px solid var(--rb-red); }
.logo { font-size: 2.5rem; color: var(--rb-red); text-shadow: 2px 2px 0 var(--rb-yellow); }
.action-hero { padding: 50px 5%; text-align: center; }
.action-hero h1 { font-size: 6rem; color: white; text-shadow: 4px 4px 0 var(--rb-red); margin-bottom: 2rem; transform: skewX(-10deg); }
.dynamic-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 20px; max-width: 1200px; margin: 0 auto; }
.grid-item img { width: 100%; height: 100%; object-fit: cover; border: 5px solid var(--rb-silver); transform: skewX(-5deg); transition: transform 0.3s; }
.grid-item img:hover { transform: skewX(-5deg) scale(1.05); }
.zoom-in { opacity: 0; transform: scale(0.8); transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.zoom-in.active { opacity: 1; transform: scale(1); }
.delay-1 { transition-delay: 0.2s; }
.delay-2 { transition-delay: 0.4s; }
@media(max-width:768px) { .dynamic-grid { grid-template-columns: 1fr; } .action-hero h1 { font-size: 3rem; } }""",
        "script.js": """document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => { document.querySelectorAll('.zoom-in').forEach(el => el.classList.add('active')); }, 100);
});"""
    },
    "porsche": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Porsche</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="navbar"><div class="logo">PORSCHE</div></header>
    <main>
        <section class="hero">
            <h1 class="fade-up">THERE IS NO SUBSTITUTE.</h1>
            <div class="hero-img-container fade-up delay-1"><img src="assets/hero.jpg" alt="Porsche"></div>
        </section>
        <section class="performance">
            <div class="perf-grid">
                <div class="perf-text fade-up">
                    <h2>PRECISION</h2>
                    <p>Over 70 years of engineering perfection. The soul of a sports car.</p>
                </div>
                <div class="perf-img fade-up delay-1"><img src="assets/product1.jpg" alt="Tachometer"></div>
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>""",
        "styles.css": """:root { --dark: #191919; --light: #f1f1f1; --red: #d5001c; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Inter', sans-serif; background: var(--dark); color: var(--light); }
.navbar { padding: 2rem 5%; text-align: center; }
.logo { font-weight: 600; font-size: 1.5rem; letter-spacing: 8px; }
.hero { text-align: center; padding: 100px 5%; }
.hero h1 { font-size: 3rem; font-weight: 300; letter-spacing: 2px; margin-bottom: 3rem; }
.hero-img-container img { width: 100%; max-width: 1000px; filter: grayscale(100%) contrast(1.2); transition: filter 0.5s; }
.hero-img-container img:hover { filter: grayscale(0%); }
.performance { padding: 100px 5%; background: #222; }
.perf-grid { display: flex; max-width: 1200px; margin: 0 auto; gap: 4rem; align-items: center; }
.perf-text, .perf-img { flex: 1; }
.perf-text h2 { font-size: 2.5rem; color: var(--red); margin-bottom: 1rem; }
.perf-img img { width: 100%; border: 1px solid #444; }
.fade-up { opacity: 0; transform: translateY(30px); transition: all 1s ease; }
.fade-up.active { opacity: 1; transform: translateY(0); }
.delay-1 { transition-delay: 0.3s; }
@media(max-width:768px) { .perf-grid { flex-direction: column; } }""",
        "script.js": """document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => { entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('active'); }); });
    document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));
    setTimeout(() => { document.querySelectorAll('.hero .fade-up').forEach(el => el.classList.add('active')); }, 100);
});"""
    },
    "under-armour": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Under Armour</title>
    <link href="https://fonts.googleapis.com/css2?family=Teko:wght@600&family=Oswald:wght@500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="navbar"><div class="logo">UNDER ARMOUR</div></header>
    <main>
        <section class="gritty-hero">
            <h1 class="smash-in">THE ONLY WAY IS THROUGH</h1>
            <div class="hero-img-box smash-in delay-1"><img src="assets/hero.jpg" alt="Training"></div>
        </section>
        <section class="gear">
            <div class="gear-content smash-in">
                <h2>PROJECT ROCK</h2>
                <img src="assets/product1.jpg" alt="Shoe">
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>""",
        "styles.css": """:root { --dark-grey: #1a1a1a; --ua-red: #cc0000; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Oswald', sans-serif; background: var(--dark-grey); color: white; text-transform: uppercase; }
h1, h2, .logo { font-family: 'Teko', sans-serif; }
.navbar { padding: 1.5rem 5%; background: #000; border-bottom: 2px solid var(--ua-red); }
.logo { font-size: 2rem; letter-spacing: 2px; }
.gritty-hero { text-align: center; padding: 100px 5%; background: radial-gradient(circle, #333 0%, #111 100%); }
.gritty-hero h1 { font-size: 6rem; line-height: 1; margin-bottom: 2rem; text-shadow: 3px 3px 0 var(--ua-red); }
.hero-img-box img { width: 100%; max-width: 900px; filter: contrast(1.2) brightness(0.9); border: 4px solid #333; }
.gear { padding: 100px 5%; text-align: center; }
.gear h2 { font-size: 4rem; color: var(--ua-red); margin-bottom: 2rem; }
.gear img { width: 100%; max-width: 600px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); }
.smash-in { opacity: 0; transform: scale(1.2); transition: all 0.5s font-weight; }
.smash-in.active { opacity: 1; transform: scale(1); }
.delay-1 { transition-delay: 0.2s; }
@media(max-width:768px) { .gritty-hero h1 { font-size: 4rem; } }""",
        "script.js": """document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => { entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('active'); }); });
    document.querySelectorAll('.smash-in').forEach(el => observer.observe(el));
    setTimeout(() => { document.querySelectorAll('.gritty-hero .smash-in').forEach(el => el.classList.add('active')); }, 100);
});"""
    },
    "louis-vuitton": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Louis Vuitton</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Montserrat:wght@300;400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="navbar"><div class="logo">LOUIS VUITTON</div></header>
    <main>
        <section class="heritage-hero">
            <div class="monogram-bg"></div>
            <div class="content fade">
                <h1>THE SPIRIT OF TRAVEL</h1>
                <img src="assets/hero.jpg" alt="LV Trunk">
            </div>
        </section>
        <section class="craftsmanship">
            <div class="craft-grid">
                <div class="text fade">
                    <h2>ART OF TRUNKMAKING</h2>
                    <p>Since 1854, Louis Vuitton has brought unique designs to the world, combining innovation with style.</p>
                </div>
                <div class="img fade delay-1"><img src="assets/product1.jpg" alt="Leather"></div>
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>""",
        "styles.css": """:root { --lv-brown: #3e2e23; --lv-gold: #cfa861; --lv-light: #f4efea; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Montserrat', sans-serif; background: var(--lv-light); color: var(--lv-brown); }
h1, h2, .logo { font-family: 'Cormorant Garamond', serif; }
.navbar { padding: 2rem; text-align: center; border-bottom: 1px solid rgba(62,46,35,0.2); }
.logo { font-size: 2rem; letter-spacing: 6px; }
.heritage-hero { position: relative; padding: 100px 5%; text-align: center; overflow: hidden; }
.monogram-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.05; background: repeating-linear-gradient(45deg, var(--lv-brown), var(--lv-brown) 10px, transparent 10px, transparent 20px); z-index: -1; }
.content h1 { font-size: 3rem; letter-spacing: 4px; margin-bottom: 3rem; color: var(--lv-gold); }
.content img { width: 100%; max-width: 800px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
.craftsmanship { padding: 100px 5%; background: var(--lv-brown); color: var(--lv-light); }
.craft-grid { display: flex; max-width: 1200px; margin: 0 auto; gap: 4rem; align-items: center; }
.craft-grid .text, .craft-grid .img { flex: 1; }
.text h2 { font-size: 2.5rem; color: var(--lv-gold); margin-bottom: 1rem; }
.text p { font-size: 1.1rem; line-height: 1.8; }
.img img { width: 100%; border: 1px solid var(--lv-gold); }
.fade { opacity: 0; transform: translateY(20px); transition: all 1.5s ease; }
.fade.active { opacity: 1; transform: translateY(0); }
.delay-1 { transition-delay: 0.4s; }
@media(max-width:768px) { .craft-grid { flex-direction: column; } }""",
        "script.js": """document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => { entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('active'); }); }, {threshold: 0.2});
    document.querySelectorAll('.fade').forEach(el => observer.observe(el));
    setTimeout(() => { document.querySelectorAll('.heritage-hero .fade').forEach(el => el.classList.add('active')); }, 100);
});"""
    },
    "sony": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sony</title>
    <link href="https://fonts.googleapis.com/css2?family=Saira:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="navbar"><div class="logo">SONY</div></header>
    <main>
        <section class="tech-hero">
            <h1 class="glow-in">CREATIVITY OUT OF THE BOX</h1>
            <div class="neon-frame glow-in delay-1"><img src="assets/hero.jpg" alt="Sony Tech"></div>
        </section>
        <section class="alpha-cam">
            <div class="alpha-content glow-in">
                <h2>ALPHA VISION</h2>
                <img src="assets/product1.jpg" alt="Camera Lens">
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>""",
        "styles.css": """:root { --bg: #050505; --text: #fff; --neon-blue: #00f3ff; --neon-pink: #ff00ea; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Saira', sans-serif; background: var(--bg); color: var(--text); }
.navbar { padding: 1.5rem 5%; background: #000; border-bottom: 1px solid #222; }
.logo { font-size: 2rem; font-weight: 600; letter-spacing: 4px; }
.tech-hero { padding: 100px 5%; text-align: center; }
.tech-hero h1 { font-size: 4rem; margin-bottom: 3rem; text-shadow: 0 0 10px var(--neon-blue); }
.neon-frame { display: inline-block; padding: 10px; background: linear-gradient(45deg, var(--neon-blue), var(--neon-pink)); border-radius: 10px; }
.neon-frame img { width: 100%; max-width: 800px; display: block; border-radius: 5px; }
.alpha-cam { padding: 100px 5%; text-align: center; background: #0a0a0a; }
.alpha-cam h2 { font-size: 3rem; color: var(--neon-pink); margin-bottom: 2rem; }
.alpha-cam img { width: 100%; max-width: 600px; border-radius: 50%; box-shadow: 0 0 30px rgba(0,243,255,0.2); }
.glow-in { opacity: 0; filter: blur(10px); transition: all 1s ease; }
.glow-in.active { opacity: 1; filter: blur(0); }
.delay-1 { transition-delay: 0.3s; }
@media(max-width:768px) { .tech-hero h1 { font-size: 2.5rem; } }""",
        "script.js": """document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => { entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('active'); }); });
    document.querySelectorAll('.glow-in').forEach(el => observer.observe(el));
    setTimeout(() => { document.querySelectorAll('.tech-hero .glow-in').forEach(el => el.classList.add('active')); }, 100);
});"""
    },
    "vans": {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vans</title>
    <link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&family=Work+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="navbar"><div class="logo">VANS</div></header>
    <main>
        <section class="skate-hero">
            <h1 class="pop">OFF THE WALL</h1>
            <div class="polaroid pop delay-1"><img src="assets/hero.jpg" alt="Skater"></div>
        </section>
        <section class="classics">
            <div class="checker-bg"></div>
            <div class="classics-content pop">
                <h2>THE CLASSIC SLIP-ON</h2>
                <img src="assets/product1.jpg" alt="Vans Shoe" class="shoe-img">
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>""",
        "styles.css": """:root { --red: #c8102e; --black: #000; --white: #fff; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Work Sans', sans-serif; background: var(--white); color: var(--black); }
h1, h2 { font-family: 'Permanent Marker', cursive; }
.navbar { padding: 1.5rem 5%; background: var(--red); color: white; text-align: center; }
.logo { font-size: 2.5rem; font-family: 'Permanent Marker', cursive; }
.skate-hero { padding: 100px 5%; text-align: center; background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"><circle cx="2" cy="2" r="1" fill="%23ccc"/></svg>'); }
.skate-hero h1 { font-size: 5rem; transform: rotate(-5deg); margin-bottom: 3rem; color: var(--red); text-shadow: 2px 2px 0 var(--black); }
.polaroid { background: white; padding: 15px 15px 50px 15px; display: inline-block; box-shadow: 5px 5px 15px rgba(0,0,0,0.3); transform: rotate(3deg); }
.polaroid img { width: 100%; max-width: 600px; }
.classics { position: relative; padding: 100px 5%; text-align: center; overflow: hidden; }
.checker-bg { position: absolute; top:0; left:0; width:100%; height:100%; background: repeating-conic-gradient(#000 0% 25%, #fff 0% 50%) 50% / 40px 40px; opacity: 0.1; z-index: -1; }
.classics h2 { font-size: 3rem; background: var(--black); color: white; display: inline-block; padding: 10px 20px; transform: rotate(-2deg); margin-bottom: 2rem; }
.shoe-img { width: 100%; max-width: 500px; filter: drop-shadow(10px 10px 0px var(--red)); }
.pop { opacity: 0; transform: scale(0.5) rotate(-10deg); transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.pop.active { opacity: 1; transform: scale(1) rotate(0); }
.skate-hero h1.active { transform: scale(1) rotate(-5deg); }
.polaroid.active { transform: scale(1) rotate(3deg); }
.classics h2.active { transform: scale(1) rotate(-2deg); }
.delay-1 { transition-delay: 0.2s; }
@media(max-width:768px) { .skate-hero h1 { font-size: 3rem; } }""",
        "script.js": """document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => { entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('active'); }); });
    document.querySelectorAll('.pop').forEach(el => observer.observe(el));
    setTimeout(() => { document.querySelectorAll('.skate-hero .pop').forEach(el => el.classList.add('active')); }, 100);
});"""
    }
}

for brand, files in data.items():
    brand_dir = os.path.join(base_dir, brand)
    os.makedirs(brand_dir, exist_ok=True)
    os.makedirs(os.path.join(brand_dir, "assets"), exist_ok=True)
    for filename, content in files.items():
        with open(os.path.join(brand_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)

print("Generated remaining 7 websites successfully!")
