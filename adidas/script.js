document.addEventListener('DOMContentLoaded', () => {
    // Reveal text animation
    setTimeout(() => {
        document.querySelectorAll('.reveal-text').forEach(el => {
            el.classList.add('active');
        });
    }, 100);

    // Parallax stripes
    const stripesBg = document.querySelector('.three-stripes-bg');
    window.addEventListener('scroll', () => {
        const scroll = window.scrollY;
        if(stripesBg) {
            stripesBg.style.transform = `skewX(-20deg) scale(1.5) translateX(${scroll * 0.1}px)`;
        }
    });
});


    // Mouse Parallax Effect
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 20;
        const heroImg = document.querySelector('.hero-img, .cover-image img');
        if (heroImg) {
            heroImg.style.transform = `translate(${x}px, ${y}px) scale(1.05)`;
        }
    });
