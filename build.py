S=[
dict(k='spring',fr='Printemps',name='Quatréa Printemps',bg='#f3ece4',ink='#2d3a2e',acc='#d98ca0',liq1='#f6c6d0',liq2='#e58ba3',cap='#9fb59a',tag='Eau de Parfum · No. I',line='Dew on the first open window.',
 mood='“A garden that wakes before you do — petals heavy with rain, light the colour of a first promise.”',
 top=('Pear blossom & bergamot','A green, sparkling opening — cold fruit and citrus rind, like stepping barefoot onto wet grass.'),
 heart=('Peony & lily of the valley','The bloom arrives: soft petals, creamy and luminous, never sweet.'),
 base=('White musk & cedar moss','A clean skin-like whisper that lingers until the light changes.'),word='Bloom'),
dict(k='summer',fr='Été',name='Quatréa Été',bg='#f2d6a2',ink='#3b1f0e',acc='#e0662f',liq1='#ffd27a',liq2='#f08a3c',cap='#c4572a',tag='Eau de Parfum · No. II',line='Salt, sun and an endless afternoon.',
 mood='“Golden hour on a Mediterranean terrace — warm stone, sea air, and fig leaves crushed between the fingers.”',
 top=('Blood orange & sea salt','Bright, juicy and mineral — a splash of citrus carried on an ocean breeze.'),
 heart=('Neroli & fig leaf','Sunlit orange blossom meets the milky green of a fig tree at noon.'),
 base=('Amber & driftwood','Warm skin, sand-dried wood, the slow glow after sunset.'),word='Soleil'),
dict(k='autumn',fr='Automne',name='Quatréa Automne',bg='#3a1d14',ink='#f1dcc4',acc='#d0893f',liq1='#b5542a',liq2='#6e2312',cap='#d0893f',tag='Eau de Parfum · No. III',line='Leaves turning, candles lit.',
 mood='“Late October in an old library — leather chairs, spiced tea, and rain tapping the copper windows.”',
 top=('Saffron & pink pepper','A spiced, glowing opening that warms like the first sip of chai.'),
 heart=('Plum & smoked rose','Dark fruit folded into a velvet rose, slightly smoky, deeply romantic.'),
 base=('Oud, leather & tonka','Rich, enveloping, a fireside embrace that lasts into the night.'),word='Ember'),
dict(k='winter',fr='Hiver',name='Quatréa Hiver',bg='#0e1726',ink='#e6edf5',acc='#9fc3e6',liq1='#d9e8f5',liq2='#7ea6cf',cap='#c9d6e3',tag='Eau de Parfum · No. IV',line='Silence after snowfall.',
 mood='“A midnight forest under fresh snow — frozen pine, distant woodsmoke, the hush of a sleeping world.”',
 top=('Frosted mint & juniper','Crisp, icy and clear — breath visible in the cold air.'),
 heart=('Iris & white tea','A powdery, silvery calm; elegant and introspective.'),
 base=('Vanilla absolute & incense','A quiet warmth beneath the frost, like hands around a candle.'),word='Neige'),
]
def bottle(s,cls='bottle',i=0):
    k=s['k']
    shapes={ # body path per season
     'spring':'M40 140 Q20 150 20 190 L20 330 Q20 360 50 360 L150 360 Q180 360 180 330 L180 190 Q180 150 160 140 Z',
     'summer':'M100 130 C30 130 15 210 15 260 C15 330 55 362 100 362 C145 362 185 330 185 260 C185 210 170 130 100 130 Z',
     'autumn':'M30 140 L170 140 L185 360 L15 360 Z',
     'winter':'M100 120 L180 200 L180 330 L100 365 L20 330 L20 200 Z'}
    return f'''<svg class="{cls}" viewBox="0 0 200 380" role="img" aria-label="{s['name']} bottle"><defs>
<linearGradient id="l{k}{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{s['liq1']}" stop-opacity=".85"/><stop offset="1" stop-color="{s['liq2']}"/></linearGradient>
<linearGradient id="g{k}{i}" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".25" stop-color="#fff" stop-opacity="0"/><stop offset=".8" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity=".35"/></linearGradient>
<clipPath id="c{k}{i}"><path d="{shapes[k]}"/></clipPath></defs>
<ellipse cx="100" cy="370" rx="80" ry="6" fill="#000" opacity=".09"/><rect x="72" y="20" width="56" height="78" rx="6" fill="{s['cap']}"/><ellipse cx="100" cy="370" rx="80" ry="7" fill="#000" opacity=".18"/><rect x="72" y="20" width="14" height="78" rx="6" fill="#fff" opacity=".25"/>
<rect x="84" y="98" width="32" height="36" fill="{s['cap']}" opacity=".7"/>
<path d="{shapes[k]}" fill="#fff" fill-opacity="{'.42' if k=='winter' else '.16'}" stroke="#fff" stroke-opacity=".5" stroke-width="2"/>
<g clip-path="url(#c{k}{i})"><rect x="0" y="175" width="200" height="200" fill="url(#l{k}{i})"/><path d="M0 178 Q50 168 100 178 T200 178 V190 H0Z" fill="#fff" opacity=".25"/><rect width="200" height="380" fill="url(#g{k}{i})"/><rect class="shine" x="-60" y="0" width="30" height="380" fill="#fff" opacity=".35" transform="skewX(-20)"/></g><path d="M34 200 Q30 260 36 320" stroke="#fff" stroke-opacity=".6" stroke-width="3" fill="none" stroke-linecap="round"/>
<text x="100" y="262" text-anchor="middle" font-family="Cormorant Garamond,serif" font-size="22" letter-spacing="3" fill="#fff">QUATRÉA</text>
<text x="100" y="286" text-anchor="middle" font-family="Manrope,sans-serif" font-size="9" letter-spacing="4" fill="#fff" opacity=".85">{s['fr'].upper()}</text></svg>'''
LOGO='''<svg viewBox="0 0 220 40" aria-label="Quatréa"><g fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="20" cy="20" r="15"/><path d="M20 5v30M5 20h30"/><circle cx="20" cy="20" r="5" fill="currentColor"/></g><text x="46" y="28" font-family="Cormorant Garamond,serif" font-size="26" letter-spacing="6" fill="currentColor">QUATRÉA</text></svg>'''
def head(title,s=None,desc='Quatréa — Maison de Parfum, Grasse. Four seasons, four Eaux de Parfum: Printemps, Été, Automne, Hiver.',season=''):
    vars=f"--bg:{s['bg']};--ink:{s['ink']};--accent:{s['acc']}" if s else ""
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="{s['bg'] if s else '#0d0b0a'}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Quatréa"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="assets/og.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Manrope:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css"><script src="assets/vendor/gsap.min.js" defer></script><script src="assets/vendor/ScrollTrigger.min.js" defer></script><script src="assets/vendor/lenis.min.js" defer></script><script src="assets/main.js" defer></script></head><body style="{vars}" data-season="{season}"><a class="skip" href="#main">Skip to content</a><div class="cursor" aria-hidden="true"></div><div class="curtain" aria-hidden="true"><svg class="loader" viewBox="0 0 40 40"><circle cx="20" cy="20" r="15" pathLength="1"/><path d="M20 5v30M5 20h30" pathLength="1"/></svg><span>Quatréa</span></div><div class="grain"></div><div class="progress"></div>
<header><nav class="nav" aria-label="Main"><a class="logo" href="index.html" aria-label="Quatréa home">{LOGO}</a><ul><li><a href="spring.html">Spring</a></li><li><a href="summer.html">Summer</a></li><li><a href="autumn.html">Autumn</a></li><li><a href="winter.html">Winter</a></li><li class="hm"><a href="about.html">Maison</a></li></ul></nav></header>'''
FOOT='''<footer class="reveal"><p class="eyebrow">Maison de Parfum · Grasse</p><h3 class="split">Wear the <em>season</em>.</h3><a class="btn magnetic" href="about.html">Our story →</a><small>A design concept by Naveed Zulfiqar · Fictional brand · 2026</small></footer>
<dialog class="modal" aria-labelledby="mt"><form method="dialog" class="mform"><p class="eyebrow">Limited first edition</p><h3 id="mt">Reserve</h3><p class="mprice"></p><label>Name<input name="n" required autocomplete="name"></label><label>E-mail<input name="e" type="email" required autocomplete="email"></label><div class="mact"><button class="btn" value="cancel" formnovalidate type="submit">Close</button><button class="btn solid" value="ok" type="submit">Confirm reservation</button></div></form></dialog><div class="toast" role="status" aria-live="polite"></div></body></html>'''
# index
idx=head('Quatréa — Four Seasons of Fragrance')+f'''<main id="main">
<section class="hero"><div class="orb" style="width:40vw;height:40vw;background:#c9a96e;left:-10vw;top:10vh"></div><div class="orb" style="width:30vw;height:30vw;background:#7ea6cf;right:-5vw;bottom:5vh"></div>
<p class="eyebrow">Maison de Parfum · Est. MMXXVI</p><h1 class="split">Four <em>seasons</em><br>one soul</h1><p>Quatréa bottles the turning of the year — four fragrances, each composed for the light, air and memory of a single season.</p><div class="scrollcue">Scroll</div></section>
<p class="manifesto">We believe scent is time made visible. The first thaw, the long gold of August, the smoke of October, the hush of snow. Each Quatréa is a season you can carry on your skin.</p>
<section class="hwrap"><div class="htrack">'''+''.join(f'''<div class="panel" data-bg="{s['bg']}" data-ink="{s['ink']}" data-accent="{s['acc']}"><div><p class="eyebrow">{s['tag']}</p><h2>{s['fr']}<em>{s['line']}</em></h2><p>{s['top'][0]} · {s['heart'][0]} · {s['base'][0]}</p><a class="btn magnetic" href="{s['k']}.html">Discover {s['k'].title()} →</a></div>{bottle(s,i=0)}</div>''' for s in S)+'''</div></section>
<div class="marquee"><div class="mt">'''+('<span>Printemps</span>·<span>Été</span>·<span>Automne</span>·<span>Hiver</span>·'*4)+'''</div></div>
<section class="facts"><div class="reveal"><b data-count="4">4</b><span>Seasons</span></div><div class="reveal"><b data-count="48">48</b><span>Rare ingredients</span></div><div class="reveal"><b data-count="12" data-suf="h">12h</b><span>Sillage</span></div></section>
</main>'''+FOOT
open('index.html','w').write(idx)
for n,s in enumerate(S):
    nx=S[(n+1)%4]
    tri=f'''<svg class="tri" viewBox="0 0 300 260"><path data-t="0" d="M150 10 L205 95 L95 95Z" fill="{s['acc']}"/><path data-t="1" d="M90 105 L210 105 L262 185 L38 185Z" fill="{s['acc']}" opacity=".18"/><path data-t="2" d="M32 195 L268 195 L300 250 L0 250Z" fill="{s['acc']}" opacity=".18"/></svg>'''
    pg=head(s['name']+' — Quatréa',s,desc=f"{s['name']}: {s['line']} Notes of {s['top'][0].lower()}, {s['heart'][0].lower()} and {s['base'][0].lower()}.",season=s['k'])+f'''<main id="main">
<section class="hero"><div class="fx" aria-hidden="true"></div><div class="orb" style="width:45vw;height:45vw;background:{s['liq1']};left:-12vw;top:5vh"></div><div class="orb" style="width:30vw;height:30vw;background:{s['acc']};right:-6vw;bottom:0"></div>
<p class="eyebrow">{s['tag']}</p><h1 class="split">{s['fr']}</h1><p>{s['line']} {s['name']} — the scent of {s['k']}, composed in three acts.</p><div class="scrollcue">Scroll</div></section>
<section class="bottlestage"><div class="fx" aria-hidden="true"></div><div class="bigword">{s['word']} · {s['word']}</div>{bottle(s,i=1)}<p class="cap">Hand-finished glass, a cap cast in the colour of the season. 50 ml · Eau de Parfum · {[145,145,165,165][n]},00 €.</p></section>
<section class="pyramid"><div class="sticky"><p class="eyebrow">The Olfactory Pyramid</p><h2 class="split">Three acts<br>of {s['k']}</h2>{tri}</div><div>
<div class="tier"><p class="k">I — Top notes</p><h3>{s['top'][0]}</h3><p>{s['top'][1]}</p></div>
<div class="tier"><p class="k">II — Heart notes</p><h3>{s['heart'][0]}</h3><p>{s['heart'][1]}</p></div>
<div class="tier"><p class="k">III — Base notes</p><h3>{s['base'][0]}</h3><p>{s['base'][1]}</p></div></div></section>
<section class="mood"><div class="layer" style="background:radial-gradient(circle at 30% 40%,{s['liq1']}aa,transparent 45%)"></div><div class="layer" style="background:radial-gradient(circle at 70% 65%,{s['liq2']}99,transparent 40%)"></div><blockquote class="split">{s['mood']}</blockquote></section>
<section class="facts"><div class="reveal"><b>50 ml</b><span>Eau de Parfum</span></div><div class="reveal"><b data-count="{[18,20,22,21][n]}" data-suf="%">%</b><span>Concentration</span></div><div class="reveal"><b>{[145,145,165,165][n]} €</b><span>50 ml · inkl. MwSt.</span></div></section>
<section class="hero reveal" style="height:70vh"><p class="eyebrow">Limited first edition</p><h2 class="split" style="font-size:clamp(3rem,8vw,7rem);margin:1.5rem 0 2.5rem">Make it <em>yours</em></h2><button class="btn magnetic" type="button" data-reserve="{s['name']}" data-price="{[145,145,165,165][n]},00 €">Reserve {s['fr']} — {[145,145,165,165][n]} € →</button></section>
<section class="nextseason" data-shift="{nx['bg']}" data-ink="{nx['ink']}"><p class="eyebrow">Next season</p><a href="{nx['k']}.html"><h3>{nx['fr']} →</h3></a></section>
</main>'''+FOOT
    open(s['k']+'.html','w').write(pg)
ab=head('La Maison — Quatréa')+'''<main id="main">
<section class="hero"><div class="orb" style="width:40vw;height:40vw;background:#c9a96e;left:20vw;top:20vh"></div><p class="eyebrow">La Maison</p><h1 class="split">The <em>story</em></h1><p>How a perfumer's notebook of four seasons became a house.</p><div class="scrollcue">Scroll</div></section>
<section class="chapter"><div class="num reveal">01</div><div class="reveal"><h2>A year in a notebook</h2><p>Quatréa began as a single journal kept by our founding perfumer: one page for every day of the year, each recording the smell of the air. After twelve months, four voices emerged — four seasons, four characters.</p></div></section>
<section class="chapter"><div class="reveal"><h2>Quatre + ére</h2><p>Our name joins the French <em>quatre</em> — four — with <em>ère</em>, an era. Four eras of the year, each lasting just long enough to be missed. The quartered circle in our emblem is the year itself.</p></div><div class="num reveal" style="text-align:right">02</div></section>
<p class="manifesto">Composed slowly, in small batches, with responsibly sourced naturals from Grasse, Calabria, Kannauj and the Bavarian Alps.</p>
<section><p class="eyebrow" style="text-align:center">The Collection</p><div class="grid4">'''+''.join(f'''<a class="card reveal" href="{s['k']}.html" style="background:{s['bg']};color:{s['ink']}">{bottle(s,i=2)}<h3>{s['fr']}</h3><span>{s['k']}</span></a>''' for s in S)+'''</div></section>
</main>'''+FOOT
open('about.html','w').write(ab)

nf=head('Lost between seasons — Quatréa',desc='Page not found.')+'''<main id="main"><section class="hero"><div class="orb" style="width:40vw;height:40vw;background:#c9a96e;left:30vw;top:20vh"></div><p class="eyebrow">Error 404</p><h1 class="split">Lost between <em>seasons</em></h1><p>The page you were looking for has evaporated, like a top note.</p><p style="margin-top:2.5rem"><a class="btn magnetic" href="index.html">Return to the maison →</a></p></section></main>'''+FOOT
open('404.html','w').write(nf)
