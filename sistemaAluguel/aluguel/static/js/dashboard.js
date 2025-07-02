// Interação da sidebar para super usuario apenas
document.addEventListener('DOMContentLoaded', function () {
    const sidebarToggle = document.getElementById('sidebarToggle');
    const adminSidebar = document.getElementById('adminSidebar');
    const mainContainer = document.getElementById('mainContainer');

    if (sidebarToggle && adminSidebar) {
        sidebarToggle.addEventListener('click', function () {
            adminSidebar.classList.toggle('active');
            mainContainer.classList.toggle('sidebar-active');
        });
    }
});