import streamlit as st
import streamlit.components.v1 as components
import time

# 1. PAGE CONFIG & TOTAL UI STRIPPING
st.set_page_config(page_title="VOID CORE | Terminal", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stDecoration"] { visibility: hidden !important; }
    .stApp { background: #020205 !important; overflow: hidden !important; }
    .main .block-container { padding: 0 !important; max-width: 100vw !important; height: 100vh !important; overflow: hidden !important; }
    iframe { position: fixed; top: 0; left: 0; width: 100vw !important; height: 100vh !important; border: none !important; }
    </style>
""", unsafe_allow_html=True)

if 'booted' not in st.session_state:
    st.session_state.booted = False

# --- PHASE 1: THE 3-SEC BOOTUP ---
if not st.session_state.booted:
    components.html("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap');
            body { background: #000; margin: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; font-family: 'Orbitron', sans-serif; }
            .msg { color: #00f2ff; font-size: 1.1rem; letter-spacing: 5px; text-align: center; margin-bottom: 20px; text-transform: uppercase; }
            .bar-bg { width: 220px; height: 2px; background: rgba(0,242,255,0.1); border-radius: 10px; overflow: hidden; }
            .bar-fill { width: 0%; height: 100%; background: #bc13fe; box-shadow: 0 0 15px #bc13fe; animation: load 3s forwards; }
            @keyframes load { to { width: 100%; } }
            .credit { position: fixed; bottom: 40px; color: #bc13fe; font-size: 0.7rem; letter-spacing: 5px; font-weight: bold; }
        </style>
        <div class="msg">BOOTING VOID CORE...</div>
        <div class="bar-bg"><div class="bar-fill"></div></div>
        <div class="credit">BY VOIDMARAUDS</div>
    """)
    time.sleep(3.2)
    st.session_state.booted = True
    st.rerun()

# --- PHASE 2: THE ICONIC HUB ---
else:
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500&display=swap" rel="stylesheet">
        <style>
            body { margin: 0; background: #020205; color: white; font-family: 'Orbitron'; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; width: 100vw; overflow: hidden; }
            #bg-stars { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }
            
            /* ICONIC FEATURE: THE CIRCUIT BORDER */
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; width: 92%; max-width: 440px; margin-top: 10px; }
            
            .btn { 
                aspect-ratio: 1/1; position: relative; 
                background: rgba(0, 0, 0, 0.6); border-radius: 15px; 
                display: flex; flex-direction: column; align-items: center; justify-content: center; 
                transition: 0.3s; cursor: pointer; overflow: hidden;
                border: 2px solid rgba(0, 242, 255, 0.2);
            }

            /* The Traveling Neon Beam */
            .btn::before {
                content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                border: 3px solid #00f2ff; border-radius: 15px;
                mask-image: linear-gradient(70deg, transparent 20%, #000 50%, transparent 80%);
                -webkit-mask-image: linear-gradient(70deg, transparent 20%, #000 50%, transparent 80%);
                animation: circuit 4s linear infinite;
                box-shadow: 0 0 15px #00f2ff;
            }

            @keyframes circuit {
                0% { transform: rotate(0deg) scale(1.5); }
                100% { transform: rotate(360deg) scale(1.5); }
            }

            .btn:hover { border-color: #bc13fe; transform: scale(1.03); }
            .btn:hover::before { border-color: #bc13fe; box-shadow: 0 0 25px #bc13fe; }

            .title-txt { font-size: 0.65rem; font-weight: 900; color: #00f2ff; z-index: 2; letter-spacing: 1px; }
            .desc-txt { font-family: 'Rajdhani'; font-size: 0.55rem; color: #888; margin-top: 8px; z-index: 2; line-height: 1.1; padding: 0 5px; }

            /* SYSTEM TICKER */
            .ticker {
                position: fixed; bottom: 0; width: 100%; background: rgba(188, 19, 254, 0.1);
                color: #bc13fe; font-size: 0.5rem; padding: 5px 0; border-top: 1px solid #bc13fe;
                font-family: 'Rajdhani'; white-space: nowrap; overflow: hidden; letter-spacing: 3px;
            }
            .ticker-wrap { display: inline-block; animation: scroll 20s linear infinite; }
            @keyframes scroll { from { transform: translateX(100%); } to { transform: translateX(-100%); } }

            /* OVERLAY */
            #warp-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #000; display: none; flex-direction: column; justify-content: center; align-items: center; z-index: 1000; }
            .loader-fill { width: 0%; height: 2px; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; margin-top: 20px; }
        </style>
    </head>
    <body>
        <canvas id="bg-stars"></canvas>
        
        <div id="warp-overlay">
            <p style="color:#bc13fe; font-size:0.6rem; letter-spacing:4px;">THE PORTAL TO VOID IS OPENING...</p>
            <h1 id="warp-title" style="color:#00f2ff; font-size:1.2rem;"></h1>
            <div style="width:200px; height:2px; background:rgba(255,255,255,0.1);"><div id="fill" class="loader-fill"></div></div>
        </div>

        <div style="text-align:center; margin-top: -50px;">
            <h1 style="color:#00f2ff; letter-spacing:15px; font-size: 2rem; margin: 0; text-shadow: 0 0 15px rgba(0,242,255,0.5);">VOID CORE</h1>
            <p style="color:#bc13fe; font-size:0.5rem; letter-spacing:6px; margin-bottom:20px;">STABLE LINK ESTABLISHED</p>
        </div>

        <div class="grid">
            <div class="btn" onclick="warp('AI CODE FLATTENER', 'https://aicodeflat.streamlit.app/')">
                <div class="title-txt">AI CODE FLATTENER</div>
                <div class="desc-txt">ZIP TO MARKDOWN</div>
            </div>
            <div class="btn" onclick="warp('MOVIE UPDATES', 'https://movievoidup.streamlit.app/')">
                <div class="title-txt">MOVIE UPDATES</div>
                <div class="desc-txt">5-MIN SYNC</div>
            </div>
            <div class="btn" onclick="warp('MOVIE VIBE SEARCH', 'https://getmoviewithvoid.streamlit.app/')">
                <div class="title-txt">VIBE SEARCH</div>
                <div class="desc-txt">GENRE FILTER</div>
            </div>
        </div>

        <div class="ticker">
            <div class="ticker-wrap">
                VOIDMARAUDS CORE ACCESS GRANTED /// SYSTEM TEMPERATURE: OPTIMAL /// PORTAL STATUS: ACTIVE /// ENCRYPTION: DEK-I AES-256 /// DATA STREAM: STABLE ///
            </div>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            // STARFIELD WITH GYRO SENSITIVITY
            const sS=new THREE.Scene(), sC=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
            const sR=new THREE.WebGLRenderer({canvas:document.getElementById('bg-stars'), alpha:true});
            sR.setSize(window.innerWidth,window.innerHeight);
            const sG=new THREE.BufferGeometry(), sP=[];
            for(let i=0;i<2500;i++) sP.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
            sG.setAttribute('position', new THREE.Float32BufferAttribute(sP,3));
            sS.add(new THREE.Points(sG, new THREE.PointsMaterial({color:0xffffff, size:0.8})));
            sC.position.z=1;

            // Tilt movement
            let mouseX = 0, mouseY = 0;
            document.addEventListener('mousemove', (e) => { mouseX = (e.clientX - window.innerWidth/2)/100; mouseY = (e.clientY - window.innerHeight/2)/100; });
            window.addEventListener('deviceorientation', (e) => { mouseX = e.gamma/10; mouseY = e.beta/10; });

            function anim(){ 
                requestAnimationFrame(anim); 
                sS.rotation.y += 0.0004 + (mouseX * 0.001); 
                sS.rotation.x += (mouseY * 0.001);
                sR.render(sS,sC); 
            } anim();

            function warp(title, url) {
                const overlay = document.getElementById('warp-overlay');
                const fill = document.getElementById('fill');
                document.getElementById('warp-title').innerText = title;
                overlay.style.display = 'flex';
                let start = null;
                function step(timestamp) {
                    if (!start) start = timestamp;
                    let progress = (timestamp - start) / 2000;
                    fill.style.width = Math.min(progress * 100, 100) + '%';
                    if (progress < 1) requestAnimationFrame(step);
                    else { window.open(url, '_blank'); setTimeout(() => { overlay.style.display='none'; fill.style.width='0%'; }, 1000); }
                }
                requestAnimationFrame(step);
            }
        </script>
    </body>
    </html>
    """)
