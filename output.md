
    # Code output
    ## User input: Make me a beautiful landing page for my cat nursery
    ### HTML Code
    ```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Purrfect Beginnings — Cat Nursery</title>
  <meta name="description" content="Purrfect Beginnings is a loving, cage‑free cat nursery with dedicated caregivers. We offer daycare, overnight boarding, neonatal care, grooming, enrichment, and health monitoring in a safe, cozy environment. Book a visit and meet our kittens.">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="page">
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="header header--sticky" role="banner">
    <div class="header__inner container">
      <a href="#home" class="brand" aria-label="Purrfect Beginnings Home">
        <span class="brand__mark" aria-hidden="true">
          <svg class="icon icon--paw" viewBox="0 0 64 64" width="28" height="28" aria-hidden="true" focusable="false">
            <path d="M31 28c-6 0-11 5-11 11 0 7 7 12 11 12s11-5 11-12c0-6-5-11-11-11zm-15-5c3 0 6-3 6-6s-3-6-6-6-6 3-6 6 3 6 6 6zm30 0c3 0 6-3 6-6s-3-6-6-6-6 3-6 6 3 6 6 6zM18 30c2 0 4-2 4-4s-2-5-4-5-5 3-5 5 3 4 5 4zm28 0c2 0 5-2 5-4s-3-5-5-5-4 3-4 5 2 4 4 4z" />
          </svg>
        </span>
        <span class="brand__text">Purrfect Beginnings</span>
      </a>

      <button class="header__toggle" id="menu-toggle" aria-controls="primary-navigation" aria-expanded="false" aria-label="Open menu">
        <span class="header__toggle-bars" aria-hidden="true">
          <svg class="icon icon--menu" viewBox="0 0 24 24" width="26" height="26" aria-hidden="true" focusable="false">
            <path d="M3 6h18v2H3zM3 11h18v2H3zM3 16h18v2H3z"/>
          </svg>
        </span>
      </button>

      <nav class="nav" id="primary-navigation" aria-label="Primary">
        <ul class="nav__list">
          <li class="nav__item"><a class="nav__link" href="#home" aria-current="page">Home</a></li>
          <li class="nav__item"><a class="nav__link" href="#about">About</a></li>
          <li class="nav__item"><a class="nav__link" href="#services">Services</a></li>
          <li class="nav__item"><a class="nav__link" href="#kittens">Kittens</a></li>
          <li class="nav__item"><a class="nav__link" href="#gallery">Gallery</a></li>
          <li class="nav__item"><a class="nav__link" href="#testimonials">Testimonials</a></li>
          <li class="nav__item"><a class="nav__link" href="#faqs">FAQs</a></li>
          <li class="nav__item"><a class="nav__link" href="#contact">Contact</a></li>
        </ul>
        <div class="nav__cta">
          <a class="button button--primary" href="#contact">Book a Visit</a>
        </div>
      </nav>
    </div>
  </header>

  <main id="main" class="main" role="main">
    <section id="home" class="section hero">
      <div class="hero__inner container">
        <div class="hero__content">
          <h1 class="hero__title">Where little paws find big love</h1>
          <p class="hero__subtitle">A gentle, cage‑free cat nursery with dedicated caregivers. Safe, cozy spaces, enrichment play, and hearts full of purrs.</p>
          <div class="hero__actions">
            <a class="button button--primary" href="#contact">Book a Visit</a>
            <a class="button button--secondary" href="#kittens">Meet Our Kittens</a>
          </div>
          <ul class="hero__proof" role="list">
            <li class="proof__item">
              <span class="stars" aria-label="Rated 4.9 out of 5 stars">
                <svg class="icon icon--star" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
                <svg class="icon icon--star" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
                <svg class="icon icon--star" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
                <svg class="icon icon--star" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
                <svg class="icon icon--star" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              </span>
              <span class="proof__text">4.9/5</span>
            </li>
            <li class="proof__item">
              <span class="badge" aria-label="Trusted by local vets">Trusted by local vets</span>
            </li>
            <li class="proof__item">
              <span class="badge" aria-label="Cage‑free care">Cage‑free care</span>
            </li>
          </ul>
        </div>
        <div class="hero__media">
          <img class="hero__image" src="https://placekitten.com/900/700" alt="A curious gray tabby kitten sitting in a cozy basket" width="900" height="700" loading="eager">
          <svg class="hero__decor hero__decor--paws" viewBox="0 0 120 60" aria-hidden="true" focusable="false">
            <circle cx="15" cy="15" r="6"></circle>
            <circle cx="30" cy="10" r="5"></circle>
            <circle cx="45" cy="15" r="6"></circle>
            <circle cx="25" cy="30" r="10"></circle>
            <circle cx="75" cy="40" r="6"></circle>
            <circle cx="90" cy="35" r="5"></circle>
            <circle cx="105" cy="40" r="6"></circle>
            <circle cx="85" cy="55" r="10"></circle>
          </svg>
          <svg class="hero__decor hero__decor--heart" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
            <path d="M12 21s-7.5-4.7-9.7-8.6C.6 9.3 2 6 5 6c2.3 0 3.3 1.4 4 2.2.7-.8 1.7-2.2 4-2.2 3 0 4.4 3.3 2.7 6.4C19.5 16.3 12 21 12 21z"></path>
          </svg>
        </div>
      </div>
    </section>

    <section id="about" class="section about">
      <div class="about__inner container">
        <div class="section__header">
          <h2 class="section__title">About Purrfect Beginnings</h2>
          <p class="section__lead">Born from a love for tiny whiskers and big hearts, our nursery is a soft place to land for kittens of all ages. We keep things calm, clean, and cozy—so curiosity can bloom safely.</p>
        </div>
        <div class="about__content">
          <p>Our mission is simple: nurture every kitten with the tenderness we’d want for our own. From bottle babies to playful teens, we provide gentle routines, enrichment, and a cage‑free environment where trust grows one purr at a time.</p>
          <ul class="pillars" role="list">
            <li class="pillars__item">
              <span class="pillars__icon" aria-hidden="true">
                <svg class="icon icon--shield" viewBox="0 0 24 24"><path d="M12 2l8 4v6c0 5-3.4 9.4-8 10-4.6-.6-8-5-8-10V6l8-4z"/></svg>
              </span>
              <div class="pillars__text">
                <h3 class="pillars__title">Safety</h3>
                <p class="pillars__desc">Vet‑advised protocols, sanitized spaces, and constant gentle supervision.</p>
              </div>
            </li>
            <li class="pillars__item">
              <span class="pillars__icon" aria-hidden="true">
                <svg class="icon icon--heart" viewBox="0 0 24 24"><path d="M12 21s-7.5-4.7-9.7-8.6C.6 9.3 2 6 5 6c2.3 0 3.3 1.4 4 2.2.7-.8 1.7-2.2 4-2.2 3 0 4.4 3.3 2.7 6.4C19.5 16.3 12 21 12 21z"/></svg>
              </span>
              <div class="pillars__text">
                <h3 class="pillars__title">Love</h3>
                <p class="pillars__desc">Calm handling, comfy naps, and a predictable routine that builds trust.</p>
              </div>
            </li>
            <li class="pillars__item">
              <span class="pillars__icon" aria-hidden="true">
                <svg class="icon icon--sparkle" viewBox="0 0 24 24"><path d="M12 2l2 5 5 2-5 2-2 5-2-5-5-2 5-2 2-5zM4 16l1 2 2 1-2 1-1 2-1-2-2-1 2-1 1-2zm16-2l1 2 2 1-2 1-1 2-1-2-2-1 2-1 1-2z"/></svg>
              </span>
              <div class="pillars__text">
                <h3 class="pillars__title">Enrichment</h3>
                <p class="pillars__desc">Play zones, climbing nooks, and puzzle feeders to spark curiosity.</p>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <section id="services" class="section services">
      <div class="services__inner container">
        <div class="section__header">
          <h2 class="section__title">Our Services</h2>
          <p class="section__lead">Thoughtful care, tailored for whiskered wonders.</p>
        </div>

        <div class="cards cards--grid services__grid">
          <article class="card service-card">
            <div class="service-card__icon" aria-hidden="true">
              <svg class="icon icon--sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"></circle><path d="M12 1v3M12 20v3M1 12h3M20 12h3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/></svg>
            </div>
            <h3 class="service-card__title">Daycare</h3>
            <p class="service-card__desc">Playtime in small groups, cozy nap suites, and gentle enrichment throughout the day.</p>
            <a class="service-card__link" href="#contact" aria-label="Learn more about Daycare">Learn more</a>
          </article>

          <article class="card service-card">
            <div class="service-card__icon" aria-hidden="true">
              <svg class="icon icon--moon" viewBox="0 0 24 24"><path d="M20 14a8 8 0 1 1-8-12 7 7 0 0 0 8 12z"/></svg>
            </div>
            <h3 class="service-card__title">Overnight Boarding</h3>
            <p class="service-card__desc">Warm, monitored rooms with bedtime routines and optional camera updates for peace of mind.</p>
            <a class="service-card__link" href="#contact" aria-label="Learn more about Overnight Boarding">Learn more</a>
          </article>

          <article class="card service-card">
            <div class="service-card__icon" aria-hidden="true">
              <svg class="icon icon--bottle" viewBox="0 0 24 24"><path d="M7 3h10v3l-2 2v11a3 3 0 0 1-6 0V8L7 6V3z"/></svg>
            </div>
            <h3 class="service-card__title">Neonatal Care</h3>
            <p class="service-card__desc">Bottle‑feeding, warmers, and vet‑partnered protocols for our tiniest treasures.</p>
            <a class="service-card__link" href="#contact" aria-label="Learn more about Neonatal Care">Learn more</a>
          </article>

          <article class="card service-card">
            <div class="service-card__icon" aria-hidden="true">
              <svg class="icon icon--spa" viewBox="0 0 24 24"><path d="M12 12c-4 0-7 2-7 5s3 5 7 5 7-2 7-5-3-5-7-5zM5 8a3 3 0 0 1 6 0v2H5V8zm8 0a3 3 0 0 1 6 0v2h-6V8z"/></svg>
            </div>
            <h3 class="service-card__title">Grooming &amp; Spa</h3>
            <p class="service-card__desc">Gentle brush‑outs, soft wipe baths, and nail trims designed for kitten comfort.</p>
            <a class="service-card__link" href="#contact" aria-label="Learn more about Grooming and Spa">Learn more</a>
          </article>

          <article class="card service-card">
            <div class="service-card__icon" aria-hidden="true">
              <svg class="icon icon--toy" viewBox="0 0 24 24"><path d="M12 2l2 2-8 8-2-2 8-8zm6 6l2 2-8 8-2-2 8-8zM4 20h4v2H4zM16 20h4v2h-4z"/></svg>
            </div>
            <h3 class="service-card__title">Enrichment &amp; Play</h3>
            <p class="service-card__desc">Climbers, tunnels, and puzzle feeders to keep minds curious and bodies active.</p>
            <a class="service-card__link" href="#contact" aria-label="Learn more about Enrichment and Play">Learn more</a>
          </article>

          <article class="card service-card">
            <div class="service-card__icon" aria-hidden="true">
              <svg class="icon icon--heart-monitor" viewBox="0 0 24 24"><path d="M3 12h4l2-4 3 8 2-4h7M2 6h20v12H2z" /></svg>
            </div>
            <h3 class="service-card__title">Health Monitoring</h3>
            <p class="service-card__desc">Daily check‑ins, appetite logs, and prompt updates so you’re always in the loop.</p>
            <a class="service-card__link" href="#contact" aria-label="Learn more about Health Monitoring">Learn more</a>
          </article>
        </div>
      </div>
    </section>

    <section id="kittens" class="section kittens">
      <div class="kittens__inner container">
        <div class="section__header">
          <h2 class="section__title">Featured Kittens</h2>
          <p class="section__lead">Say meow to a few sweet faces currently cuddling with us.</p>
        </div>

        <div class="cards cards--grid kittens__grid">
          <article class="card kitten-card" aria-label="Kitten: Luna">
            <div class="kitten-card__media">
              <img src="https://placekitten.com/420/300" alt="Luna, a fluffy gray kitten lounging on a blanket" width="420" height="300" loading="lazy">
              <span class="kitten-card__status kitten-card__status--ready" aria-label="Ready for visits">Ready</span>
            </div>
            <div class="kitten-card__body">
              <h3 class="kitten-card__name">Luna</h3>
              <p class="kitten-card__meta">10 weeks • Female</p>
              <ul class="kitten-card__tags" role="list">
                <li class="tag">Cuddly</li>
                <li class="tag">Playful</li>
              </ul>
            </div>
          </article>

          <article class="card kitten-card" aria-label="Kitten: Milo">
            <div class="kitten-card__media">
              <img src="https://placekitten.com/421/300" alt="Milo, an orange tabby kitten peeking over a cushion" width="421" height="300" loading="lazy">
              <span class="kitten-card__status kitten-card__status--soon" aria-label="Available soon">Soon</span>
            </div>
            <div class="kitten-card__body">
              <h3 class="kitten-card__name">Milo</h3>
              <p class="kitten-card__meta">8 weeks • Male</p>
              <ul class="kitten-card__tags" role="list">
                <li class="tag">Curious</li>
                <li class="tag">Gentle</li>
              </ul>
            </div>
          </article>

          <article class="card kitten-card" aria-label="Kitten: Willow">
            <div class="kitten-card__media">
              <img src="https://placekitten.com/420/301" alt="Willow, a calico kitten with bright eyes" width="420" height="301" loading="lazy">
              <span class="kitten-card__status kitten-card__status--special" aria-label="Special care needed">Special Care</span>
            </div>
            <div class="kitten-card__body">
              <h3 class="kitten-card__name">Willow</h3>
              <p class="kitten-card__meta">12 weeks • Female</p>
              <ul class="kitten-card__tags" role="list">
                <li class="tag">Calm</li>
                <li class="tag">Affectionate</li>
              </ul>
            </div>
          </article>

          <article class="card kitten-card" aria-label="Kitten: Oliver">
            <div class="kitten-card__media">
              <img src="https://placekitten.com/422/300" alt="Oliver, a tuxedo kitten playing with a feather toy" width="422" height="300" loading="lazy">
              <span class="kitten-card__status kitten-card__status--ready" aria-label="Ready for visits">Ready</span>
            </div>
            <div class="kitten-card__body">
              <h3 class="kitten-card__name">Oliver</h3>
              <p class="kitten-card__meta">9 weeks • Male</p>
              <ul class="kitten-card__tags" role="list">
                <li class="tag">Playful</li>
                <li class="tag">Brave</li>
              </ul>
            </div>
          </article>

          <article class="card kitten-card" aria-label="Kitten: Maple">
            <div class="kitten-card__media">
              <img src="https://placekitten.com/420/302" alt="Maple, a brown tabby kitten curled up asleep" width="420" height="302" loading="lazy">
              <span class="kitten-card__status kitten-card__status--soon" aria-label="Available soon">Soon</span>
            </div>
            <div class="kitten-card__body">
              <h3 class="kitten-card__name">Maple</h3>
              <p class="kitten-card__meta">7 weeks • Female</p>
              <ul class="kitten-card__tags" role="list">
                <li class="tag">Dreamy</li>
                <li class="tag">Gentle</li>
              </ul>
            </div>
          </article>

          <article class="card kitten-card" aria-label="Kitten: Theo">
            <div class="kitten-card__media">
              <img src="https://placekitten.com/421/301" alt="Theo, a cream kitten sitting by a window" width="421" height="301" loading="lazy">
              <span class="kitten-card__status kitten-card__status--ready" aria-label="Ready for visits">Ready</span>
            </div>
            <div class="kitten-card__body">
              <h3 class="kitten-card__name">Theo</h3>
              <p class="kitten-card__meta">11 weeks • Male</p>
              <ul class="kitten-card__tags" role="list">
                <li class="tag">Cuddly</li>
                <li class="tag">Curious</li>
              </ul>
            </div>
          </article>
        </div>

        <div class="kittens__actions">
          <a class="button button--outline" href="#contact">See All Kittens</a>
        </div>
      </div>
    </section>

    <section id="gallery" class="section gallery">
      <div class="gallery__inner container">
        <div class="section__header">
          <h2 class="section__title">Gallery</h2>
          <p class="section__lead">A peek into our soft, sunny spaces.</p>
        </div>

        <div class="mosaic" role="list">
          <figure class="mosaic__item" role="listitem">
            <img src="https://placekitten.com/700/500" alt="Sunlit playroom with soft blankets and toys" width="700" height="500" loading="lazy">
          </figure>
          <figure class="mosaic__item" role="listitem">
            <img src="https://placekitten.com/500/500" alt="Kitten batting at a feather wand" width="500" height="500" loading="lazy">
          </figure>
          <figure class="mosaic__item" role="listitem">
            <img src="https://placekitten.com/600/400" alt="Cozy nap nook with a sleeping kitten" width="600" height="400" loading="lazy">
          </figure>
          <figure class="mosaic__item" role="listitem">
            <img src="https://placekitten.com/450/600" alt="Caregiver gently holding a tiny bottle baby" width="450" height="600" loading="lazy">
          </figure>
          <figure class="mosaic__item" role="listitem">
            <img src="https://placekitten.com/800/500" alt="Climbing shelves with curious kittens exploring" width="800" height="500" loading="lazy">
          </figure>
          <figure class="mosaic__item" role="listitem">
            <img src="https://placekitten.com/500/650" alt="Fluffy kitten gazing out a sunny window" width="500" height="650" loading="lazy">
          </figure>
          <figure class="mosaic__item" role="listitem">
            <img src="https://placekitten.com/640/480" alt="Puzzle feeder time on a soft rug" width="640" height="480" loading="lazy">
          </figure>
          <figure class="mosaic__item" role="listitem">
            <img src="https://placekitten.com/650/450" alt="Two kittens cuddled together in a basket" width="650" height="450" loading="lazy">
          </figure>
          <figure class="mosaic__item" role="listitem">
            <img src="https://placekitten.com/540/360" alt="Grooming station with brushes and towels" width="540" height="360" loading="lazy">
          </figure>
        </div>
      </div>
    </section>

    <section id="testimonials" class="section testimonials">
      <div class="testimonials__inner container">
        <div class="section__header">
          <h2 class="section__title">What Cat Parents Say</h2>
        </div>

        <div class="cards cards--grid testimonials__grid">
          <article class="card testimonial-card">
            <div class="testimonial-card__stars" aria-label="5 out of 5 stars">
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
            </div>
            <blockquote class="testimonial-card__quote">
              “The team treated Luna like family. Daily updates and the sweetest photos—I felt so at ease.”
            </blockquote>
            <div class="testimonial-card__author">
              <img class="testimonial-card__avatar" src="https://placekitten.com/80/80" alt="Avatar of Luna’s parent" width="80" height="80" loading="lazy">
              <span class="testimonial-card__name">Avery P.</span>
            </div>
          </article>

          <article class="card testimonial-card">
            <div class="testimonial-card__stars" aria-label="5 out of 5 stars">
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
            </div>
            <blockquote class="testimonial-card__quote">
              “Bottle‑baby care was incredible. The staff’s knowledge and kindness made all the difference.”
            </blockquote>
            <div class="testimonial-card__author">
              <img class="testimonial-card__avatar" src="https://placekitten.com/81/81" alt="Avatar of Oliver’s parent" width="81" height="81" loading="lazy">
              <span class="testimonial-card__name">Jordan R.</span>
            </div>
          </article>

          <article class="card testimonial-card">
            <div class="testimonial-card__stars" aria-label="4.5 out of 5 stars">
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true" style="opacity:.5"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
            </div>
            <blockquote class="testimonial-card__quote">
              “Clean, calm, and so thoughtful. Maple came home relaxed and happy every time.”
            </blockquote>
            <div class="testimonial-card__author">
              <img class="testimonial-card__avatar" src="https://placekitten.com/82/82" alt="Avatar of Maple’s parent" width="82" height="82" loading="lazy">
              <span class="testimonial-card__name">Casey M.</span>
            </div>
          </article>

          <article class="card testimonial-card">
            <div class="testimonial-card__stars" aria-label="5 out of 5 stars">
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
              <svg class="icon icon--star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.1 6.3 7 .9-5 4.9 1.2 6.9L12 17l-6.3 4 1.2-6.9-5-4.9 7-.9L12 2z"/></svg>
            </div>
            <blockquote class="testimonial-card__quote">
              “Thoughtful updates and the kindest team. We booked our next visit before picking Theo up!”
            </blockquote>
            <div class="testimonial-card__author">
              <img class="testimonial-card__avatar" src="https://placekitten.com/83/83" alt="Avatar of Theo’s parent" width="83" height="83" loading="lazy">
              <span class="testimonial-card__name">Morgan L.</span>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section id="faqs" class="section faqs">
      <div class="faqs__inner container">
        <div class="section__header">
          <h2 class="section__title">FAQs</h2>
          <p class="section__lead">Answers to common questions from cat parents.</p>
        </div>
        <div class="faqs__items">
          <details class="faq">
            <summary class="faq__summary">What vaccinations are required?</summary>
            <div class="faq__content">
              <p>For kittens old enough, we require age‑appropriate vaccines per vet guidance. Bottle babies follow individualized care plans.</p>
            </div>
          </details>
          <details class="faq">
            <summary class="faq__summary">What should I bring for daycare or boarding?</summary>
            <div class="faq__content">
              <p>Bring your kitten’s food, any medications, and a small comfort item. We provide beds, toys, and water bowls.</p>
            </div>
          </details>
          <details class="faq">
            <summary class="faq__summary">How do I book a visit?</summary>
            <div class="faq__content">
              <p>Use the form below to request a date and time. We’ll confirm within one business day.</p>
            </div>
          </details>
          <details class="faq">
            <summary class="faq__summary">Can I tour the nursery?</summary>
            <div class="faq__content">
              <p>Yes! We offer scheduled tours to keep the environment calm. Please book ahead to reserve a quiet window.</p>
            </div>
          </details>
          <details class="faq">
            <summary class="faq__summary">What are your health and cleanliness protocols?</summary>
            <div class="faq__content">
              <p>We follow vet‑advised sanitation routines, air purification, and health checks. Spaces are cleaned between groups and throughout the day.</p>
            </div>
          </details>
          <details class="faq">
            <summary class="faq__summary">Do you offer updates during stays?</summary>
            <div class="faq__content">
              <p>Absolutely. Expect daily notes and photos, with video updates available for overnight guests.</p>
            </div>
          </details>
        </div>
      </div>
    </section>

    <section id="contact" class="section contact">
      <div class="contact__inner container">
        <div class="contact__grid">
          <div class="contact__info">
            <h2 class="section__title">Get in Touch</h2>
            <address class="contact__address">
              <p><strong>Address:</strong> 123 Whisker Way, Suite 4, Purrville, PA 19000</p>
              <p><strong>Hours:</strong> Mon–Sat 9:00am–6:00pm • Sun by appointment</p>
              <p><strong>Email:</strong> <a href="mailto:hello@purrfectbeginnings.example" class="link">hello@purrfectbeginnings.example</a></p>
              <p><strong>Phone:</strong> <a href="tel:+15551234567" class="link">(555) 123‑4567</a></p>
            </address>
            <ul class="social social--list" role="list" aria-label="Social media">
              <li><a class="social__link" href="#" aria-label="Follow on Instagram">Instagram</a></li>
              <li><a class="social__link" href="#" aria-label="Follow on Facebook">Facebook</a></li>
              <li><a class="social__link" href="#" aria-label="Follow on TikTok">TikTok</a></li>
            </ul>

            <div class="contact__map">
              <div class="map" role="img" aria-label="Map placeholder of Purrville location"></div>
              <p><a class="link" href="https://maps.google.com?q=123+Whisker+Way+Purrville+PA+19000" target="_blank" rel="noopener">Open in Google Maps</a></p>
            </div>
          </div>

          <div class="contact__form">
            <h3 class="contact__form-title">Request a Visit</h3>
            <form class="form" action="#" method="post" aria-label="Request a Visit form">
              <div class="form__field">
                <label class="form__label" for="parent-name">Parent Name</label>
                <input class="form__input" type="text" id="parent-name" name="parent_name" placeholder="Your full name" required>
              </div>
              <div class="form__field">
                <label class="form__label" for="email">Email</label>
                <input class="form__input" type="email" id="email" name="email" placeholder="you@example.com" required>
              </div>
              <div class="form__field">
                <label class="form__label" for="phone">Phone</label>
                <input class="form__input" type="tel" id="phone" name="phone" placeholder="(555) 123‑4567" inputmode="tel">
              </div>
              <div class="form__field form__field--split">
                <div class="form__field">
                  <label class="form__label" for="date">Preferred Date</label>
                  <input class="form__input" type="date" id="date" name="preferred_date" required>
                </div>
                <div class="form__field">
                  <label class="form__label" for="time">Preferred Time</label>
                  <input class="form__input" type="time" id="time" name="preferred_time" required>
                </div>
              </div>
              <div class="form__field">
                <label class="form__label" for="message">Message</label>
                <textarea class="form__textarea" id="message" name="message" placeholder="Tell us about your kitten and any special notes" rows="5"></textarea>
              </div>
              <div class="form__actions">
                <button class="button button--primary" type="submit">Request a Visit</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer" role="contentinfo">
    <div class="footer__inner container">
      <div class="footer__brand">
        <a href="#home" class="brand brand--footer" aria-label="Purrfect Beginnings Home">
          <span class="brand__mark" aria-hidden="true">
            <svg class="icon icon--paw" viewBox="0 0 64 64" width="24" height="24" aria-hidden="true" focusable="false">
              <path d="M31 28c-6 0-11 5-11 11 0 7 7 12 11 12s11-5 11-12c0-6-5-11-11-11zm-15-5c3 0 6-3 6-6s-3-6-6-6-6 3-6 6 3 6 6 6zm30 0c3 0 6-3 6-6s-3-6-6-6-6 3-6 6 3 6 6 6zM18 30c2 0 4-2 4-4s-2-5-4-5-5 3-5 5 3 4 5 4zm28 0c2 0 5-2 5-4s-3-5-5-5-4 3-4 5 2 4 4 4z" />
            </svg>
          </span>
          <span class="brand__text">Purrfect Beginnings</span>
        </a>
      </div>

      <nav class="footer__nav" aria-label="Footer">
        <ul class="footer__list">
          <li><a class="footer__link" href="#about">About</a></li>
          <li><a class="footer__link" href="#services">Services</a></li>
          <li><a class="footer__link" href="#kittens">Kittens</a></li>
          <li><a class="footer__link" href="#contact">Contact</a></li>
        </ul>
      </nav>

      <ul class="footer__social" role="list" aria-label="Social media">
        <li><a class="social__link" href="#" aria-label="Instagram">Instagram</a></li>
        <li><a class="social__link" href="#" aria-label="Facebook">Facebook</a></li>
        <li><a class="social__link" href="#" aria-label="TikTok">TikTok</a></li>
      </ul>

      <div class="footer__meta">
        <a class="footer__top" href="#home" aria-label="Back to top">Back to top ↑</a>
        <p class="footer__copy">© <span id="year"></span> Purrfect Beginnings. All rights reserved.</p>
      </div>
    </div>

    <svg class="footer__decor" viewBox="0 0 120 60" aria-hidden="true" focusable="false">
      <circle cx="20" cy="20" r="6"></circle>
      <circle cx="35" cy="15" r="5"></circle>
      <circle cx="50" cy="20" r="6"></circle>
      <circle cx="30" cy="35" r="10"></circle>
      <path d="M90 50s-7.5-4.7-9.7-8.6C78.6 38.3 80 35 83 35c2.3 0 3.3 1.4 4 2.2.7-.8 1.7-2.2 4-2.2 3 0 4.4 3.3 2.7 6.4C97.5 45.3 90 50 90 50z"></path>
    </svg>
  </footer>

  <script>
    (function () {
      const toggle = document.getElementById('menu-toggle');
      const nav = document.getElementById('primary-navigation');
      const year = document.getElementById('year');

      function setYear() {
        if (year) year.textContent = new Date().getFullYear();
      }
      setYear();

      function closeOnEscape(e) {
        if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
          toggle.setAttribute('aria-expanded', 'false');
          nav.classList.remove('is-open');
          toggle.setAttribute('aria-label', 'Open menu');
          toggle.focus();
        }
      }

      toggle.addEventListener('click', function () {
        const expanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', String(!expanded));
        nav.classList.toggle('is-open', !expanded);
        this.setAttribute('aria-label', expanded ? 'Open menu' : 'Close menu');
      });

      document.addEventListener('keydown', closeOnEscape);

      // Close menu when a nav link is clicked (mobile-friendly)
      nav.addEventListener('click', function (e) {
        const link = e.target.closest('a');
        if (link && toggle.getAttribute('aria-expanded') === 'true') {
          toggle.setAttribute('aria-expanded', 'false');
          nav.classList.remove('is-open');
          toggle.setAttribute('aria-label', 'Open menu');
        }
      });
    })();
  </script>
</body>
</html>
```

    ### CSS Code
    ```css
/* ------------------------------
   Purrfect Beginnings — styles.css
   Soft, playful, pastel aesthetic
   ------------------------------ */

/* Fonts (optional) */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

/* CSS Variables */
:root {
  /* Palette */
  --color-bg: #ffffff;
  --color-bg-soft: #fbfbff;
  --color-surface: #ffffff;
  --color-elevated: #ffffff;
  --color-muted: #f3f2fb;
  --color-border: #e8e6f5;

  --color-text: #2a2730;
  --color-text-muted: #5f5b6b;

  --color-primary: #6f6cf6; /* lavender/indigo */
  --color-primary-600: #5d59e9;
  --color-primary-700: #4e4ad6;
  --color-primary-100: #ecebff;

  --color-secondary: #ff82a9; /* rosy pink */
  --color-secondary-600: #f56f98;
  --color-secondary-700: #e65e88;
  --color-secondary-100: #ffe7f0;

  --color-accent: #6bd1c6; /* mint/teal */
  --color-accent-700: #49b7ae;

  --color-success: #52c27f;
  --color-warning: #f2a93b;
  --color-info: #58b0f5;
  --color-danger: #ef5b7b;

  --color-star: #f5b301;

  --shadow-sm: 0 1px 2px rgba(30, 27, 38, 0.06), 0 1px 1px rgba(30, 27, 38, 0.04);
  --shadow-md: 0 6px 16px rgba(30, 27, 38, 0.08), 0 2px 6px rgba(30, 27, 38, 0.05);
  --shadow-lg: 0 14px 30px rgba(30, 27, 38, 0.12), 0 4px 12px rgba(30, 27, 38, 0.08);

  --radius-sm: 10px;
  --radius-md: 14px;
  --radius-lg: 18px;
  --radius-pill: 999px;

  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-7: 1.75rem;
  --space-8: 2rem;
  --space-9: 2.5rem;
  --space-10: 3rem;

  --container-max: 1200px;
  --container-pad: 1rem;

  --focus: 2px solid var(--color-primary);
  --focus-ring: 0 0 0 3px rgba(111, 108, 246, 0.35);

  --transition-fast: 150ms ease;
  --transition: 220ms cubic-bezier(.2,.7,.3,1);
  --transition-slow: 400ms cubic-bezier(.2,.7,.3,1);
}

/* Reset and base */
*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
  scroll-behavior: smooth;
}

body.page {
  margin: 0;
  color: var(--color-text);
  background: var(--color-bg);
  font-family: "Nunito", ui-rounded, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Apple Color Emoji", "Segoe UI Emoji";
  line-height: 1.6;
  font-size: 16px;
}

img, svg, video, canvas {
  display: block;
  max-width: 100%;
}

svg {
  color: inherit;
  fill: currentColor;
}

.icon {
  width: 1em;
  height: 1em;
  display: inline-block;
  vertical-align: -0.15em;
}

a {
  color: var(--color-primary-700);
  text-decoration: underline;
  text-underline-offset: 0.15em;
}

a:hover {
  color: var(--color-primary);
}

a:focus-visible,
button:focus-visible,
input:focus-visible,
textarea:focus-visible,
select:focus-visible,
summary:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: 10px;
}

.container {
  width: min(100% - (var(--container-pad) * 2), var(--container-max));
  margin-inline: auto;
}

/* Skip link */
.skip-link {
  position: absolute;
  left: -9999px;
  top: auto;
  width: 1px;
  height: 1px;
  overflow: hidden;
}

.skip-link:focus-visible {
  position: fixed;
  left: var(--space-4);
  top: var(--space-4);
  width: auto;
  height: auto;
  padding: var(--space-3) var(--space-5);
  background: var(--color-primary);
  color: #fff;
  border-radius: var(--radius-pill);
  z-index: 10000;
  text-decoration: none;
  box-shadow: var(--shadow-md);
}

/* Sections */
.section {
  padding-block: clamp(2.5rem, 5vw, 5rem);
  background: transparent;
}

.section__header {
  margin-bottom: var(--space-7);
}

.section__title {
  margin: 0 0 var(--space-3);
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  line-height: 1.2;
  letter-spacing: 0.2px;
}

.section__lead {
  margin: 0;
  color: var(--color-text-muted);
  font-size: clamp(1rem, 1.6vw, 1.125rem);
}

/* Utility */
.badge {
  display: inline-block;
  padding: 0.35rem 0.6rem;
  border-radius: var(--radius-pill);
  background: var(--color-primary-100);
  color: var(--color-primary-700);
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: .2px;
}

/* Header */
.header {
  position: relative;
  z-index: 1000;
}

.header--sticky {
  position: sticky;
  top: 0;
  backdrop-filter: saturate(1.2) blur(10px);
  background: color-mix(in srgb, var(--color-bg) 70%, transparent);
  border-bottom: 1px solid rgba(104, 98, 130, 0.06);
}

.header__inner {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding-block: var(--space-3);
  position: relative;
}

/* Brand */
.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  text-decoration: none;
  color: inherit;
  font-weight: 800;
  letter-spacing: .2px;
}

.brand:hover .brand__text {
  color: var(--color-primary-700);
}

.brand__mark {
  display: inline-grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 12px;
  background: radial-gradient(120% 120% at 0% 0%, #fff 0%, var(--color-primary-100) 50%, #ffffff 100%);
  box-shadow: inset 0 0 0 1px var(--color-border), var(--shadow-sm);
  color: var(--color-primary-700);
}

.brand--footer .brand__mark {
  width: 36px;
  height: 36px;
}

/* Header Toggle */
.header__toggle {
  margin-left: auto;
  display: inline-grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: var(--color-muted);
  border: 1px solid var(--color-border);
  color: var(--color-text);
  box-shadow: var(--shadow-sm);
  cursor: pointer;
  transition: background var(--transition), transform var(--transition-fast);
}

.header__toggle:hover {
  background: #efeefd;
}

.header__toggle:active {
  transform: scale(0.98);
}

/* Navigation */
.nav {
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  background: color-mix(in srgb, var(--color-bg) 85%, transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--color-border);
  box-shadow: var(--shadow-md);
  visibility: hidden;
  opacity: 0;
  max-height: 0;
  overflow: hidden;
  transform: translateY(-6px);
  transition: visibility 0s linear .25s, opacity var(--transition), transform var(--transition), max-height var(--transition-slow);
}

.nav.is-open {
  visibility: visible;
  opacity: 1;
  max-height: 80vh;
  transform: translateY(0);
  transition-delay: 0s;
}

.nav__list {
  list-style: none;
  padding: var(--space-4);
  margin: 0;
  display: grid;
  gap: var(--space-2);
}

.nav__item {}

.nav__link {
  display: block;
  text-decoration: none;
  color: var(--color-text);
  padding: .75rem 1rem;
  border-radius: var(--radius-md);
  transition: background var(--transition), color var(--transition), transform var(--transition-fast);
}

.nav__link[aria-current="page"] {
  background: var(--color-primary-100);
  color: var(--color-primary-700);
  font-weight: 700;
}

.nav__link:hover {
  background: var(--color-muted);
  color: var(--color-primary-700);
}

.nav__cta {
  padding: 0 var(--space-4) var(--space-4);
}

/* Buttons */
.button {
  appearance: none;
  border: 0;
  border-radius: var(--radius-pill);
  padding: 0.875rem 1.25rem;
  font-weight: 800;
  letter-spacing: .25px;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  transition: transform var(--transition-fast), box-shadow var(--transition), background var(--transition), color var(--transition), border-color var(--transition);
  will-change: transform;
}

.button--primary {
  background: linear-gradient(180deg, var(--color-primary) 0%, var(--color-primary-600) 100%);
  color: #fff;
  box-shadow: 0 6px 18px rgba(111, 108, 246, .35), inset 0 0 0 1px rgba(255,255,255,.2);
}

.button--primary:hover {
  background: linear-gradient(180deg, var(--color-primary-600) 0%, var(--color-primary-700) 100%);
  transform: translateY(-1px);
  box-shadow: 0 10px 22px rgba(111, 108, 246, .4);
}

.button--primary:active {
  transform: translateY(0);
}

.button--secondary {
  background: linear-gradient(180deg, var(--color-secondary) 0%, var(--color-secondary-600) 100%);
  color: #fff;
  box-shadow: 0 6px 18px rgba(245, 111, 152, .28), inset 0 0 0 1px rgba(255,255,255,.2);
}

.button--secondary:hover {
  background: linear-gradient(180deg, var(--color-secondary-600) 0%, var(--color-secondary-700) 100%);
  transform: translateY(-1px);
}

.button--outline {
  background: #fff;
  color: var(--color-primary-700);
  border: 2px solid var(--color-primary-600);
  box-shadow: var(--shadow-sm);
}

.button--outline:hover {
  background: var(--color-primary-100);
}

.button:focus-visible {
  box-shadow: var(--focus-ring), 0 0 0 1px rgba(255,255,255,.8) inset;
}

/* Hero */
.hero {
  position: relative;
  overflow: clip;
  background:
    radial-gradient(1200px 500px at 85% -10%, #f0f7ff 0%, rgba(240,247,255,0) 60%),
    radial-gradient(700px 400px at -10% 20%, #fff7fb 0%, rgba(255,247,251,0) 60%),
    linear-gradient(180deg, var(--color-bg-soft) 0%, #ffffff 100%);
}

.hero__inner {
  display: grid;
  gap: var(--space-8);
  align-items: center;
}

.hero__title {
  font-size: clamp(2rem, 5vw, 3rem);
  line-height: 1.1;
  margin: 0 0 var(--space-3);
  letter-spacing: .3px;
}

.hero__subtitle {
  margin: 0 0 var(--space-5);
  color: var(--color-text-muted);
  font-size: clamp(1.05rem, 2.2vw, 1.2rem);
}

.hero__actions {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
  margin-bottom: var(--space-5);
}

.hero__proof {
  display: flex;
  gap: var(--space-5);
  align-items: center;
  padding: 0;
  margin: 0;
  list-style: none;
  color: var(--color-text-muted);
}

.proof__item {
  display: inline-flex;
  gap: .5rem;
  align-items: center;
  font-weight: 700;
}

.stars {
  display: inline-flex;
  gap: 2px;
  color: var(--color-star);
}

.hero__media {
  position: relative;
}

.hero__image {
  border-radius: clamp(14px, 2vw, 22px);
  box-shadow: var(--shadow-lg);
  animation: float 8s ease-in-out infinite;
  border: 1px solid var(--color-border);
  background: #fff;
  will-change: transform, box-shadow;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

.hero__decor {
  position: absolute;
  opacity: .35;
  color: var(--color-secondary-600);
}

.hero__decor--paws {
  right: -10px;
  top: -10px;
  width: 120px;
  height: 60px;
  color: var(--color-accent);
}

.hero__decor--heart {
  left: -12px;
  bottom: -12px;
  width: 60px;
  height: 60px;
  color: var(--color-secondary);
  animation: bob 6s ease-in-out infinite;
}

@keyframes bob {
  0%, 100% { transform: translateY(0) rotate(-8deg); }
  50% { transform: translateY(-6px) rotate(-5deg); }
}

/* About - Pillars */
.pillars {
  list-style: none;
  padding: 0;
  margin: var(--space-6) 0 0;
  display: grid;
  gap: var(--space-4);
}

.pillars__item {
  display: grid;
  grid-template-columns: 52px 1fr;
  gap: var(--space-3);
  align-items: start;
  padding: var(--space-4);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: linear-gradient(180deg, #fff 0%, #fdfcff 100%);
  box-shadow: var(--shadow-sm);
}

.pillars__icon {
  display: inline-grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 14px;
  background: var(--color-primary-100);
  color: var(--color-primary-700);
  box-shadow: inset 0 0 0 1px var(--color-border);
}

.pillars__title {
  margin: 0 0 .25rem;
  font-size: 1.05rem;
}

.pillars__desc {
  margin: 0;
  color: var(--color-text-muted);
}

/* Cards */
.cards--grid {
  display: grid;
  gap: var(--space-4);
}

.card {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-surface);
  box-shadow: var(--shadow-sm);
  padding: var(--space-5);
  transition: transform var(--transition), box-shadow var(--transition), border-color var(--transition);
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  border-color: #dedbf1;
}

/* Services */
.service-card__icon {
  display: inline-grid;
  place-items: center;
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: var(--color-secondary-100);
  color: var(--color-secondary-700);
  margin-bottom: var(--space-4);
  box-shadow: inset 0 0 0 1px var(--color-border);
}

.service-card__title {
  margin: 0 0 .5rem;
  font-size: 1.2rem;
}

.service-card__desc {
  margin: 0 0 1rem;
  color: var(--color-text-muted);
}

.service-card__link {
  color: var(--color-primary-700);
  font-weight: 800;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  position: relative;
}

.service-card__link::after {
  content: '→';
  transition: transform var(--transition);
}

.service-card__link:hover::after {
  transform: translateX(2px);
}

/* Kittens */
.kitten-card {
  padding: 0;
  overflow: hidden;
}

.kitten-card__media {
  position: relative;
  aspect-ratio: 21/15;
  background: #f7f7fb;
}

.kitten-card__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.kitten-card__status {
  position: absolute;
  left: .75rem;
  top: .75rem;
  padding: .35rem .6rem;
  border-radius: var(--radius-pill);
  font-weight: 800;
  font-size: .85rem;
  color: #fff;
  box-shadow: var(--shadow-sm);
}

.kitten-card__status--ready { background: var(--color-success); }
.kitten-card__status--soon { background: var(--color-warning); }
.kitten-card__status--special { background: var(--color-danger); }

.kitten-card__body {
  padding: var(--space-4);
}

.kitten-card__name {
  margin: 0 0 .25rem;
  font-size: 1.15rem;
}

.kitten-card__meta {
  margin: 0 0 .75rem;
  color: var(--color-text-muted);
}

.kitten-card__tags {
  display: flex;
  gap: .5rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.tag {
  padding: .35rem .6rem;
  border-radius: var(--radius-pill);
  font-weight: 700;
  font-size: .85rem;
  background: var(--color-muted);
  color: var(--color-text);
  border: 1px solid var(--color-border);
}

.kittens__actions {
  margin-top: var(--space-6);
  display: flex;
  justify-content: center;
}

/* Gallery */
.gallery {
  background: linear-gradient(180deg, #ffffff 0%, #fcfbff 100%);
}

.mosaic {
  display: grid;
  gap: var(--space-3);
  grid-template-columns: repeat(2, 1fr);
}

.mosaic__item {
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-sm);
  background: #fff;
}

.mosaic__item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Testimonials */
.testimonial-card {
  display: grid;
  gap: var(--space-4);
}

.testimonial-card__stars {
  color: var(--color-star);
  display: inline-flex;
  gap: 2px;
}

.testimonial-card__quote {
  margin: 0;
  font-size: 1.05rem;
}

.testimonial-card__author {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.testimonial-card__avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #fff;
  box-shadow: var(--shadow-sm);
}

/* FAQs */
.faqs__items {
  display: grid;
  gap: var(--space-3);
}

.faq {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: #fff;
  box-shadow: var(--shadow-sm);
  overflow: hidden;
}

.faq__summary {
  list-style: none;
  cursor: pointer;
  padding: var(--space-4) var(--space-5);
  margin: 0;
  font-weight: 800;
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  gap: var(--space-4);
}

.faq__summary::-webkit-details-marker {
  display: none;
}

.faq__summary::after {
  content: '▾';
  display: inline-block;
  transition: transform var(--transition);
  color: var(--color-primary-700);
}

.faq[open] .faq__summary::after {
  transform: rotate(180deg);
}

.faq__content {
  padding-inline: var(--space-5);
  overflow: hidden;
  max-height: 0;
  color: var(--color-text-muted);
  transition: max-height var(--transition-slow), padding-block var(--transition);
}

.faq[open] .faq__content {
  padding-block: 0 1rem;
  max-height: 300px;
}

/* Contact */
.contact__grid {
  display: grid;
  gap: var(--space-6);
}

.contact__address p {
  margin: 0 0 .5rem;
}

.social--list {
  display: flex;
  gap: var(--space-4);
  padding: 0;
  margin: var(--space-4) 0 var(--space-5);
  list-style: none;
}

.social__link {
  text-decoration: none;
  font-weight: 800;
  color: var(--color-primary-700);
  padding: .4rem .75rem;
  border-radius: var(--radius-pill);
  background: var(--color-primary-100);
  border: 1px solid var(--color-border);
  transition: transform var(--transition-fast), background var(--transition);
}

.social__link:hover {
  background: #e6e5ff;
  transform: translateY(-1px);
}

/* Map placeholder */
.map {
  width: 100%;
  height: 220px;
  border-radius: var(--radius-md);
  background:
    radial-gradient(80% 60% at 20% 20%, #f0f7ff 0%, transparent 60%),
    radial-gradient(60% 50% at 80% 30%, #fff7fb 0%, transparent 60%),
    linear-gradient(180deg, #fafbff 0%, #ffffff 100%);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-sm);
}

/* Form */
.form {
  display: grid;
  gap: var(--space-4);
  padding: var(--space-5);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: linear-gradient(180deg, #ffffff 0%, #fdfcff 100%);
  box-shadow: var(--shadow-sm);
}

.form__field {
  display: grid;
  gap: .5rem;
}

.form__field--split {
  display: grid;
  gap: var(--space-4);
}

.form__label {
  font-weight: 700;
}

.form__input,
.form__textarea,
select.form__input {
  appearance: none;
  width: 100%;
  padding: .8rem 1rem;
  border-radius: 14px;
  border: 1px solid var(--color-border);
  background: #fff;
  color: var(--color-text);
  font: inherit;
  line-height: 1.4;
  box-shadow: inset 0 2px 4px rgba(30,27,38,0.04);
  transition: border-color var(--transition), box-shadow var(--transition), background var(--transition);
}

.form__input::placeholder,
.form__textarea::placeholder {
  color: #9b96ac;
}

.form__input:focus,
.form__textarea:focus {
  outline: none;
  border-color: var(--color-primary-600);
  box-shadow: var(--focus-ring), inset 0 2px 6px rgba(30,27,38,0.04);
}

.form__textarea {
  resize: vertical;
  min-height: 140px;
}

.form__actions {
  display: flex;
  justify-content: flex-start;
}

/* Footer */
.footer {
  margin-top: var(--space-8);
  border-top: 1px solid var(--color-border);
  background: linear-gradient(180deg, #ffffff 0%, #faf8ff 100%);
  position: relative;
}

.footer__inner {
  display: grid;
  gap: var(--space-6);
  padding-block: var(--space-6);
  align-items: start;
}

.footer__nav .footer__list {
  display: flex;
  gap: var(--space-4);
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer__link {
  text-decoration: none;
  color: var(--color-text);
  font-weight: 700;
  padding: .25rem .5rem;
  border-radius: 8px;
  transition: background var(--transition), color var(--transition);
}

.footer__link:hover {
  color: var(--color-primary-700);
  background: var(--color-muted);
}

.footer__social {
  display: flex;
  gap: var(--space-3);
  padding: 0;
  margin: 0;
}

.footer__top {
  text-decoration: none;
  font-weight: 800;
  color: var(--color-primary-700);
}

.footer__copy {
  color: var(--color-text-muted);
}

.footer__decor {
  position: absolute;
  right: 1rem;
  bottom: .5rem;
  width: 120px;
  height: 60px;
  color: var(--color-accent);
  opacity: .25;
}

/* Link variants inside content */
.link {
  text-decoration: underline;
  text-underline-offset: 0.2em;
  font-weight: 700;
}

/* Icons default color */
.icon--star { color: var(--color-star); }
.icon--heart { color: var(--color-secondary-600); }
.icon--paw { color: var(--color-primary-700); }

/* Proof text */
.proof__text {
  font-weight: 800;
  color: var(--color-text);
}

/* Accessibility: focus visible for nav links */
.nav__link:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
}

/* Responsive Layouts */

/* >= 600px */
@media (min-width: 600px) {
  .cards--grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .mosaic {
    grid-template-columns: repeat(3, 1fr);
  }

  .form__field--split {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* >= 900px */
@media (min-width: 900px) {
  .header__inner {
    padding-block: var(--space-4);
  }

  .header__toggle {
    display: none;
  }

  .nav {
    all: unset;
    display: flex;
    align-items: center;
    margin-left: auto;
  }

  .nav__list {
    all: unset;
    display: flex;
    gap: var(--space-2);
  }

  .nav__link {
    padding: .6rem .9rem;
    border-radius: var(--radius-pill);
  }

  .nav__cta {
    padding: 0 0 0 var(--space-3);
  }

  .hero__inner {
    grid-template-columns: 1.05fr .95fr;
    gap: var(--space-10);
  }

  .pillars {
    grid-template-columns: repeat(3, 1fr);
  }

  .cards--grid.services__grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .cards--grid.kittens__grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .cards--grid.testimonials__grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .contact__grid {
    grid-template-columns: 1fr 1.1fr;
    align-items: start;
  }

  .mosaic {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* >= 1200px */
@media (min-width: 1200px) {
  .hero__title {
    font-size: 3.25rem;
  }

  .cards--grid.kittens__grid {
    grid-template-columns: repeat(6, 1fr);
  }

  .cards--grid.testimonials__grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* Animations: reduce motion preference */
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .hero__image,
  .hero__decor--heart {
    animation: none;
  }
  .button,
  .card,
  .nav,
  .faq__content {
    transition: none !important;
  }
}

```

    
