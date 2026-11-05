(function(){
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const hasG=typeof gsap!=='undefined';
const curtain=document.querySelector('.curtain');
// split text
document.querySelectorAll('.split').forEach(el=>{el.innerHTML=el.innerHTML.split(/(<[^>]+>|\s+)/).map(t=>{if(!t||/^\s+$/.test(t))return t; if(t[0]==='<')return t; return '<span class="w"><span>'+t+'</span></span>'}).join('')});
document.querySelectorAll('.manifesto').forEach(el=>{el.innerHTML=el.textContent.trim().split(/\s+/).map(w=>'<span class="wd">'+w+'</span>').join(' ')});
// page transitions
document.querySelectorAll('a[href$=".html"]').forEach(a=>a.addEventListener('click',e=>{
 if(e.metaKey||e.ctrlKey||!hasG||reduce)return;e.preventDefault();const h=a.getAttribute('href');
 gsap.set(curtain,{transformOrigin:'bottom'});gsap.to(curtain,{scaleY:1,duration:.7,ease:'expo.inOut',onComplete:()=>location.href=h});}));
window.addEventListener('pageshow',e=>{if(e.persisted&&curtain)gsap.set(curtain,{scaleY:0})});

// fx particles
document.querySelectorAll('.fx').forEach(fx=>{if(reduce)return;const n=innerWidth<760?14:28;for(let i=0;i<n;i++){const e=document.createElement('i');e.style.left=Math.random()*100+'%';e.style.animationDuration=(8+Math.random()*10)+'s';e.style.animationDelay=(-Math.random()*16)+'s';e.style.setProperty('--dx',(Math.random()*200-100)+'px');e.style.transform='scale('+(.5+Math.random())+')';fx.appendChild(e)}});
// reserve modal
const dlg=document.querySelector('.modal'),toast=document.querySelector('.toast');let item='';
document.querySelectorAll('[data-reserve]').forEach(b=>b.addEventListener('click',()=>{item=b.dataset.reserve;dlg.querySelector('#mt').textContent=item;dlg.querySelector('.mprice').textContent='50 ml Eau de Parfum · '+b.dataset.price+' · inkl. MwSt.';dlg.showModal()}));
if(dlg)dlg.addEventListener('close',()=>{if(dlg.returnValue==='ok'){toast.textContent='Merci — '+item+' is reserved for you. We will be in touch.';toast.classList.add('on');setTimeout(()=>toast.classList.remove('on'),4200);dlg.querySelector('form').reset()}});
// cursor + magnetic
const fine=matchMedia('(hover:hover) and (pointer:fine)').matches,cur=document.querySelector('.cursor');
if(fine&&!reduce&&cur&&hasG){const xs=gsap.quickTo(cur,'x',{duration:.35,ease:'power3'}),ys=gsap.quickTo(cur,'y',{duration:.35,ease:'power3'});addEventListener('mousemove',e=>{xs(e.clientX);ys(e.clientY)});
 document.querySelectorAll('a,button').forEach(a=>{a.addEventListener('mouseenter',()=>cur.classList.add('big'));a.addEventListener('mouseleave',()=>cur.classList.remove('big'))});
 document.querySelectorAll('.magnetic').forEach(m=>{m.addEventListener('mousemove',e=>{const r=m.getBoundingClientRect();gsap.to(m,{x:(e.clientX-r.left-r.width/2)*.35,y:(e.clientY-r.top-r.height/2)*.35,duration:.6,ease:'power3.out'})});m.addEventListener('mouseleave',()=>gsap.to(m,{x:0,y:0,duration:1,ease:'elastic.out(1,.4)'}))});}
if(!hasG||reduce){if(curtain)curtain.style.display='none';document.querySelectorAll('.wd').forEach(w=>w.style.opacity=1);return;}
gsap.registerPlugin(ScrollTrigger);sessionStorage.q||setTimeout(()=>sessionStorage.q=1,2000);
if(typeof Lenis!=='undefined'){const lenis=new Lenis({lerp:.08});lenis.on('scroll',ScrollTrigger.update);gsap.ticker.add(t=>lenis.raf(t*1000));gsap.ticker.lagSmoothing(0);}
gsap.timeline().to(curtain,{scaleY:0,transformOrigin:'top',duration:1.1,ease:'expo.inOut',delay:sessionStorage.q?.1:1.4})
 .from('.hero h1.split .w>span',{yPercent:110,duration:1.2,stagger:.06,ease:'expo.out'},'-=.4')
 .from('.hero .eyebrow,.hero p,.scrollcue',{opacity:0,y:20,stagger:.1,duration:1},'-=.8');
gsap.to('.progress',{scaleX:1,ease:'none',scrollTrigger:{start:0,end:'max',scrub:true}});
document.querySelectorAll('.hero').forEach(h=>h.querySelector('h1')&&gsap.to(h.querySelectorAll('h1'),{yPercent:30,opacity:.2,scrollTrigger:{trigger:h,start:'top top',end:'bottom top',scrub:true}}));
document.querySelectorAll('.orb').forEach((o,i)=>gsap.to(o,{y:(i%2?-1:1)*200,scrollTrigger:{trigger:o.parentNode,start:'top bottom',end:'bottom top',scrub:true}}));
document.querySelectorAll('.manifesto').forEach(m=>gsap.to(m.querySelectorAll('.wd'),{opacity:1,stagger:.05,scrollTrigger:{trigger:m,start:'top 70%',end:'bottom 60%',scrub:true}}));
document.querySelectorAll('.split:not(h1)').forEach(s=>gsap.from(s.querySelectorAll('.w>span'),{yPercent:110,duration:1,stagger:.05,ease:'expo.out',scrollTrigger:{trigger:s,start:'top 85%'}}));
document.querySelectorAll('.reveal').forEach(r=>gsap.from(r,{y:60,opacity:0,duration:1.2,ease:'expo.out',scrollTrigger:{trigger:r,start:'top 88%'}}));
// horizontal seasons with color shifts
const track=document.querySelector('.htrack');
if(track){const panels=[...track.children];
 const tw=gsap.to(track,{x:()=>-(track.scrollWidth-innerWidth),ease:'none',scrollTrigger:{trigger:'.hwrap',pin:true,scrub:1,end:()=>'+='+track.scrollWidth,invalidateOnRefresh:true,
 onUpdate:s=>{const i=Math.min(panels.length-1,Math.round(s.progress*(panels.length-1)));const p=panels[i].dataset;document.body.style.background=p.bg;document.body.style.color=p.ink;document.documentElement.style.setProperty('--accent',p.accent)},
 onLeaveBack:()=>{document.body.style.background='';document.body.style.color='';document.documentElement.style.removeProperty('--accent')}}});
 panels.forEach(p=>gsap.from(p.querySelector('.bottle'),{rotate:-8,y:80,scrollTrigger:{trigger:p,containerAnimation:tw,start:'left right',end:'center center',scrub:true}}));}
// bottle reveal pinned
document.querySelectorAll('.bottlestage').forEach(st=>{const tl=gsap.timeline({scrollTrigger:{trigger:st,pin:true,scrub:1,end:'+=120%'}});
 tl.from(st.querySelector('.bottle'),{scale:.4,y:200,rotate:-12,opacity:0,ease:'power2.out'}).from(st.querySelector('.bigword'),{xPercent:40},0).to(st.querySelector('.bigword'),{xPercent:-30},'>').from(st.querySelector('.cap'),{opacity:0,y:40},'<');});
document.querySelectorAll('.tier').forEach((t,i)=>ScrollTrigger.create({trigger:t,start:'top center',end:'bottom center',onToggle:s=>{if(s.isActive){document.querySelectorAll('.tri path[data-t]').forEach(p=>p.style.opacity=p.dataset.t==i?1:.18)}}}));
document.querySelectorAll('.mood .layer').forEach((l,i)=>gsap.fromTo(l,{yPercent:-10*(i+1)},{yPercent:10*(i+1),ease:'none',scrollTrigger:{trigger:l.parentNode,start:'top bottom',end:'bottom top',scrub:true}}));
document.querySelectorAll('[data-count]').forEach(el=>{const o={v:0};gsap.to(o,{v:+el.dataset.count,duration:2,ease:'power2.out',scrollTrigger:{trigger:el,start:'top 85%'},onUpdate:()=>el.textContent=Math.round(o.v)+(el.dataset.suf||'')})});
const mq=document.querySelector('.marquee .mt');if(mq)gsap.to(mq,{xPercent:-50,ease:'none',scrollTrigger:{trigger:'.marquee',start:'top bottom',end:'bottom top',scrub:true}});
// season page color shift into next
document.querySelectorAll('[data-shift]').forEach(s=>ScrollTrigger.create({trigger:s,start:'top 60%',end:'bottom 40%',onToggle:x=>{document.body.style.background=x.isActive?s.dataset.shift:'';document.body.style.color=x.isActive?s.dataset.ink:''}}));
addEventListener('load',()=>ScrollTrigger.refresh());
})();
