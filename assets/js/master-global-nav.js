/* =============================================================================
   TINITIATE MASTERCLASS ACADEMY - UNIFIED GLOBAL INTERACTIVITY
   Subjects Dropdown, In-Page Scrollspy, and Theme Synchronization
   ============================================================================= */

(function() {
  let dropdownTimeout = null;

  function adjustMegaMenuPosition() {
    const menu = document.querySelector('#subjectsDropdown .master-dropdown-menu');
    if (!menu) return;
    // reset first
    menu.style.transform = '';
    const rect = menu.getBoundingClientRect();
    if (rect.right > window.innerWidth - 16) {
      const overflow = rect.right - (window.innerWidth - 16);
      menu.style.transform = `translateX(-${overflow}px)`;
    } else if (rect.left < 16) {
      menu.style.transform = `translateX(${16 - rect.left}px)`;
    }
  }

  // 1. Dropdown Toggle Function
  window.toggleSubjectsDropdown = function(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    const dd = document.getElementById('subjectsDropdown');
    if (dd) {
      clearTimeout(dropdownTimeout);
      const willOpen = !dd.classList.contains('open');
      dd.classList.toggle('open');
      if (willOpen) {
        requestAnimationFrame(adjustMegaMenuPosition);
      }
    }
  };

  // Setup hover and click listeners once DOM is ready
  function initSubjectsDropdown() {
    const dd = document.getElementById('subjectsDropdown');
    if (!dd) return;

    dd.addEventListener('mouseenter', () => {
      clearTimeout(dropdownTimeout);
      dd.classList.add('open');
      requestAnimationFrame(adjustMegaMenuPosition);
    });

    dd.addEventListener('mouseleave', () => {
      dropdownTimeout = setTimeout(() => {
        dd.classList.remove('open');
      }, 350); // 350ms buffer so mouse never accidentally collapses menu
    });
  }

  // Close dropdown on outside click
  document.addEventListener('click', function(e) {
    const dd = document.getElementById('subjectsDropdown');
    if (dd && !dd.contains(e.target)) {
      dd.classList.remove('open');
    }
  });

  // 2. In-Page Scrollspy for Right Sidebar Navigation
  document.addEventListener('DOMContentLoaded', function() {
    initSubjectsDropdown();
    const inpageLinks = document.querySelectorAll('.sidebar-inpage-nav .inpage-link');
    if (inpageLinks.length === 0) return;

    const sections = [];
    inpageLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        const target = document.getElementById(href.substring(1));
        if (target) {
          sections.push({ id: href.substring(1), elem: target, link: link });
        }
      }
    });

    if (sections.length === 0) return;

    function onScrollSpy() {
      const scrollPos = window.scrollY + 120;
      let activeIndex = 0;
      for (let i = 0; i < sections.length; i++) {
        const top = sections[i].elem.getBoundingClientRect().top + window.scrollY;
        if (scrollPos >= top - 20) {
          activeIndex = i;
        }
      }

      sections.forEach((sec, idx) => {
        if (idx === activeIndex) {
          sec.link.classList.add('active');
        } else {
          sec.link.classList.remove('active');
        }
      });
    }

    window.addEventListener('scroll', onScrollSpy, { passive: true });
    onScrollSpy();

    // Re-init lucide icons if available
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }
  });
})();
