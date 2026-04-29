import streamlit as st
import streamlit.components.v1 as components
import time

# 1. PAGE CONFIG & TOTAL UI STRIPPING
st.set_page_config(page_title="VOID CORE", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stDecoration"] { visibility: hidden !important; }
    .stApp { background: #020205 !important; overflow: hidden !important; }
    .main .block-container { padding: 0 !important; max-width: 100vw !important; height: 100vh !important; overflow: hidden !important; }
    
    iframe { 
        position: fixed;
        top: 0; left: 0;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. SESSION STATE FOR BOOTUP
if 'booted' not in st.session_state:
    st.session_state.booted = False

# --- PHASE 1: THE 3-SEC BOOTUP ---
if not st.session_state.booted:
    components.html("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap');
            body { 
                background: #000; margin: 0; overflow: hidden; 
                display: flex; flex-direction: column; justify-content: center; align-items: center; 
                height: 100vh; width: 100vw; font-family: 'Orbitron', sans-serif; 
            }
            .msg { color: #00f2ff; font-size: clamp(0.9rem, 4vw, 1.3rem); letter-spacing: 4px; text-align: center; margin-bottom: 20px; text-transform: uppercase; }
            .bar-bg { width: 220px; height: 3px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; }
            .bar-fill { width: 0%; height: 100%; background: #bc13fe; box-shadow: 0 0 15px #bc13fe; animation: load 3s forwards ease-in-out; }
            @keyframes load { to { width: 100%; } }
            .credit { position: fixed; bottom: 40px; color: #bc13fe; font-size: 0.7rem; letter-spacing: 4px; font-weight: bold; }
        </style>
        <div class="msg">Portal to void core is opening...</div>
        <div class="bar-bg"><div class="bar-fill"></div></div>
        <div class="credit">BY VOIDMARAUDS</div>
    """)
    time.sleep(3.2)
    st.session_state.booted = True
    st.rerun()

# --- PHASE 2: THE MAIN HUB ---
else:
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500&display=swap" rel="stylesheet">
        <style>
            body { 
                margin: 0; background: #020205; color: white; font-family: 'Orbitron'; 
                display: flex; flex-direction: column; align-items: center; justify-content: center; 
                height: 100vh; width: 100vw; overflow: hidden; 
            }
            #bg-stars { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }
            
            #warp-overlay { 
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
                background: rgba(0,0,0,0.98); display: none; flex-direction: column; 
                justify-content: center; align-items: center; z-index: 100; text-align: center; 
            }
            .portal-msg { color: #bc13fe; font-size: 0.65rem; letter-spacing: 3px; margin-bottom: 10px; font-weight: 900; }
            .loader-container { width: 240px; height: 3px; background: rgba(255,255,255,0.1); border-radius: 10px; margin-top: 25px; overflow: hidden; }
            .loader-fill { width: 0%; height: 100%; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; }

            /* PERFECTLY CENTERED HUB */
            .main-container { display: flex; flex-direction: column; align-items: center; width: 90%; max-width: 450px; margin-top: -30px; }
            .hub-title { color: #00f2ff; letter-spacing: 12px; font-size: clamp(1.8rem, 7vw, 2.3rem); margin: 0; text-align: center; text-shadow: 0 0 15px rgba(0,242,255,0.5); }
            .hub-subtitle { color: #bc13fe; font-size: 0.55rem; letter-spacing: 5px; margin-top: 5px; margin-bottom: 30px; opacity: 0.9; }

            /* THICK NEON GRID */
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; width: 100%; }
            
            .btn { 
                aspect-ratio: 1/1; 
                /* THICK OUTLINE START */
                border: 3px solid #00f2ff; 
                box-shadow: 0 0 10px rgba(0, 242, 255, 0.4), inset 0 0 10px rgba(0, 242, 255, 0.2);
                border-radius: 20px; 
                display: flex; flex-direction: column; align-items: center; justify-content: center; 
                color: #00f2ff; transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); padding: 10px; text-align: center;
                background: rgba(255,255,255,0.02); backdrop-filter: blur(8px); cursor: pointer; text-decoration: none;
                animation: neon-breath 3s infinite alternate;
            }

            @keyframes neon-breath {
                from { border-width: 3px; box-shadow: 0 0 8px #00f2ff, inset 0 0 5px #00f2ff; }
                to { border-width: 3px; box-shadow: 0 0 18px #00f2ff, inset 0 0 12px #00f2ff; }
            }

            .btn:hover { 
                border-color: #bc13fe; 
                color: #bc13fe;
                box-shadow: 0 0 35px #bc13fe, inset 0 0 20px #bc13fe;
                transform: translateY(-5px) scale(1.02);
                animation: none; /* Stop breathing on hover */
            }
            
            .title-txt { font-size: 0.7rem; font-weight: 900; pointer-events: none; letter-spacing: 1px; }
            .desc-txt { font-family: 'Rajdhani'; font-size: 0.58rem; color: #aaa; margin-top: 8px; pointer-events: none; line-height: 1.2; padding: 0 5px; }

            .footer-credit { position: fixed; bottom: 30px; color: #bc13fe; font-size: 0.75rem; letter-spacing: 4px; font-weight: bold; text-transform: uppercase; z-index: 10; }
        </style>
    </head>
    <body>
        <canvas id="bg-stars"></canvas>
        
        <div id="warp-overlay">
            <p class="portal-msg">THE PORTAL TO VOID IS OPENING...</p>
            <h1 style="color: #00f2ff; font-size: 1.1rem; letter-spacing: 3px;" id="warp-title"></h1>
            <p style="font-family:'Rajdhani'; color:#777; font-size:0.75rem; margin-top:8px; padding: 0 20px;" id="warp-desc"></p>
            <div class="loader-container"><div id="fill" class="loader-fill"></div></div>
            <p style="font-size: 0.55rem; margin-top: 20px; color: #bc13fe; letter-spacing: 3px; font-weight: bold;">CREDIT: VOIDMARAUDS</p>
        </div>

        <div class="main-container">
            <h1 class="hub-title">VOID CORE</h1>
            <p class="hub-subtitle">TERMINAL ACCESS</p>

            <div class="grid">
                <div class="btn" onclick="warp('AI CODE FLATTENER', 'DECONSTRUCTING ZIP TO MARKDOWN', 'https://aicodeflat.streamlit.app/')">
                    <div class="title-txt">AI CODE FLATTENER</div>
                    <div class="desc-txt">Flattening zip codes to MD files</div>
                </div>
                <div class="btn" onclick="warp('MOVIE UPDATES', 'REAL-TIME CINEMATIC SYNC', 'https://movievoidup.streamlit.app/')">
                    <div class="title-txt">MOVIE UPDATES</div>
                    <div class="desc-txt">Updates every 5 mins with search</div>
                </div>
                <div class="btn" onclick="warp('MOVIE VIBE SEARCH', 'GENRE & EMOTION FILTERING', 'https://getmoviewithvoid.streamlit.app/')">
                    <div class="title-txt">MOVIE VIBE SEARCH</div>
                    <div class="desc-txt">Search movies by genre, vibe, type</div>
                </div>
            </div>
        </div>

        <div class="footer-credit">VOIDMARAUDS</div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const sS=new THREE.Scene(), sC=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
            const sR=new THREE.WebGLRenderer({canvas:document.getElementById('bg-stars'), alpha:true});
            sR.setSize(window.innerWidth,window.innerHeight);
            const sG=new THREE.BufferGeometry(), sP=[];
            for(let i=0;i<2500;i++) sP.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
            sG.setAttribute('position', new THREE.Float32BufferAttribute(sP,3));
            sS.add(new THREE.Points(sG, new THREE.PointsMaterial({color:0xffffff, size:0.8})));
            sC.position.z=1;
            function animS(){ requestAnimationFrame(animS); sS.rotation.y+=0.0004; sR.render(sS,sC); } animS();

            function warp(title, desc, url) {
                const overlay = document.getElementById('warp-overlay');
                const fill = document.getElementById('fill');
                document.getElementById('warp-title').innerText = title;
                document.getElementById('warp-desc').innerText = desc;
                overlay.style.display = 'flex';
                let start = null;
                function step(timestamp) {
                    if (!start) start = timestamp;
                    let progress = (timestamp - start) / 2000;
                    fill.style.width = Math.min(progress * 100, 100) + '%';
                    if (progress < 1) { requestAnimationFrame(step); } 
                    else { 
                        window.open(url, '_blank');
                        setTimeout(() => { overlay.style.display = 'none'; fill.style.width = '0%'; }, 1000);
                    }
                }
                requestAnimationFrame(step);
            }
        </script>
    </body>
    </html>
    """)
