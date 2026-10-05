// Native disclosure remains usable when JavaScript is unavailable.
const menu = document.querySelector('.mobile-menu');
if (menu) {
    const trigger = menu.querySelector('summary');
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && menu.open) {
            menu.open = false;
            trigger.focus();
        }
    });
    document.addEventListener('click', (event) => {
        if (!menu.contains(event.target)) menu.open = false;
        else if (event.target.closest('a')) menu.open = false;
    });
    window.addEventListener('pageshow', () => { menu.open = false; });
    window.matchMedia('(min-width: 641px)').addEventListener('change', (event) => {
        if (event.matches) menu.open = false;
    });
}
