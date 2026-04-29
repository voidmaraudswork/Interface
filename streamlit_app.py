import streamlit as st
import streamlit.components.v1 as components

# 1. PAGE CONFIG & TOTAL UI STRIPPING
st.set_page_config(page_title="VOID CORE", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stDecoration"] { visibility: hidden !important; }
    .stApp { background: #020205 !important; overflow: hidden !important; }
    .main .block-container { padding: 0 !important; max-width: 100vw !important; height: 100vh !important; overflow: hidden !important; }
    iframe { position: fixed; top: 0; left: 0; width: 100vw !important; height: 100vh !important; border: none !important; }
    </style>
""", unsafe_allow_html=True)

# 2. THE COMPLETE PORTAL (Intro + Hub + Warp)
components.html("""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #020205; color: white; font-family: 'Orbitron'; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; width: 100vw; overflow: hidden; }
        
        /* 3D Starfield Background */
        #bg-stars { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }

        /* BOOT SCREEN */
        #boot-screen { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #000; z-index: 2000; display: flex; flex-direction: column; justify-content: center; align-items: center; }
        .boot-msg { color: #00f2ff; font-size: 0.9rem; letter-spacing: 5px; margin-bottom: 20px; text-transform: uppercase; text-shadow: 0 0 10px #00f2ff; }
        .boot-bar { width: 200px; height: 2px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; }
        .boot-fill { width: 0%; height: 100%; background: #bc13fe; animation: boot-load 3s forwards ease-in-out; }
        @keyframes boot-load { to { width: 100%; } }

        /* WARP OVERLAY */
        #warp-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.95); display: none; flex-direction: column; justify-content: center; align-items: center; z-index: 1000; text-align: center; backdrop-filter: blur(20px); }
        .warp-msg { color: #bc13fe; font-size: 0.7rem; letter-spacing: 4px; margin-bottom: 10px; font-weight: bold; }
        .warp-fill { width: 0%; height: 3px; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; }

        /* HUB CONTENT */
        .main-container { display: flex; flex-direction: column; align-items: center; width: 90%; max-width: 440px; margin-top: -30px; }
        .hub-title { color: #00f2ff; letter-spacing: 12px; font-size: clamp(1.8rem, 7vw, 2.3rem); margin: 0; text-shadow: 0 0 15px rgba(0,242,255,0.5); }
        .hub-subtitle { color: #bc13fe; font-size: 0.55rem; letter-spacing: 5px; margin-top: 5px; margin-bottom: 30px; }

        /* NEON FLOW BUTTONS */
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; width: 100%; }
        
        .btn-container {
            position: relative; aspect-ratio: 1/1; border-radius: 15px; padding: 3px; /* The Border Thickness */
            background: linear-gradient(0deg, #00f2ff, #bc13fe, #00f2ff);
            background-size: 100% 200%;
            animation: flow 3s linear infinite;
            overflow: hidden; cursor: pointer;
        }
        
        @keyframes flow {
            0% { background-position: 0% 0%; }
            100% { background-position: 0% 200%; }
        }

        .btn-inner {
            width: 100%; height: 100%; background: #08080a; border-radius: 12px;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            color: #00f2ff; text-align: center;
        }

        .title-txt { font-size: 0.65rem; font-weight: 900; letter-spacing: 1px; color: #00f2ff !important; }
        .desc-txt { font-family: 'Rajdhani'; font-size: 0.55rem; color: #888 !important; margin-top: 8px; line-height: 1.1; padding: 0 10px; }

        /* FOOTER CREDIT */
        .footer-credit { position: fixed; bottom: 30px; color: #bc13fe; font-size: 0.75rem; letter-spacing: 4px; font-weight: bold; }
    </style>
</head>
<body>
    <!-- 1. BOOT SEQUENCE -->
    <div id="boot-screen">
        <div class="boot-msg">Portal to void core is opening...</div>
        <div class="boot-bar"><div class="boot-fill"></div></div>
        <div style="position:fixed; bottom:30px; color:#444; font-size:0.6rem; letter-spacing:3px;">VOIDMARAUDS</div>
    </div>

    <!-- 2. WARP OVERLAY -->
    <div id="warp-overlay">
        <p class="warp-msg">THE PORTAL TO VOID IS OPENING...</p>
        <h1 id="warp-title" style="color:#00f2ff; font-size:1.1rem; margin:0;"></h1>
        <p id="warp-desc" style="font-family:'Rajdhani'; color:#777; font-size:0.8rem; margin-top:10px; margin-bottom:20px;"></p>
        <div style="width:200px; height:3px; background:rgba(255,255,255,0.1);"><div id="fill" class="warp-fill"></div></div>
        <p style="font-size:0.5rem; margin-top:20px; color:#bc13fe; letter-spacing:3px;">CREDIT: VOIDMARAUDS</p>
    </div>

    <canvas id="bg-stars"></canvas>
    
    <div class="main-container">
        <h1 class="hub-title">VOID CORE</h1>
        <p class="hub-subtitle">TERMINAL ACCESS</p>

        <div class="grid">
            <div class="btn-container" onclick="warp('AI CODE FLATTENER', 'Flattening zip codes to MD files', 'https://aicodeflat.streamlit.app/')">
                <div class="btn-inner">
                    <div class="title-txt">AI CODE FLATTENER</div>
                    <div class="desc-txt">Flattening zip codes to MD files</div>
                </div>
            </div>
            <div class="btn-container" onclick="warp('MOVIE UPDATES', 'Updates every 5 mins with search', 'https://movievoidup.streamlit.app/')">
                <div class="btn-inner">
                    <div class="title-txt">MOVIE UPDATES</div>
                    <div class="desc-txt">Updates every 5 mins with search</div>
                </div>
            </div>
            <div class="btn-container" onclick="warp('MOVIE VIBE SEARCH', 'Search by genre, vibe, type etc', 'https://getmoviewithvoid.streamlit.app/')">
                <div class="btn-inner">
                    <div class="title-txt">MOVIE VIBE SEARCH</div>
                    <div class="desc-txt">Search by genre, vibe, type etc</div>
                </div>
            </div>
        </div>
    </div>

    <div class="footer-credit">VOIDMARAUDS</div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Starfield
        const sS=new THREE.Scene(), sC=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
        const sR=new THREE.WebGLRenderer({canvas:document.getElementById('bg-stars'), alpha:true});
        sR.setSize(window.innerWidth,window.innerHeight);
        const sG=new THREE.BufferGeometry(), sP=[];
        for(let i=0;i<2500;i++) sP.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
        sG.setAttribute('position', new THREE.Float32BufferAttribute(sP,3));
        sS.add(new THREE.Points(sG, new THREE.PointsMaterial({color:0xffffff, size:0.8})));
        sC.position.z=1;
        function anim(){ requestAnimationFrame(anim); sS.rotation.y+=0.0004; sR.render(sS,sC); } anim();

        // Boot Transition
        setTimeout(() => { document.getElementById('boot-screen').style.display = 'none'; }, 3200);

        // Warp Logic
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
