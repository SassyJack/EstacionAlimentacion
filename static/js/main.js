// Scripts globales del proyecto

document.addEventListener('DOMContentLoaded', function() {
    // Inicialización de componentes comunes
    console.log('Data Warehouse Project inicializado');

    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    const handleScroll = () => {
        if (!navbar) return;
        if (window.scrollY > 24) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    };

    handleScroll();
    window.addEventListener('scroll', handleScroll, { passive: true });

    navLinks.forEach(link => {
        link.addEventListener('mouseenter', () => link.classList.add('hover'));
        link.addEventListener('mouseleave', () => link.classList.remove('hover'));
    });

    // Aquí puedes agregar funcionalidades JavaScript adicionales
});
