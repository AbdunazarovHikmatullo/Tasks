const aside = document.querySelector("aside");
const asideTrigger = document.getElementById("aside-trigger");
const showCreateModalBtn = document.getElementById("showCreateListModal");
const modalContainer = document.getElementById("createListModal");

// --- Управление ASIDE ---
asideTrigger.addEventListener("click", () => {
    const isMobile = window.innerWidth <= 720;
    if (isMobile) {
        aside.classList.toggle("active-mobile");
    } else {
        aside.classList.toggle("hidden-aside");
    }
});

// --- Управление МОДАЛКОЙ ---
// Открыть
showCreateModalBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    modalContainer.style.display = 'flex';
});

// Закрыть при клике по фону (используем твой .modal как оверлей)
window.addEventListener("click", (e) => {
    if (e.target === modalContainer) {
        modalContainer.style.display = 'none';
    }
});

// Закрыть по кнопке ESC
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalContainer.style.display === 'flex') {
        modalContainer.style.display = 'none';
    }
});