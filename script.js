/* =========================================================
   D'Zen Derma - JavaScript
   ========================================================= */

(function() {
  'use strict';

  var $ = document.querySelector.bind(document);
  var $$ = document.querySelectorAll.bind(document);

  /* ---------- Header & Scroll Vars ---------- */
  var header = document.getElementById('header') || document.querySelector('.header');
  var lastScroll = 0;

  /* ---------- Native Scroll Logic ---------- */
  window.addEventListener('scroll', function() {
    var scroll = window.scrollY;
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var pct = max > 0 ? (scroll / max) * 100 : 0;

    // Scroll Progress
    var bar = $('.scroll-progress span');
    if (bar) bar.style.width = pct + '%';

    // Header Hide on Scroll
    if (header) {
      if (scroll > lastScroll && scroll > 200) {
        header.classList.add('hidden');
      } else {
        header.classList.remove('hidden');
      }
    }
    lastScroll = scroll;
  });

  /* ---------- Smooth Anchor Links ---------- */
  $$('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;

      var target = $(targetId);
      if (target) {
        e.preventDefault();
        var offset = 80;
        var targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: targetPosition, behavior: 'smooth' });
      }
    });
  });

  /* ---------- Mobile Menu ---------- */
  var menuToggle = document.getElementById('menuToggle');
  var mobileMenu = document.getElementById('mobileMenu');

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', function() {
      var isOpen = menuToggle.classList.toggle('is-open');
      mobileMenu.classList.toggle('is-open', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    $$('.mobile-nav a').forEach(function(link) {
      link.addEventListener('click', function() {
        menuToggle.classList.remove('is-open');
        mobileMenu.classList.remove('is-open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ---------- FAQ Accordion ---------- */
  $$('.faq-item').forEach(function(item) {
    var question = item.querySelector('.faq-question');
    var answer = item.querySelector('.faq-answer');

    if (question && answer) {
      question.addEventListener('click', function() {
        var isOpen = item.classList.contains('is-open');

        // Close all
        $$('.faq-item').forEach(function(i) {
          i.classList.remove('is-open');
          var a = i.querySelector('.faq-answer');
          if (a) a.style.maxHeight = '0';
        });

        // Toggle current
        if (!isOpen) {
          item.classList.add('is-open');
          answer.style.maxHeight = answer.scrollHeight + 'px';
        }
      });
    }
  });

  /* ---------- Reveal on Scroll ---------- */
  var revealItems = $$('.reveal');

  if ('IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

    revealItems.forEach(function(el) {
      revealObserver.observe(el);
    });
  } else {
    revealItems.forEach(function(el) {
      el.classList.add('visible');
    });
  }

  /* ---------- GSAP Animations ---------- */
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    // Hero
    gsap.from('.hero-title', { opacity: 0, y: 60, duration: 1.2, delay: 0.4, ease: 'power3.out' });
    gsap.from('.hero-tagline', { opacity: 0, y: 40, duration: 1, delay: 0.7, ease: 'power3.out' });
    gsap.from('.hero-cta', { opacity: 0, y: 30, duration: 1, delay: 1, ease: 'power3.out' });

    // About
    gsap.from('.about-content', {
      scrollTrigger: { trigger: '.about', start: 'top 80%' },
      opacity: 0, x: -60, duration: 1, ease: 'power3.out'
    });
    gsap.from('.about-media', {
      scrollTrigger: { trigger: '.about', start: 'top 80%' },
      opacity: 0, x: 60, duration: 1, ease: 'power3.out'
    });

    // Treatment cards
    gsap.from('.treatment-item', {
      scrollTrigger: { trigger: '.treatment-grid', start: 'top 85%' },
      opacity: 0, y: 50, duration: 0.8, stagger: 0.1, ease: 'power3.out'
    });

    // Space
    gsap.from('.space-content', {
      scrollTrigger: { trigger: '.space', start: 'top 75%' },
      opacity: 0, x: 60, duration: 1, ease: 'power3.out'
    });

    // Concerns
    gsap.from('.concern-item', {
      scrollTrigger: { trigger: '.concerns-grid', start: 'top 85%' },
      opacity: 0, y: 40, duration: 0.6, stagger: 0.1, ease: 'power3.out'
    });

    // Programs
    gsap.from('.programs-left', {
      scrollTrigger: { trigger: '.programs', start: 'top 75%' },
      opacity: 0, x: -60, duration: 1, ease: 'power3.out'
    });
    gsap.from('.programs-right', {
      scrollTrigger: { trigger: '.programs', start: 'top 75%' },
      opacity: 0, x: 60, duration: 1, ease: 'power3.out'
    });

    // Founders
    gsap.from('.founders-image', {
      scrollTrigger: { trigger: '.founders', start: 'top 75%' },
      opacity: 0, x: -60, duration: 1, ease: 'power3.out'
    });
    gsap.from('.founders-content', {
      scrollTrigger: { trigger: '.founders', start: 'top 75%' },
      opacity: 0, x: 60, duration: 1, ease: 'power3.out'
    });

    // Journal
    gsap.from('.journal-item', {
      scrollTrigger: { trigger: '.journal-grid', start: 'top 85%' },
      opacity: 0, y: 50, duration: 0.8, stagger: 0.12, ease: 'power3.out'
    });

    // Book
    gsap.from('.book-left', {
      scrollTrigger: { trigger: '.book', start: 'top 75%' },
      opacity: 0, x: -60, duration: 1, ease: 'power3.out'
    });
    gsap.from('.book-right', {
      scrollTrigger: { trigger: '.book', start: 'top 75%' },
      opacity: 0, x: 60, duration: 1, ease: 'power3.out'
    });

    // Refresh ScrollTrigger on resize
    window.addEventListener('resize', function() {
      ScrollTrigger.refresh();
    });
  }

  /* ---------- Hover Effects on Cards ---------- */
  $$('.treatment-item, .journal-item').forEach(function(card) {
    var img = card.querySelector('.treatment-img, .journal-img');

    if (img) {
      card.addEventListener('mouseenter', function() {
        gsap.to(img, { scale: 1.04, duration: 0.6, ease: 'power2.out' });
      });
      card.addEventListener('mouseleave', function() {
        gsap.to(img, { scale: 1, duration: 0.4, ease: 'power2.out' });
      });
    }
  });

  /* ---------- About Us Accordion ---------- */
  $$('.about-accordion').forEach(function(accordion) {
    var header = accordion.querySelector('.accordion-header');
    var content = accordion.querySelector('.accordion-content');

    if (header && content) {
      header.addEventListener('click', function() {
        var isOpen = accordion.classList.contains('is-open');

        // Close all accordions
        $$('.about-accordion').forEach(function(acc) {
          acc.classList.remove('is-open');
          var c = acc.querySelector('.accordion-content');
          if (c) c.style.maxHeight = '0';
        });

        // Open clicked accordion if it was closed
        if (!isOpen) {
          accordion.classList.add('is-open');
          content.style.maxHeight = content.scrollHeight + 'px';
        }
      });
    }
  });

  /* ---------- About Us Section Animations ---------- */
  gsap.from('.about-us-subtitle', {
    scrollTrigger: { trigger: '.about-us', start: 'top 80%' },
    opacity: 0, y: 30, duration: 0.8, ease: 'power3.out'
  });
  gsap.from('.about-us-title', {
    scrollTrigger: { trigger: '.about-us', start: 'top 80%' },
    opacity: 0, y: 40, duration: 1, delay: 0.15, ease: 'power3.out'
  });
  gsap.from('.about-us-intro', {
    scrollTrigger: { trigger: '.about-us', start: 'top 80%' },
    opacity: 0, y: 30, duration: 0.8, delay: 0.3, ease: 'power3.out'
  });
  gsap.from('.about-us-divider', {
    scrollTrigger: { trigger: '.about-us', start: 'top 80%' },
    opacity: 0, scaleX: 0, duration: 0.8, delay: 0.4, ease: 'power3.out'
  });
  gsap.from('.about-paragraph', {
    scrollTrigger: { trigger: '.about-left-column', start: 'top 85%' },
    opacity: 0, y: 30, duration: 0.8, ease: 'power3.out'
  });
  gsap.from('.about-accordion', {
    scrollTrigger: { trigger: '.about-accordions', start: 'top 85%' },
    opacity: 0, y: 40, duration: 0.6, stagger: 0.15, ease: 'power3.out'
  });
  gsap.from('.about-image-container', {
    scrollTrigger: { trigger: '.about-image-container', start: 'top 85%' },
    opacity: 0, scale: 0.9, duration: 1, ease: 'power3.out'
  });
  gsap.from('.about-watermark', {
    scrollTrigger: { trigger: '.about-wave', start: 'top 90%' },
    opacity: 0, duration: 1.2, ease: 'power2.out'
  });

  /* ---------- Treatments Slider ---------- */
  var treatmentsTrack = document.querySelector('.treatments-track');
  var treatPrevBtn = document.querySelector('.treatments-nav .prev-btn');
  var treatNextBtn = document.querySelector('.treatments-nav .next-btn');

  if (treatmentsTrack && treatPrevBtn && treatNextBtn) {
    function updateNavButtons() {
      var scrollLeft = treatmentsTrack.scrollLeft;
      var maxScroll = treatmentsTrack.scrollWidth - treatmentsTrack.clientWidth;
      treatPrevBtn.disabled = scrollLeft <= 5;
      treatNextBtn.disabled = scrollLeft >= maxScroll - 5;
    }

    treatPrevBtn.addEventListener('click', function() {
      var card = treatmentsTrack.querySelector('.treatment-card');
      if (card) {
        var cardWidth = card.getBoundingClientRect().width;
        var gap = parseFloat(getComputedStyle(treatmentsTrack).gap) || 24;
        treatmentsTrack.scrollBy({
          left: -(cardWidth + gap) * 2,
          behavior: 'smooth'
        });
      }
    });

    treatNextBtn.addEventListener('click', function() {
      var card = treatmentsTrack.querySelector('.treatment-card');
      if (card) {
        var cardWidth = card.getBoundingClientRect().width;
        var gap = parseFloat(getComputedStyle(treatmentsTrack).gap) || 24;
        treatmentsTrack.scrollBy({
          left: (cardWidth + gap) * 2,
          behavior: 'smooth'
        });
      }
    });

    treatmentsTrack.addEventListener('scroll', updateNavButtons);
    window.addEventListener('resize', updateNavButtons);

    updateNavButtons();
  }

  /* ---------- Testimonials Slider ---------- */
  var testimonialsTrack = document.querySelector('.testimonials-track');
  var testPrevBtn = document.querySelector('.testimonials-slider .prev-btn');
  var testNextBtn = document.querySelector('.testimonials-slider .next-btn');

  if (testimonialsTrack && testPrevBtn && testNextBtn) {
    var scrollAmount = testimonialsTrack.offsetWidth / 3;

    testPrevBtn.addEventListener('click', function() {
      testimonialsTrack.scrollBy({
        left: -scrollAmount,
        behavior: 'smooth'
      });
    });

    testNextBtn.addEventListener('click', function() {
      testimonialsTrack.scrollBy({
        left: scrollAmount,
        behavior: 'smooth'
      });
    });
  }

})();