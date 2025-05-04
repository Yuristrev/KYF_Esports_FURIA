document.addEventListener('DOMContentLoaded', function () {
    const menuIcon = document.getElementById('menu-icon');
    const body = document.body;

    menuIcon.addEventListener('click', function () {
        body.classList.toggle('menu-open');
    });
});
