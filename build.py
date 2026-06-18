#!/usr/bin/env python3
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
deck = (ROOT / "act2-loopcraft" / "index.html").read_text()
# relocate the fourth-resource slide out of Act II into Act I (after the debt overlay)
_m = deck.index('class="slide s-fourth')
_fs = deck.rfind('<section', 0, _m)
_fe = deck.index('</section>', _m) + len('</section>')
FOURTH_IN_ACT1 = deck[_fs:_fe].replace('<div class="pagenum">05 / 9</div>', '<div class="pagenum">Act I</div>')
deck = deck[:_fs] + deck[_fe:]

def b64(p): return base64.b64encode(p.read_bytes()).decode()
png_b64   = b64(ROOT / "act1-debt-overlay" / "ml-debt.png")
svg_b64   = b64(ROOT / "act1-debt-overlay" / "agent-debt.svg")
jpg_b64   = b64(ROOT / "act2-loopcraft" / "5-models-same-harness-different-config.jpeg")
horse_b64 = b64(ROOT / "horse_harness.png")
vid_b64   = b64(ROOT / "anshuc-video-web.mp4")
loop_b64  = b64(ROOT / "loopcraft.jpg")  # actually a PNG despite the extension
about_b64 = b64(ROOT / "about-frame.jpg")

EXTRA_CSS = """
  /* ─── OPENING — harness engineering is ancient ─── */
  .s-open { background: var(--ink); }
  .s-open.hairlines::before, .s-open.hairlines::after { background: var(--paper); }
  .s-open .oeyebrow, .s-open .otitle, .s-open .osub, .s-open .oname { color: var(--paper); }
  .s-open .ometa { color: var(--paper); opacity: 0.75; }
  .s-open .ocap { color: var(--paper); opacity: 0.6; }
  .s-open .obyline { border-top-color: var(--paper); }
  .s-open .pagenum { color: var(--paper); opacity: 0.6; }
  .s-open .open-img img { border: 1.5px solid var(--paper); border-radius: 3px; background:#fff; }
  .s-open .open-frame { position: absolute; inset: clamp(76px, 8vh, 130px) clamp(36px, 3.6vw, 80px) clamp(90px, 9vh, 140px); display: grid; grid-template-columns: 1.08fr 0.92fr; gap: clamp(32px, 5vw, 90px); align-items: center; z-index: 5; }
  .s-open .oeyebrow { font-family: 'Hanken Grotesk', sans-serif; font-weight: 600; text-transform: uppercase; letter-spacing: 0.18em; font-size: clamp(12px, 0.95vw, 15px); color: var(--ink); margin-bottom: clamp(18px, 2.4vh, 34px); }
  .s-open .otitle { font-family: 'Newsreader', Georgia, serif; font-weight: 400; font-size: clamp(40px, min(5vw, 8.4vh), 96px); line-height: 1.0; letter-spacing: -0.006em; color: var(--ink); margin: 0; }
  .s-open .osub { font-family: 'Hanken Grotesk', sans-serif; font-size: clamp(15px, 1.05vw, 19px); line-height: 1.5; color: var(--ink); max-width: 42ch; margin-top: clamp(20px, 2.6vh, 38px); }
  .s-open .open-img { display: flex; align-items: center; justify-content: center; }
  .s-open .open-img img { max-width: 100%; max-height: 52vh; object-fit: contain; display: block; }
  .s-open .open-img { flex-direction: column; gap: clamp(10px, 1.4vh, 18px); }
  .s-open .ocap { align-self: center; text-align: center; font-family: 'Hanken Grotesk', sans-serif; font-weight: 600; text-transform: uppercase; letter-spacing: 0.16em; font-size: clamp(10px, 0.78vw, 13px); color: var(--ink); opacity: 0.55; }
  .s-open .obyline { margin-top: clamp(22px, 3vh, 44px); padding-top: clamp(12px, 1.6vh, 20px); border-top: 1.5px solid var(--ink); }
  .s-open .oname { font-family: 'Newsreader', Georgia, serif; font-size: clamp(20px, 1.9vw, 34px); color: var(--ink); }
  .s-open .ometa { font-family: 'DM Mono', ui-monospace, monospace; font-size: clamp(12px, 0.9vw, 15px); color: var(--ink); opacity: 0.7; letter-spacing: 0.04em; margin-top: 4px; }

  /* ─── ACT I — DEBT OVERLAY (click/key reveal, no opacity blend) ─── */
  .s-overlay { background: var(--paper); }
  .s-overlay .ov-stage { flex: 1; min-height: 0; display: flex; align-items: center; justify-content: center; padding: clamp(8px, 1.6vh, 22px) 0; }
  .s-overlay .figure { position: relative; width: min(88%, 1120px); max-height: 100%; aspect-ratio: 1333 / 533; cursor: pointer; }
  .s-overlay .figure img { position: absolute; inset: 0; width: 100%; height: 100%; display: block; object-fit: contain; }
  .s-overlay .figure .base { z-index: 1; }
  .s-overlay .figure .ov { z-index: 2; opacity: 0; transition: opacity 520ms ease; }
  .s-overlay .figure.revealed .ov { opacity: 1; }
  .s-overlay .ov-controls { display: flex; align-items: center; gap: clamp(12px, 2vw, 28px); flex-wrap: wrap; border-top: 1.5px solid var(--ink); padding-top: clamp(10px, 1.3vh, 18px); }
  .s-overlay .pill { font-family: 'DM Mono', monospace; font-size: clamp(11px, 0.82vw, 13px); border: 1.5px solid var(--ink); border-radius: 2px; padding: 6px 13px; cursor: pointer; background: var(--paper); color: var(--ink); letter-spacing: 0.04em; }
  .s-overlay .pill.on { background: var(--ink); color: var(--paper); }
  .s-overlay .ov-hint { font-family: 'DM Mono', monospace; font-size: clamp(10px, 0.78vw, 13px); opacity: 0.55; letter-spacing: 0.04em; margin-left: auto; }

  /* ─── ABOUT credentials strip ─── */
  .s-about .cred { margin-top: clamp(16px, 2.2vh, 30px); padding-top: clamp(12px, 1.6vh, 20px); border-top: 1.5px solid var(--ink); display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px clamp(16px, 2vw, 32px); }
  .s-about .cred .cred-lab { font-family: 'Hanken Grotesk', sans-serif; font-weight: 600; text-transform: uppercase; letter-spacing: 0.16em; font-size: clamp(11px, 0.82vw, 13px); color: var(--ink); opacity: 0.6; }
  .s-about .cred .ci { font-family: 'DM Mono', ui-monospace, monospace; font-size: clamp(11px, 0.86vw, 14px); color: var(--ink); }
  .s-about .about-body { flex: 1; min-height: 0; display: grid; grid-template-columns: 1.4fr 0.6fr; gap: clamp(26px, 3.2vw, 64px); align-items: stretch; margin-top: clamp(14px, 2vh, 28px); }
  .s-about .about-main { display: flex; flex-direction: column; min-height: 0; justify-content: center; }
  .s-about .about-main .about-lead { margin-top: 0; }
  .s-about .about-fig { display: flex; flex-direction: column; min-height: 0; gap: clamp(8px, 1.2vh, 14px); }
  .s-about .about-fig img { flex: 1; min-height: 0; width: 100%; object-fit: cover; object-position: 46% 26%; border: 1.5px solid var(--ink); border-radius: 3px; display: block; }
  .s-about .about-cap { font-family: 'Hanken Grotesk', sans-serif; font-weight: 600; text-transform: uppercase; letter-spacing: 0.14em; font-size: clamp(10px, 0.78vw, 13px); color: var(--ink); opacity: 0.55; text-align: right; }

  /* opening cobalt: color overrides LAST so they beat the .s-open base rules */
  .s-open .oeyebrow, .s-open .otitle, .s-open .osub, .s-open .oname { color: var(--paper); }
  .s-open .ometa { color: var(--paper); opacity: 0.75; }
  .s-open .ocap { color: var(--paper); opacity: 0.6; }
  .s-open .obyline { border-top-color: var(--paper); }
  .s-open .pagenum { color: var(--paper); opacity: 0.6; }
"""

OPENING_SLIDE = """
    <!-- OPENING — HARNESS ENGINEERING IS ANCIENT ─────────────────────── -->
    <section class="slide s-open hairlines active">
      <div class="open-frame">
        <div class="otext">
          <div class="oeyebrow caption">The agent as compiler</div>
          <h1 class="otitle">Harness engineering is as old as metallurgy.</h1>
          <p class="osub">A horse harness is an engineered system: collar, traces, and reins, all tuned to turn raw power into directed work. The discipline is thousands of years old.</p>
          <div class="obyline">
            <div class="oname">Nirant Kasliwal</div>
            <div class="ometa">Scaled Focus &middot; nirantk.com &middot; @nirantk</div>
          </div>
        </div>
        <div class="open-img">
          <img src="data:image/png;base64,__HORSE__" alt="An engraving of a horse harness: collar, traces, and reins" />
          <div class="ocap caption">The original harness</div>
        </div>
      </div>
      <div class="pagenum">Opening</div>
    </section>
"""

ABOUT_SLIDE = """
    <!-- ACT I — ABOUT · NIRANT / SCALED FOCUS ─────────────────────────── -->
    <section class="slide s-about hairlines">
      <div class="topframe">
        <div class="topbar">
          <div class="h">I'm Nirant.</div>
          <div class="lab-tag caption">Scaled Focus</div>
        </div>
        <div class="about-body">
          <div class="about-main">
            <div class="about-lead">We help agent companies build better agent harnesses.</div>
            <div class="timeline">
              <div class="trow"><div class="yr">2025</div><div class="tt">Helped Ragas modernize. Ran search evals with Littlebird.ai.</div></div>
              <div class="trow"><div class="yr">2026</div><div class="tt">Helped Kavana cut costs 40% with caching, at 1M chats a day. LiteLLM contributors.</div></div>
              <div class="trow"><div class="yr">Now</div><div class="tt">Optimizing a presentations harness to 10 cents a deck.</div></div>
            </div>
            <div class="cred">
              <span class="cred-lab">Earlier</span>
              <span class="ci">Author, "NLP in Python", 5,000+ copies</span>
              <span class="ci">Built FastEmbed, used by NVIDIA Nemo Guardrails and 3,000+ repos</span>
              <span class="ci">Top 5 GenAI Scientists in India, 2023</span>
            </div>
          </div>
          <div class="about-fig">
            <img src="about-frame.jpg" alt="Nirant presenting NLP for Indic Languages at Wingify DevFest 2018" />
            <div class="about-cap">NLP for Indic Languages, Wingify DevFest 2018</div>
          </div>
        </div>
      </div>
      <div class="pagenum">Act I</div>
    </section>
"""

DIVIDER_ACT2 = """
    <!-- TRANSITION — END OF ACT I → ACT II ────────────────────────────── -->
    <section class="slide s-divider">
      <div class="dpx" aria-hidden="true">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <defs><pattern id="dpxA" width="2.4" height="100" patternUnits="userSpaceOnUse"><line x1="0.5" y1="0" x2="0.5" y2="100" stroke="#F0EBDE" stroke-width="1.0"/></pattern></defs>
          <rect x="36" y="0"  width="38" height="14" fill="url(#dpxA)"/>
          <rect x="22" y="14" width="50" height="12" fill="url(#dpxA)"/>
          <rect x="34" y="26" width="46" height="11" fill="url(#dpxA)"/>
          <rect x="16" y="37" width="60" height="13" fill="url(#dpxA)"/>
          <rect x="28" y="50" width="48" height="11" fill="url(#dpxA)"/>
          <rect x="18" y="61" width="62" height="14" fill="url(#dpxA)"/>
          <rect x="34" y="75" width="44" height="12" fill="url(#dpxA)"/>
          <rect x="22" y="87" width="50" height="13" fill="url(#dpxA)"/>
        </svg>
      </div>
      <div class="dframe">
        <div class="deyebrow">Act II</div>
        <h2 class="dtitle">Coding Agents<br/>are Compilers.</h2>
        <div class="dsub">With general models, coding agents combine to show convergent behaviour.</div>
      </div>
      <div class="pagenum"></div>
    </section>
"""

OVERLAY_SLIDE = """
    <!-- ACT I — ML DEBT vs AGENT DEBT, CLICK/KEY REVEAL ─────────────── -->
    <section class="slide s-overlay hairlines">
      <div class="topframe">
        <div class="topbar">
          <div class="h">The shape was always the same.</div>
          <div class="lab-tag caption">ML debt, 2014 &nbsp;&#8596;&nbsp; harness, today</div>
        </div>
        <div class="ov-stage">
          <div class="figure" id="ovfig">
            <img class="base" src="data:image/png;base64,__MLDEBT__" alt="ML technical debt, Sculley et al. 2014: a tiny ML Code box surrounded by infrastructure" />
            <img class="ov" id="ovimg" src="data:image/svg+xml;base64,__AGENTDEBT__" alt="Harness engineering: a tiny LLM box surrounded by harness layers" />
          </div>
        </div>
        <div class="ov-controls">
          <button class="pill" id="ovBase">ML 2014</button>
          <button class="pill" id="ovAgent">Agent</button>
          <span class="ov-hint">click the figure, or &#8593; / &#8595;, to reveal the agent-era harness</span>
        </div>
      </div>
      <div class="pagenum">Act I</div>
    </section>
"""

CONNECTOR_SLIDE = """
    <!-- BRIDGE — ACT I → ACT II ───────────────────────────────────────── -->
    <section class="slide s-manifesto hairlines">
      <div class="pixel-glitch" aria-hidden="true">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <defs><pattern id="vsBridge" width="2.4" height="100" patternUnits="userSpaceOnUse"><line x1="0.5" y1="0" x2="0.5" y2="100" stroke="#1F2BE0" stroke-width="1.0"/></pattern></defs>
          <rect x="36" y="0" width="38" height="14" fill="url(#vsBridge)"/>
          <rect x="22" y="14" width="50" height="12" fill="url(#vsBridge)"/>
          <rect x="34" y="26" width="46" height="11" fill="url(#vsBridge)"/>
          <rect x="16" y="37" width="60" height="13" fill="url(#vsBridge)"/>
          <rect x="28" y="50" width="48" height="11" fill="url(#vsBridge)"/>
          <rect x="18" y="61" width="62" height="14" fill="url(#vsBridge)"/>
          <rect x="34" y="75" width="44" height="12" fill="url(#vsBridge)"/>
          <rect x="22" y="87" width="50" height="13" fill="url(#vsBridge)"/>
        </svg>
      </div>
      <div class="stmt-wrap">
        <p class="stmt">The model is the smallest box, and it should keep getting smaller. Everything that matters is the harness around it. That <span class="amb">model</span> + <span class="amb">harness</span> = <span class="amb">agent</span>.</p>
        <div class="attr">
          <div class="who caption">The bridge</div>
          <div class="meta-tag caption">Act I &#8594; Act II</div>
        </div>
      </div>
      <div class="pagenum">Act I &#8594; II</div>
    </section>
"""

OVERLAY_JS = """
<script>
  (function(){
    const fig=document.getElementById('ovfig'); if(!fig) return;
    const base=document.getElementById('ovBase'), agent=document.getElementById('ovAgent');
    const on=()=>fig.classList.contains('revealed');
    const set=v=>{fig.classList.toggle('revealed',v);agent.classList.toggle('on',v);base.classList.toggle('on',!v);};
    fig.addEventListener('click',()=>set(!on()));
    base.addEventListener('click',e=>{e.stopPropagation();set(false);});
    agent.addEventListener('click',e=>{e.stopPropagation();set(true);});
    set(false);
    document.addEventListener('keydown',e=>{
      const sl=fig.closest('.slide'); if(!sl||!sl.classList.contains('active')) return;
      if(e.key==='ArrowUp'){e.preventDefault();set(true);}
      else if(e.key==='ArrowDown'){e.preventDefault();set(false);}
    });
  })();
</script>
"""

POLICY_SLIDE = """
    <!-- ACT I — CODE IS THE POLICY -->
    <section class="slide s-chapter hairlines">
      <div class="pixel-glitch" aria-hidden="true">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <defs><pattern id="vsPolicy" width="2.4" height="100" patternUnits="userSpaceOnUse"><line x1="0.5" y1="0" x2="0.5" y2="100" stroke="#1F2BE0" stroke-width="1.0"/></pattern></defs>
          <rect x="36" y="0" width="38" height="14" fill="url(#vsPolicy)"/>
          <rect x="22" y="14" width="50" height="12" fill="url(#vsPolicy)"/>
          <rect x="34" y="26" width="46" height="11" fill="url(#vsPolicy)"/>
          <rect x="16" y="37" width="60" height="13" fill="url(#vsPolicy)"/>
          <rect x="28" y="50" width="48" height="11" fill="url(#vsPolicy)"/>
          <rect x="18" y="61" width="62" height="14" fill="url(#vsPolicy)"/>
          <rect x="34" y="75" width="44" height="12" fill="url(#vsPolicy)"/>
          <rect x="22" y="87" width="50" height="13" fill="url(#vsPolicy)"/>
        </svg>
      </div>
      <div class="frame">
        <div class="nm-tag">Reinforcement learning, in one line</div>
        <div class="ttl">Code is the policy.</div>
        <div class="lede">The harness is just code: the loop, the tools, the prompt. In reinforcement learning, the policy is what turns a state into an action, and that code shapes what the agent does as much as the weights do. So the harness is the policy. Liang et al. named it early: Code as Policies, arxiv.org/abs/2209.07753.</div>
      </div>
      <div class="pagenum"></div>
    </section>
"""

deck = deck.replace("</style>", EXTRA_CSS + "</style>", 1)
deck = deck.replace("slide s-cover hairlines active", "slide s-cover hairlines", 1)
deck = deck.replace('<div class="stage">', '<div class="stage">\n' + OPENING_SLIDE + ABOUT_SLIDE + OVERLAY_SLIDE + FOURTH_IN_ACT1 + POLICY_SLIDE + CONNECTOR_SLIDE + DIVIDER_ACT2, 1)
deck = deck.replace("</body>", OVERLAY_JS + "\n</body>", 1)
deck = deck.replace("__HORSE__", horse_b64).replace("__MLDEBT__", png_b64).replace("__AGENTDEBT__", svg_b64)
deck = deck.replace('src="5-models-same-harness-different-config.jpeg"', 'src="data:image/jpeg;base64,' + jpg_b64 + '"')
deck = deck.replace('src="anshuc-video-web.mp4"', 'src="data:video/mp4;base64,' + vid_b64 + '"')
deck = deck.replace('src="loopcraft.jpg"', 'src="data:image/png;base64,' + loop_b64 + '"')
deck = deck.replace('src="about-frame.jpg"', 'src="data:image/jpeg;base64,' + about_b64 + '"')
deck = deck.replace("<title>Act II · Coding Agents Are Compilers · Loopcraft</title>",
                    "<title>The Agent as Compiler</title>", 1)

import re as _re
_total = deck.count('class="pagenum"')
_ctr = [0]
def _renum(_m):
    _ctr[0] += 1
    return '<div class="pagenum">%02d / %d</div>' % (_ctr[0], _total)
deck = _re.sub(r'<div class="pagenum">[^<]*</div>', _renum, deck)

out = ROOT / "agent-as-compiler.html"
out.write_text(deck)
print("wrote", out, "size", round(out.stat().st_size/1048576, 2), "MB")
print("slides:", deck.count('<section class="slide'))
print("active slides:", deck.count('hairlines active'))
print("opening present:", 'as old as metallurgy' in deck)
print("video embedded:", 'data:video/mp4;base64,' in deck)
print("ext media refs (want 0):", deck.count('src="') - deck.count('src="data:'))
