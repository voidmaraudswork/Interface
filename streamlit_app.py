import streamlit as st
import streamlit.components.v1 as components

# 1. PAGE CONFIG & UI CLEANUP
st.set_page_config(page_title="NEXUS COMMAND", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stDecoration"] { visibility: hidden !important; }
    .stApp { background: #020205 !important; }
    .main .block-container { padding: 0 !important; max-width: 100vw !important; }
    </style>
""", unsafe_allow_html=True)

# 2. THE FULL PORTAL ENGINE
components.html("""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #020205; color: white; font-family: 'Orbitron'; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; overflow: hidden; }
        
        #bg-stars { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }
        #lightning-canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 99; pointer-events: none; }
        
        /* WARP OVERLAY */
        #warp-overlay { 
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
            background: rgba(0,0,0,0.9); display: none; flex-direction: column; 
            justify-content: center; align-items: center; z-index: 100; text-align: center; 
        }

        /* NEON LOADING BAR */
        .loader-container { width: 300px; height: 6px; background: rgba(255,255,255,0.1); border-radius: 10px; margin-top: 30px; overflow: hidden; border: 1px solid rgba(255, 0, 255, 0.3); }
        .loader-fill { width: 0%; height: 100%; background: linear-gradient(90deg, #ff00ff, #bc13fe); box-shadow: 0 0 15px #ff00ff; }

        /* GRID SYSTEM */
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; width: 92%; max-width: 500px; z-index: 10; margin-top: 20px; }
        
        .btn { 
            aspect-ratio: 1/1; border: 1px solid #00f2ff; border-radius: 20px; 
            display: flex; flex-direction: column; align-items: center; justify-content: center; 
            color: #00f2ff; transition: 0.3s; padding: 15px; text-align: center;
            background: rgba(255,255,255,0.02); backdrop-filter: blur(5px); cursor: pointer;
        }
        .btn:hover { border-color: #ff00ff; color: #ff00ff; box-shadow: 0 0 20px rgba(255,0,255,0.4); }

        .title-txt { font-size: 0.75rem; font-weight: 900; pointer-events: none; }
        .desc-txt { font-family: 'Rajdhani'; font-size: 0.6rem; color: #ccc; margin-top: 8px; pointer-events: none; line-height: 1.1; }

        .warp-h { color: #ff00ff; font-size: 1.6rem; text-shadow: 0 0 20px #ff00ff; margin: 0; }
        .warp-p { font-family: 'Rajdhani'; color: #00f2ff; letter-spacing: 2px; font-size: 0.9rem; margin-top: 10px; padding: 0 20px; }
    </style>
</head>
<body>
    <canvas id="bg-stars"></canvas>
    <canvas id="lightning-canvas"></canvas>
    
    <div id="warp-overlay">
        <h1 class="warp-h" id="warp-title"></h1>
        <p class="warp-p" id="warp-desc"></p>
        <div class="loader-container">
            <div id="fill" class="loader-fill"></div>
        </div>
        <p style="font-size: 0.6rem; margin-top: 15px; color: #ff00ff; letter-spacing: 3px;">INITIATING NEURAL LINK</p>
    </div>

    <h1 style="color:#00f2ff; letter-spacing:15px; font-size: 2.2rem; margin-bottom: 25px;">NEXUS</h1>

    <div class="grid">
        <div class="btn" onclick="warp('AI CODE FLATTENER', 'Flattening zip codes to MD files', 'https://aicodeflat.streamlit.app/')">
            <div class="title-txt">AI CODE FLATTENER</div>
            <div class="desc-txt">Flattening zip codes to MD files</div>
        </div>
        <div class="btn" onclick="warp('MOVIE UPDATES', 'Movie updates every 5 mins with search facility', 'https://movievoidup.streamlit.app/')">
            <div class="title-txt">MOVIE UPDATES</div>
            <div class="desc-txt">Movie updates every 5 mins with search facility</div>
        </div>
        <div class="btn" onclick="warp('MOVIE VIBE SEARCH', 'Search movies by searching genre, vibe, type etc', 'https://getmoviewithvoid.streamlit.app/')">
            <div class="title-txt">MOVIE VIBE SEARCH</div>
            <div class="desc-txt">Search movies by searching genre, vibe, type etc</div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // 1. STARFIELD
        const sS=new THREE.Scene(), sC=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
        const sR=new THREE.WebGLRenderer({canvas:document.getElementById('bg-stars'), alpha:true});
        sR.setSize(window.innerWidth,window.innerHeight);
        const sG=new THREE.BufferGeometry(), sP=[];
        for(let i=0;i<3000;i++) sP.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
        sG.setAttribute('position', new THREE.Float32BufferAttribute(sP,3));
        sS.add(new THREE.Points(sG, new THREE.PointsMaterial({color:0xffffff, size:0.7})));
        sC.position.z=1;
        function animS(){ requestAnimationFrame(animS); sS.rotation.y+=0.0003; sR.render(sS,sC); } animS();

        // 2. LIGHTNING
        const lC = document.getElementById('lightning-canvas');
        const ctx = lC.getContext('2d');
        lC.width = window.innerWidth; lC.height = window.innerHeight;

        function drawLightning(color) {
            ctx.strokeStyle = color; ctx.lineWidth = 2; ctx.shadowBlur = 15; ctx.shadowColor = color;
            ctx.beginPath();
            let x = Math.random()*lC.width, y = 0;
            ctx.moveTo(x, y);
            for(let i=0; i<10; i++) {
                x += Math.random()*100-50; y += lC.height/10;
                ctx.lineTo(x, y);
            }
            ctx.stroke();
        }

        // 3. WARP & LOADING
        function warp(title, desc, url) {
            const overlay = document.getElementById('warp-overlay');
            const fill = document.getElementById('fill');
            document.getElementById('warp-title').innerText = title;
            document.getElementById('warp-desc').innerText = desc;
            overlay.style.display = 'flex';

            let start = null;
            function step(timestamp) {
                if (!start) start = timestamp;
                let progress = (timestamp - start) / 2000; // 2 Seconds
                fill.style.width = Math.min(progress * 100, 100) + '%';

                ctx.clearRect(0,0,lC.width, lC.height);
                if (Math.random() > 0.7) {
                    drawLightning(Math.random() > 0.5 ? '#ff00ff' : '#ffffff');
                }

                if (progress < 1) {
                    requestAnimationFrame(step);
                } else {
                    window.open(url, '_blank');
                    setTimeout(() => { overlay.style.display = 'none'; fill.style.width = '0%'; }, 500);
                }
            }
            requestAnimationFrame(step);
        }
    </script>
</body>
</html>
""", height=900)
