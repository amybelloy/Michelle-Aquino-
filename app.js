document.addEventListener('DOMContentLoaded', () => {
    // Scroll Effect for Header
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Mobile Menu Logic
    const hamburgerBtn = document.getElementById('hamburger-btn');
    const closeMenuBtn = document.getElementById('close-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileOverlay = document.getElementById('mobile-overlay');

    if (hamburgerBtn && mobileMenu && mobileOverlay) {
        function openMenu() {
            mobileMenu.classList.add('is-open');
            mobileOverlay.classList.add('is-open');
            hamburgerBtn.classList.add('is-active');
            hamburgerBtn.setAttribute('aria-expanded', 'true');
            document.body.style.overflow = 'hidden';
        }

        function closeMenu() {
            mobileMenu.classList.remove('is-open');
            mobileOverlay.classList.remove('is-open');
            hamburgerBtn.classList.remove('is-active');
            hamburgerBtn.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        }

        hamburgerBtn.addEventListener('click', openMenu);
        
        if (closeMenuBtn) {
            closeMenuBtn.addEventListener('click', closeMenu);
        }
        
        mobileOverlay.addEventListener('click', closeMenu);

        // Close menu when any link is clicked
        const mobileLinks = document.querySelectorAll('.mobile-nav-list a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', closeMenu);
        });
    }

    // Intersection Observer for fade-in effects
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.section, .card, .step, .service-row').forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
});
