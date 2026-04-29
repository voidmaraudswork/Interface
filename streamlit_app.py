import streamlit as st
import streamlit.components.v1 as components
import time

# 1. PAGE SETUP
st.set_page_config(page_title="NEXUS COMMAND", layout="wide", initial_sidebar_state="collapsed")

# 2. THE "ULTRA-CLEAN" MOBILE CSS
st.markdown("""
    <style>
    /* Hide all Streamlit UI */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    [data-testid="stDecoration"] {display: none;}
    [data-testid="stToolbar"] {display: none;}
    
    /* Force Full Screen & Dark Mode */
    .stApp { background-color: #020205; }
    .main .block-container {
        padding: 0 !important;
        max-width: 100vw !important;
        height: 100vh !important;
    }

    /* --- SIDE-BY-SIDE SQUARE GRID --- */
    .nexus-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 40px;
        font-family: 'Orbitron', sans-serif;
    }

    .nexus-grid {
        display: grid;
        grid-template-columns: 1fr 1fr; /* Two columns side-by-side */
        gap: 15px;                      /* Small gap */
        width: 90%;                     /* Fit mobile width */
        max-width: 500px;
        margin-top: 20px;
    }

    .nexus-btn {
        aspect-ratio: 1 / 1;            /* Forces Square shape */
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 242, 255, 0.3);
        border-radius: 15px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-decoration: none;
        color: #00f2ff !important;
        transition: 0.3s;
        backdrop-filter: blur(10px);
        text-align: center;
        padding: 10px;
    }

    .nexus-btn:active, .nexus-btn:hover {
        background: rgba(0, 242, 255, 0.1);
        border-color: #00f2ff;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.4);
        transform: scale(0.98);
    }

    .btn-icon { font-size: 2rem; margin-bottom: 10px; }
    .btn-text { font-size: 0.7rem; letter-spacing: 2px; font-weight: bold; text-transform: uppercase; }

    /* Title Styling */
    .title { color: #00f2ff; font-size: 3rem; letter-spacing: 10px; margin: 0; }
    .subtitle { color: #bc13fe; font-size: 0.6rem; letter-spacing: 5px; margin-bottom: 20px; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# 3. BOOT LOGIC
if 'booted' not in st.session_state:
    st.session_state.booted = False

# --- PHASE 1: STUNNING 3-SEC INTRO ---
if not st.session_state.booted:
    components.html("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap');
            body { background: #000; margin: 0; overflow: hidden; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; }
            .t { font-family: 'Orbitron'; color: #00f2ff; font-size: 2.5rem; letter-spacing: 10px; text-shadow: 0 0 20px #00f2ff; z-index: 2; }
            .loader { width: 200px; height: 2px; background: rgba(255,255,255,0.1); margin-top: 20px; z-index: 2; overflow: hidden; }
            .fill { width: 0%; height: 100%; background: #00f2ff; animation: p 3s forwards; }
            @keyframes p { to { width: 100%; } }
        </style>
        <div class="t">NEXUS</div>
        <div class="loader"><div class="fill"></div></div>
        <canvas id="w" style="position:fixed; top:0; left:0; z-index:1;"></canvas>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const s=new THREE.Scene(), c=new THREE.PerspectiveCamera(60,window.innerWidth/window.innerHeight,1,1000);
            c.position.z=1; c.rotation.x=Math.PI/2;
            const r=new THREE.WebGLRenderer({canvas:document.getElementById('w'), alpha:true});
            r.setSize(window.innerWidth,window.innerHeight);
            const g=new THREE.BufferGeometry(), p=[];
            for(let i=0;i<8000;i++) p.push(Math.random()*600-300, Math.random()*600-300, Math.random()*600-300);
            g.setAttribute('position', new THREE.Float32BufferAttribute(p,3));
            const m=new THREE.Points(g, new THREE.PointsMaterial({color:0xffffff, size:0.5}));
            s.add(m);
            function a(){ 
                const pos=g.attributes.position.array;
                for(let i=0;i<8000;i++){ pos[i*3+1]-=15; if(pos[i*3+1]<-300) pos[i*3+1]=300; }
                g.attributes.position.needsUpdate=true;
                r.render(s,c); requestAnimationFrame(a);
            } a();
        </script>
    """, height=1000)
    time.sleep(3.3)
    st.session_state.booted = True
    st.rerun()

# --- PHASE 2: SIDE-BY-SIDE MOBILE HUB ---
else:
    # 3D Starfield Background
    components.html("""
        <canvas id="s" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1;"></canvas>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const sc=new THREE.Scene(), cam=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
            const ren=new THREE.WebGLRenderer({canvas:document.getElementById('s'), alpha:true});
            ren.setSize(window.innerWidth,window.innerHeight);
            const ge=new THREE.BufferGeometry(), ps=[];
            for(let i=0;i<3000;i++) ps.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
            ge.setAttribute('position', new THREE.Float32BufferAttribute(ps,3));
            sc.add(new THREE.Points(ge, new THREE.PointsMaterial({color:0xffffff, size:0.8})));
            cam.position.z=1;
            function an(){ requestAnimationFrame(an); sc.rotation.y+=0.0005; ren.render(sc,cam); } an();
        </script>
    """, height=0)

    # UI Content
    st.markdown(f"""
        <div class="nexus-wrapper">
            <h1 class="title">NEXUS</h1>
            <p class="subtitle">PORTAL OPERATIONAL</p>
            
            <div class="nexus-grid">
                <!-- TOP TWO SQUARE BUTTONS -->
                <a href="https://aicodeflat.streamlit.app/" class="nexus-btn">
                    <div class="btn-icon">🧠</div>
                    <div class="btn-text">AI CODE</div>
                </a>
                <a href="https://movievoidup.streamlit.app/" class="nexus-btn">
                    <div class="btn-icon">🎬</div>
                    <div class="btn-text">MOVIE VOID</div>
                </a>
                
                <!-- FUTURE LINKS AUTOMATICALLY GO BELOW -->
                <a href="#" class="nexus-btn" style="opacity: 0.3;">
                    <div class="btn-icon">🛰️</div>
                    <div class="btn-text">LINK 3</div>
                </a>
                <a href="#" class="nexus-btn" style="opacity: 0.3;">
                    <div class="btn-icon">🛡️</div>
                    <div class="btn-text">LINK 4</div>
                </a>
            </div>
            
            <p style="margin-top: 40px; font-size: 0.5rem; color: rgba(0,242,255,0.4); letter-spacing: 2px;">
                DEK-I ENCRYPTION ACTIVE
            </p>
        </div>
    """, unsafe_allow_html=True)
