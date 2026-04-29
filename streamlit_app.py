import streamlit as st
import streamlit.components.v1 as components

# 1. PAGE CONFIG & HIDE STREAMLIT UI
st.set_page_config(page_title="NEXUS PORTAL", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu, header, footer, [data-testid="stHeader"] { visibility: hidden; }
    .stApp { background: #020205 !important; }
    .main .block-container { padding: 0 !important; max-width: 100vw !important; }
    </style>
""", unsafe_allow_html=True)

# 2. THE FULL-SCREEN ENGINE
components.html("""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #020205; color: white; font-family: 'Orbitron'; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; overflow: hidden; }
        
        /* Starfield Background */
        #bg-stars { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }
        
        /* High-Voltage Lightning Canvas */
        #lightning-canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 99; pointer-events: none; }
        
        /* Warp Overlay */
        #warp-overlay { 
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
            background: rgba(0,0,0,0.8); display: none; flex-direction: column; 
            justify-content: center; align-items: center; z-index: 100; text-align: center; 
        }

        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; width: 92%; max-width: 500px; z-index: 10; margin-top: 20px;}
        
        .btn { 
            aspect-ratio: 1/1; border: 1px solid #00f2ff; border-radius: 20px; 
            display: flex; flex-direction: column; align-items: center; justify-content: center; 
            text-decoration: none; color: #00f2ff; transition: 0.3s; padding: 15px; text-align: center;
            background: rgba(255,255,255,0.02); backdrop-filter: blur(5px); cursor: pointer;
        }

        .btn:hover { border-color: #ff00ff; color: #ff00ff; box-shadow: 0 0 20px rgba(255,0,255,0.4); }

        .title-txt { font-size: 0.8rem; font-weight: 900; pointer-events: none; }
        .desc-txt { font-family: 'Rajdhani'; font-size: 0.6rem; color: #ccc; margin-top: 8px; line-height: 1.2; pointer-events: none; }

        .warp-h { color: #ff00ff; font-size: 1.5rem; text-shadow: 0 0 20px #ff00ff; margin-bottom: 10px; }
        .warp-p { font-family: 'Rajdhani'; color: #00f2ff; letter-spacing: 2px; }
    </style>
</head>
<body>
    <canvas id="bg-stars"></canvas>
    <canvas id="lightning-canvas"></canvas>
    
    <div id="warp-overlay">
        <h1 class="warp-h" id="warp-title">INITIALIZING...</h1>
        <p class="warp-p" id="warp-desc"></p>
    </div>

    <h1 style="color:#00f2ff; letter-spacing:15px; font-size: 2.5rem; margin-bottom: 30px;">NEXUS</h1>

    <div class="grid">
        <!-- Button 1 -->
        <div class="btn" onclick="warp('AI CODE FLATTENER', 'FLATTENING ZIP CODES TO MD FILES', 'https://aicodeflat.streamlit.app/')">
            <div class="title-txt">AI CODE FLATTENER</div>
            <div class="desc-txt">Flattening zip codes to MD files</div>
        </div>
        <!-- Button 2 -->
        <div class="btn" onclick="warp('MOVIE UPDATES', 'MOVIE UPDATES EVERY 5 MINS WITH SEARCH', 'https://movievoidup.streamlit.app/')">
            <div class="title-txt">MOVIE UPDATES</div>
            <div class="desc-txt">Movie updates every 5 mins with search facility</div>
        </div>
        <!-- Button 3 -->
        <div class="btn" onclick="warp('MOVIE VIBE SEARCH', 'SEARCH MOVIES BY GENRE, VIBE, TYPE', 'https://getmoviewithvoid.streamlit.app/')">
            <div class="title-txt">MOVIE VIBE SEARCH</div>
            <div class="desc-txt">Search movies by searching genre, vibe, type etc</div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // 1. STARFIELD BACKGROUND
        const sScene=new THREE.Scene(), sCam=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
        const sRen=new THREE.WebGLRenderer({canvas:document.getElementById('bg-stars'), alpha:true});
        sRen.setSize(window.innerWidth,window.innerHeight);
        const sGeo=new THREE.BufferGeometry(), sPos=[];
        for(let i=0;i<3000;i++) sPos.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
        sGeo.setAttribute('position', new THREE.Float32BufferAttribute(sPos,3));
        sScene.add(new THREE.Points(sGeo, new THREE.PointsMaterial({color:0xffffff, size:0.7})));
        sCam.position.z=1;
        function animStars(){ requestAnimationFrame(animStars); sScene.rotation.y+=0.0003; sRen.render(sScene,sCam); } animStars();

        // 2. LIGHTNING ENGINE
        const lCanvas = document.getElementById('lightning-canvas');
        const ctx = lCanvas.getContext('2d');
        lCanvas.width = window.innerWidth;
        lCanvas.height = window.innerHeight;

        function createLightning(x1, y1, x2, y2, color) {
            ctx.strokeStyle = color;
            ctx.lineWidth = 2;
            ctx.shadowBlur = 15;
            ctx.shadowColor = color;
            ctx.beginPath();
            ctx.moveTo(x1, y1);
            
            let segments = 10;
            let currX = x1;
            let currY = y1;
            
            for(let i=0; i<segments; i++) {
                currX += (x2 - x1)/segments + (Math.random()*60 - 30);
                currY += (y2 - y1)/segments + (Math.random()*60 - 30);
                ctx.lineTo(currX, currY);
            }
            ctx.lineTo(x2, y2);
            ctx.stroke();
        }

        // 3. WARP ACTION
        function warp(title, desc, url) {
            document.getElementById('warp-title').innerText = title;
            document.getElementById('warp-desc').innerText = desc;
            document.getElementById('warp-overlay').style.display = 'flex';
            
            let strikes = 0;
            const interval = setInterval(() => {
                ctx.clearRect(0,0,lCanvas.width, lCanvas.height);
                const colors = ['#ff00ff', '#bc13fe', '#ffffff'];
                for(let i=0; i<3; i++) {
                    createLightning(Math.random()*lCanvas.width, 0, Math.random()*lCanvas.width, lCanvas.height, colors[Math.floor(Math.random()*colors.length)]);
                }
                strikes++;
                if(strikes > 20) {
                    clearInterval(interval);
                    window.open(url, '_blank');
                    setTimeout(() => { location.reload(); }, 500);
                }
            }, 100);
        }
    </script>
</body>
</html>
""", height=900)
