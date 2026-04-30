document.addEventListener('DOMContentLoaded', () => {
    // Intersection Observer for bouncy animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll('.pop-in').forEach(el => observer.observe(el));
    
    // Initial hero load
    setTimeout(() => {
        document.querySelectorAll('#hero .pop-in').forEach(el => {
            el.classList.add('active');
        });
    }, 100);
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
