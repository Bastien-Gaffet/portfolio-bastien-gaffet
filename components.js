/**
 * components.js — Bastien Gaffet
 * Shared nav, footer, cosmos and command palette for all pages.
 *
 * HOW TO USE ON A PAGE:
 *   1. Add <canvas id="cosmos"></canvas> as first child of <body>
 *   2. Add <script src="/components.js"></script> before </body>
 *   3. Remove the old <nav>, <footer>, cosmos JS and palette code
 *   4. The rest is automatic.
 *
 * TO CUSTOMISE A PAGE:
 *   Add an entry to PAGE_CONFIG below with the clean path as key.
 *
 * URLS: every page is served clean, without ".html" (Netlify resolves
 * "/about" to "about.html" automatically). All keys below and all hrefs
 * injected by this file use the clean form. Never write ".html" in a link.
 */

// ══════════════════════════════════════════════════════════════════════════
// PAGE CONFIGURATION
// Each key is the clean page path (e.g. 'about', 'project/robotj4', '' for home).
// All fields are optional — defaults are used for anything not specified.
//
// Fields:
//   noNav    : true            — hide the main top-right nav entirely
//   backNav  : { href, label }  — show a back link top-left (project/product/post pages)
//   noFooter : true            — hide the site footer entirely
// ══════════════════════════════════════════════════════════════════════════
const PAGE_CONFIG = {
  // Home / Story: narrative page, deliberately no footer
  '':                         { noFooter: true },
  // Pages with no nav and no footer.
  // langToggle: true opts a chrome-free page back into the language switcher.
  'links':                    { noNav: true,  noFooter: true, langToggle: true },
  'secret':                   { noNav: true,  noFooter: true },
  // Pages with a back-nav top-left (project/product/post pages).
  // The language toggle rides along inside .back-nav on these.
  'project/robotj4':          { backNav: { href: '/work', label: 'Work', labelFr: 'Projets' } },
  'project/tourny':           { backNav: { href: '/work', label: 'Work', labelFr: 'Projets' } },
  'project/glacify':          { backNav: { href: '/work', label: 'Work', labelFr: 'Projets' } },
  'project/equiliz':          { backNav: { href: '/work', label: 'Work', labelFr: 'Projets' } },
  'project/prepatrack':       { backNav: { href: '/work', label: 'Work', labelFr: 'Projets' } },
  'project/cobblekit':        { backNav: { href: '/work', label: 'Work', labelFr: 'Projets' } },
  'lab':                      { backNav: { href: '/work', label: 'Work', labelFr: 'Projets' } },
  'project/kairoo':           { backNav: { href: '/work', label: 'Work', labelFr: 'Projets' } },
  'project/krino':            { backNav: { href: '/work', label: 'Work', labelFr: 'Projets' } },
  'project/cdp-scraper':      { backNav: { href: '/work', label: 'Work', labelFr: 'Projets' } },
  'product/cosmos-wallpaper': { backNav: { href: '/shop', label: 'Shop', labelFr: 'Boutique' } },
  // Blog posts:
  'notes/cern':               { backNav: { href: '/blog', label: 'Notes', labelFr: 'Notes' } },
  // 'notes/post-slug':        { backNav: { href: '/blog', label: 'Notes', labelFr: 'Notes' } },
};

// ══════════════════════════════════════════════════════════════════════════
// PAGES — command palette index
// ══════════════════════════════════════════════════════════════════════════
const PAGES = [
  { group:'Explore',  name:'Story',       desc:'The narrative introduction',            href:'/' },
  { group:'Explore',  name:'Work',        desc:'Projects and creations',                href:'/work' },
  { group:'Explore',  name:'Photography', desc:'Selected photographs',                  href:'/photography' },
  { group:'Explore',  name:'Universe',    desc:'Passions, interests, dreams',           href:'/universe' },
  { group:'Explore',  name:'Notes',       desc:'Articles and observations',     href:'/blog' },
  { group:'Notes',    name:'At CERN, I found a society', desc:'A week at CERN, EUCYS prize', href:'/notes/cern' },
  { group:'Projects', name:'Robot J4',    desc:'Robotic arm, Minimax AI, EUCYS 2025',  href:'/project/robotj4' },
  { group:'Projects', name:'Tourny',      desc:'Sport tournament management platform', href:'/project/tourny' },
  { group:'Projects', name:'Glacify',     desc:'Ice cream ordering app, playful UX',   href:'/project/glacify' },
  { group:'Projects', name:'Equiliz',     desc:'Shared expenses app, closed beta',       href:'/project/equiliz' },
  { group:'Projects', name:'PrepaTrack',  desc:'Rank simulator for prépa students (on hold)', href:'/project/prepatrack' },
  { group:'Projects', name:'Cobblekit',  desc:'Free Minecraft tools for players and admins', href:'/project/cobblekit' },
  { group:'Projects', name:'Lab',        desc:'Small projects, tools and experiments', href:'/lab' },
  { group:'Projects', name:'Kairoo',      desc:'Mirror hours app, early prototype',   href:'/project/kairoo' },
  { group:'Projects', name:'Krino',       desc:'Desktop photo sorting app, Tauri',     href:'/project/krino' },
  { group:'Projects', name:'cdp-scraper', desc:'CLI backup tool for cahier-de-prepa',  href:'/project/cdp-scraper' },
  { group:'Me',       name:'About',       desc:'Bio and background',                    href:'/about' },
  { group:'Me',       name:'CV',          desc:'Interactive resume',                    href:'/cv' },
  { group:'Me',       name:'Timeline',    desc:'Milestones and projects',               href:'/timeline' },
  { group:'Me',       name:'TIPE',        desc:'Research on epoxy resin mechanics',     href:'/tipe' },
  { group:'Me',       name:'Uses',        desc:'Tools, software, hardware',             href:'/uses' },
  { group:'Me',       name:'Now',         desc:'What I am doing right now',             href:'/now' },
  { group:'Me',       name:'Press',       desc:'Articles and mentions',                 href:'/press' },
  { group:'Me',       name:'Contact',     desc:'Get in touch',                          href:'/contact' },
  { group:'Me',       name:'Links',       desc:'All my links in one place',             href:'/links' },
  { group:'Create',   name:'Shop',        desc:'Digital products',                      href:'/shop' },
  { group:'Create',   name:'Cosmos Wallpaper Generator', desc:'Generative tool, from €4 on Ko-fi', href:'/product/cosmos-wallpaper' },
  { group:'Create',   name:'Changelog',   desc:'Updates to site and products',          href:'/changelog' },
];

// ══════════════════════════════════════════════════════════════════════════
// HELPERS
// ══════════════════════════════════════════════════════════════════════════
const MAIN_PAGES = ['/','/about','/universe','/work'];
const PAGE_NAMES = {
  'photography':'Photography','blog':'Notes','contact':'Contact',
  'cv':'CV','uses':'Uses','links':'Links','shop':'Shop',
  'product/cosmos-wallpaper':'Cosmos Generator','project/robotj4':'Robot J4',
  'project/tourny':'Tourny','project/glacify':'Glacify',
  'project/kairoo':'Kairoo','project/cobblekit':'Cobblekit','lab':'Lab','project/equiliz':'Equiliz','project/prepatrack':'PrepaTrack','project/krino':'Krino',
  'project/cdp-scraper':'cdp-scraper','tipe':'TIPE','timeline':'Timeline',
  'press':'Press','changelog':'Changelog','now':'Now',
  'cosmos-demo':'Cosmos Demo','notes/cern':'At CERN, I found a society',
};

// currentPath: pathname without leading slash and without .html extension
// e.g. '/project/robotj4.html' or '/project/robotj4' → 'project/robotj4'
//      '/about.html' or '/about' → 'about'
//      '/' → ''
const currentPath = location.pathname.replace(/^\//, '').replace(/\.html$/, '').replace(/\/$/, '');
const config = PAGE_CONFIG[currentPath === 'index' ? '' : currentPath] || {};

// ══════════════════════════════════════════════════════════════════════════
// LANGUAGE
// ══════════════════════════════════════════════════════════════════════════
let _langPref = 'en';
try { _langPref = localStorage.getItem('lang') || ((navigator.language || 'en').toLowerCase().startsWith('fr') ? 'fr' : 'en'); } catch (e) {}
if (_langPref === 'fr') {
  document.documentElement.classList.add('lang-fr');
  document.documentElement.lang = 'fr';
}
window.setLang = function(lang) {
  const fr = lang === 'fr';
  document.documentElement.classList.toggle('lang-fr', fr);
  document.documentElement.lang = lang;
  try { localStorage.setItem('lang', lang); } catch (e) {}
  document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
  document.querySelectorAll('.lang-opt').forEach(btn => btn.classList.toggle('active', btn.dataset.lang === lang));
  document.querySelectorAll('.lang-indicator').forEach(ind => ind.classList.toggle('fr', fr));
};

// The glass EN/FR capsule. Same markup everywhere; only its placement changes.
function _langToggleHTML() {
  const fr = _langPref === 'fr';
  return `<div class="lang-toggle-wrap"><span class="lang-indicator${fr ? ' fr' : ''}"></span><button class="lang-opt${!fr ? ' active' : ''}" data-lang="en" onclick="setLang('en')">EN</button><button class="lang-opt${fr ? ' active' : ''}" data-lang="fr" onclick="setLang('fr')">FR</button></div>`;
}

// Standalone pill, fixed top-left, fades out after a short scroll.
// Skipped on back-nav pages: the back link already occupies that exact spot,
// so there the toggle is injected inline into .back-nav instead (see NAV below).
if (!config.backNav && (!config.noNav || config.langToggle)) {
  const _pill = document.createElement('div');
  _pill.id = 'lang-pill';
  _pill.innerHTML = _langToggleHTML();
  document.body.insertBefore(_pill, document.body.firstChild);
  let _pillHidden = false;
  window.addEventListener('scroll', () => {
    const hide = window.scrollY > 40;
    if (hide !== _pillHidden) { _pillHidden = hide; _pill.classList.toggle('hidden', hide); }
  }, { passive: true });
}

// ══════════════════════════════════════════════════════════════════════════
// ANALYTICS
// ══════════════════════════════════════════════════════════════════════════
(function() {
  const s = document.createElement('script');
  s.defer = true;
  s.src = 'https://cloud.umami.is/script.js';
  s.setAttribute('data-website-id', 'cc0431fb-5a53-4ce2-bcb1-1e3009b53177');
  document.head.appendChild(s);
})();

// ══════════════════════════════════════════════════════════════════════════
// SEO — canonical, theme-color, RSS autodiscovery, JSON-LD structured data
// ══════════════════════════════════════════════════════════════════════════

// RSS autodiscovery
const _rss = document.createElement('link');
_rss.rel = 'alternate';
_rss.type = 'application/rss+xml';
_rss.title = 'Notes — Bastien Gaffet';
_rss.href = 'https://bastiengaffet.fr/feed.xml';
document.head.appendChild(_rss);

// Canonical URL
const _canon = document.createElement('link');
_canon.rel = 'canonical';
_canon.href = 'https://bastiengaffet.fr/' + (currentPath === 'index' ? '' : currentPath);
document.head.appendChild(_canon);

// Favicon (planet logo) and touch icon
[['icon', '/favicon.ico', 'image/x-icon', '16x16 32x32 48x48'], ['icon', '/favicon-32.png', 'image/png', '32x32'], ['apple-touch-icon', '/apple-touch-icon.png', '', '180x180']].forEach(function (f) {
  if (document.querySelector('link[rel="' + f[0] + '"][href="' + f[1] + '"]')) return;
  const l = document.createElement('link');
  l.rel = f[0]; l.href = f[1];
  if (f[2]) l.type = f[2];
  if (f[3]) l.setAttribute('sizes', f[3]);
  document.head.appendChild(l);
});

// Theme color (mobile browser chrome)
const _theme = document.createElement('meta');
_theme.name = 'theme-color';
_theme.content = '#8C4DE6';
document.head.appendChild(_theme);

// JSON-LD helper
function _ld(schema) {
  const s = document.createElement('script');
  s.type = 'application/ld+json';
  s.textContent = JSON.stringify(schema);
  document.head.appendChild(s);
}

// WebSite schema, every page
_ld({ "@context":"https://schema.org", "@type":"WebSite",
  "name":"Bastien Gaffet", "url":"https://bastiengaffet.fr/",
  "description":"Portfolio of Bastien Gaffet, a student in prépa who builds apps, games and websites for fun.",
  "author":{ "@id":"https://bastiengaffet.fr/#bastien" },
  "inLanguage":["fr","en"] });

// Person schema: one stable identity, on the home page and About
if (currentPath === '' || currentPath === 'index' || currentPath === 'about') {
  _ld({ "@context":"https://schema.org", "@type":"Person",
    "@id":"https://bastiengaffet.fr/#bastien",
    "name":"Bastien Gaffet", "url":"https://bastiengaffet.fr/",
    "description":"Student in CPGE PC* at Lycée Descartes, Tours. Builds apps, games and websites for fun.",
    "sameAs":["https://github.com/Bastien-Gaffet"] });
}

// BreadcrumbList schema — project and product pages
const _crumbs = {
  'project/robotj4':          { parent:'/work',  parentName:'Work',  name:'Robot J4' },
  'project/tourny':           { parent:'/work',  parentName:'Work',  name:'Tourny' },
  'project/glacify':          { parent:'/work',  parentName:'Work',  name:'Glacify' },
  'project/equiliz':          { parent:'/work',  parentName:'Work',  name:'Equiliz' },
  'project/prepatrack':       { parent:'/work',  parentName:'Work',  name:'PrepaTrack' },
  'project/cobblekit':        { parent:'/work',  parentName:'Work',  name:'Cobblekit' },
  'lab':                      { parent:'/work',  parentName:'Work',  name:'Lab' },
  'project/kairoo':           { parent:'/work',  parentName:'Work',  name:'Kairoo' },
  'project/krino':            { parent:'/work',  parentName:'Work',  name:'Krino' },
  'project/cdp-scraper':      { parent:'/work',  parentName:'Work',  name:'cdp-scraper' },
  'product/cosmos-wallpaper': { parent:'/shop',  parentName:'Shop',  name:'Cosmos Wallpaper' },
  'notes/cern':               { parent:'/blog',  parentName:'Notes', name:'At CERN, I found a society' },
};
if (_crumbs[currentPath]) {
  const b = _crumbs[currentPath];
  _ld({ "@context":"https://schema.org", "@type":"BreadcrumbList",
    "itemListElement":[
      { "@type":"ListItem", "position":1, "name":b.parentName, "item":"https://bastiengaffet.fr"+b.parent },
      { "@type":"ListItem", "position":2, "name":b.name,       "item":"https://bastiengaffet.fr/"+currentPath }
    ]});
}

// ══════════════════════════════════════════════════════════════════════════
// NAV
// ══════════════════════════════════════════════════════════════════════════
if (!config.noNav) {
  const nav = document.createElement('nav');
  nav.id = 'site-nav';
  nav.innerHTML = `
    <a href="/"><span class="t-en">Story</span><span class="t-fr">Intro</span></a>
    <a href="/about"><span class="t-en">About</span><span class="t-fr">À propos</span></a>
    <a href="/universe"><span class="t-en">Universe</span><span class="t-fr">Univers</span></a>
    <a href="/work"><span class="t-en">Work</span><span class="t-fr">Projets</span></a>
    <span class="nav-sep"></span>
    <button class="nav-search-btn" onclick="cmdOpen()" aria-label="Search pages">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
    </button>
  `;
  document.body.insertBefore(nav, document.body.firstChild);

  // Highlight current main nav link
  nav.querySelectorAll('a').forEach(a => {
    if (a.getAttribute('href') === '/' + currentPath) a.classList.add('current');
  });
}

// Back nav (top-left) for project/product/post pages.
// Carries the language toggle inline, since the standalone pill is skipped here.
if (config.backNav) {
  const back = document.createElement('div');
  back.className = 'back-nav';
  const _bn = config.backNav;
  const _backLabel = _bn.labelFr
    ? `<span class="t-en">${_bn.label}</span><span class="t-fr">${_bn.labelFr}</span>`
    : _bn.label;
  back.innerHTML = `<a href="${_bn.href}" class="back-link">← ${_backLabel}</a>` + _langToggleHTML();
  document.body.insertBefore(back, document.body.firstChild);
  // Lets the stylesheet know the top-left corner is taken, so the main nav can
  // collapse to its search button on small screens instead of colliding.
  document.body.classList.add('has-back-nav');
}

// ══════════════════════════════════════════════════════════════════════════
// FOOTER
// ══════════════════════════════════════════════════════════════════════════
if (!config.noFooter) {

  const footer = document.createElement('footer');
  footer.id = 'site-footer';
  footer.innerHTML = `
    <div class="footer-inner">
      <div class="footer-brand">
        <img class="footer-logo" src="/img/logos/planet.png" alt="" width="30" height="30">
        <span class="footer-sig">Bastien Gaffet</span>
        <p class="footer-tagline t-en">Student in prépa. I build apps, games and websites for fun.</p>
        <p class="footer-tagline t-fr">Étudiant en prépa. Je crée des applications, des jeux et des sites pour le plaisir.</p>
        <button class="footer-search-pill" onclick="cmdOpen()">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <span class="t-en">Search pages</span><span class="t-fr">Rechercher</span>
          <span class="fkbd">/</span>
        </button>
      </div>
      <div>
        <span class="footer-col-label t-en">Explore</span><span class="footer-col-label t-fr">Explorer</span>
        <ul class="footer-links">
          <li><a href="/"><span class="t-en">Story</span><span class="t-fr">Intro</span></a></li>
          <li><a href="/work"><span class="t-en">Work</span><span class="t-fr">Projets</span></a></li>
          <li><a href="/photography"><span class="t-en">Photography</span><span class="t-fr">Photographie</span></a></li>
          <li><a href="/universe"><span class="t-en">Universe</span><span class="t-fr">Univers</span></a></li>
          <li><a href="/lab"><span class="t-en">Lab</span><span class="t-fr">Labo</span></a></li>
          <li><a href="/blog">Notes <span class="fnew">new</span></a></li>
        </ul>
      </div>
      <div>
        <span class="footer-col-label t-en">Me</span><span class="footer-col-label t-fr">Moi</span>
        <ul class="footer-links">
          <li><a href="/about"><span class="t-en">About</span><span class="t-fr">À propos</span></a></li>
          <li><a href="/cv">CV</a></li>
          <li><a href="/uses"><span class="t-en">Uses</span><span class="t-fr">Outils</span></a></li>
          <li><a href="/contact">Contact</a></li>
          <li><a href="/links"><span class="t-en">Links</span><span class="t-fr">Liens</span></a></li>
        </ul>
      </div>
      <div>
        <span class="footer-col-label t-en">Create</span><span class="footer-col-label t-fr">Créer</span>
        <ul class="footer-links">
          <li><a href="/shop"><span class="t-en">Shop</span><span class="t-fr">Boutique</span></a></li>
          <li><a href="/product/cosmos-wallpaper">Cosmos Generator</a></li>
          <li><a href="https://cobblekit.bastiengaffet.fr/" target="_blank" rel="noopener">Cobblekit</a></li>
          <li><a href="https://equiliz.bastiengaffet.fr/" target="_blank" rel="noopener">Equiliz</a></li>
          <li><a href="https://webtouraine.bastiengaffet.fr/" target="_blank" rel="noopener">Webtouraine</a></li>
          <li><a href="https://ko-fi.com/bastiengft" target="_blank" rel="noopener"><img class="kofi-cup-inline" src="/img/logos/kofi-cup.png" alt="" width="14" height="11">Ko-fi</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span class="footer-copy">© 2026 Bastien Gaffet · <a href="https://bastiengaffet.fr">bastiengaffet.fr</a></span>
      <span class="footer-sig-small t-en">Built by hand, no framework.</span>
      <span class="footer-sig-small t-fr">Fait à la main, sans framework.</span>
    </div>
  `;
  document.body.appendChild(footer);
}

// ══════════════════════════════════════════════════════════════════════════
// COMMAND PALETTE
// ══════════════════════════════════════════════════════════════════════════
const overlayEl = document.createElement('div');
overlayEl.id = 'cmd-overlay';
overlayEl.onclick = e => { if (e.target === overlayEl) cmdClose(); };
overlayEl.innerHTML = `
  <div id="cmd-box">
    <div id="cmd-input-wrap">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input id="cmd-input" aria-label="Search pages" placeholder="Search pages..." autocomplete="off" spellcheck="false">
      <span id="cmd-esc" onclick="cmdClose()">Esc</span>
    </div>
    <div id="cmd-results"></div>
  </div>
`;
document.body.appendChild(overlayEl);

let cmdActive = -1;

function hl(text, q) {
  if (!q) return text;
  const idx = text.toLowerCase().indexOf(q.toLowerCase());
  if (idx === -1) return text;
  return text.slice(0,idx)+'<mark>'+text.slice(idx,idx+q.length)+'</mark>'+text.slice(idx+q.length);
}

window.cmdOpen = function() {
  overlayEl.classList.add('open');
  const inp = document.getElementById('cmd-input');
  inp.value = ''; cmdActive = -1; cmdRender('');
  setTimeout(() => inp.focus(), 30);
};
window.cmdClose = function() {
  if (!overlayEl.classList.contains('open')) return;
  overlayEl.classList.add('closing');
  setTimeout(() => overlayEl.classList.remove('open', 'closing'), 160);
};

function cmdRender(query) {
  const q = query.trim();
  const results = document.getElementById('cmd-results');
  results.innerHTML = ''; cmdActive = -1;
  const filtered = q ? PAGES.filter(p =>
    p.name.toLowerCase().includes(q.toLowerCase()) ||
    p.desc.toLowerCase().includes(q.toLowerCase())
  ) : PAGES;
  if (!filtered.length) { results.innerHTML = '<p class="cmd-empty">No page found.</p>'; return; }
  const groups = {};
  filtered.forEach(p => { if(!groups[p.group]) groups[p.group]=[]; groups[p.group].push(p); });
  Object.entries(groups).forEach(([group, pages]) => {
    const label = document.createElement('p');
    label.className = 'cmd-group-label'; label.textContent = group;
    results.appendChild(label);
    pages.forEach(p => {
      const a = document.createElement('a');
      a.className = 'cmd-item'; a.href = p.href;
      a.innerHTML = `<div class="cmd-item-text"><p class="cmd-item-name">${hl(p.name,q)}</p><p class="cmd-item-desc">${hl(p.desc,q)}</p></div><span class="cmd-arrow">›</span>`;
      results.appendChild(a);
    });
  });
}

document.getElementById('cmd-input').addEventListener('input', e => cmdRender(e.target.value));
document.getElementById('cmd-input').addEventListener('keydown', e => {
  const items = [...document.querySelectorAll('.cmd-item')];
  if (e.key==='ArrowDown'){ e.preventDefault(); cmdActive=Math.min(cmdActive+1,items.length-1); }
  else if (e.key==='ArrowUp'){ e.preventDefault(); cmdActive=Math.max(cmdActive-1,0); }
  else if (e.key==='Enter'){ if(items[cmdActive])items[cmdActive].click(); else if(items[0])items[0].click(); }
  else if (e.key==='Escape'){ cmdClose(); }
  items.forEach((el,i) => el.classList.toggle('active', i===cmdActive));
  if(items[cmdActive]) items[cmdActive].scrollIntoView({block:'nearest'});
});
window.addEventListener('keydown', e => {
  if (e.key==='/' && document.activeElement.tagName!=='INPUT' && document.activeElement.tagName!=='TEXTAREA') {
    e.preventDefault(); cmdOpen();
  }
  if (e.key==='Escape') cmdClose();
});

// ══════════════════════════════════════════════════════════════════════════
// COSMOS
// ══════════════════════════════════════════════════════════════════════════
const canvas = document.getElementById('cosmos');
if (canvas) {
  const ctx = canvas.getContext('2d');
  let W, H, stars = [];
  const NUM_STARS = 220;
  function resize() { W=canvas.width=innerWidth; H=canvas.height=innerHeight; }
  function initStars() {
    stars = [];
    for (let i=0; i<NUM_STARS; i++) {
      const a=Math.random()*Math.PI*2, r=Math.random()*Math.max(W,H)*.65;
      stars.push({x:W/2+Math.cos(a)*r,y:H/2+Math.sin(a)*r,rad:Math.random()*1.1+.15,
        alpha:Math.random()*.5+.08,twinkle:Math.random()*Math.PI*2,
        speed:(Math.random()*.3+.05)*.00008,angle:a,radius:r});
    }
  }
  function draw(t) {
    ctx.clearRect(0,0,W,H);
    const bg=ctx.createRadialGradient(W/2,H/2,0,W/2,H/2,Math.max(W,H)*.8);
    bg.addColorStop(0,'rgba(14,10,30,1)'); bg.addColorStop(.3,'rgba(8,6,18,1)'); bg.addColorStop(1,'rgba(5,6,10,1)');
    ctx.fillStyle=bg; ctx.fillRect(0,0,W,H);
    const cx=W/2, cy=H/2;
    const g1=ctx.createRadialGradient(cx,cy,0,cx,cy,Math.min(W,H)*.5);
    g1.addColorStop(0,'rgba(100,50,200,0)'); g1.addColorStop(.3,'rgba(100,50,200,.06)');
    g1.addColorStop(.7,'rgba(60,20,140,.09)'); g1.addColorStop(1,'rgba(0,0,0,0)');
    ctx.fillStyle=g1; ctx.fillRect(0,0,W,H);
    stars.forEach(s => {
      s.angle+=s.speed; s.x=cx+Math.cos(s.angle)*s.radius; s.y=cy+Math.sin(s.angle)*s.radius;
      const a=Math.max(0,Math.min(1,s.alpha+Math.sin(s.twinkle+t*.001)*.25));
      ctx.beginPath(); ctx.arc(s.x,s.y,s.rad,0,Math.PI*2);
      ctx.fillStyle=`rgba(220,210,255,${a})`; ctx.fill();
    });
    requestAnimationFrame(draw);
  }
  resize(); initStars(); requestAnimationFrame(draw);
  window.addEventListener('resize', () => { resize(); initStars(); });
}
