import streamlit as st
import streamlit.components.v1 as components

# 1. PAGE CONFIG & UI STRIPPING
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
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@700&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #020205; color: white; font-family: 'Orbitron'; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; width: 100vw; overflow: hidden; }
        #bg-stars { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }

        /* BOOT SCREEN */
        #boot-screen { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #000; z-index: 9000; display: flex; flex-direction: column; justify-content: center; align-items: center; transition: 0.8s; }
        .boot-bar { width: 200px; height: 2px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; margin-top:20px; }
        .boot-fill { width: 0%; height: 100%; background: #bc13fe; animation: boot-load 3s forwards ease-in-out; }
        @keyframes boot-load { to { width: 100%; } }

        /* SELECTION POPUP */
        #selection-popup { 
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
            background: rgba(0,0,0,0.95); z-index: 8000; display: none; 
            flex-direction: column; justify-content: center; align-items: center; 
            backdrop-filter: blur(20px); text-align: center;
        }
        .modal-box { 
            width: 90%; max-width: 450px; padding: 30px; border: 2px solid #00f2ff; 
            background: #050505; border-radius: 25px; box-shadow: 0 0 40px rgba(0, 242, 255, 0.2);
        }
        .select-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 25px 0; }
        .select-item { 
            padding: 10px; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; 
            font-size: 0.5rem; cursor: pointer; transition: 0.3s;
        }
        .select-item.active { border-color: #bc13fe; background: rgba(188, 19, 254, 0.2); color: white; box-shadow: 0 0 15px #bc13fe; }
        .confirm-btn { 
            width: 100%; padding: 15px; border: 1px solid #00f2ff; background: transparent; 
            color: #00f2ff; font-family: 'Orbitron'; cursor: pointer; opacity: 0.3; pointer-events: none;
        }
        .confirm-btn.ready { opacity: 1; pointer-events: auto; background: rgba(0, 242, 255, 0.1); }

        /* MAIN HUB UI */
        .main-container { display: flex; flex-direction: column; align-items: center; width: 90%; max-width: 440px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; width: 100%; margin-top: 20px; }
        
        .btn-container {
            position: relative; aspect-ratio: 1/1; border-radius: 18px; padding: 3px; 
            background: linear-gradient(0deg, #00f2ff, #bc13fe, #00f2ff);
            background-size: 100% 200%; animation: flow 3s linear infinite;
            overflow: hidden; cursor: pointer;
        }
        @keyframes flow { 0% { background-position: 0% 0%; } 100% { background-position: 0% 200%; } }
        
        .btn-inner { width: 100%; height: 100%; background: #08080a; border-radius: 15px; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #00f2ff; text-align: center; }
        
        /* RED CROSS LOCK */
        .locked-overlay {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(255, 0, 0, 0.2); backdrop-filter: grayscale(1) blur(2px);
            z-index: 50; display: flex; justify-content: center; align-items: center;
            pointer-events: auto; cursor: not-allowed;
        }
        .locked-overlay::before, .locked-overlay::after {
            content: ''; position: absolute; width: 80%; height: 6px; background: #ff0055;
            box-shadow: 0 0 20px #ff0055; border-radius: 10px;
        }
        .locked-overlay::before { transform: rotate(45deg); }
        .locked-overlay::after { transform: rotate(-45deg); }

        /* WARP */
        #warp-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #000; display: none; flex-direction: column; justify-content: center; align-items: center; z-index: 7000; }
        .warp-fill { width: 0%; height: 2px; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; }
    </style>
</head>
<body>
    <canvas id="bg-stars"></canvas>

    <!-- 1. BOOT SEQUENCE -->
    <div id="boot-screen">
        <div style="color:#00f2ff; letter-spacing:5px;">PORTAL TO VOID CORE IS OPENING...</div>
        <div class="boot-bar"><div class="boot-fill"></div></div>
    </div>

    <!-- 2. SELECTION PROTOCOL POPUP -->
    <div id="selection-popup">
        <div class="modal-box">
            <h2 style="color:#00f2ff; font-size:1rem; letter-spacing:2px; margin:0;">SELECTION PROTOCOL</h2>
            <p style="font-family:'Rajdhani'; color:#888; font-size:0.7rem; margin-top:10px;">Select exactly 2 modules to stabilize. The remaining path will be locked for 24 hours.</p>
            
            <div class="select-grid">
                <div class="select-item" onclick="toggleSelect(this, 'btn-1')">AI CODE<br>FLATTENER</div>
                <div class="select-item" onclick="toggleSelect(this, 'btn-2')">MOVIE<br>UPDATES</div>
                <div class="select-item" onclick="toggleSelect(this, 'btn-3')">VIBE<br>SEARCH</div>
            </div>

            <button class="confirm-btn" id="confirm-protocol" onclick="finalizeChoices()">INITIALIZE GATEWAY</button>
        </div>
    </div>

    <!-- 3. WARP OVERLAY -->
    <div id="warp-overlay">
        <p style="color:#bc13fe; font-size:0.6rem; letter-spacing:4px;">THE PORTAL TO VOID IS OPENING...</p>
        <h1 id="warp-title" style="color:#00f2ff; font-size:1.1rem;"></h1>
        <div style="width:200px; height:2px; background:rgba(255,255,255,0.1); margin:20px 0;"><div id="fill" class="warp-fill"></div></div>
        <p style="font-size:0.5rem; color:#bc13fe; letter-spacing:3px;">VOIDMARAUDS</p>
    </div>

    <div class="main-container">
        <h1 style="color:#00f2ff; letter-spacing:15px; font-size: 2.2rem; margin:0;">VOID CORE</h1>
        <p style="color:#bc13fe; font-size:0.55rem; letter-spacing:6px; margin-bottom:30px;">TERMINAL ACCESS</p>

        <div class="grid">
            <div class="btn-container" id="btn-1" onclick="handleLaunch('btn-1', 'AI CODE FLATTENER', 'DECONSTRUCTING ZIP TO MARKDOWN', 'https://aicodeflat.streamlit.app/')">
                <div class="btn-inner"><b>AI CODE</b></div>
            </div>
            <div class="btn-container" id="btn-2" onclick="handleLaunch('btn-2', 'MOVIE UPDATES', 'REAL-TIME CINEMATIC SYNC', 'https://movievoidup.streamlit.app/')">
                <div class="btn-inner"><b>MOVIE UPDATES</b></div>
            </div>
            <div class="btn-container" id="btn-3" onclick="handleLaunch('btn-3', 'VIBE SEARCH', 'GENRE & EMOTION FILTERING', 'https://getmoviewithvoid.streamlit.app/')">
                <div class="btn-inner"><b>VIBE SEARCH</b></div>
            </div>
        </div>
    </div>

    <div style="position:fixed; bottom:30px; color:#bc13fe; font-size:0.75rem; font-weight:bold; letter-spacing:5px;">VOIDMARAUDS</div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Starfield Setup
        const sS=new THREE.Scene(), sC=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
        const sR=new THREE.WebGLRenderer({canvas:document.getElementById('bg-stars'), alpha:true});
        sR.setSize(window.innerWidth,window.innerHeight);
        const sG=new THREE.BufferGeometry(), sP=[];
        for(let i=0;i<2500;i++) sP.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
        sG.setAttribute('position', new THREE.Float32BufferAttribute(sP,3));
        sS.add(new THREE.Points(sG, new THREE.PointsMaterial({color:0xffffff, size:0.8})));
        sC.position.z=1;
        function anim(){ requestAnimationFrame(anim); sS.rotation.y+=0.0004; sR.render(sS,sC); } anim();

        // State & Protocol Logic
        let selectedIds = [];
        let storage = JSON.parse(localStorage.getItem('void_protocol_v3')) || { active: [], locked: [], expiry: null };

        // Check Expiry
        if(storage.expiry && Date.now() > storage.expiry) {
            storage = { active: [], locked: [], expiry: null };
            localStorage.removeItem('void_protocol_v3');
        }

        window.onload = () => {
            setTimeout(() => {
                document.getElementById('boot-screen').style.opacity = '0';
                setTimeout(() => {
                    document.getElementById('boot-screen').style.display = 'none';
                    if(!storage.expiry) {
                        document.getElementById('selection-popup').style.display = 'flex';
                    } else {
                        applyLocks();
                    }
                }, 800);
            }, 3000);
        };

        function toggleSelect(el, id) {
            if(selectedIds.includes(id)) {
                selectedIds = selectedIds.filter(i => i !== id);
                el.classList.remove('active');
            } else {
                if(selectedIds.length < 2) {
                    selectedIds.push(id);
                    el.classList.add('active');
                }
            }
            const btn = document.getElementById('confirm-protocol');
            if(selectedIds.length === 2) btn.classList.add('ready');
            else btn.classList.remove('ready');
        }

        function finalizeChoices() {
            const allIds = ['btn-1', 'btn-2', 'btn-3'];
            const locked = allIds.filter(id => !selectedIds.includes(id));
            storage = {
                active: selectedIds,
                locked: locked,
                expiry: Date.now() + 86400000 // 24 Hours
            };
            localStorage.setItem('void_protocol_v3', JSON.stringify(storage));
            document.getElementById('selection-popup').style.display = 'none';
            applyLocks();
        }

        function applyLocks() {
            storage.locked.forEach(id => {
                const btn = document.getElementById(id);
                btn.style.pointerEvents = 'none';
                const overlay = document.createElement('div');
                overlay.className = 'locked-overlay';
                btn.appendChild(overlay);
            });
        }

        function handleLaunch(id, title, desc, url) {
            if(storage.locked.includes(id)) return;
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
