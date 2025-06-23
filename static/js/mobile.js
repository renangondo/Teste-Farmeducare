document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.querySelector(".sidebar");
  const overlay = document.querySelector(".overlay");
  const mobileBtn = document.querySelector(".mobile-menu-btn");

  if (!sidebar || !overlay || !mobileBtn) {
    console.error("Elementos essenciais não encontrados");
    return;
  }

  function toggleMenu() {
    sidebar.classList.toggle("active");
    overlay.classList.toggle("active");
    document.body.style.overflow = sidebar.classList.contains("active")
      ? "hidden"
      : "";
  }

  mobileBtn.addEventListener("click", toggleMenu);
  overlay.addEventListener("click", toggleMenu);

  document.querySelectorAll(".menu-item a").forEach((item) => {
    item.addEventListener("click", function () {
      if (window.innerWidth <= 992) {
        toggleMenu();
      }
    });
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth > 992) {
      sidebar.classList.remove("active");
      overlay.classList.remove("active");
      document.body.style.overflow = "";
    }
  });
});
