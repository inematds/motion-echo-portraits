from pathlib import Path
from bs4 import BeautifulSoup
r=Path(__file__).resolve().parents[1]
for lang in ['pt','en','es']:
 folder=r if lang=='pt' else r/lang
 for filename in ['curso.html','landing.html']:
  p=folder/filename;soup=BeautifulSoup(p.read_text(),'html.parser')
  for a in soup.select('a[href^="guia/index.html"]'):
   a['href']=('guia/index.html' if lang=='pt' else '../guia/'+lang+'/index.html')+('#prompts' if '#prompts' in a['href'] else '')
  nav=soup.select_one('nav.langs')
  if nav:nav['aria-label']='Language' if lang=='en' else 'Idioma'
  if filename=='curso.html' and not soup.select_one('script[data-course-languages]'):
   sc=soup.new_tag('script',src=('assets/' if lang=='pt' else '../assets/')+'idiomas.js');sc['data-course-languages']='';soup.body.append(sc)
  p.write_text(str(soup))
 guide=r/'guia'/('index.html' if lang=='pt' else lang+'/index.html');soup=BeautifulSoup(guide.read_text(),'html.parser')
 if not soup.select_one('#course-link'):
  a=soup.new_tag('a',href='../landing.html' if lang=='pt' else '../../'+lang+'/landing.html');a['class']='btn ghost';a['id']='course-link';a.string={'pt':'Fazer o curso v6','en':'Take the v6 course','es':'Hacer el curso v6'}[lang];soup.select_one('.cta').append(a)
 for node in soup.find_all(string=lambda t:t and 'v1.0.0' in t):node.replace_with(node.replace('v1.0.0','v1.1.0'))
 guide.write_text(str(soup))
 readme=r/('README.md' if lang=='pt' else 'README.'+lang+'.md');txt=readme.read_text();title={'pt':'Curso v6','en':'v6 course','es':'Curso v6'}[lang];link='https://inematds.github.io/motion-echo-portraits/'+('' if lang=='pt' else lang+'/')+'landing.html'
 if '## '+title not in txt:txt+='\n## '+title+'\n\n['+title+']('+link+') · 4 '+({'pt':'aulas práticas','en':'practical lessons','es':'clases prácticas'}[lang])+'.\n'
 txt=txt.replace('1.0.0','1.1.0');readme.write_text(txt)
print('Links curso↔guia, seletor interno e READMEs atualizados nos3idiomas.')
