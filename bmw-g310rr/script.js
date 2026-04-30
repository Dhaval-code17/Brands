document.addEventListener('DOMContentLoaded', () => {
    // Scroll reveal
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add('active');
        });
    }, { threshold: 0.15 });
    document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale').forEach(el => observer.observe(el));

    // Hero immediate reveal
    setTimeout(() => {
        document.querySelectorAll('.hero .reveal, .hero .reveal-left, .hero .reveal-right').forEach(el => el.classList.add('active'));
    }, 100);

    // Parallax on mouse
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 30;
        const y = (e.clientY / window.innerHeight - 0.5) * 15;
        const bike = document.querySelector('.hero-bike');
        if (bike) bike.style.transform = `translateY(${y}px) translateX(${x * 0.3}px)`;
    });

    // Navbar scroll effect
    window.addEventListener('scroll', () => {
        const nav = document.querySelector('.navbar');
        if (window.scrollY > 50) nav.style.padding = '1rem 5%';
        else nav.style.padding = '1.5rem 5%';
    });

    // Stat number counter animation
    const statNums = document.querySelectorAll('.stat-num');
    const statObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = el.textContent;
                const num = parseFloat(target);
                if (!isNaN(num)) {
                    let start = 0;
                    const step = num / 50;
                    const timer = setInterval(() => {
                        start += step;
                        if (start >= num) { el.textContent = target; clearInterval(timer); }
                        else el.textContent = Math.floor(start) + (target.includes('cc') ? 'cc' : target.includes('kg') ? 'kg' : '');
                    }, 30);
                }
                statObserver.unobserve(el);
            }
        });
    }, { threshold: 0.5 });
    statNums.forEach(el => statObserver.observe(el));
});
