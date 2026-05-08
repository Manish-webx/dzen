/* =========================================================
   D'Zen Derma — Homepage interactions
   ========================================================= */

(() => {
  const $  = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));

  /* ---------- Loader ---------- */
  const loader = $('#loader');
  window.addEventListener('load', () => {
    setTimeout(() => loader && loader.classList.add('is-done'), 1300);
  });

  /* ---------- Custom cursor ---------- */
  const cursor = $('#cursor');
  const cursorDot = $('#cursorDot');
  let cx = 0, cy = 0, tx = 0, ty = 0;

  if (matchMedia('(pointer:fine)').matches) {
    document.addEventListener('mousemove', (e) => {
      tx = e.clientX; ty = e.clientY;
      cursorDot.style.transform = `translate3d(${tx - 2}px, ${ty - 2}px, 0)`;
    });
    const tick = () => {
      cx += (tx - cx) * 0.16;
      cy += (ty - cy) * 0.16;
      cursor.style.transform = `translate3d(${cx - 18}px, ${cy - 18}px, 0)`;
      requestAnimationFrame(tick);
    };
    tick();

    const hoverables = 'a, button, .pillars-list li, .concern, .principle, .step, .founder, .spread, .post, .loc, .press li, .quote-dots button, input, select';
    document.addEventListener('mouseover', (e) => {
      if (e.target.closest(hoverables)) {
        cursor.classList.add('is-hover');
        const label = e.target.closest('a, .concern, .post, .founder, .spread, .loc');
        cursor.querySelector('span').textContent = label ? '↗' : '';
      }
    });
    document.addEventListener('mouseout', (e) => {
      if (e.target.closest(hoverables)) {
        cursor.classList.remove('is-hover');
        cursor.querySelector('span').textContent = '';
      }
    });
  }

  /* ---------- Header scroll state ---------- */
  const header = $('#header');
  let lastY = 0;
  const onScroll = () => {
    const y = window.scrollY;
    header.classList.toggle('is-scrolled', y > 30);
    if (y > 240 && y > lastY) header.classList.add('is-hidden');
    else header.classList.remove('is-hidden');
    lastY = y;

    const max = document.documentElement.scrollHeight - window.innerHeight;
    const pct = max > 0 ? (y / max) * 100 : 0;
    const bar = document.querySelector('#progress span');
    if (bar) bar.style.width = pct + '%';
  };
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- Mobile menu ---------- */
  const menuToggle = $('#menuToggle');
  const mobileMenu = $('#mobileMenu');
  menuToggle?.addEventListener('click', () => {
    const open = menuToggle.classList.toggle('is-open');
    menuToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    mobileMenu.classList.toggle('is-open', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });
  $$('.mobile-menu a').forEach(a => a.addEventListener('click', () => {
    menuToggle.classList.remove('is-open');
    menuToggle.setAttribute('aria-expanded', 'false');
    mobileMenu.classList.remove('is-open');
    document.body.style.overflow = '';
  }));

  /* ---------- Mega Menu - close on outside click ---------- */
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.mega-menu-wrapper')) {
      $$('.mega-menu-wrapper').forEach(w => w.classList.remove('active'));
    }
  });

  /* ---------- Mega Menu - keyboard accessibility ---------- */
  $$('.mega-menu-wrapper').forEach(wrapper => {
    const link = wrapper.querySelector('.nav-link');
    const menu = wrapper.querySelector('.mega-menu');
    if (!link || !menu) return;

    link.addEventListener('focus', () => {
      $$('.mega-menu-wrapper').forEach(w => w.classList.remove('active'));
      wrapper.classList.add('active');
    });
  });

  /* ---------- Reveal on scroll ---------- */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
  $$('.reveal').forEach(el => io.observe(el));

  /* ---------- Number count-up ---------- */
  const counters = $$('[data-count]');
  const counterIO = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const el = e.target;
      const target = parseInt(el.dataset.count, 10);
      const dur = 1800;
      const t0 = performance.now();
      const fmt = target >= 1000 ? (n) => n.toLocaleString('en-IN') : (n) => String(n);
      const step = (t) => {
        const p = Math.min(1, (t - t0) / dur);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = fmt(Math.round(target * eased));
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
      counterIO.unobserve(el);
    });
  }, { threshold: 0.5 });
  counters.forEach(el => counterIO.observe(el));

  /* ---------- Magnetic buttons (subtle) ---------- */
  $$('[data-magnetic]').forEach((el) => {
    el.addEventListener('mousemove', (e) => {
      const r = el.getBoundingClientRect();
      const x = e.clientX - (r.left + r.width / 2);
      const y = e.clientY - (r.top + r.height / 2);
      el.style.transform = `translate(${x * 0.14}px, ${y * 0.18}px)`;
    });
    el.addEventListener('mouseleave', () => { el.style.transform = ''; });
  });

  /* ---------- Testimonial slider ---------- */
  const deck = $('#quoteDeck');
  if (deck) {
    const quotes = $$('.quote', deck);
    const dots = $('#quoteDots');
    const prev = $('#quotePrev');
    const next = $('#quoteNext');
    let idx = 0;
    let auto;

    dots.innerHTML = quotes.map((_, i) =>
      `<button aria-label="Go to testimonial ${i+1}" class="${i === idx ? 'is-active' : ''}" data-i="${i}"></button>`
    ).join('');

    const go = (n) => {
      idx = (n + quotes.length) % quotes.length;
      quotes.forEach((q, i) => q.classList.toggle('is-active', i === idx));
      $$('button', dots).forEach((d, i) => d.classList.toggle('is-active', i === idx));
    };

    dots.addEventListener('click', (e) => {
      const b = e.target.closest('button[data-i]');
      if (!b) return;
      go(parseInt(b.dataset.i, 10));
      restart();
    });
    prev?.addEventListener('click', () => { go(idx - 1); restart(); });
    next?.addEventListener('click', () => { go(idx + 1); restart(); });

    const start = () => { auto = setInterval(() => go(idx + 1), 7500); };
    const restart = () => { clearInterval(auto); start(); };
    start();

    const deckIO = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) start();
        else clearInterval(auto);
      });
    }, { threshold: 0.2 });
    deckIO.observe(deck);
  }

  /* ---------- Parallax (background image translate on scroll) ---------- */
  const parallaxNodes = $$('[data-parallax-y]');
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (parallaxNodes.length && !reduceMotion) {
    let ticking = false;
    const update = () => {
      const vh = window.innerHeight;
      parallaxNodes.forEach((el) => {
        const parent = el.parentElement;
        const r = parent.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        const speed = parseFloat(el.dataset.parallaxY) || 0.15;
        const center = (r.top + r.height / 2) - vh / 2;
        const offset = center * -speed;
        el.style.transform = `translate3d(0, ${offset.toFixed(2)}px, 0)`;
      });
      ticking = false;
    };
    const onParallax = () => {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    };
    window.addEventListener('scroll', onParallax, { passive: true });
    window.addEventListener('resize', onParallax);
    update();
  }

  /* ---------- Smooth anchor (offset for sticky header) ---------- */
  $$('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const href = a.getAttribute('href');
      if (href.length > 1) {
        const t = $(href);
        if (t) {
          e.preventDefault();
          const top = t.getBoundingClientRect().top + window.scrollY - 80;
          window.scrollTo({ top, behavior: 'smooth' });
        }
      }
    });
  });

})();
