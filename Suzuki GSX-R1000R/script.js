document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('active'); });
    }, { threshold: 0.15 });
    document.querySelectorAll('.slide-up, .fade-up, .fade-left').forEach(el => observer.observe(el));
    setTimeout(() => { document.querySelectorAll('.hero .slide-up').forEach(el => el.classList.add('active')); }, 100);
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 25;
        const y = (e.clientY / window.innerHeight - 0.5) * 12;
        const bike = document.querySelector('.hero-bike');
        if (bike) bike.style.transform = `translateY(${y}px) rotate(${x * 0.05}deg)`;
    });
    window.addEventListener('scroll', () => {
        const nav = document.querySelector('.navbar');
        if (window.scrollY > 50) nav.style.borderBottomWidth = '3px';
        else nav.style.borderBottomWidth = '2px';
    });
});
