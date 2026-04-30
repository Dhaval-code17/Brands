document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => { entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('active'); }); });
    document.querySelectorAll('.glow-in').forEach(el => observer.observe(el));
    setTimeout(() => { document.querySelectorAll('.tech-hero .glow-in').forEach(el => el.classList.add('active')); }, 100);
});

    // Mouse Parallax Effect
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 20;
        const heroImg = document.querySelector('.hero-img, .hero-img-box img, .hero-img-container img, .content img, .neon-frame img, .polaroid img, .grid-item img');
        if (heroImg) {
            heroImg.style.transform = `translate(${x}px, ${y}px) scale(1.05)`;
        }
    });
