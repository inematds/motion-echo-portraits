/* Language navigation kept separate from the unmodified v6 engine. */
(function(){
 const locale=document.documentElement.lang.startsWith('pt')?'pt':document.documentElement.lang;
 const root=locale==='pt'?'':'../';
 const label={pt:'Idioma',en:'Language',es:'Idioma'}[locale];
 const menu=document.getElementById('menu');
 if(!menu||menu.querySelector('.course-languages'))return;
 const nav=document.createElement('nav');nav.className='course-languages';nav.setAttribute('aria-label',label);nav.style.cssText='display:flex;gap:12px;flex-wrap:wrap;margin-top:20px';
 for(const lang of ['pt','en','es']){const a=document.createElement('a');a.className='btn';a.dataset.path=root+(lang==='pt'?'':lang+'/')+'curso.html';a.textContent=lang.toUpperCase();if(lang===locale)a.setAttribute('aria-current','page');nav.append(a)}
 menu.append(nav);
 function update(){nav.querySelectorAll('a').forEach(a=>a.href=a.dataset.path+(location.hash||'#trilha'))}
 update();addEventListener('hashchange',update);
})();
