document.addEventListener('DOMContentLoaded', () => {
    // Parallax elements
    const heroImg = document.querySelector('.hero-img');
    const redBlock = document.querySelector('.red-block');

    window.addEventListener('scroll', () => {
        const scroll = window.scrollY;
        if(heroImg && scroll < 800) {
            heroImg.style.transform = `rotate(-15deg) translateY(${scroll * -0.2}px)`;
            redBlock.style.transform = `skew(-20deg) translateY(${scroll * 0.1}px)`;
        }
    });

    // Intersection Observer for animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll('.stagger-in').forEach(el => observer.observe(el));
    
    setTimeout(() => {
        document.querySelectorAll('.stagger-in').forEach(el => {
            if(el.getBoundingClientRect().top < window.innerHeight) {
                el.classList.add('active');
            }
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
