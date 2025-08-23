# Indo-Chinese 3-Recipe Website

Save the code below as index.html and open in your browser.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Indo‑Chinese Dinner Tonight — 3 Quick Recipes</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
  <style>
    :root{
      --bg:#0b0f12;
      --card:#11171b;
      --text:#e8edf2;
      --muted:#a8b3bd;
      --accent:#ff3b30; /* chili red */
      --accent2:#2dd4bf; /* jade */
      --border:#1f2a31;
      --shadow: 0 10px 30px rgba(0,0,0,.35);
    }
    *{box-sizing:border-box}
    html,body{margin:0;background:linear-gradient(180deg,#0b0f12 0%, #0d1216 100%);color:var(--text);font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;line-height:1.55}
    a{color:var(--accent2);text-decoration:none}
    a:hover{text-decoration:underline}
    .container{max-width:1100px;margin:auto;padding:24px}
    header.site{
      position:sticky;top:0;z-index:10;
      backdrop-filter:saturate(1.2) blur(8px);
      background:rgba(11,15,18,.65);
      border-bottom:1px solid var(--border);
    }
    .site-inner{display:flex;align-items:center;gap:18px;justify-content:space-between}
    .brand{display:flex;align-items:center;gap:10px}
    .logo{width:36px;height:36px;border-radius:10px;background:conic-gradient(from 20deg,var(--accent),#ff7b54 30%,#ffc857 60%,var(--accent2));box-shadow:0 0 0 3px rgba(255,255,255,.04)}
    .brand b{font-weight:800;letter-spacing:.3px}
    nav ul{display:flex;gap:18px;list-style:none;margin:0;padding:0}
    nav a{color:var(--text);opacity:.9}
    .hero{padding:56px 24px 28px}
    .hero h1{font-family:"Playfair Display",serif;font-size:clamp(28px,4vw,44px);margin:0 0 10px;letter-spacing:.2px}
    .hero p{color:var(--muted);margin:0 0 18px}
    .cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:8px}
    .btn{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--border);background:var(--card);color:var(--text);padding:10px 14px;border-radius:10px;box-shadow:var(--shadow)}
    .btn.primary{background:linear-gradient(135deg,var(--accent) 0%, #ff8c66 100%);color:white;border:none}
    .grid{display:grid;grid-template-columns:repeat(12,1fr);gap:22px}
    .card{grid-column:span 12;background:linear-gradient(180deg,rgba(255,255,255,.02),rgba(255,255,255,.01));border:1px solid var(--border);border-radius:16px;box-shadow:var(--shadow);overflow:hidden}
    .card-inner{padding:20px}
    .label{display:inline-block;font-size:12px;text-transform:uppercase;letter-spacing:.12em;color:white;background:linear-gradient(135deg,var(--accent) 0%, #ff8c66 100%);padding:6px 10px;border-radius:999px;margin-bottom:8px}
    h2{margin:6px 0 8px;font-size:clamp(22px,2.8vw,30px)}
    .meta{display:flex;flex-wrap:wrap;gap:10px;color:var(--muted);font-size:14px;margin:0 0 12px}
    .meta span{display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border:1px dashed var(--border);border-radius:999px}
    .split{display:grid;grid-template-columns:1fr;gap:18px}
    @media(min-width:860px){.split{grid-template-columns:1fr 1fr}}
    h3{margin:12px 0 8px;font-size:18px}
    ul,ol{margin:0 0 10px 18px}
    li{margin:6px 0}
    .tip{margin-top:10px;padding:12px 14px;border:1px solid var(--border);background:rgba(45,212,191,.08);border-radius:12px;color:#bff7ee}
    .note{color:var(--muted);font-size:14px}
    .footer{margin-top:28px;color:var(--muted);text-align:center;border-top:1px solid var(--border);padding:20px}
    .tag{color:white;background:linear-gradient(135deg,var(--accent2),#7cf7e7);padding:2px 10px;border-radius:999px;font-size:12px}
    .shopping{grid-column:span 12}
    .recipe{grid-column:span 12}
    @media(min-width:960px){
      .recipe{grid-column:span 6}
    }
    .steps li{padding-left:4px}
    .badge{font-size:12px;color:#111;background:#ffe27a;border-radius:6px;padding:2px 6px;margin-left:6px}
    .print{float:right}
    .print button{background:transparent;border:1px solid var(--border);color:var(--text);padding:6px 10px;border-radius:8px}
    .print button:hover{border-color:#2a3942}
    /* anchor spacing */
    .anchor{scroll-margin-top:96px}

    /* Print */
    @media print{
      header.site,.cta,.print,.footer{display:none !important}
      body{background:white;color:#111}
      .card{box-shadow:none;border:1px solid #ddd}
    }
  </style>
</head>
<body>
  <header class="site">
    <div class="container site-inner">
      <div class="brand">
        <div class="logo" aria-hidden="true"></div>
        <b>Indo‑Chinese Tonight</b>
      </div>
      <nav aria-label="Site">
        <ul>
          <li><a href="#recipes">Recipes</a></li>
          <li><a href="#shopping-list">Shopping List</a></li>
          <li><a href="#plan">Plan</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <section class="hero container">
    <h1>3 Indo‑Chinese crowd‑pleasers for tonight</h1>
    <p>Starter to main in under 90 minutes: Veg Manchow Soup, Chilli Paneer (gravy), and Vegetable Hakka Noodles.</p>
    <div class="cta">
      <a class="btn primary" href="#recipes">Jump to Recipes</a>
      <a class="btn" href="#shopping-list">Get Shopping List</a>
    </div>
  </section>

  <main class="container grid" id="recipes">
    <!-- Recipe 1: Veg Manchow Soup -->
    <article class="card recipe anchor" id="manchow-soup">
      <div class="card-inner">
        <div class="print"><button onclick="window.print()" aria-label="Print recipe">Print</button></div>
        <span class="label">Starter</span>
        <h2>Veg Manchow Soup <span class="badge">Vegan‑friendly</span></h2>
        <p class="note">A hearty, peppery Indo‑Chinese soup topped with crunchy fried noodles.</p>
        <div class="meta">
          <span>Prep: 10 min</span>
          <span>Cook: 15 min</span>
          <span>Serves: 4</span>
          <span>Heat: Medium</span>
        </div>
        <div class="split">
          <div>
            <h3>Ingredients</h3>
            <ul>
              <li>2 tbsp oil</li>
              <li>5 cloves garlic, finely chopped</li>
              <li>1 tbsp ginger, finely chopped</li>
              <li>1–2 green chillies, slit</li>
              <li>3 spring onions, whites + greens separated, chopped</li>
              <li>1/3 cup carrot, very finely chopped</li>
              <li>1/3 cup cabbage, very finely shredded</li>
              <li>1/3 cup capsicum, finely chopped</li>
              <li>1/3 cup mushrooms, finely chopped (optional)</li>
              <li>3 cups vegetable stock or water</li>
              <li>1.5 tbsp soy sauce (light)</li>
              <li>1 tbsp vinegar</li>
              <li>1–2 tsp red chilli sauce (to taste)</li>
              <li>1/2 tsp black pepper, freshly ground</li>
              <li>Salt to taste</li>
              <li>2 tbsp cornflour mixed with 3 tbsp water (slurry)</li>
              <li>1 cup fried noodles, for topping</li>
              <li>Fresh coriander & spring onion greens, to garnish</li>
            </ul>
          </div>
          <div>
            <h3>Steps</h3>
            <ol class="steps">
              <li>Heat oil in a pot on medium‑high. Add garlic, ginger, and chillies; sauté 30–40 seconds until fragrant.</li>
              <li>Add spring onion whites; sauté 30 seconds. Add carrot, cabbage, capsicum, and mushrooms; stir‑fry 2–3 minutes.</li>
              <li>Pour in stock, soy sauce, vinegar, chilli sauce, and pepper. Bring to a boil, then simmer 3 minutes.</li>
              <li>Whisk the cornflour slurry and stir into the soup. Simmer 2–3 minutes until lightly thickened. Adjust salt.</li>
              <li>Turn off heat; stir in spring onion greens. Ladle into bowls, top generously with fried noodles and coriander.</li>
            </ol>
            <div class="tip">Tip: For extra body, add 1 tsp finely chopped green beans with the other veg. For vegan, ensure noodles are egg‑free.</div>
          </div>
        </div>
      </div>
    </article>

    <!-- Recipe 2: Chilli Paneer (Gravy) -->
    <article class="card recipe anchor" id="chilli-paneer">
      <div class="card-inner">
        <div class="print"><button onclick="window.print()" aria-label="Print recipe">Print</button></div>
        <span class="label">Main</span>
        <h2>Chilli Paneer (Gravy)</h2>
        <p class="note">Soft paneer tossed in a glossy, spicy‑tangy sauce with onions and peppers.</p>
        <div class="meta">
          <span>Prep: 15 min</span>
          <span>Cook: 20 min</span>
          <span>Serves: 4</span>
          <span>Heat: Medium‑High</span>
        </div>
        <div class="split">
          <div>
            <h3>Ingredients</h3>
            <ul>
              <li>400 g paneer, 1‑inch cubes</li>
              <li>2 tbsp cornflour + 1 tbsp all‑purpose flour</li>
              <li>1/2 tsp each: salt, black pepper</li>
              <li>1 tsp soy sauce (for coating)</li>
              <li>3 tbsp oil (for shallow frying)</li>
              <li>1 tbsp oil (for sauce)</li>
              <li>6 cloves garlic, finely chopped</li>
              <li>1 tbsp ginger, finely chopped</li>
              <li>2 green chillies, slit</li>
              <li>1 medium onion, petals</li>
              <li>1 green capsicum + 1 red capsicum, squares</li>
              <li>2 tbsp light soy sauce</li>
              <li>1 tbsp vinegar</li>
              <li>1 tbsp green chilli sauce or schezwan sauce</li>
              <li>1 tbsp tomato ketchup (balance)</li>
              <li>1 tsp sugar (balance)</li>
              <li>1/2 tsp black pepper</li>
              <li>1.25 cups water or stock</li>
              <li>1.5 tbsp cornflour mixed with 2.5 tbsp water (slurry)</li>
              <li>2 tsp sesame oil (finish)</li>
              <li>Spring onion greens, to garnish</li>
            </ul>
          </div>
          <div>
            <h3>Steps</h3>
            <ol class="steps">
              <li>Coat paneer with cornflour, flour, salt, pepper, and 1 tsp soy. Toss to evenly coat.</li>
              <li>Heat 3 tbsp oil in a wide pan. Shallow‑fry paneer on medium until light golden, 3–4 minutes. Remove; keep aside.</li>
              <li>In the same pan, add 1 tbsp oil. Sauté garlic, ginger, and green chillies 30–40 seconds.</li>
              <li>Add onion petals and capsicum; stir‑fry 2 minutes on high (keep them crisp).</li>
              <li>Add light soy, vinegar, chilli sauce, ketchup, sugar, pepper, and water/stock. Bring to a boil.</li>
              <li>Stir in cornflour slurry; simmer 2 minutes until the sauce turns glossy and slightly thick.</li>
              <li>Add fried paneer; toss gently 1–2 minutes to coat. Finish with sesame oil. Check salt/heat and adjust.</li>
              <li>Garnish with spring onion greens. Serve hot with noodles or fried rice.</li>
            </ol>
            <div class="tip">Swap: Use tofu for a vegan version. Air‑fry coated tofu at 200°C/390°F for ~10–12 min, tossing once.</div>
          </div>
        </div>
      </div>
    </article>

    <!-- Recipe 3: Vegetable Hakka Noodles -->
    <article class="card recipe anchor" id="hakka-noodles">
      <div class="card-inner">
        <div class="print"><button onclick="window.print()" aria-label="Print recipe">Print</button></div>
        <span class="label">Main</span>
        <h2>Vegetable Hakka Noodles</h2>
        <p class="note">Springy noodles stir‑fried with crunchy veggies, soy, vinegar, and pepper.</p>
        <div class="meta">
          <span>Prep: 10 min</span>
          <span>Cook: 15 min</span>
          <span>Serves: 4</span>
          <span>Heat: Adjustable</span>
        </div>
        <div class="split">
          <div>
            <h3>Ingredients</h3>
            <ul>
              <li>300 g Hakka noodles (or thin wheat noodles)</li>
              <li>1.5 tbsp oil (plus 1 tsp for noodles)</li>
              <li>5 cloves garlic, finely chopped</li>
              <li>1 tsp ginger, finely chopped</li>
              <li>1–2 green chillies, slit</li>
              <li>3 spring onions, whites + greens separated, chopped</li>
              <li>1 cup cabbage, shredded</li>
              <li>1/2 cup carrot, julienned</li>
              <li>1/2 cup capsicum, thin strips</li>
              <li>1/3 cup green beans, thinly sliced (optional)</li>
              <li>1.5 tbsp light soy sauce</li>
              <li>1 tbsp vinegar</li>
              <li>1–2 tsp green chilli sauce (optional)</li>
              <li>1/2 tsp black pepper</li>
              <li>Salt to taste</li>
              <li>1 tsp toasted sesame oil (finish)</li>
            </ul>
          </div>
          <div>
            <h3>Steps</h3>
            <ol class="steps">
              <li>Boil noodles in salted water until just al dente. Drain, rinse quickly, and toss with 1 tsp oil. Set aside.</li>
              <li>Heat a wok on high until smoking. Add 1.5 tbsp oil, then garlic, ginger, and chillies; sauté 20–30 seconds.</li>
              <li>Add spring onion whites, cabbage, carrot, capsicum, and beans; stir‑fry 2–3 minutes on high (crisp‑tender).</li>
              <li>Add noodles, soy, vinegar, chilli sauce, pepper, and salt. Toss rapidly 1–2 minutes to coat without breaking.</li>
              <li>Finish with sesame oil and spring onion greens. Serve hot with Chilli Paneer.</li>
            </ol>
            <div class="tip">Tip: Keep heat high and avoid crowding the wok to prevent soggy noodles. Work in batches if needed.</div>
          </div>
        </div>
      </div>
    </article>

    <!-- Shopping List -->
    <section class="card shopping anchor" id="shopping-list">
      <div class="card-inner">
        <span class="label">Shopping</span>
        <h2>Consolidated Shopping List <span class="tag">3 recipes</span></h2>
        <div class="split">
          <div>
            <h3>Produce</h3>
            <ul>
              <li>Garlic (16+ cloves)</li>
              <li>Ginger (2–3 inch piece)</li>
              <li>Green chillies (6–8)</li>
              <li>Spring onions (2 bunches)</li>
              <li>Onion (1 medium)</li>
              <li>Carrots (3–4)</li>
              <li>Cabbage (1 small)</li>
              <li>Capsicum/bell peppers (3–4, mixed colors)</li>
              <li>Green beans (1 small handful, optional)</li>
              <li>Mushrooms (1 small pack, optional)</li>
              <li>Coriander (small bunch)</li>
            </ul>
            <h3>Pantry & Sauces</h3>
            <ul>
              <li>Light soy sauce</li>
              <li>Vinegar (white or rice)</li>
              <li>Red/green chilli sauce (or schezwan)</li>
              <li>Tomato ketchup</li>
              <li>Black pepper</li>
              <li>Sugar</li>
              <li>Vegetable stock cubes or broth</li>
              <li>Cornflour (cornstarch)</li>
              <li>All‑purpose flour (maida)</li>
              <li>Sesame oil</li>
              <li>Neutral cooking oil</li>
              <li>Salt</li>
            </ul>
          </div>
          <div>
            <h3>Protein & Grains</h3>
            <ul>
              <li>Paneer (400 g) or firm tofu (for vegan swap)</li>
              <li>Hakka noodles (300 g)</li>
              <li>Fried noodles (for soup topping) — or make by frying thin noodles</li>
            </ul>
            <div class="tip">Make ahead: Chop all veggies and mix all sauces for each dish in small bowls before you start cooking to keep the wok moving fast.</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Plan & Timing -->
    <section class="card anchor" id="plan">
      <div class="card-inner">
        <span class="label">Plan</span>
        <h2>Tonight’s Flow (≈75–90 minutes)</h2>
        <ol class="steps">
          <li>Prep all chopping first (15–20 min). Boil noodles and set aside.</li>
          <li>Start Manchow Soup (15–20 min). Keep warm.</li>
          <li>Shallow‑fry paneer and set aside (10 min).</li>
          <li>Stir‑fry Hakka Noodles (10–12 min).</li>
          <li>Finish Chilli Paneer gravy and toss paneer in (10–12 min). Serve immediately.</li>
        </ol>
        <p class="note">Serve order: Soup → Hakka Noodles + Chilli Paneer. Adjust chilli and soy to taste as brands vary in saltiness/heat.</p>
      </div>
    </section>

  </main>

  <footer class="footer">
    Cooked with spice and speed. Happy cooking!
  </footer>
</body>
</html>
```
