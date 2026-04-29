import streamlit as st
import streamlit.components.v1 as components

# 1. PAGE CONFIG
st.set_page_config(page_title="VOID CORE", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stDecoration"] { visibility: hidden !important; }
    .stApp { background: #020205 !important; overflow: hidden !important; }
    .main .block-container { padding: 0 !important; max-width: 100vw !important; height: 100vh !important; overflow: hidden !important; }
    iframe { position: fixed; top: 0; left: 0; width: 100vw !important; height: 100vh !important; border: none !important; }
    </style>
""", unsafe_allow_html=True)

# 2. THE CORE ENGINE
components.html("""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #020205; color: white; font-family: 'Orbitron'; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; width: 100vw; overflow: hidden; }
        #bg-stars { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }

        /* PHASE 1: BOOT SCREEN */
        #boot-screen { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #000; z-index: 9000; display: flex; flex-direction: column; justify-content: center; align-items: center; }
        .boot-bar { width: 200px; height: 2px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; margin-top:20px; }
        .boot-fill { width: 0%; height: 100%; background: #bc13fe; animation: boot-load 3s forwards ease-in-out; }
        @keyframes boot-load { to { width: 100%; } }

        /* PHASE 2: SELECTION PROTOCOL POPUP */
        #selection-popup { 
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
            background: rgba(0,0,0,0.95); z-index: 8000; display: none; 
            flex-direction: column; justify-content: center; align-items: center; 
            backdrop-filter: blur(25px); text-align: center;
        }
        .modal-box { 
            width: 85%; max-width: 450px; padding: 25px; border: 3px solid #00f2ff; 
            background: #050505; border-radius: 25px; box-shadow: 0 0 40px rgba(0, 242, 255, 0.4);
        }
        .select-grid { display: flex; flex-direction: column; gap: 10px; margin: 20px 0; }
        .select-item { 
            padding: 12px; border: 1px solid rgba(0, 242, 255, 0.2); border-radius: 12px; 
            text-align: left; cursor: pointer; transition: 0.3s;
        }
        .select-item.active { border-color: #bc13fe; background: rgba(188, 19, 254, 0.15); box-shadow: 0 0 15px #bc13fe; }
        .confirm-btn { 
            width: 100%; padding: 15px; border: 1px solid #00f2ff; background: transparent; 
            color: #00f2ff; font-family: 'Orbitron'; cursor: pointer; opacity: 0.3; pointer-events: none;
        }
        .confirm-btn.ready { opacity: 1; pointer-events: auto; background: rgba(0, 242, 255, 0.1); }

        /* MAIN HUB UI */
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; width: 92%; max-width: 440px; margin-top: 15px; }
        
        /* FLOWING NEON BORDERS */
        .btn-container {
            position: relative; aspect-ratio: 1/1; border-radius: 18px; padding: 3px; 
            background: linear-gradient(0deg, #00f2ff, #bc13fe, #00f2ff);
            background-size: 100% 200%; animation: flow 3s linear infinite;
            overflow: hidden; cursor: pointer;
        }
        @keyframes flow { 0% { background-position: 0% 0%; } 100% { background-position: 0% 200%; } }
        
        .btn-inner { width: 100%; height: 100%; background: #08080a; border-radius: 16px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
        .title-sm { font-size: 0.65rem; color: #00f2ff; font-weight: 900; padding: 0 5px; text-transform: uppercase; }
        .desc-sm { font-family: 'Rajdhani'; font-size: 0.5rem; color: #777; margin-top: 5px; padding: 0 10px; line-height: 1.1; }

        /* NEON RED CROSS FOR LOCKED MODULE */
        .locked-overlay {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(255, 0, 0, 0.15); backdrop-filter: grayscale(1) blur(3px);
            z-index: 100; display: flex; justify-content: center; align-items: center;
        }
        .locked-overlay::before, .locked-overlay::after {
            content: ''; position: absolute; width: 85%; height: 6px; background: #ff0055;
            box-shadow: 0 0 20px #ff0055; border-radius: 10px;
        }
        .locked-overlay::before { transform: rotate(45deg); }
        .locked-overlay::after { transform: rotate(-45deg); }

        /* PHASE 3: WARP OVERLAY */
        #warp-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #000; display: none; flex-direction: column; justify-content: center; align-items: center; z-index: 7000; }
        .warp-fill { width: 0%; height: 3px; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; }
    </style>
</head>
<body>
    <canvas id="bg-stars"></canvas>

    <!-- BOOT SCREEN -->
    <div id="boot-screen">
        <div style="color:#00f2ff; letter-spacing:5px; font-size:0.8rem; text-align:center;">PORTAL TO VOID CORE IS OPENING...</div>
        <div class="boot-bar"><div class="boot-fill"></div></div>
    </div>

    <!-- SELECTION POPUP -->
    <div id="selection-popup">
        <div class="modal-box">
            <h2 style="color:#00f2ff; font-size:0.9rem; letter-spacing:2px; margin:0;">SELECT 2 MODULES</h2>
            <p style="font-family:'Rajdhani'; color:#777; font-size:0.7rem; margin-top:8px;">PORTAL TO VOID CORE IS OPENING... <br>Choose 2 modules to stabilize for 24 hours.</p>
            
            <div class="select-grid">
                <div class="select-item" onclick="toggleSelect(this, 'btn-1')">
                    <b style="color:#00f2ff; font-size:0.7rem;">AI CODE FLATTENER</b><br>
                    <small style="color:#666; font-family:'Rajdhani';">Flattening zip codes to MD files</small>
                </div>
                <div class="select-item" onclick="toggleSelect(this, 'btn-2')">
                    <b style="color:#00f2ff; font-size:0.7rem;">MOVIE UPDATES</b><br>
                    <small style="color:#666; font-family:'Rajdhani';">Updates every 5 mins with search</small>
                </div>
                <div class="select-item" onclick="toggleSelect(this, 'btn-3')">
                    <b style="color:#00f2ff; font-size:0.7rem;">VIBE SEARCH</b><br>
                    <small style="color:#666; font-family:'Rajdhani';">Search movies by genre, vibe, type etc</small>
                </div>
            </div>
            <button class="confirm-btn" id="confirm-protocol" onclick="finalizeChoices()">LOCK SELECTION</button>
        </div>
    </div>

    <!-- LOADING WARP -->
    <div id="warp-overlay">
        <p style="color:#bc13fe; font-size:0.6rem; letter-spacing:4px; font-weight:bold;">PORTAL TO VOID CORE IS OPENING...</p>
        <h1 id="warp-title" style="color:#00f2ff; font-size:1.2rem; margin:10px 0;"></h1>
        <div style="width:200px; height:3px; background:rgba(255,255,255,0.1); margin:15px 0;"><div id="fill" class="warp-fill"></div></div>
        <p style="font-size:0.55rem; color:#bc13fe; letter-spacing:4px; font-weight:bold;">CREDIT: VOIDMARAUDS</p>
    </div>

    <!-- MAIN INTERFACE -->
    <h1 style="color:#00f2ff; letter-spacing:15px; font-size: 2rem; margin:0; margin-top:-20px;">VOID CORE</h1>
    <p style="color:#bc13fe; font-size:0.5rem; letter-spacing:6px; margin-bottom:20px;">TERMINAL ACCESS</p>

    <div class="grid">
        <div class="btn-container" id="btn-1" onclick="handleInteraction('btn-1', 'AI CODE FLATTENER', 'Flattening zip codes to MD files', 'https://aicodeflat.streamlit.app/')">
            <div class="btn-inner"><div class="title-sm">AI CODE FLATTENER</div><div class="desc-sm">Flattening zip codes to MD files</div></div>
        </div>
        <div class="btn-container" id="btn-2" onclick="handleInteraction('btn-2', 'MOVIE UPDATES', 'Updates every 5 mins with search', 'https://movievoidup.streamlit.app/')">
            <div class="btn-inner"><div class="title-sm">MOVIE UPDATES</div><div class="desc-sm">Updates every 5 mins with search facility</div></div>
        </div>
        <div class="btn-container" id="btn-3" onclick="handleInteraction('btn-3', 'VIBE SEARCH', 'Search by genre, vibe, type', 'https://getmoviewithvoid.streamlit.app/')">
            <div class="btn-inner"><div class="title-sm">MOVIE VIBE SEARCH</div><div class="desc-sm">Search by genre, vibe, type etc</div></div>
        </div>
    </div>

    <div style="position:fixed; bottom:30px; color:#bc13fe; font-size:0.8rem; font-weight:bold; letter-spacing:6px;">VOIDMARAUDS</div>

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

        // Local Storage Protocol
        let storage = JSON.parse(localStorage.getItem('void_final_v1')) || { active: [], locked: [], expiry: null };
        if(storage.expiry && Date.now() > storage.expiry) { storage = { active: [], locked: [], expiry: null }; localStorage.removeItem('void_final_v1'); }

        window.onload = () => {
            setTimeout(() => { document.getElementById('boot-screen').style.display = 'none'; if(storage.expiry) applyLocks(); }, 3200);
        };

        function handleInteraction(id, title, desc, url) {
            if(storage.locked.includes(id)) return;
            if(!storage.expiry) { document.getElementById('selection-popup').style.display = 'flex'; return; }
            runWarp(title, url);
        }

        let selectedIds = [];
        function toggleSelect(el, id) {
            if(selectedIds.includes(id)) { selectedIds = selectedIds.filter(i => i !== id); el.classList.remove('active'); }
            else if(selectedIds.length < 2) { selectedIds.push(id); el.classList.add('active'); }
            const btn = document.getElementById('confirm-protocol');
            if(selectedIds.length === 2) btn.classList.add('ready'); else btn.classList.remove('ready');
        }

        function finalizeChoices() {
            const allIds = ['btn-1', 'btn-2', 'btn-3'];
            storage = { active: selectedIds, locked: allIds.filter(id => !selectedIds.includes(id)), expiry: Date.now() + 86400000 };
            localStorage.setItem('void_final_v1', JSON.stringify(storage));
            document.getElementById('selection-popup').style.display = 'none';
            applyLocks();
        }

        function applyLocks() {
            storage.locked.forEach(id => {
                const btn = document.getElementById(id);
                btn.style.pointerEvents = 'none';
                if(!btn.querySelector('.locked-overlay')) {
                    const overlay = document.createElement('div'); overlay.className = 'locked-overlay'; btn.appendChild(overlay);
                }
            });
        }

        function runWarp(title, url) {
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
""", height=1000)
