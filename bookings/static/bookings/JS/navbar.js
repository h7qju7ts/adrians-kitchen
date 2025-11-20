const menuBtn = document.getElementById("nav-toggle");
const sideMenu = document.getElementById("side-menu");
const closeBtn = document.getElementById("close-menu");

menuBtn.addEventListener("click", () => {
    sideMenu.classList.add("open");
});

closeBtn.addEventListener("click", () => {
    sideMenu.classList.remove("open");
});

document.addEventListener("click", (e) => {
    if (!sideMenu.contains(e.target) && e.target !== menuBtn) {
        sideMenu.classList.remove("open");
    }
});