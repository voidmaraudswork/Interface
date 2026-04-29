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
        
        /* WARP OVERLAY (No Lightning) */
        #warp-overlay { 
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
            background: rgba(0,0,0,0.95); display: none; flex-direction: column; 
            justify-content: center; align-items: center; z-index: 100; text-align: center; 
            backdrop-filter: blur(10px);
        }

        /* NEON LOADING BAR */
        .loader-container { width: 280px; height: 4px; background: rgba(255,255,255,0.1); border-radius: 10px; margin-top: 30px; overflow: hidden; }
        .loader-fill { width: 0%; height: 100%; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; }

        /* GRID SYSTEM - SIDE BY SIDE MOBILE */
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; width: 92%; max-width: 500px; z-index: 10; margin-top: 20px; }
        
        .btn { 
            aspect-ratio: 1/1; border: 1px solid rgba(0, 242, 255, 0.3); border-radius: 20px; 
            display: flex; flex-direction: column; align-items: center; justify-content: center; 
            color: #00f2ff; transition: 0.3s; padding: 15px; text-align: center;
            background: rgba(255,255,255,0.02); backdrop-filter: blur(5px); cursor: pointer;
        }
        .btn:hover { border-color: #00f2ff; box-shadow: 0 0 20px rgba(0, 242, 255, 0.2); transform: translateY(-5px); }

        .title-txt { font-size: 0.75rem; font-weight: 900; pointer-events: none; letter-spacing: 1px; }
        .desc-txt { font-family: 'Rajdhani'; font-size: 0.6rem; color: #ccc; margin-top: 8px; pointer-events: none; line-height: 1.1; }

        .warp-h { color: #00f2ff; font-size: 1.5rem; letter-spacing: 5px; margin: 0; text-transform: uppercase; }
        .warp-p { font-family: 'Rajdhani'; color: #888; letter-spacing: 2px; font-size: 0.8rem; margin-top: 10px; padding: 0 20px; }
    </style>
</head>
<body>
    <canvas id="bg-stars"></canvas>
    
    <div id="warp-overlay">
        <h1 class="warp-h" id="warp-title"></h1>
        <p class="warp-p" id="warp-desc"></p>
        <div class="loader-container">
            <div id="fill" class="loader-fill"></div>
        </div>
        <p style="font-size: 0.5rem; margin-top: 15px; color: #00f2ff; letter-spacing: 4px; opacity: 0.6;">SYNCING DATA MODULE</p>
    </div>

    <h1 style="color:#00f2ff; letter-spacing:15px; font-size: 2.2rem; margin-bottom: 10px;">NEXUS</h1>
    <p style="color: #bc13fe; font-size: 0.6rem; letter-spacing: 5px; margin-bottom: 30px;">PORTAL OPERATIONAL</p>

    <div class="grid">
        <!-- Module 1 -->
        <div class="btn" onclick="warp('AI CODE FLATTENER', 'Flattening zip codes to MD files', 'https://aicodeflat.streamlit.app/')">
            <div class="title-txt">AI CODE FLATTENER</div>
            <div class="desc-txt">Flattening zip codes to MD files</div>
        </div>
        <!-- Module 2 -->
        <div class="btn" onclick="warp('MOVIE UPDATES', 'Movie updates every 5 mins with search facility', 'https://movievoidup.streamlit.app/')">
            <div class="title-txt">MOVIE UPDATES</div>
            <div class="desc-txt">Updates every 5 mins with search facility</div>
        </div>
        <!-- Module 3 -->
        <div class="btn" onclick="warp('MOVIE VIBE SEARCH', 'Search movies by genre, vibe, type etc', 'https://getmoviewithvoid.streamlit.app/')">
            <div class="title-txt">MOVIE VIBE SEARCH</div>
            <div class="desc-txt">Search by genre, vibe, type etc</div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // 1. STARFIELD BACKGROUND
        const sS=new THREE.Scene(), sC=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
        const sR=new THREE.WebGLRenderer({canvas:document.getElementById('bg-stars'), alpha:true});
        sR.setSize(window.innerWidth,window.innerHeight);
        const sG=new THREE.BufferGeometry(), sP=[];
        for(let i=0;i<3000;i++) sP.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
        sG.setAttribute('position', new THREE.Float32BufferAttribute(sP,3));
        sS.add(new THREE.Points(sG, new THREE.PointsMaterial({color:0xffffff, size:0.7})));
        sC.position.z=1;
        function animS(){ requestAnimationFrame(animS); sS.rotation.y+=0.0004; sR.render(sS,sC); } animS();

        // 2. WARP & LOADING ACTION
        function warp(title, desc, url) {
            const overlay = document.getElementById('warp-overlay');
            const fill = document.getElementById('fill');
            document.getElementById('warp-title').innerText = title;
            document.getElementById('warp-desc').innerText = desc;
            overlay.style.display = 'flex';

            let start = null;
            function step(timestamp) {
                if (!start) start = timestamp;
                let progress = (timestamp - start) / 2000; // Exact 2 Seconds
                fill.style.width = Math.min(progress * 100, 100) + '%';

                if (progress < 1) {
                    requestAnimationFrame(step);
                } else {
                    window.open(url, '_blank');
                    // Reset overlay after launch
                    setTimeout(() => { 
                        overlay.style.display = 'none'; 
                        fill.style.width = '0%'; 
                    }, 800);
                }
            }
            requestAnimationFrame(step);
        }
    </script>
</body>
</html>
""", height=900)
