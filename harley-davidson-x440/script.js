document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('active'); });
    }, { threshold: 0.15 });
    document.querySelectorAll('.appear, .appear-l, .appear-r').forEach(el => observer.observe(el));
    setTimeout(() => { document.querySelectorAll('.hero .appear, .hero .appear-l, .hero .appear-r').forEach(el => el.classList.add('active')); }, 100);
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 10;
        const moto = document.querySelector('.hero-moto');
        if (moto) moto.style.transform = `translateY(${y}px) translateX(${x * 0.2}px)`;
    });
});
