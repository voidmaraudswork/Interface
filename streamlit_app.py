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

# 2. THE ENGINE
components.html("""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@700&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #020205; color: white; font-family: 'Orbitron'; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; width: 100vw; overflow: hidden; }
        
        #bg-stars { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }

        /* BOOT SCREEN */
        #boot-screen { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #000; z-index: 5000; display: flex; flex-direction: column; justify-content: center; align-items: center; }
        .boot-fill { width: 0%; height: 100%; background: #bc13fe; animation: boot-load 3s forwards ease-in-out; }
        @keyframes boot-load { to { width: 100%; } }

        /* ATTENTION GRABBING POPUP (PROTOCOL LOCK) */
        #protocol-popup { 
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
            background: rgba(0,0,0,0.9); z-index: 4000; display: none; 
            flex-direction: column; justify-content: center; align-items: center; 
            backdrop-filter: blur(15px); text-align: center;
        }
        .alert-box { 
            width: 85%; max-width: 350px; padding: 30px; border: 2px solid #ff0055; 
            background: #110005; border-radius: 20px; box-shadow: 0 0 30px #ff0055;
            animation: glitch-border 0.3s infinite;
        }
        @keyframes glitch-border { 0% { border-color: #ff0055; } 50% { border-color: #00f2ff; } 100% { border-color: #ff0055; } }
        
        .alert-h { color: #ff0055; font-size: 1.2rem; letter-spacing: 3px; margin-bottom: 15px; }
        .alert-p { font-family: 'Rajdhani'; color: #fff; font-size: 0.9rem; line-height: 1.4; margin-bottom: 25px; }
        .confirm-btn { 
            padding: 12px 30px; border: 1px solid #ff0055; background: transparent; 
            color: #ff0055; font-family: 'Orbitron'; cursor: pointer; transition: 0.3s;
        }
        .confirm-btn:hover { background: #ff0055; color: white; }

        /* WARP OVERLAY */
        #warp-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.98); display: none; flex-direction: column; justify-content: center; align-items: center; z-index: 3000; text-align: center; }
        .warp-fill { width: 0%; height: 3px; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; }

        /* HUB UI */
        .main-container { display: flex; flex-direction: column; align-items: center; width: 90%; max-width: 440px; margin-top: -30px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; width: 100%; margin-top: 20px;}
        
        .btn-container {
            position: relative; aspect-ratio: 1/1; border-radius: 18px; padding: 3px; 
            background: linear-gradient(0deg, #00f2ff, #bc13fe, #00f2ff);
            background-size: 100% 200%; animation: flow 3s linear infinite;
            overflow: hidden; cursor: pointer;
        }
        @keyframes flow { 0% { background-position: 0% 0%; } 100% { background-position: 0% 200%; } }
        
        .btn-inner { width: 100%; height: 100%; background: #08080a; border-radius: 15px; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #00f2ff; }
        .locked { opacity: 0.2; filter: grayscale(1); cursor: not-allowed; }
    </style>
</head>
<body>
    <canvas id="bg-stars"></canvas>

    <!-- 1. BOOT SEQUENCE -->
    <div id="boot-screen">
        <div style="color:#00f2ff; letter-spacing:5px; margin-bottom:20px;">Portal to void core is opening...</div>
        <div style="width:200px; height:2px; background:rgba(255,255,255,0.1);"><div class="boot-fill"></div></div>
    </div>

    <!-- 2. THE CHALLENGING POPUP (PROTOCOL 24) -->
    <div id="protocol-popup">
        <div class="alert-box">
            <h2 class="alert-h">⚠️ QUOTA PROTOCOL</h2>
            <p class="alert-p" id="alert-text">ATTENTION: You can only choose 2 of the buttons for 24 hours. Choose your path wisely, Marauder.</p>
            <button class="confirm-btn" id="protocol-confirm">ACCEPT & PROCEED</button>
        </div>
    </div>

    <!-- 3. WARP OVERLAY -->
    <div id="warp-overlay">
        <p style="color:#bc13fe; font-size:0.7rem; letter-spacing:4px;">THE PORTAL TO VOID IS OPENING...</p>
        <h1 id="warp-title" style="color:#00f2ff; font-size:1.1rem; margin:0;"></h1>
        <div style="width:200px; height:2px; background:rgba(255,255,255,0.1); margin: 20px 0;"><div id="fill" class="warp-fill"></div></div>
        <p style="color:#bc13fe; font-size:0.5rem; letter-spacing:3px;">VOIDMARAUDS</p>
    </div>

    <div class="main-container">
        <h1 style="color:#00f2ff; letter-spacing:15px; font-size: 2.2rem; margin:0;">VOID CORE</h1>
        <p style="color:#bc13fe; font-size:0.55rem; letter-spacing:6px; margin-bottom:30px;">TERMINAL ACCESS</p>

        <div class="grid">
            <div class="btn-container" id="btn-1" onclick="handleBtn('AI CODE FLATTENER', 'Flattening zip codes to MD files', 'https://aicodeflat.streamlit.app/')">
                <div class="btn-inner"><b>AI CODE</b><br><small style="font-size:0.5rem; color:#888;">FLATTENER</small></div>
            </div>
            <div class="btn-container" id="btn-2" onclick="handleBtn('MOVIE UPDATES', 'Updates every 5 mins with search', 'https://movievoidup.streamlit.app/')">
                <div class="btn-inner"><b>MOVIE</b><br><small style="font-size:0.5rem; color:#888;">UPDATES</small></div>
            </div>
            <div class="btn-container" id="btn-3" onclick="handleBtn('VIBE SEARCH', 'Search movies by genre, vibe, type etc', 'https://getmoviewithvoid.streamlit.app/')">
                <div class="btn-inner"><b>VIBE</b><br><small style="font-size:0.5rem; color:#888;">SEARCH</small></div>
            </div>
        </div>
    </div>

    <div style="position:fixed; bottom:30px; color:#bc13fe; font-size:0.75rem; font-weight:bold; letter-spacing:5px;">VOIDMARAUDS</div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Starfield Logic
        const sS=new THREE.Scene(), sC=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
        const sR=new THREE.WebGLRenderer({canvas:document.getElementById('bg-stars'), alpha:true});
        sR.setSize(window.innerWidth,window.innerHeight);
        const sG=new THREE.BufferGeometry(), sP=[];
        for(let i=0;i<2500;i++) sP.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
        sG.setAttribute('position', new THREE.Float32BufferAttribute(sP,3));
        sS.add(new THREE.Points(sG, new THREE.PointsMaterial({color:0xffffff, size:0.8})));
        sC.position.z=1;
        function anim(){ requestAnimationFrame(anim); sS.rotation.y+=0.0004; sR.render(sS,sC); } anim();

        setTimeout(() => { document.getElementById('boot-screen').style.display='none'; }, 3200);

        // --- PROTOCOL LOGIC ---
        let storage = JSON.parse(localStorage.getItem('void_core_data')) || { choices: [], timestamp: null };
        
        // Reset if 24 hours passed
        if(storage.timestamp && (Date.now() - storage.timestamp > 86400000)) {
            storage = { choices: [], timestamp: null };
            localStorage.setItem('void_core_data', JSON.stringify(storage));
        }

        function handleBtn(title, desc, url) {
            if (storage.choices.includes(title)) {
                runWarp(title, desc, url);
                return;
            }

            if (storage.choices.length >= 2) {
                document.getElementById('alert-text').innerText = "LIMIT REACHED: Your 24-hour quota is exhausted. Access to new modules is denied.";
                document.getElementById('protocol-popup').style.display = 'flex';
                document.getElementById('protocol-confirm').onclick = () => { document.getElementById('protocol-popup').style.display='none'; };
                return;
            }

            // Show selection warning
            document.getElementById('alert-text').innerText = `CRITICAL CHOICE: Opening "${title}" will use 1 of your 2 daily slots. You cannot undo this for 24 hours. Continue?`;
            document.getElementById('protocol-popup').style.display = 'flex';
            
            document.getElementById('protocol-confirm').onclick = () => {
                storage.choices.push(title);
                if(!storage.timestamp) storage.timestamp = Date.now();
                localStorage.setItem('void_core_data', JSON.stringify(storage));
                document.getElementById('protocol-popup').style.display='none';
                runWarp(title, desc, url);
            };
        }

        function runWarp(title, desc, url) {
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
