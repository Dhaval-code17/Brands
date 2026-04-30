document.addEventListener('DOMContentLoaded', () => {
    // Start hero bg subtle zoom
    const heroImg = document.getElementById('hero-img');
    if(heroImg) {
        setTimeout(() => {
            heroImg.style.transform = 'scale(1)';
        }, 100);
    }

    // Scroll Animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.2, rootMargin: '0px 0px -50px 0px' });

    document.querySelectorAll('.fade-in-up, .slide-in-left, .slide-in-right').forEach(el => observer.observe(el));
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
