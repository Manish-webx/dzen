import os

source_file = "index1.html"
target_file = "acne-treatment.html"

with open(source_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find important indices
header_end = -1
contact_start = -1
contact_end = -1
main_end = -1

for i, line in enumerate(lines):
    if "<main>" in line:
        header_end = i
    if "<!-- Contact / Booking Section -->" in line:
        contact_start = i
    if "</main>" in line:
        main_end = i

# Create new content
new_content = lines[:header_end + 1]

# Custom CSS for this page
new_content.append("""        <style>
            /* Specific styles for service page */
            .service-hero {
                padding-top: 150px;
                padding-bottom: 80px;
                background-color: var(--cream);
                position: relative;
                overflow: hidden;
            }
            .trust-bar {
                background: var(--off-white);
                padding: 40px 0;
                border-bottom: 1px solid rgba(0,0,0,0.05);
            }
            .trust-item {
                text-align: center;
            }
            .trust-icon {
                width: 48px;
                height: 48px;
                margin-bottom: 16px;
                color: var(--warm-gold);
            }
            .trust-title {
                font-family: var(--font-primary);
                font-size: 1.1rem;
                color: var(--deep-brown);
                margin-bottom: 8px;
            }
            .trust-desc {
                font-size: 0.9rem;
                color: var(--text-color);
            }
            .process-step {
                display: flex;
                margin-bottom: 2rem;
                align-items: flex-start;
            }
            .step-number {
                width: 40px;
                height: 40px;
                background: var(--warm-gold);
                color: white;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: bold;
                margin-right: 20px;
                flex-shrink: 0;
            }
            .step-content h4 {
                color: var(--deep-brown);
                margin-bottom: 10px;
            }
            .faq-item {
                border-bottom: 1px solid rgba(0,0,0,0.1);
                padding: 20px 0;
            }
            .faq-question {
                font-family: var(--font-primary);
                font-size: 1.2rem;
                color: var(--deep-brown);
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin: 0;
            }
            .faq-answer {
                margin-top: 15px;
                color: var(--text-color);
                display: none;
            }
            .faq-question.active + .faq-answer {
                display: block;
            }
        </style>
""")

# 1. Hero Section
new_content.append("""
        <section class="service-hero">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-6">
                        <span class="section-subtitle">ADVANCED DERMATOLOGY</span>
                        <h1 class="hero-title text-dark" style="font-size: 3.5rem; margin-bottom: 20px;">Advanced Acne Treatment in Gurgaon</h1>
                        <p class="section-desc text-dark" style="margin-bottom: 30px;">
                            Achieve clear, healthy skin with our root-cause focused approach. Natural results, customized protocols, and expert care by leading dermatologists.
                        </p>
                        <div class="d-flex gap-3">
                            <a href="#book" class="btn-primary-pill">
                                <span>Book Appointment</span>
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="18" height="18">
                                    <path d="M5 12h14M12 5l7 7-7 7" />
                                </svg>
                            </a>
                            <a href="https://wa.me/918800000000" class="btn-primary-pill" style="background: #25D366; border-color: #25D366; color: white;">
                                <span>WhatsApp Now</span>
                            </a>
                        </div>
                        <div class="mt-4 d-flex align-items-center gap-4">
                            <div class="d-flex align-items-center gap-2">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--warm-gold)" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                                <span style="font-size: 0.9rem; font-weight: 500; color: var(--deep-brown);">15+ Years Experience</span>
                            </div>
                            <div class="d-flex align-items-center gap-2">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--warm-gold)" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                                <span style="font-size: 0.9rem; font-weight: 500; color: var(--deep-brown);">Safe & Painless</span>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 mt-5 mt-lg-0">
                        <img src="https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?w=800&q=80" alt="Clear Skin Treatment" class="img-fluid rounded-4 shadow-lg" style="object-fit: cover; height: 500px; width: 100%;">
                    </div>
                </div>
            </div>
        </section>
""")

# 2. USP / Highlights
new_content.append("""
        <section class="trust-bar">
            <div class="container">
                <div class="row g-4">
                    <div class="col-6 col-md-3">
                        <div class="trust-item reveal">
                            <svg class="trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                                <circle cx="12" cy="7" r="4"></circle>
                            </svg>
                            <h3 class="trust-title">Expert Surgeons</h3>
                            <p class="trust-desc">Board-certified dermatologists</p>
                        </div>
                    </div>
                    <div class="col-6 col-md-3">
                        <div class="trust-item reveal">
                            <svg class="trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                                <line x1="8" y1="21" x2="16" y2="21"></line>
                                <line x1="12" y1="17" x2="12" y2="21"></line>
                            </svg>
                            <h3 class="trust-title">Latest Technology</h3>
                            <p class="trust-desc">Advanced medical devices</p>
                        </div>
                    </div>
                    <div class="col-6 col-md-3">
                        <div class="trust-item reveal">
                            <svg class="trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                                <polyline points="22 4 12 14.01 9 11.01"></polyline>
                            </svg>
                            <h3 class="trust-title">Natural Results</h3>
                            <p class="trust-desc">Scar-free, holistic healing</p>
                        </div>
                    </div>
                    <div class="col-6 col-md-3">
                        <div class="trust-item reveal">
                            <svg class="trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                            </svg>
                            <h3 class="trust-title">Patient Safety</h3>
                            <p class="trust-desc">100% safe protocols</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""")

# 3. About Service
new_content.append("""
        <section class="py-5" style="background: white;">
            <div class="container py-5">
                <div class="row align-items-center">
                    <div class="col-lg-6 mb-4 mb-lg-0 reveal">
                        <span class="section-subtitle">ABOUT THE TREATMENT</span>
                        <h2 class="section-title text-dark" style="text-align: left;">Understanding Acne & Our Approach</h2>
                        <p class="section-desc text-dark mt-4">
                            Acne is more than just a surface-level skin condition; it's often a reflection of internal imbalances. At D'Zen Derma, we move beyond quick fixes and superficial treatments. Our approach is to identify the root cause—whether hormonal, dietary, or environmental—and create a comprehensive, customized protocol.
                        </p>
                        <p class="section-desc text-dark mt-3">
                            We utilize a blend of advanced clinical treatments and integrative wellness strategies to not only clear existing breakouts but also prevent future ones, ensuring long-term skin health and radiance.
                        </p>
                    </div>
                    <div class="col-lg-6 reveal">
                        <img src="https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?w=800&q=80" alt="Facial Treatment" class="img-fluid rounded-4 shadow">
                    </div>
                </div>
            </div>
        </section>
""")

# 4. Symptoms / Use Cases
new_content.append("""
        <section class="py-5" style="background: var(--off-white);">
            <div class="container py-5">
                <div class="section-header text-center reveal">
                    <span class="section-subtitle">SYMPTOMS & CONCERNS</span>
                    <h2 class="section-title text-dark">Signs You May Need Professional Treatment</h2>
                    <p class="section-desc text-dark mx-auto">Not all acne is the same. We treat a wide spectrum of acne types and related concerns.</p>
                </div>
                <div class="row g-4 mt-4">
                    <div class="col-md-6 col-lg-3">
                        <div class="p-4 bg-white rounded-4 shadow-sm h-100 reveal">
                            <h4 style="color: var(--deep-brown); margin-bottom: 15px;">Hormonal Acne</h4>
                            <p class="text-muted">Deep, cystic breakouts typically appearing along the jawline and chin, often linked to menstrual cycles or hormonal fluctuations.</p>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3">
                        <div class="p-4 bg-white rounded-4 shadow-sm h-100 reveal">
                            <h4 style="color: var(--deep-brown); margin-bottom: 15px;">Cystic Acne</h4>
                            <p class="text-muted">Large, red, painful, and deep breakouts that can lead to permanent scarring if not treated by a professional.</p>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3">
                        <div class="p-4 bg-white rounded-4 shadow-sm h-100 reveal">
                            <h4 style="color: var(--deep-brown); margin-bottom: 15px;">Adult Acne</h4>
                            <p class="text-muted">Persistent breakouts occurring well beyond the teenage years, requiring a delicate balance of anti-acne and anti-aging care.</p>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3">
                        <div class="p-4 bg-white rounded-4 shadow-sm h-100 reveal">
                            <h4 style="color: var(--deep-brown); margin-bottom: 15px;">Blackheads & Whiteheads</h4>
                            <p class="text-muted">Congested pores leading to comedonal acne, treated effectively with deep clinical extraction and exfoliation.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""")

# 5. Process
new_content.append("""
        <section class="py-5" style="background: white;">
            <div class="container py-5">
                <div class="section-header text-center reveal">
                    <span class="section-subtitle">OUR PROCESS</span>
                    <h2 class="section-title text-dark">The D'Zen Protocol</h2>
                </div>
                <div class="row justify-content-center mt-5">
                    <div class="col-lg-8">
                        <div class="process-step reveal">
                            <div class="step-number">1</div>
                            <div class="step-content">
                                <h4>Deep Consultation & Root Cause Analysis</h4>
                                <p class="text-muted">We begin with an in-depth analysis of your skin, lifestyle, diet, and medical history to uncover the underlying triggers of your acne.</p>
                            </div>
                        </div>
                        <div class="process-step reveal">
                            <div class="step-number">2</div>
                            <div class="step-content">
                                <h4>Customized Treatment Plan</h4>
                                <p class="text-muted">Based on our findings, we design a personalized protocol that may include clinical peels, laser therapy, or medical extractions.</p>
                            </div>
                        </div>
                        <div class="process-step reveal">
                            <div class="step-number">3</div>
                            <div class="step-content">
                                <h4>Clinical Execution</h4>
                                <p class="text-muted">Our expert dermatologists perform the treatments using state-of-the-art technology in a safe, sterile, and relaxing environment.</p>
                            </div>
                        </div>
                        <div class="process-step reveal">
                            <div class="step-number">4</div>
                            <div class="step-content">
                                <h4>Aftercare & Maintenance</h4>
                                <p class="text-muted">We guide you through a tailored home-care regimen and schedule follow-ups to ensure your skin remains clear and healthy.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""")

# 6. Before & After
new_content.append("""
        <section class="py-5" style="background: var(--cream);">
            <div class="container py-5">
                <div class="section-header text-center reveal">
                    <span class="section-subtitle">REAL RESULTS</span>
                    <h2 class="section-title text-dark">Before & After</h2>
                    <p class="section-desc text-dark mx-auto">See the transformative power of our personalized acne protocols.</p>
                </div>
                <div class="row g-4 mt-4 justify-content-center">
                    <div class="col-md-5 reveal">
                        <div class="position-relative">
                            <img src="https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=600&q=80" alt="Before" class="img-fluid rounded-4 shadow" style="width: 100%; height: 350px; object-fit: cover;">
                            <div class="position-absolute bottom-0 start-0 m-3 bg-white px-3 py-1 rounded-pill shadow-sm" style="font-weight: 600; font-size: 0.8rem; color: var(--deep-brown);">Before</div>
                        </div>
                    </div>
                    <div class="col-md-2 d-flex align-items-center justify-content-center reveal">
                        <svg viewBox="0 0 24 24" width="40" height="40" stroke="var(--warm-gold)" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </div>
                    <div class="col-md-5 reveal">
                        <div class="position-relative">
                            <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&q=80" alt="After" class="img-fluid rounded-4 shadow" style="width: 100%; height: 350px; object-fit: cover;">
                            <div class="position-absolute bottom-0 start-0 m-3 bg-white px-3 py-1 rounded-pill shadow-sm" style="font-weight: 600; font-size: 0.8rem; color: var(--deep-brown);">After</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""")

# 7. Pricing
new_content.append("""
        <section class="py-5" style="background: white;">
            <div class="container py-5">
                <div class="row align-items-center bg-white rounded-4 shadow-sm p-4 p-md-5 border" style="border-color: rgba(0,0,0,0.05) !important;">
                    <div class="col-md-8 mb-4 mb-md-0 reveal">
                        <h3 style="color: var(--deep-brown); margin-bottom: 15px;">Acne Treatment Cost</h3>
                        <p class="text-muted mb-0">Our treatments are highly customized. Costs depend on the severity of your acne and the specific protocols required (e.g., peels, lasers, medications).</p>
                        <ul class="list-unstyled mt-3 mb-0 text-muted">
                            <li class="mb-2"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--warm-gold)" stroke-width="2" class="me-2"><polyline points="20 6 9 17 4 12"></polyline></svg> Transparent pricing with no hidden charges</li>
                            <li class="mb-2"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--warm-gold)" stroke-width="2" class="me-2"><polyline points="20 6 9 17 4 12"></polyline></svg> EMI options available</li>
                        </ul>
                    </div>
                    <div class="col-md-4 text-md-end reveal">
                        <div class="p-4 rounded-4" style="background: var(--off-white);">
                            <span class="d-block text-muted mb-2">Starting from</span>
                            <h2 style="color: var(--warm-gold); font-family: var(--font-primary); font-weight: 700;">₹4,500*</h2>
                            <span class="d-block text-muted mt-2" style="font-size: 0.8rem;">*per session</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""")

# 8. Doctor Profile
new_content.append("""
        <section class="doctors-section py-5" style="background: var(--deep-brown); padding-top: 80px !important; padding-bottom: 80px !important; position: relative;">
            <div class="container position-relative" style="z-index: 2;">
                <div class="row align-items-center">
                    <div class="col-lg-4 mb-4 mb-lg-0 reveal">
                        <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=600&q=80" alt="Dr. Aarushi Passi Bhandari" class="img-fluid rounded-4 shadow">
                    </div>
                    <div class="col-lg-8 ps-lg-5 reveal">
                        <span class="section-subtitle text-white-50" style="text-align: left;">MEET OUR EXPERT</span>
                        <h2 class="section-title text-white" style="text-align: left;">Dr. Aarushi Passi Bhandari</h2>
                        <h5 class="text-white mb-4" style="font-weight: 400; font-family: var(--font-primary); color: var(--warm-gold) !important;">Scientific Authority & Lead Dermatologist</h5>
                        <p class="text-white-50 mb-4" style="max-width: 800px;">
                            With over 15 years of clinical excellence, Dr. Aarushi specializes in complex dermatological conditions including severe cystic and hormonal acne. Her science-first approach ensures that treatments are not only effective but also preserve the long-term integrity of your skin.
                        </p>
                        <div class="doctor-credentials mt-4" style="justify-content: flex-start;">
                            <span class="doctor-cred text-white border-light">MD Dermatology</span>
                            <span class="doctor-cred text-white border-light">Global Fellowships</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""")

# 9. FAQ
new_content.append("""
        <section class="py-5" style="background: white;">
            <div class="container py-5">
                <div class="section-header text-center reveal">
                    <span class="section-subtitle">FAQ</span>
                    <h2 class="section-title text-dark">Frequently Asked Questions</h2>
                </div>
                <div class="row justify-content-center mt-4">
                    <div class="col-lg-8">
                        <div class="faq-list reveal">
                            <div class="faq-item">
                                <h4 class="faq-question">Is the acne treatment painful? <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></h4>
                                <div class="faq-answer">Most of our acne treatments are minimally invasive and involve little to no discomfort. If clinical extractions or lasers are required, we ensure your comfort with numbing agents and careful techniques.</div>
                            </div>
                            <div class="faq-item">
                                <h4 class="faq-question">How long does it take to see results? <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></h4>
                                <div class="faq-answer">While some immediate reduction in inflammation can be seen after the first session, significant clearing typically takes 4 to 8 weeks, depending on the severity of the acne and the body's natural healing cycle.</div>
                            </div>
                            <div class="faq-item">
                                <h4 class="faq-question">What is the recovery time? <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></h4>
                                <div class="faq-answer">Recovery time is minimal. Chemical peels or micro-needling may result in a few days of mild redness or peeling. We will provide a strict aftercare routine to accelerate healing.</div>
                            </div>
                            <div class="faq-item">
                                <h4 class="faq-question">Will my acne come back? <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></h4>
                                <div class="faq-answer">Because we treat the root cause, long-term remission is highly likely. However, lifestyle changes, hormonal shifts, or stress can occasionally trigger minor breakouts, which can be managed with maintenance sessions.</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""")

# 10. Related Treatments
new_content.append("""
        <section class="py-5" style="background: var(--off-white);">
            <div class="container py-5">
                <div class="section-header text-center reveal">
                    <span class="section-subtitle">COMPLEMENTARY CARE</span>
                    <h2 class="section-title text-dark">Related Treatments</h2>
                </div>
                <div class="row g-4 mt-4 justify-content-center">
                    <div class="col-md-4 reveal">
                        <div class="card border-0 rounded-4 overflow-hidden shadow-sm h-100">
                            <img src="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=500&q=80" class="card-img-top" alt="Acne Scar Revision" style="height: 200px; object-fit: cover;">
                            <div class="card-body p-4">
                                <h5 class="card-title" style="color: var(--deep-brown); font-family: var(--font-primary);">Acne Scar Revision</h5>
                                <p class="card-text text-muted">Advanced laser and microneedling treatments to smooth texture and erase past damage.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 reveal">
                        <div class="card border-0 rounded-4 overflow-hidden shadow-sm h-100">
                            <img src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=500&q=80" class="card-img-top" alt="Chemical Peels" style="height: 200px; object-fit: cover;">
                            <div class="card-body p-4">
                                <h5 class="card-title" style="color: var(--deep-brown); font-family: var(--font-primary);">Clinical Peels</h5>
                                <p class="card-text text-muted">Customized exfoliating treatments to deeply cleanse pores and rejuvenate the skin surface.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""")

# 11. FAQ script
new_content.append("""
        <script>
            document.addEventListener('DOMContentLoaded', () => {
                const faqs = document.querySelectorAll('.faq-question');
                faqs.forEach(faq => {
                    faq.addEventListener('click', () => {
                        faq.classList.toggle('active');
                        // Rotate arrow icon
                        const icon = faq.querySelector('svg');
                        if(faq.classList.contains('active')) {
                            icon.style.transform = 'rotate(180deg)';
                        } else {
                            icon.style.transform = 'rotate(0deg)';
                        }
                    });
                });
            });
        </script>
""")

# Add contact section from original
new_content.extend(lines[contact_start:main_end + 1])

# Add footer and scripts
new_content.extend(lines[main_end + 1:])

# Replace <title>
for i, line in enumerate(new_content):
    if "<title>" in line:
        new_content[i] = '    <title>Advanced Acne Treatment in Gurgaon | D\'Zen Derma</title>\n'
    if '<meta name="description"' in line:
        new_content[i+1] = '        content="Get advanced, root-cause focused acne treatment at D\'Zen Derma. Customized protocols for clear, healthy skin." />\n'

with open(target_file, "w", encoding="utf-8") as f:
    f.writelines(new_content)

print(f"Successfully generated {target_file}")
