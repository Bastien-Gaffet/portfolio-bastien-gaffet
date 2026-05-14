/**
 * components.js — Bastien Gaffet
 * Shared nav, footer, cosmos and command palette for all pages.
 *
 * HOW TO USE ON A PAGE:
 *   1. Add <canvas id="cosmos"></canvas> as first child of <body>
 *   2. Add <script src="components.js"></script> before </body>
 *   3. Remove the old <nav>, <footer>, cosmos JS and palette code
 *   4. The rest is automatic.
 *
 * TO CUSTOMISE A PAGE:
 *   Add an entry to PAGE_CONFIG below with the filename as key.
 */

// ══════════════════════════════════════════════════════════════════════════
// PAGE CONFIGURATION
// Each key is the HTML filename (e.g. 'about.html').
// All fields are optional — defaults are used for anything not specified.
//
// Fields:
//   noNav    : true            — hide the main top-right nav entirely
//   backNav  : { href, label }  — show a back link top-left (project/product/post pages)
//   noFooter : true            — hide the site footer entirely
// ══════════════════════════════════════════════════════════════════════════
const PAGE_CONFIG = {
  // Pages with no nav and no footer
  'links.html':                   { noNav: true,  noFooter: true },
  'secret.html':                  { noNav: true,  noFooter: true },
  // Pages with a back-nav top-left (project/product/post pages)
  'project-robotj4.html':         { backNav: { href: 'work.html', label: 'Work' } },
  'project-tourny.html':          { backNav: { href: 'work.html', label: 'Work' } },
  'project-glacify.html':         { backNav: { href: 'work.html', label: 'Work' } },
  'project-hopetime.html':        { backNav: { href: 'work.html', label: 'Work' } },
  'product-cosmos-wallpaper.html':{ backNav: { href: 'shop.html',    label: 'Shop' } },
  // Blog posts — add as you publish:
  // 'post-example.html':         { backNav: { href: 'blog.html',    label: 'Notes' } },
};

// ══════════════════════════════════════════════════════════════════════════
// PAGES — command palette index
// ══════════════════════════════════════════════════════════════════════════
const PAGES = [
  { group:'Explore',  name:'Story',       desc:'The narrative introduction',            href:'story.html' },
  { group:'Explore',  name:'Work',        desc:'Projects and creations',                href:'work.html' },
  { group:'Explore',  name:'Photography', desc:'Selected photographs',                  href:'photography.html' },
  { group:'Explore',  name:'Universe',    desc:'Passions, interests, dreams',           href:'universe.html' },
  { group:'Explore',  name:'Notes',       desc:'Monthly articles and observations',     href:'blog.html' },
  { group:'Projects', name:'Robot J4',    desc:'Robotic arm, Minimax AI, EUCYS 2025',  href:'project-robotj4.html' },
  { group:'Me',       name:'About',       desc:'Bio and background',                    href:'about.html' },
  { group:'Me',       name:'CV',          desc:'Interactive resume',                    href:'cv.html' },
  { group:'Me',       name:'Timeline',    desc:'Milestones and projects',               href:'timeline.html' },
  { group:'Me',       name:'TIPE',        desc:'Research on epoxy resin mechanics',     href:'tipe.html' },
  { group:'Me',       name:'Uses',        desc:'Tools, software, hardware',             href:'uses.html' },
  { group:'Me',       name:'Now',         desc:'What I am doing right now',             href:'now.html' },
  { group:'Me',       name:'Press',       desc:'Articles and mentions',                 href:'press.html' },
  { group:'Me',       name:'Contact',     desc:'Get in touch',                          href:'contact.html' },
  { group:'Me',       name:'Links',       desc:'All my links in one place',             href:'links.html' },
  { group:'Create',   name:'Shop',        desc:'Digital products',                      href:'shop.html' },
  { group:'Create',   name:'Cosmos Wallpaper Generator', desc:'Generative tool, from €4 on Ko-fi', href:'product-cosmos-wallpaper.html' },
  { group:'Create',   name:'Changelog',   desc:'Updates to site and products',          href:'changelog.html' },
];

// ══════════════════════════════════════════════════════════════════════════
// HELPERS
// ══════════════════════════════════════════════════════════════════════════
const MAIN_PAGES = ['story.html','about.html','universe.html','work.html'];
const PAGE_NAMES = {
  'photography.html':'Photography','blog.html':'Notes','contact.html':'Contact',
  'cv.html':'CV','uses.html':'Uses','links.html':'Links','shop.html':'Shop',
  'product-cosmos-wallpaper.html':'Cosmos Generator','project-robotj4.html':'Robot J4',
  'project-tourny.html':'Tourny','project-glacify.html':'Glacify',
  'project-hopetime.html':'HopeTime','tipe.html':'TIPE','timeline.html':'Timeline',
  'press.html':'Press','changelog.html':'Changelog','now.html':'Now',
  'cosmos-demo.html':'Cosmos Demo',
};

const currentFile = location.pathname.split('/').pop() || 'index.html';
const config = PAGE_CONFIG[currentFile] || {};

// ══════════════════════════════════════════════════════════════════════════
// NAV
// ══════════════════════════════════════════════════════════════════════════
if (!config.noNav) {
  const pageName = (!MAIN_PAGES.includes(currentFile) && PAGE_NAMES[currentFile])
    ? PAGE_NAMES[currentFile] : '';

  const nav = document.createElement('nav');
  nav.id = 'site-nav';
  nav.innerHTML = `
    <a href="story.html">Story</a>
    <a href="about.html">About</a>
    <a href="universe.html">Universe</a>
    <a href="work.html">Work</a>
    ${pageName ? `<span class="nav-sep"></span><span id="nav-page-label">${pageName}</span>` : ''}
    <span class="nav-sep"></span>
    <button class="nav-search-btn" onclick="cmdOpen()" aria-label="Search pages">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
    </button>
  `;
  document.body.insertBefore(nav, document.body.firstChild);

  // Highlight current main nav link
  nav.querySelectorAll('a').forEach(a => {
    if (a.getAttribute('href') === currentFile) a.classList.add('current');
  });
}

// Back nav (top-left) for project/product/post pages
if (config.backNav) {
  const back = document.createElement('div');
  back.className = 'back-nav';
  back.innerHTML = `<a href="${config.backNav.href}" class="back-link">← ${config.backNav.label}</a>`;
  document.body.insertBefore(back, document.body.firstChild);
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
        <span class="footer-sig">Bastien Gaffet</span>
        <p class="footer-tagline">Engineering student. Building things at the intersection of software, hardware and design.</p>
        <button class="footer-search-pill" onclick="cmdOpen()">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          Search pages
          <span class="fkbd">/</span>
        </button>
      </div>
      <div>
        <span class="footer-col-label">Explore</span>
        <ul class="footer-links">
          <li><a href="story.html">Story</a></li>
          <li><a href="work.html">Work</a></li>
          <li><a href="photography.html">Photography</a></li>
          <li><a href="universe.html">Universe</a></li>
          <li><a href="blog.html">Notes <span class="fnew">new</span></a></li>
        </ul>
      </div>
      <div>
        <span class="footer-col-label">Me</span>
        <ul class="footer-links">
          <li><a href="about.html">About</a></li>
          <li><a href="cv.html">CV</a></li>
          <li><a href="uses.html">Uses</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="links.html">Links</a></li>
        </ul>
      </div>
      <div>
        <span class="footer-col-label">Create</span>
        <ul class="footer-links">
          <li><a href="shop.html">Shop</a></li>
          <li><a href="product-cosmos-wallpaper.html">Cosmos Generator</a></li>
          <li><a href="https://ko-fi.com/bastien_gft" target="_blank" rel="noopener">Ko-fi</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span class="footer-copy">© 2025 Bastien Gaffet — <a href="https://bastiengaffet.fr">bastiengaffet.fr</a></span>
      <span class="footer-sig-small">Built by hand, no framework.</span>
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
      <input id="cmd-input" placeholder="Search pages..." autocomplete="off" spellcheck="false">
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
window.cmdClose = function() { overlayEl.classList.remove('open'); };

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
