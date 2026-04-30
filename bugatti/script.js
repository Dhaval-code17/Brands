document.addEventListener('DOMContentLoaded', () => {
    // Initial animations
    setTimeout(() => {
        document.querySelectorAll('#hero .fade-in').forEach(el => {
            el.classList.add('active');
        });
    }, 200);

    // Scroll animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.3 });

    document.querySelectorAll('.reveal-up').forEach(el => observer.observe(el));

    // Horizontal Scroll Logic for Desktop
    const horizSection = document.querySelector('.horizontal-scroll-section');
    const horizContainer = document.querySelector('.horizontal-container');
    
    if (window.innerWidth > 768) {
        window.addEventListener('scroll', () => {
            const rect = horizSection.getBoundingClientRect();
            if (rect.top <= 0 && rect.bottom >= window.innerHeight) {
                // Section is taking up the whole screen, trigger horizontal move
                // Note: Real horizontal scrolling usually requires GSAP or sticky wrappers.
                // We'll use a simpler translate based on scroll depth inside the section.
                const scrolled = -rect.top; 
                const maxScroll = horizSection.offsetHeight - window.innerHeight;
                const percent = scrolled / maxScroll;
                horizContainer.style.transform = `translateX(-${percent * 75}vw)`;
            }
        });
        
        // Make the section taller to allow scrolling
        horizSection.style.height = "400vh";
        horizContainer.style.position = "sticky";
        horizContainer.style.top = "15vh";
    }
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
