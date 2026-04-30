document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('active'); });
    }, { threshold: 0.12 });
    document.querySelectorAll('.drop-in, .rise').forEach(el => observer.observe(el));
    setTimeout(() => { document.querySelectorAll('.hero .drop-in, .hero .rise').forEach(el => el.classList.add('active')); }, 100);
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 10;
        const img = document.querySelector('.hayabusa-img');
        if (img) img.style.transform = `translateY(${y}px) translateX(${x * 0.2}px)`;
        document.querySelectorAll('.ring').forEach((ring, i) => {
            ring.style.transform = `rotate(${x * (i + 1) * 0.5}deg)`;
        });
    });
});
