document.addEventListener("DOMContentLoaded", () => {
  
    // Handle the redirection for the Home Page link
    const homePageLink = document.getElementById('homePageLink');
    if (homePageLink) {
      const homePageUrl = homePageLink.getAttribute('data-url');
      
      homePageLink.addEventListener('click', () => {
        window.location.href = homePageUrl;  // Redirects to the home page using the URL from the data attribute
      });
    }
  
    // Sidebar item click handling
    const sidebarItems = document.querySelectorAll(".sidebar li");
    const sections = document.querySelectorAll(".section");
  
    sidebarItems.forEach(item => {
      item.addEventListener("click", () => {
        // Remove 'active' from all sidebar items and hide all sections
        sidebarItems.forEach(i => i.classList.remove("active"));
        sections.forEach(section => section.classList.remove("active"));
  
        // Add 'active' to clicked sidebar item
        item.classList.add("active");
  
        // Show the corresponding section
        const targetId = item.getAttribute("data-target");
        const targetSection = document.getElementById(targetId);
        if (targetSection) {
          targetSection.classList.add("active");
        }
      });
    });
  
  });
  