import os
path = os.path.expanduser('~/projects/locay-web/index.html')
with open(path, 'w') as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Locay - Nightlife, Found.</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#070709;--surface:rgba(255,255,255,0.04);--border:rgba(255,255,255,0.07);--text:#f0efed;--muted:#7a8a96;--dim:#3a4855;--platinum:#e5e4e2;--blue:#536878;--yes:#5cd4a0}
html{scroll-behavior:smooth}
body{font-family:Inter,sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;-webkit-font-smoothing:antialiased}
#bg-canvas{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none}
nav{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:18px 40px;background:rgba(7,7,9,0.7);backdrop-filter:blur(20px);border-bottom:1px solid var(--border)}
.nav-logo{font-size:20px;font-weight:900;color:var(--text);text-decoration:none;cursor:pointer;letter-spacing:-0.5px}
.nav-links{display:flex;gap:28px;list-style:none;align-items:center}
.nav-links a{font-size:13px;color:var(--muted);text-decoration:none;font-weight:500;cursor:pointer;transition:color 0.15s}
.nav-links a:hover{color:var(--text)}
.nav-cta{height:36px;padding:0 18px;background:var(--platinum);color:#070709;font-size:13px;font-weight:700;border:none;border-radius:999px;cursor:pointer;font-family:inherit}
.hero{position:relative;z-index:1;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:140px 24px 80px}
.hero-eyebrow{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--border);border-radius:999px;padding:6px 16px;font-size:12px;font-weight:500;color:var(--muted);margin-bottom:32px;background:var(--surface)}
.dot{width:6px;height:6px;border-radius:50%;background:var(--yes);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:0.5;transform:scale(0.8)}}
.hero h1{font-size:clamp(72px,13vw,160px);font-weight:900;letter-spacing:-6px;line-height:0.9;color:var(--text);margin-bottom:20px}
.hero-sub{font-size:16px;font-weight:400;letter-spacing:6px;text-transform:uppercase;color:var(--muted);margin-bottom:28px}
.hero-desc{font-size:20px;color:var(--muted);max-width:500px;line-height:1.6;font-weight:300;margin-bottom:52px}
.hero-desc strong{color:var(--text);font-weight:600}
#rotating-city{display:inline-block;transition:opacity 0.3s ease,transform 0.3s ease;color:var(--platinum)}
.waitlist-wrap{width:100%;max-width:520px;display:flex;flex-direction:column;align-items:center;gap:12px}
.waitlist-row{display:flex;gap:8px;width:100%;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:16px;padding:6px 6px 6px 16px}
.waitlist-row input{flex:1;background:none;border:none;outline:none;font-size:15px;color:var(--text);font-family:inherit;min-width:0}
.waitlist-row input::placeholder{color:var(--dim)}
.waitlist-row select{background:none;border:none;outline:none;font-size:13px;color:var(--muted);font-family:inherit;cursor:pointer;padding:0 8px}
.waitlist-row select option{background:#1a2530;color:var(--text)}
.btn-submit{height:44px;padding:0 24px;background:var(--platinum);color:#070709;font-size:14px;font-weight:700;border:none;border-radius:12px;cursor:pointer;font-family:inherit;white-space:nowrap}
.waitlist-note{font-size:12px;color:var(--dim)}
.success-msg{display:none;font-size:14px;color:var(--yes);padding:12px 20px;background:rgba(92,212,160,0.08);border:1px solid rgba(92,212,160,0.2);border-radius:10px;width:100%;text-align:center}
.stats{position:relative;z-index:1;display:flex;justify-content:center;border-top:1px solid var(--border);border-bottom:1px solid var(--border);background:rgba(255,255,255,0.02);padding:28px 24px;flex-wrap:wrap}
.stat{flex:1;min-width:140px;display:flex;flex-direction:column;align-items:center;padding:0 24px;text-align:center}
.stat+.stat{border-left:1px solid var(--border)}
.stat-num{font-size:28px;font-weight:800;color:var(--text);letter-spacing:-1px;margin-bottom:4px}
.stat-label{font-size:12px;color:var(--muted);font-weight:500}
.section{position:relative;z-index:1;max-width:1100px;margin:0 auto;padding:100px 32px}
.section-label{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--blue);margin-bottom:14px;display:block}
.section h2{font-size:clamp(32px,4vw,52px);font-weight:800;letter-spacing:-1.5px;color:var(--text);margin-bottom:16px;line-height:1.1}
.section-desc{font-size:17px;color:var(--muted);max-width:540px;line-height:1.65;margin-bottom:60px;font-weight:300}
.audience-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.a-card{background:var(--surface);border:1px solid var(--border);border-radius:24px;padding:36px;transition:border-color 0.2s,transform 0.2s}
.a-card:hover{border-color:rgba(229,228,226,0.15);transform:translateY(-2px)}
.a-icon{font-size:36px;margin-bottom:20px;display:block}
.a-card h3{font-size:22px;font-weight:800;color:var(--text);margin-bottom:10px}
.a-card p{font-size:14px;color:var(--muted);line-height:1.65;margin-bottom:24px;font-weight:300}
.a-features{list-style:none;display:flex;flex-direction:column;gap:10px}
.a-features li{font-size:13px;color:var(--muted);display:flex;align-items:flex-start;gap:10px}
.a-features li::before{content:"to";color:var(--platinum);font-weight:700;font-size:12px;flex-shrink:0}
.steps-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.step{background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:28px}
.step-num{font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--blue);margin-bottom:16px;display:block}
.step-emoji{font-size:28px;margin-bottom:14px;display:block}
.step h4{font-size:17px;font-weight:700;color:var(--text);margin-bottom:8px}
.step p{font-size:13px;color:var(--muted);line-height:1.6;font-weight:300}
.faq-list{display:flex;flex-direction:column;gap:2px;max-width:720px}
.faq-item{border:1px solid var(--border);border-radius:12px;overflow:hidden}
.faq-q{width:100%;display:flex;align-items:center;justify-content:space-between;padding:18px 20px;background:none;border:none;font-size:15px;font-weight:600;color:var(--text);font-family:inherit;cursor:pointer;text-align:left;gap:16px}
.faq-arrow{font-size:12px;color:var(--muted);transition:transform 0.2s}
.faq-item.open .faq-arrow{transform:rotate(180deg)}
.faq-a{display:none;padding:0 20px 18px;font-size:14px;color:var(--muted);line-height:1.65;font-weight:300}
.faq-item.open .faq-a{display:block}
.cta-section{position:relative;z-index:1;text-align:center;padding:100px 24px}
.cta-section h2{font-size:clamp(36px,5vw,64px);font-weight:900;letter-spacing:-2px;color:var(--text);margin-bottom:16px}
.cta-section p{font-size:16px;color:var(--muted);margin-bottom:40px;font-weight:300}
footer{position:relative;z-index:1;border-top:1px solid var(--border);padding:40px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px}
.footer-logo{font-size:18px;font-weight:900;color:var(--text)}
.footer-links{display:flex;gap:20px;flex-wrap:wrap}
.footer-links a{font-size:12px;color:var(--dim);text-decoration:none;cursor:pointer;transition:color 0.15s}
.footer-links a:hover{color:var(--muted)}
.footer-copy{font-size:12px;color:var(--dim);width:100%;margin-top:8px}
.divider{height:1px;background:var(--border);position:relative;z-index:1;margin:0 32px}
.legal-page{display:none;max-width:720px;margin:0 auto;padding:120px 32px 80px;position:relative;z-index:1}
.legal-page.active{display:block}
.legal-back{display:inline-flex;align-items:center;gap:6px;font-size:13px;color:var(--muted);cursor:pointer;margin-bottom:40px;text-decoration:none}
.legal-page h1{font-size:36px;font-weight:900;color:var(--text);margin-bottom:6px}
.legal-date{font-size:13px;color:var(--dim);margin-bottom:40px}
.legal-page h2{font-size:18px;font-weight:700;color:var(--text);margin:32px 0 10px}
.legal-page p,.legal-page li{font-size:14px;color:var(--muted);line-height:1.7;margin-bottom:10px;font-weight:300}
.legal-page ul{padding-left:20px;margin-bottom:12px}
.legal-page a{color:var(--platinum)}
#main-content{display:block}
@media(max-width:768px){nav{padding:14px 20px}.nav-links{display:none}.audience-grid,.steps-grid{grid-template-columns:1fr}.stat+.stat{border-left:none;border-top:1px solid var(--border)}.stats{flex-direction:column}.divider{margin:0 20px}footer{flex-direction:column;padding:32px 24px}}
</style>
</head>
<body>
<canvas id="bg-canvas"></canvas>
<nav>
  <a class="nav-logo" onclick="showMain()">locay</a>
  <ul class="nav-links">
    <li><a href="#how-it-works">how it works</a></li>
    <li><a href="#for-planners">for planners</a></li>
    <li><a href="#faq">faq</a></li>
    <li><a onclick="showPrivacy()">privacy</a></li>
    <li><a onclick="showTerms()">terms</a></li>
    <button class="nav-cta" onclick="document.getElementById('wl-email').focus();window.scrollTo({top:0,behavior:'smooth'})">join waitlist</button>
  </ul>
</nav>
<div id="main-content">
<section class="hero">
  <div class="hero-eyebrow"><span class="dot"></span>Beta launching soon</div>
  <h1>locay</h1>
  <p class="hero-sub">nightlife, found.</p>
  <p class="hero-desc">Stop scrolling five apps to find one good night out. Locay puts <strong>the best <span id="rotating-city">NYC</span> events</strong> in a single swipe feed.</p>
  <div class="waitlist-wrap">
    <form class="waitlist-row" onsubmit="handleWaitlist(event)">
      <input id="wl-email" type="email" placeholder="your@email.com" required/>
      <select id="wl-role"><option value="attendee">I want to find events</option><option value="planner">I want to list events</option></select>
      <button type="submit" class="btn-submit">join waitlist</button>
    </form>
    <div class="success-msg" id="success-msg">You are on the list. We will reach out before launch.</div>
    <p class="waitlist-note">No spam. No noise. Just your next night out.</p>
  </div>
</section>
<div class="stats">
  <div class="stat"><span class="stat-num">NYC</span><span class="stat-label">launching first</span></div>
  <div class="stat"><span class="stat-num">21-35</span><span class="stat-label">target demographic</span></div>
  <div class="stat"><span class="stat-num">6</span><span class="stat-label">event categories</span></div>
  <div class="stat"><span class="stat-num">2 min</span><span class="stat-label">to list your event</span></div>
</div>
<div class="divider"></div>
<section class="section" id="how-it-works">
  <span class="section-label">the experience</span>
  <h2>your city's nightlife in a swipe feed</h2>
  <p class="section-desc">Every swipe teaches Locay what to surface next. Underground parties, rooftop raves, live jazz, comedy nights, wellness events — all in one place.</p>
</section>
<div class="divider"></div>
<section class="section" id="for-planners">
  <span class="section-label">who it's for</span>
  <h2>built for both sides of the night</h2>
  <p class="section-desc">Locay connects the people looking for a great time with the people creating it.</p>
  <div class="audience-grid">
    <div class="a-card">
      <span class="a-icon">🎉</span>
      <h3>for attendees</h3>
      <p>One feed. Every event worth going to. Swipe to save, show up.</p>
      <ul class="a-features">
        <li>Swipe through a personalized feed of events</li>
        <li>Save events to your calendar with one swipe</li>
        <li>See what's trending near you</li>
        <li>Night parties, day parties, live music and more</li>
        <li>24-hour reminders before saved events</li>
      </ul>
    </div>
    <div class="a-card">
      <span class="a-icon">📣</span>
      <h3>for planners and venues</h3>
      <p>Reach nightlife regulars actively looking for something to do this weekend.</p>
      <ul class="a-features">
        <li>List your event in under 2 minutes</li>
        <li>Reach attendees aged 21-35</li>
        <li>Boost for priority placement in the feed</li>
        <li>Track saves and engagement in real time</li>
        <li>Build a following for your events</li>
      </ul>
    </div>
  </div>
</section>
<div class="divider"></div>
<section class="section">
  <span class="section-label">how it works</span>
  <h2>three steps to your next night out</h2>
  <p class="section-desc">Finding a good event should be as easy as choosing what to watch.</p>
  <div class="steps-grid">
    <div class="step"><span class="step-num">01</span><span class="step-emoji">📍</span><h4>set your city</h4><p>Allow location or type your city. We pull the best upcoming events near you.</p></div>
    <div class="step"><span class="step-num">02</span><span class="step-emoji">👆</span><h4>swipe to decide</h4><p>Swipe right to save. Each card shows date, price, vibe, and how many people already saved it.</p></div>
    <div class="step"><span class="step-num">03</span><span class="step-emoji">🎉</span><h4>show up</h4><p>Your saved events live in your calendar. We remind you 24 hours before. Tap for tickets.</p></div>
  </div>
</section>
<div class="divider"></div>
<section class="section" id="faq">
  <span class="section-label">questions</span>
  <h2>things people ask</h2>
  <p class="section-desc">Everything you need to know before you join.</p>
  <div class="faq-list">
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">When does Locay launch?<span class="faq-arrow">v</span></button><div class="faq-a">We are currently in beta. Join the waitlist to be first when we open to the public.</div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">What kinds of events are on Locay?<span class="faq-arrow">v</span></button><div class="faq-a">Night parties, day parties, live music, health and wellness, speaking engagements, comedy, and more.</div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">Is Locay free for attendees?<span class="faq-arrow">v</span></button><div class="faq-a">Yes. Discovering and saving events is completely free. Ticket prices are set by the event organizer.</div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">How do I list my event?<span class="faq-arrow">v</span></button><div class="faq-a">Create a planner account, tap the plus tab, select your event type, fill in the details, and publish. Under 2 minutes.</div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">What cities does Locay cover?<span class="faq-arrow">v</span></button><div class="faq-a">Launching in New York City first. More cities coming based on demand.</div></div>
  </div>
</section>
<div class="divider"></div>
<section class="cta-section">
  <h2>your next night out starts here</h2>
  <p>Join the waitlist. Be first.</p>
  <form class="waitlist-row" style="max-width:460px;margin:0 auto" onsubmit="handleWaitlist2(event)">
    <input id="wl-email-2" type="email" placeholder="your@email.com" required/>
    <button type="submit" class="btn-submit">join waitlist</button>
  </form>
  <div class="success-msg" id="success-msg-2" style="max-width:460px;margin:12px auto 0">You are on the list. We will reach out before launch.</div>
</section>
<footer>
  <span class="footer-logo">locay</span>
  <div class="footer-links">
    <a onclick="showPrivacy()">privacy policy</a>
    <a onclick="showTerms()">terms of service</a>
    <a href="mailto:support@locayapp.com">support@locayapp.com</a>
  </div>
  <p class="footer-copy">2026 Locay. All rights reserved.</p>
</footer>
</div>
<div id="privacy-page" class="legal-page">
  <a class="legal-back" onclick="showMain()">back to locay</a>
  <h1>Privacy Policy</h1><p class="legal-date">Last updated: October 4, 2026</p>
  <p>Locay operates the Locay mobile application. This Privacy Policy explains how we collect, use, and protect your information.</p>
  <h2>Information We Collect</h2>
  <ul><li>Account information: Email address and display name via Clerk.</li><li>Location data: With your permission, to show nearby events.</li><li>Usage data: Events you view, swipe on, and save.</li><li>Session data: Timestamps and duration to improve performance.</li></ul>
  <h2>How We Use Your Information</h2>
  <ul><li>To show relevant events near you</li><li>To save events to your calendar</li><li>To send reminders about upcoming events</li><li>To improve your experience</li></ul>
  <h2>Information Sharing</h2><p>We do not sell your data. We share only with Clerk, service providers under confidentiality agreements, and when required by law.</p>
  <h2>Contact</h2><p><a href="mailto:support@locayapp.com">support@locayapp.com</a></p>
</div>
<div id="terms-page" class="legal-page">
  <a class="legal-back" onclick="showMain()">back to locay</a>
  <h1>Terms of Service</h1><p class="legal-date">Last updated: October 4, 2026</p>
  <p>These Terms govern your use of the Locay mobile application. By using the App you agree to these Terms.</p>
  <h2>Eligibility</h2><p>You must be at least 18 years old to use Locay.</p>
  <h2>User Accounts</h2><p>You are responsible for your account and all activity under it.</p>
  <h2>Event Listings</h2><p>Locay is a discovery platform. We do not organize or host events. Details are provided by third-party organizers.</p>
  <h2>Acceptable Use</h2><ul><li>No unlawful use</li><li>No false event listings</li><li>No harassment</li><li>No unauthorized system access</li></ul>
  <h2>Limitation of Liability</h2><p>To the fullest extent permitted by law, Locay is not liable for indirect damages from use of the App.</p>
  <h2>Contact</h2><p><a href="mailto:support@locayapp.com">support@locayapp.com</a></p>
</div>
<script>
const cities=['NYC','Atlanta','LA','Chicago','Miami','Houston','DC','Brooklyn','Philly','Detroit','Dallas','New Orleans','Austin','Fort Lauderdale','San Francisco'];
let cityIndex=0;
const cityEl=document.getElementById('rotating-city');
function rotateCity(){cityEl.style.opacity='0';cityEl.style.transform='translateY(-8px)';setTimeout(()=>{cityIndex=(cityIndex+1)%cities.length;cityEl.textContent=cities[cityIndex];cityEl.style.opacity='1';cityEl.style.transform='translateY(0)'},300)}
setInterval(rotateCity,2000);
const canvas=document.getElementById('bg-canvas');
const ctx=canvas.getContext('2d');
let W,H,particles,time=0;
function resize(){W=canvas.width=window.innerWidth;H=canvas.height=window.innerHeight}
function initParticles(){particles=Array.from({length:80},()=>({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.5+0.3,speed:Math.random()*0.3+0.1,angle:Math.random()*Math.PI*2,drift:(Math.random()-0.5)*0.01,opacity:Math.random()*0.4+0.05}))}
function drawWave(yBase,amp,freq,phase,color,alpha){ctx.beginPath();ctx.moveTo(0,H);for(let x=0;x<=W;x+=2){const y=yBase+Math.sin(x*freq+phase+time)*amp+Math.sin(x*freq*0.5+phase*1.3+time*0.7)*amp*0.5;ctx.lineTo(x,y)}ctx.lineTo(W,H);ctx.closePath();ctx.fillStyle='rgba('+color+','+alpha+')';ctx.fill()}
function animate(){ctx.clearRect(0,0,W,H);const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#070709');g.addColorStop(0.5,'#090d10');g.addColorStop(1,'#0d1318');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);drawWave(H*0.82,30,0.004,0,'42,56,64',0.3);drawWave(H*0.86,22,0.006,1.5,'53,104,120',0.2);drawWave(H*0.90,16,0.008,3,'83,104,120',0.15);drawWave(H*0.94,12,0.010,4.5,'100,130,150',0.1);particles.forEach(p=>{p.angle+=p.drift;p.x+=Math.cos(p.angle)*p.speed;p.y+=Math.sin(p.angle)*p.speed*0.5-0.08;if(p.y<-10)p.y=H+10;if(p.x<-10)p.x=W+10;if(p.x>W+10)p.x=-10;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle='rgba(229,228,226,'+p.opacity+')';ctx.fill()});time+=0.008;requestAnimationFrame(animate)}
resize();initParticles();animate();
window.addEventListener('resize',()=>{resize();initParticles()});
function showMain(){document.getElementById('main-content').style.display='block';document.getElementById('privacy-page').classList.remove('active');document.getElementById('terms-page').classList.remove('active');window.scrollTo(0,0)}
function showPrivacy(){document.getElementById('main-content').style.display='none';document.getElementById('privacy-page').classList.add('active');document.getElementById('terms-page').classList.remove('active');window.scrollTo(0,0)}
function showTerms(){document.getElementById('main-content').style.display='none';document.getElementById('terms-page').classList.add('active');document.getElementById('privacy-page').classList.remove('active');window.scrollTo(0,0)}
function handleWaitlist(e){e.preventDefault();document.querySelector('.waitlist-row').style.display='none';document.getElementById('success-msg').style.display='block'}
function handleWaitlist2(e){e.preventDefault();e.target.style.display='none';document.getElementById('success-msg-2').style.display='block'}
function toggleFaq(btn){btn.closest('.faq-item').classList.toggle('open')}
</script>
</body>
</html>""")
print('Done -', os.path.getsize(path), 'bytes')
