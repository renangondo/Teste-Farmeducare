// admin_section.js - Funcionalidades para a seção de administração

document.addEventListener("DOMContentLoaded", function () {
  // Verifica se o usuário é superuser
  const isSuperuser = document.body.querySelector(".admin-section") !== null;
  if (!isSuperuser) return;

  // Configuração da seção admin
  function initAdminSection() {
    const adminSection = document.querySelector(".admin-section");
    const adminToggle = document.querySelector(".admin-toggle");

    if (!adminSection || !adminToggle) return;

    // Estado inicial (oculto)
    let isVisible = false;
    adminSection.style.display = "none";

    // Alternar visibilidade da seção admin
    function toggleAdminSection() {
      isVisible = !isVisible;

      if (isVisible) {
        adminSection.style.display = "block";
        adminToggle.innerHTML =
          '<i class="fas fa-eye-slash"></i> Ocultar Admin';
      } else {
        adminSection.style.display = "none";
        adminToggle.innerHTML = '<i class="fas fa-cogs"></i> Área Admin';
      }
    }

    // Event listener para o botão de toggle
    adminToggle.addEventListener("click", toggleAdminSection);

    // Tecla "A" + Ctrl abre/fecha a seção admin
    document.addEventListener("keydown", function (e) {
      if (e.ctrlKey && e.key === "a") {
        e.preventDefault();
        toggleAdminSection();
      }

      // Tecla ESC fecha a seção
      if (e.key === "Escape" && isVisible) {
        toggleAdminSection();
      }
    });
  }

  // Inicializa a seção admin
  initAdminSection();
});
