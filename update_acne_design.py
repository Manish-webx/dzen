import os

target_file = "acne-treatment.html"

with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find the end of the service-hero section and start of contact section
hero_end_idx = -1
contact_start_idx = -1

for i, line in enumerate(lines):
    if "<!-- Contact / Booking Section -->" in line:
        contact_start_idx = i
        break

# The hero section ends with </section> right before <section class="trust-bar">
for i in range(contact_start_idx):
    if '<section class="trust-bar">' in lines[i]:
        # Backtrack to find the </section> of hero
        for j in range(i-1, -1, -1):
            if "</section>" in lines[j]:
                hero_end_idx = j
                break
        break

# If we couldn't find it, fallback to manual search for </section> after service-hero
if hero_end_idx == -1:
    in_hero = False
    for i in range(contact_start_idx):
        if '<section class="service-hero">' in lines[i]:
            in_hero = True
        if in_hero and "</section>" in lines[i]:
            hero_end_idx = i
            break

new_content = lines[:hero_end_idx + 1]

premium_sections = """
        <!-- Trust Bar Premium -->
        <section class="trust-bar py-5" style="background: var(--off-white); border-bottom: 1px solid var(--border);">
            <div class="container">
                <div class="row g-4 justify-content-center">
                    <div class="col-6 col-md-3">
                        <div class="trust-item reveal text-center">
                            <svg class="trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width: 40px; height: 40px; color: var(--warm-gold); margin-bottom: 12px;">
                                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                                <circle cx="12" cy="7" r="4"></circle>
                            </svg>
                            <h3 class="trust-title" style="font-family: var(--serif); font-size: 1.2rem; color: var(--deep-brown);">Expert Surgeons</h3>
                            <p class="trust-desc" style="font-size: 0.9rem; color: var(--text-muted);">Board-certified dermatologists</p>
                        </div>
                    </div>
                    <div class="col-6 col-md-3">
                        <div class="trust-item reveal text-center">
                            <svg class="trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width: 40px; height: 40px; color: var(--warm-gold); margin-bottom: 12px;">
                                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                                <line x1="8" y1="21" x2="16" y2="21"></line>
                                <line x1="12" y1="17" x2="12" y2="21"></line>
                            </svg>
                            <h3 class="trust-title" style="font-family: var(--serif); font-size: 1.2rem; color: var(--deep-brown);">Latest Technology</h3>
                            <p class="trust-desc" style="font-size: 0.9rem; color: var(--text-muted);">Advanced medical devices</p>
                        </div>
                    </div>
                    <div class="col-6 col-md-3">
                        <div class="trust-item reveal text-center">
                            <svg class="trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width: 40px; height: 40px; color: var(--warm-gold); margin-bottom: 12px;">
                                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                                <polyline points="22 4 12 14.01 9 11.01"></polyline>
                            </svg>
                            <h3 class="trust-title" style="font-family: var(--serif); font-size: 1.2rem; color: var(--deep-brown);">Natural Results</h3>
                            <p class="trust-desc" style="font-size: 0.9rem; color: var(--text-muted);">Scar-free, holistic healing</p>
                        </div>
                    </div>
                    <div class="col-6 col-md-3">
                        <div class="trust-item reveal text-center">
                            <svg class="trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width: 40px; height: 40px; color: var(--warm-gold); margin-bottom: 12px;">
                                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                            </svg>
                            <h3 class="trust-title" style="font-family: var(--serif); font-size: 1.2rem; color: var(--deep-brown);">Patient Safety</h3>
                            <p class="trust-desc" style="font-size: 0.9rem; color: var(--text-muted);">100% safe protocols</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About Premium -->
        <section class="about-us" id="about-us" style="padding-top: 100px; padding-bottom: 100px;">
            <div class="about-bg-gradient"></div>
            <div class="overlay-pattern"></div>
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-6 mb-5 mb-lg-0 reveal">
                        <span class="section-subtitle">ABOUT THE TREATMENT</span>
                        <h2 class="section-title">Understanding Acne & Our Approach</h2>
                        <p class="section-desc mt-4 text-white-50" style="color: rgba(255,255,255,0.8) !important;">
                            Acne is more than just a surface-level skin condition; it's often a reflection of internal imbalances. At D'Zen Derma, we move beyond quick fixes and superficial treatments. Our approach is to identify the root cause—whether hormonal, dietary, or environmental—and create a comprehensive, customized protocol.
                        </p>
                        <p class="section-desc mt-3 text-white-50" style="color: rgba(255,255,255,0.8) !important;">
                            We utilize a blend of advanced clinical treatments and integrative wellness strategies to not only clear existing breakouts but also prevent future ones, ensuring long-term skin health and radiance.
                        </p>
                    </div>
                    <div class="col-lg-6 reveal text-center">
                        <img src="https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?w=800&q=80" alt="Facial Treatment" class="img-fluid rounded-4 shadow-lg" style="max-height: 500px; object-fit: cover;">
                    </div>
                </div>
            </div>
        </section>

        <!-- Concerns Premium -->
        <style>
            #concerns-acne {
                background-color: #FAF8F5 !important;
                background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.15'/%3E%3C/svg%3E") !important;
                padding-bottom: 100px;
            }
        </style>
        <section class="concerns-section" id="concerns-acne">
            <div class="concerns-wave-bg">
                <svg viewBox="0 0 1440 300" fill="none" preserveAspectRatio="none">
                    <path d="M-50,200 C 400,-100 200,400 720,150 C 1100,-100 1000,400 1500,100" stroke="var(--warm-gold)" stroke-width="1" stroke-opacity="0.6" vector-effect="non-scaling-stroke" />
                </svg>
            </div>
            <div class="container">
                <div class="section-header reveal text-center">
                    <span class="section-subtitle">SYMPTOMS & CONCERNS</span>
                    <h2 class="section-title text-dark">Signs You May Need Professional Treatment</h2>
                </div>
                <div class="concerns-grid mt-5">
                    <div class="concern-item reveal">
                        <div class="concern-blob-wrapper">
                            <div class="concern-blob-bg"></div>
                            <div class="concern-image">
                                <img src="https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?w=600&q=80" alt="Hormonal Acne">
                                <div class="concern-overlay"></div>
                                <h3 class="concern-title">Hormonal</h3>
                            </div>
                        </div>
                    </div>
                    <div class="concern-item reveal">
                        <div class="concern-blob-wrapper">
                            <div class="concern-blob-bg" style="animation-delay: -2s;"></div>
                            <div class="concern-image" style="animation-delay: -1.5s;">
                                <img src="https://images.unsplash.com/photo-1528319725582-ddc096101511?w=600&q=80" alt="Cystic Acne">
                                <div class="concern-overlay"></div>
                                <h3 class="concern-title">Cystic</h3>
                            </div>
                        </div>
                    </div>
                    <div class="concern-item reveal">
                        <div class="concern-blob-wrapper">
                            <div class="concern-blob-bg" style="animation-delay: -4s;"></div>
                            <div class="concern-image" style="animation-delay: -3s;">
                                <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600&q=80" alt="Adult Acne">
                                <div class="concern-overlay"></div>
                                <h3 class="concern-title">Adult</h3>
                            </div>
                        </div>
                    </div>
                    <div class="concern-item reveal">
                        <div class="concern-blob-wrapper">
                            <div class="concern-blob-bg" style="animation-delay: -6s;"></div>
                            <div class="concern-image" style="animation-delay: -4.5s;">
                                <img src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=600&q=80" alt="Comedonal Acne">
                                <div class="concern-overlay"></div>
                                <h3 class="concern-title">Comedonal</h3>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Process Premium -->
        <section style="background: var(--cream); padding-top: 100px; padding-bottom: 100px;">
            <div class="container">
                <div class="section-header text-center reveal">
                    <span class="section-subtitle">OUR PROCESS</span>
                    <h2 class="section-title text-dark">The D'Zen Protocol</h2>
                </div>
                <div class="row justify-content-center mt-5">
                    <div class="col-lg-8 reveal">
                        <div class="philosophy-details-card" style="box-shadow: none; background: transparent; padding: 0;">
                            <div class="philosophy-pane active" style="position: relative; margin-bottom: 40px; opacity: 1; visibility: visible; transform: none;">
                                <div class="pane-watermark" style="right: auto; left: -20px; top: -30px; font-size: 120px;">01</div>
                                <h3 class="pane-title" style="position: relative; z-index: 2;">Deep Consultation</h3>
                                <p class="pane-desc" style="position: relative; z-index: 2;">We begin with an in-depth analysis of your skin, lifestyle, diet, and medical history to uncover the underlying triggers of your acne.</p>
                            </div>
                            <div class="decor-line" style="margin: 30px 0; background: var(--warm-gold);"></div>
                            
                            <div class="philosophy-pane active" style="position: relative; margin-bottom: 40px; opacity: 1; visibility: visible; transform: none;">
                                <div class="pane-watermark" style="right: auto; left: -20px; top: -30px; font-size: 120px;">02</div>
                                <h3 class="pane-title" style="position: relative; z-index: 2;">Customized Plan</h3>
                                <p class="pane-desc" style="position: relative; z-index: 2;">Based on our findings, we design a personalized protocol that may include clinical peels, laser therapy, or medical extractions.</p>
                            </div>
                            <div class="decor-line" style="margin: 30px 0; background: var(--warm-gold);"></div>
                            
                            <div class="philosophy-pane active" style="position: relative; margin-bottom: 40px; opacity: 1; visibility: visible; transform: none;">
                                <div class="pane-watermark" style="right: auto; left: -20px; top: -30px; font-size: 120px;">03</div>
                                <h3 class="pane-title" style="position: relative; z-index: 2;">Clinical Execution</h3>
                                <p class="pane-desc" style="position: relative; z-index: 2;">Our expert dermatologists perform the treatments using state-of-the-art technology in a safe, sterile, and relaxing environment.</p>
                            </div>
                            <div class="decor-line" style="margin: 30px 0; background: var(--warm-gold);"></div>
                            
                            <div class="philosophy-pane active" style="position: relative; margin-bottom: 0; opacity: 1; visibility: visible; transform: none;">
                                <div class="pane-watermark" style="right: auto; left: -20px; top: -30px; font-size: 120px;">04</div>
                                <h3 class="pane-title" style="position: relative; z-index: 2;">Aftercare</h3>
                                <p class="pane-desc" style="position: relative; z-index: 2;">We guide you through a tailored home-care regimen and schedule follow-ups to ensure your skin remains clear and healthy.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Before & After Premium -->
        <section style="background: white; padding-top: 100px; padding-bottom: 100px;">
            <div class="container">
                <div class="section-header text-center reveal">
                    <span class="section-subtitle">REAL RESULTS</span>
                    <h2 class="section-title text-dark">Before & After</h2>
                    <p class="section-desc text-dark mx-auto">See the transformative power of our personalized acne protocols.</p>
                </div>
                <div class="row g-4 mt-5 justify-content-center">
                    <div class="col-md-5 reveal">
                        <div class="position-relative">
                            <img src="https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=600&q=80" alt="Before" class="img-fluid rounded-4 shadow-lg" style="width: 100%; height: 400px; object-fit: cover;">
                            <div class="position-absolute bottom-0 start-0 m-4 bg-white px-4 py-2 rounded-pill shadow-sm" style="font-family: var(--sans); font-weight: 600; font-size: 0.8rem; color: var(--deep-brown); letter-spacing: 0.1em; text-transform: uppercase;">Before</div>
                        </div>
                    </div>
                    <div class="col-md-2 d-flex align-items-center justify-content-center reveal">
                        <svg viewBox="0 0 24 24" width="40" height="40" stroke="var(--warm-gold)" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </div>
                    <div class="col-md-5 reveal">
                        <div class="position-relative">
                            <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&q=80" alt="After" class="img-fluid rounded-4 shadow-lg" style="width: 100%; height: 400px; object-fit: cover;">
                            <div class="position-absolute bottom-0 start-0 m-4 bg-white px-4 py-2 rounded-pill shadow-sm" style="font-family: var(--sans); font-weight: 600; font-size: 0.8rem; color: var(--deep-brown); letter-spacing: 0.1em; text-transform: uppercase;">After</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Pricing Premium -->
        <section class="about-us" style="padding-top: 100px; padding-bottom: 100px;">
            <div class="about-bg-gradient"></div>
            <div class="overlay-pattern"></div>
            <div class="container">
                <div class="row align-items-center justify-content-center reveal">
                    <div class="col-lg-10">
                        <div class="philosophy-details-card d-flex flex-column flex-md-row align-items-center" style="position: relative; z-index: 2; display: flex !important; margin: 0;">
                            <div class="flex-grow-1 p-4 p-md-5">
                                <h3 class="pane-title mb-3" style="color: var(--deep-brown);">Acne Treatment Investment</h3>
                                <p class="pane-desc text-muted">Our treatments are highly customized. Costs depend on the severity of your acne and the specific protocols required (e.g., peels, lasers, medications).</p>
                                <ul class="list-unstyled mt-4 text-muted" style="font-size: 0.95rem;">
                                    <li class="mb-2"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--warm-gold)" stroke-width="2" class="me-2"><polyline points="20 6 9 17 4 12"></polyline></svg> Transparent pricing with no hidden charges</li>
                                    <li class="mb-2"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--warm-gold)" stroke-width="2" class="me-2"><polyline points="20 6 9 17 4 12"></polyline></svg> EMI options available</li>
                                </ul>
                            </div>
                            <div class="p-4 p-md-5 text-center text-md-end border-md-start border-light" style="min-width: 250px;">
                                <span class="d-block mb-2 text-muted" style="font-family: var(--sans); font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase;">Starting from</span>
                                <h2 style="font-family: var(--serif); font-weight: 600; font-size: 3.5rem; color: var(--warm-gold); margin: 0;">₹4,500<span style="font-size: 1rem; color: var(--text-color);">*</span></h2>
                                <span class="d-block mt-2 text-muted" style="font-family: var(--sans); font-size: 11px;">*per session</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Doctor Profile -->
        <section class="doctors-section" style="padding-top: 100px; padding-bottom: 100px;">
            <div class="doctors-fixed-bg" style="background-image: url('https://images.unsplash.com/photo-1629909613654-28e377c37b09?w=1600&q=80');"></div>
            <div class="doctors-overlay"></div>
            <div class="container relative-content" style="position: relative; z-index: 2;">
                <div class="row align-items-center doctors-row reveal">
                    <div class="col-lg-8 mb-5 mb-lg-0 pe-lg-5">
                        <div class="section-header text-light" style="text-align: left; margin-bottom: 32px;">
                            <span class="section-subtitle">MEET OUR EXPERT</span>
                            <h2 class="section-title">Dr. Aarushi Passi Bhandari</h2>
                        </div>
                        <h5 class="text-white mb-4" style="font-weight: 400; font-family: var(--font-primary); color: var(--warm-gold) !important; font-size: 1.25rem;">Scientific Authority & Lead Dermatologist</h5>
                        <p class="doctors-text text-white-50">
                            With over 15 years of clinical excellence, Dr. Aarushi specializes in complex dermatological conditions including severe cystic and hormonal acne. Her science-first approach ensures that treatments are not only effective but also preserve the long-term integrity of your skin.
                        </p>
                        <div class="doctor-credentials mt-5" style="justify-content: flex-start;">
                            <span class="doctor-cred">MD Dermatology</span>
                            <span class="doctor-cred">Global Fellowships</span>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="doctor-portrait-large">
                            <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=600&q=80" alt="Dr. Aarushi Passi Bhandari" class="img-fluid w-100 portrait-img" style="border-radius: var(--radius-lg);">
                            <div class="doctor-portrait-info" style="border-radius: 0 0 var(--radius-lg) var(--radius-lg);">
                                <h4 class="doctor-portrait-name">Dr. Aarushi Passi Bhandari</h4>
                                <span class="doctor-portrait-role">Scientific Authority</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- FAQ Premium -->
        <section style="background: var(--off-white); padding-top: 100px; padding-bottom: 100px;">
            <div class="container">
                <div class="section-header text-center reveal">
                    <span class="section-subtitle">FAQ</span>
                    <h2 class="section-title text-dark">Frequently Asked Questions</h2>
                </div>
                <div class="row justify-content-center mt-5">
                    <div class="col-lg-8">
                        <div class="faq-list reveal bg-white rounded-4 shadow-sm p-4 p-md-5">
                            <div class="faq-item" style="border-bottom: 1px solid var(--border); padding-bottom: 24px; margin-bottom: 24px;">
                                <h4 class="faq-question">Is the acne treatment painful? <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s;"><polyline points="6 9 12 15 18 9"></polyline></svg></h4>
                                <div class="faq-answer">Most of our acne treatments are minimally invasive and involve little to no discomfort. If clinical extractions or lasers are required, we ensure your comfort with numbing agents and careful techniques.</div>
                            </div>
                            <div class="faq-item" style="border-bottom: 1px solid var(--border); padding-bottom: 24px; margin-bottom: 24px;">
                                <h4 class="faq-question">How long does it take to see results? <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s;"><polyline points="6 9 12 15 18 9"></polyline></svg></h4>
                                <div class="faq-answer">While some immediate reduction in inflammation can be seen after the first session, significant clearing typically takes 4 to 8 weeks, depending on the severity of the acne and the body's natural healing cycle.</div>
                            </div>
                            <div class="faq-item" style="border-bottom: 1px solid var(--border); padding-bottom: 24px; margin-bottom: 24px;">
                                <h4 class="faq-question">What is the recovery time? <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s;"><polyline points="6 9 12 15 18 9"></polyline></svg></h4>
                                <div class="faq-answer">Recovery time is minimal. Chemical peels or micro-needling may result in a few days of mild redness or peeling. We will provide a strict aftercare routine to accelerate healing.</div>
                            </div>
                            <div class="faq-item" style="padding-bottom: 0; margin-bottom: 0;">
                                <h4 class="faq-question">Will my acne come back? <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s;"><polyline points="6 9 12 15 18 9"></polyline></svg></h4>
                                <div class="faq-answer">Because we treat the root cause, long-term remission is highly likely. However, lifestyle changes, hormonal shifts, or stress can occasionally trigger minor breakouts, which can be managed with maintenance sessions.</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Related Treatments Premium -->
        <section style="background: white; padding-top: 100px; padding-bottom: 100px;">
            <div class="container">
                <div class="section-header text-center reveal">
                    <span class="section-subtitle">COMPLEMENTARY CARE</span>
                    <h2 class="section-title text-dark">Related Treatments</h2>
                </div>
                <div class="row g-5 mt-4 justify-content-center">
                    <div class="col-md-5 reveal">
                        <a href="#" class="card border-0 rounded-0 overflow-hidden bg-transparent text-decoration-none">
                            <div style="overflow: hidden; border-radius: var(--radius-lg); position: relative;">
                                <img src="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=600&q=80" class="card-img-top" alt="Acne Scar Revision" style="height: 350px; object-fit: cover; transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                            </div>
                            <div class="card-body p-4 px-0 text-center">
                                <h3 class="card-title" style="font-family: var(--serif); font-size: 1.5rem; color: var(--deep-brown);">Acne Scar Revision</h3>
                                <p class="card-text text-muted mt-2">Advanced laser and microneedling treatments to smooth texture and erase past damage.</p>
                                <span style="font-family: var(--sans); font-size: 11px; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; color: var(--warm-gold); margin-top: 15px; display: inline-block;">Learn More &rarr;</span>
                            </div>
                        </a>
                    </div>
                    <div class="col-md-5 reveal">
                        <a href="#" class="card border-0 rounded-0 overflow-hidden bg-transparent text-decoration-none">
                            <div style="overflow: hidden; border-radius: var(--radius-lg); position: relative;">
                                <img src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=600&q=80" class="card-img-top" alt="Chemical Peels" style="height: 350px; object-fit: cover; transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                            </div>
                            <div class="card-body p-4 px-0 text-center">
                                <h3 class="card-title" style="font-family: var(--serif); font-size: 1.5rem; color: var(--deep-brown);">Clinical Peels</h3>
                                <p class="card-text text-muted mt-2">Customized exfoliating treatments to deeply cleanse pores and rejuvenate the skin surface.</p>
                                <span style="font-family: var(--sans); font-size: 11px; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; color: var(--warm-gold); margin-top: 15px; display: inline-block;">Learn More &rarr;</span>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </section>
"""

new_content.append(premium_sections)

# Append everything from Contact section onwards
new_content.extend(lines[contact_start_idx:])

with open(target_file, "w", encoding="utf-8") as f:
    f.writelines(new_content)

print(f"Successfully updated {target_file}")
