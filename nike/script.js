document.addEventListener('DOMContentLoaded', () => {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.fade-up, .slide-in, .slide-in-right, .slide-in-left, .reveal');
    animatedElements.forEach(el => observer.observe(el));
    
    // Initial hero animation
    setTimeout(() => {
        document.querySelectorAll('#hero .fade-up').forEach(el => {
            el.classList.add('active');
        });
    }, 100);

    // Glitch effect on scroll for header
    const glitchText = document.querySelector('.glitch');
    window.addEventListener('scroll', () => {
        const scroll = window.scrollY;
        if(scroll > 50 && scroll < 300) {
            glitchText.style.transform = `skewX(${Math.random() * 10 - 5}deg)`;
            glitchText.style.textShadow = `${Math.random() * 10}px 0 0 rgba(255,0,0,0.5), -${Math.random() * 10}px 0 0 rgba(0,255,255,0.5)`;
        } else {
            glitchText.style.transform = 'none';
            glitchText.style.textShadow = 'none';
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
