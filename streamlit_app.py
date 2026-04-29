import streamlit as st
import streamlit.components.v1 as components
import time

# 1. PAGE CONFIG & UI HIDING
st.set_page_config(page_title="VOID CORE", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stDecoration"] { visibility: hidden !important; }
    .stApp { background: #020205 !important; }
    .main .block-container { padding: 0 !important; max-width: 100vw !important; }
    </style>
""", unsafe_allow_html=True)

# 2. SESSION STATE FOR BOOT SEQUENCE
if 'booted' not in st.session_state:
    st.session_state.booted = False

# --- PHASE 1: THE 3-SEC BOOTUP WINDOW ---
if not st.session_state.booted:
    components.html("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap');
            body { background: #000; margin: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; font-family: 'Orbitron'; overflow: hidden; }
            .msg { color: #00f2ff; font-size: 1.2rem; letter-spacing: 5px; text-align: center; text-shadow: 0 0 15px #00f2ff; margin-bottom: 25px; text-transform: uppercase; }
            .bar-bg { width: 280px; height: 2px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; }
            .bar-fill { width: 0%; height: 100%; background: #bc13fe; box-shadow: 0 0 15px #bc13fe; animation: load 3s forwards ease-in-out; }
            @keyframes load { to { width: 100%; } }
            .credit { position: fixed; bottom: 20px; color: rgba(255,255,255,0.3); font-size: 0.6rem; letter-spacing: 3px; }
        </style>
        <div class="msg">Portal to void core is opening...</div>
        <div class="bar-bg"><div class="bar-fill"></div></div>
        <div class="credit">BY VOIDMARAUDS</div>
    """, height=1000)
    time.sleep(3.5)
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
            body { margin: 0; background: #020205; color: white; font-family: 'Orbitron'; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; overflow: hidden; }
            #bg-stars { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }
            
            /* LOADING OVERLAY */
            #warp-overlay { 
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
                background: rgba(0,0,0,0.98); display: none; flex-direction: column; 
                justify-content: center; align-items: center; z-index: 100; text-align: center; 
            }
            .portal-msg { color: #bc13fe; font-size: 0.6rem; letter-spacing: 4px; margin-bottom: 15px; font-weight: bold; }
            .loader-container { width: 260px; height: 3px; background: rgba(255,255,255,0.1); border-radius: 10px; margin-top: 30px; overflow: hidden; }
            .loader-fill { width: 0%; height: 100%; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; }

            /* HUB UI */
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; width: 92%; max-width: 500px; z-index: 10; margin-top: 20px; }
            .btn { 
                aspect-ratio: 1/1; border: 1px solid rgba(0, 242, 255, 0.2); border-radius: 20px; 
                display: flex; flex-direction: column; align-items: center; justify-content: center; 
                color: #00f2ff; transition: 0.3s; padding: 15px; text-align: center;
                background: rgba(255,255,255,0.02); backdrop-filter: blur(10px); cursor: pointer;
            }
            .btn:hover { border-color: #00f2ff; box-shadow: 0 0 25px rgba(0, 242, 255, 0.2); transform: translateY(-5px); }
            .title-txt { font-size: 0.75rem; font-weight: 900; pointer-events: none; }
            .desc-txt { font-family: 'Rajdhani'; font-size: 0.6rem; color: #888; margin-top: 8px; pointer-events: none; line-height: 1.1; }

            /* CREDIT FOOTER */
            .footer-credit { position: fixed; bottom: 15px; color: rgba(255,255,255,0.2); font-size: 0.5rem; letter-spacing: 4px; text-transform: uppercase; }
        </style>
    </head>
    <body>
        <canvas id="bg-stars"></canvas>
        
        <!-- CLICK LOADING OVERLAY -->
        <div id="warp-overlay">
            <p class="portal-msg">THE PORTAL TO VOID IS OPENING...</p>
            <h1 style="color: #00f2ff; font-size: 1.4rem; letter-spacing: 4px;" id="warp-title"></h1>
            <p style="font-family:'Rajdhani'; color:#555; font-size:0.8rem; margin-top:8px;" id="warp-desc"></p>
            <div class="loader-container"><div id="fill" class="loader-fill"></div></div>
            <p style="font-size: 0.4rem; margin-top: 20px; color: #333; letter-spacing: 2px;">CREDIT: VOIDMARAUDS</p>
        </div>

        <h1 style="color:#00f2ff; letter-spacing:18px; font-size: 2.2rem; margin-bottom: 5px;">VOID CORE</h1>
        <p style="color: #bc13fe; font-size: 0.55rem; letter-spacing: 6px; margin-bottom: 35px; opacity: 0.8;">TERMINAL ACCESS</p>

        <div class="grid">
            <div class="btn" onclick="warp('AI CODE FLATTENER', 'DECONSTRUCTING ZIP TO MARKDOWN', 'https://aicodeflat.streamlit.app/')">
                <div class="title-txt">AI CODE FLATTENER</div>
                <div class="desc-txt">Flattening zip codes to MD files</div>
            </div>
            <div class="btn" onclick="warp('MOVIE UPDATES', 'REAL-TIME CINEMATIC SYNC', 'https://movievoidup.streamlit.app/')">
                <div class="title-txt">MOVIE UPDATES</div>
                <div class="desc-txt">Updates every 5 mins with search facility</div>
            </div>
            <div class="btn" onclick="warp('MOVIE VIBE SEARCH', 'GENRE & EMOTION FILTERING', 'https://getmoviewithvoid.streamlit.app/')">
                <div class="title-txt">MOVIE VIBE SEARCH</div>
                <div class="desc-txt">Search movies by genre, vibe, type etc</div>
            </div>
        </div>

        <div class="footer-credit">voidmarauds</div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            // BACKGROUND STARS
            const sS=new THREE.Scene(), sC=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
            const sR=new THREE.WebGLRenderer({canvas:document.getElementById('bg-stars'), alpha:true});
            sR.setSize(window.innerWidth,window.innerHeight);
            const sG=new THREE.BufferGeometry(), sP=[];
            for(let i=0;i<3000;i++) sP.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
            sG.setAttribute('position', new THREE.Float32BufferAttribute(sP,3));
            sS.add(new THREE.Points(sG, new THREE.PointsMaterial({color:0xffffff, size:0.7})));
            sC.position.z=1;
            function animS(){ requestAnimationFrame(animS); sS.rotation.y+=0.0004; sR.render(sS,sC); } animS();

            // WARP LOADING
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
    """, height=1000)
