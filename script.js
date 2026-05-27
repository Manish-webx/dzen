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

  /* ---------- Drag to Scroll Functionality ---------- */
  function makeDraggable(slider) {
    if (!slider) return;
    var isDown = false;
    var isDragging = false;
    var startX;
    var scrollLeft;

    var originalScrollBehavior;
    var originalScrollSnap;

    // Prevent default drag behavior on images to allow our custom drag
    slider.querySelectorAll('img').forEach(function(img) {
      img.addEventListener('dragstart', function(e) { e.preventDefault(); });
    });

    function disableSnapAndSmooth() {
      originalScrollBehavior = getComputedStyle(slider).scrollBehavior;
      originalScrollSnap = getComputedStyle(slider).scrollSnapType;
      slider.style.scrollBehavior = 'auto';
      slider.style.scrollSnapType = 'none';
    }

    function enableSnapAndSmooth() {
      slider.style.scrollBehavior = originalScrollBehavior || '';
      slider.style.scrollSnapType = originalScrollSnap || '';
      // Also remove inline styles if they are empty
      if (slider.style.scrollBehavior === '') slider.style.removeProperty('scroll-behavior');
      if (slider.style.scrollSnapType === '') slider.style.removeProperty('scroll-snap-type');
    }

    slider.addEventListener('mousedown', function(e) {
      isDown = true;
      isDragging = false;
      slider.style.cursor = 'grabbing';
      disableSnapAndSmooth();
      startX = e.pageX - slider.offsetLeft;
      scrollLeft = slider.scrollLeft;
    });
    slider.addEventListener('mouseleave', function() {
      if (!isDown) return;
      isDown = false;
      slider.style.cursor = '';
      enableSnapAndSmooth();
    });
    slider.addEventListener('mouseup', function() {
      if (!isDown) return;
      isDown = false;
      slider.style.cursor = '';
      enableSnapAndSmooth();
      // Delay resetting isDragging so the click event is caught
      setTimeout(function() { isDragging = false; }, 50);
    });
    slider.addEventListener('mousemove', function(e) {
      if (!isDown) return;
      e.preventDefault();
      var x = e.pageX - slider.offsetLeft;
      var walk = (x - startX) * 1.5;
      if (Math.abs(walk) > 5) {
        isDragging = true;
      }
      slider.scrollLeft = scrollLeft - walk;
    });

    slider.addEventListener('touchstart', function(e) {
      isDown = true;
      isDragging = false;
      disableSnapAndSmooth();
      startX = e.touches[0].pageX - slider.offsetLeft;
      scrollLeft = slider.scrollLeft;
    }, {passive: true});
    slider.addEventListener('touchend', function() {
      if (!isDown) return;
      isDown = false;
      enableSnapAndSmooth();
      setTimeout(function() { isDragging = false; }, 50);
    });
    slider.addEventListener('touchmove', function(e) {
      if (!isDown) return;
      var x = e.touches[0].pageX - slider.offsetLeft;
      var walk = (x - startX) * 1.5;
      if (Math.abs(walk) > 5) {
        isDragging = true;
      }
      slider.scrollLeft = scrollLeft - walk;
    }, {passive: true});

    slider.addEventListener('click', function(e) {
      if (isDragging) {
        e.preventDefault();
        e.stopPropagation();
      }
    }, true);
  }

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
    makeDraggable(treatmentsTrack);
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
    makeDraggable(testimonialsTrack);
  }

  /* ---------- Philosophy Wheel Interaction ---------- */
  var wheelNodes = document.querySelectorAll('.wheel-node');
  var philosophyPanes = document.querySelectorAll('.philosophy-pane');

  if (wheelNodes.length > 0 && philosophyPanes.length > 0) {
    function activateNode(nodeId) {
      // Deactivate all nodes and panes
      wheelNodes.forEach(function(n) {
        n.classList.remove('active');
      });
      philosophyPanes.forEach(function(p) {
        p.classList.remove('active');
      });

      // Activate target node and pane
      var targetNode = document.querySelector('.wheel-node[data-node="' + nodeId + '"]');
      var targetPane = document.getElementById('pane-' + nodeId);

      if (targetNode) targetNode.classList.add('active');
      if (targetPane) targetPane.classList.add('active');
    }

    wheelNodes.forEach(function(node) {
      node.addEventListener('mouseenter', function() {
        var nodeId = this.getAttribute('data-node');
        activateNode(nodeId);
      });
      
      node.addEventListener('click', function() {
        var nodeId = this.getAttribute('data-node');
        activateNode(nodeId);
      });
    });
  }

  /* ---------- Signature Editorial Accordion ---------- */
  var sigItems = document.querySelectorAll('.sig-accordion-item');
  var sigImages = document.querySelectorAll('.sig-showcase-img');

  if (sigItems.length > 0 && sigImages.length > 0) {
    sigItems.forEach(function(item) {
      item.addEventListener('mouseenter', function() {
        // Remove active class from all items and images
        sigItems.forEach(function(i) { i.classList.remove('active'); });
        sigImages.forEach(function(img) { img.classList.remove('active'); });

        // Add active class to hovered item
        this.classList.add('active');
        
        // Find corresponding image and activate it
        var targetId = this.getAttribute('data-sig-target');
        var targetImg = document.querySelector('.sig-showcase-img[data-sig-img="' + targetId + '"]');
        if (targetImg) {
          targetImg.classList.add('active');
        }
      });
    });
  }

  /* ---------- Press Collage & Lightbox ---------- */
  var pressTiles = $$('.press-tile');
  var lightbox = document.getElementById('pressLightbox');
  var lightboxImg = document.getElementById('pressLightboxImg');
  var lightboxCaption = document.getElementById('pressLightboxCaption');
  var lightboxClose = document.getElementById('pressLightboxClose');

  if (pressTiles.length > 0 && lightbox && lightboxImg && lightboxCaption) {
    pressTiles.forEach(function(tile) {
      tile.addEventListener('click', function() {
        var imgEl = this.querySelector('img');
        if (!imgEl) return;
        var imgSrc = imgEl.getAttribute('src');
        var captionText = this.getAttribute('data-caption') || '';
        
        lightboxImg.setAttribute('src', imgSrc);
        lightboxImg.setAttribute('alt', imgEl.getAttribute('alt') || '');
        lightboxCaption.textContent = captionText;
        
        lightbox.setAttribute('aria-hidden', 'false');
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
      });
    });

    var closeLightbox = function() {
      lightbox.setAttribute('aria-hidden', 'true');
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
      setTimeout(function() {
        lightboxImg.setAttribute('src', '');
        lightboxCaption.textContent = '';
      }, 300);
    };

    if (lightboxClose) {
      lightboxClose.addEventListener('click', closeLightbox);
    }

    lightbox.addEventListener('click', function(e) {
      if (e.target === lightbox || e.target.classList.contains('press-lightbox-content')) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && lightbox.classList.contains('active')) {
        closeLightbox();
      }
    });
  }

  /* ---------- Quick Actions Toggle ---------- */
  var quickActionsToggle = document.getElementById('quickActionsToggle');
  var quickActionsMenu = document.getElementById('quickActionsMenu');

  if (quickActionsToggle && quickActionsMenu) {
    quickActionsToggle.addEventListener('click', function() {
      var isActive = quickActionsMenu.classList.toggle('active');
      quickActionsToggle.classList.toggle('active', isActive);
    });

    // Close when clicking outside
    document.addEventListener('click', function(e) {
      if (!quickActionsToggle.contains(e.target) && !quickActionsMenu.contains(e.target)) {
        quickActionsMenu.classList.remove('active');
        quickActionsToggle.classList.remove('active');
      }
    });
  }

})();

// ==========================================
// Molecule 3D Animation (Supports Multiple)
// ==========================================
(function () {
    const svgs = document.querySelectorAll('.mol-svg');
    if (!svgs.length) return;

    // Icosahedron vertices (golden-ratio based)
    const phi = (1 + Math.sqrt(5)) / 2;
    const V = [
        [0, 1, phi], [0, -1, phi],
        [0, 1, -phi], [0, -1, -phi],
        [1, phi, 0], [-1, phi, 0],
        [1, -phi, 0], [-1, -phi, 0],
        [phi, 0, 1], [-phi, 0, 1],
        [phi, 0, -1], [-phi, 0, -1],
    ];

    const E = [];
    for (let i = 0; i < V.length; i++) {
        for (let j = i + 1; j < V.length; j++) {
            const dx = V[i][0] - V[j][0], dy = V[i][1] - V[j][1], dz = V[i][2] - V[j][2];
            const d2 = dx * dx + dy * dy + dz * dz;
            if (Math.abs(d2 - 4) < 0.01) E.push([i, j]);
        }
    }

    const NS = 'http://www.w3.org/2000/svg';
    const RADIUS = 110;
    const PERSPECTIVE = 5;

    const instances = Array.from(svgs).map(svg => {
        let nodesG = svg.querySelector('#mol-nodes');
        let edgesG = svg.querySelector('#mol-edges');
        
        if (!nodesG) { nodesG = document.createElementNS(NS, 'g'); nodesG.id = 'mol-nodes'; svg.appendChild(nodesG); }
        if (!edgesG) { edgesG = document.createElementNS(NS, 'g'); edgesG.id = 'mol-edges'; edgesG.setAttribute('stroke', 'rgba(217,164,65,0.3)'); svg.insertBefore(edgesG, nodesG); }

        const nodeEls = V.map(() => {
            const c = document.createElementNS(NS, 'circle');
            c.setAttribute('r', '0');
            c.setAttribute('fill', 'url(#molNode)');
            nodesG.appendChild(c);
            return c;
        });
        const edgeEls = E.map(() => {
            const l = document.createElementNS(NS, 'line');
            edgesG.appendChild(l);
            return l;
        });

        const halo = document.createElementNS(NS, 'circle');
        halo.setAttribute('cx', '0');
        halo.setAttribute('cy', '0');
        halo.setAttribute('r', '110');
        halo.setAttribute('fill', 'rgba(255, 220, 150, 0.10)');
        halo.setAttribute('filter', 'url(#molGlow)');
        svg.insertBefore(halo, edgesG);

        return {
            svg,
            nodeEls,
            edgeEls,
            ax: 0.4 + Math.random(),
            ay: Math.random() * Math.PI * 2
        };
    });

    let lastT = performance.now();

    function project(p) {
        const f = PERSPECTIVE / (PERSPECTIVE + p[2]);
        return {
            x: p[0] * RADIUS * f / phi,
            y: p[1] * RADIUS * f / phi,
            d: (p[2] + phi) / (2 * phi),
            f
        };
    }

    function rotate(p, ay, ax) {
        let [x, y, z] = p;
        let cy = Math.cos(ay), sy = Math.sin(ay);
        let x1 = x * cy + z * sy;
        let z1 = -x * sy + z * cy;
        let cx = Math.cos(ax), sx = Math.sin(ax);
        let y1 = y * cx - z1 * sx;
        let z2 = y * sx + z1 * cx;
        return [x1, y1, z2];
    }

    function tick(t) {
        const dt = Math.min(80, t - lastT) / 1000;
        lastT = t;

        instances.forEach(inst => {
            inst.ay += dt * 0.32;
            inst.ax += dt * 0.06;

            const axEff = inst.ax + Math.sin(t / 4000) * 0.08;
            const projected = V.map(p => project(rotate(p, inst.ay, axEff)));

            projected.forEach((p, i) => {
                const r = 4.2 + p.d * 4.8;
                const op = 0.45 + p.d * 0.55;
                const el = inst.nodeEls[i];
                el.setAttribute('cx', p.x.toFixed(2));
                el.setAttribute('cy', p.y.toFixed(2));
                el.setAttribute('r', r.toFixed(2));
                el.setAttribute('opacity', op.toFixed(2));
            });

            E.forEach(([a, b], i) => {
                const pa = projected[a], pb = projected[b];
                const op = (0.18 + Math.min(pa.d, pb.d) * 0.65);
                const sw = 0.6 + Math.min(pa.d, pb.d) * 1.4;
                const el = inst.edgeEls[i];
                el.setAttribute('x1', pa.x.toFixed(2));
                el.setAttribute('y1', pa.y.toFixed(2));
                el.setAttribute('x2', pb.x.toFixed(2));
                el.setAttribute('y2', pb.y.toFixed(2));
                el.setAttribute('opacity', op.toFixed(2));
                el.setAttribute('stroke-width', sw.toFixed(2));
            });
        });

        requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
})();

// ==========================================
// Lenis Smooth Scroll Initialization
// ==========================================
if (typeof Lenis !== 'undefined') {
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), 
    direction: 'vertical',
    gestureDirection: 'vertical',
    smooth: true,
    mouseMultiplier: 1,
    smoothTouch: false,
    touchMultiplier: 2,
    infinite: false,
  });

  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }

  requestAnimationFrame(raf);
}