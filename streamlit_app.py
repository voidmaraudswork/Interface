import streamlit as st
import streamlit.components.v1 as components
import time

# 1. PAGE SETUP (The Foundation)
st.set_page_config(page_title="NEXUS COMMAND", layout="wide", initial_sidebar_state="collapsed")

# 2. THE "GHOST" CSS (Removes every single Streamlit UI element)
st.markdown("""
    <style>
    /* Hide Everything: Menu, Header, Footer, Deploy Button, Decoration Bar */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    [data-testid="stDecoration"] {display: none;}
    [data-testid="stToolbar"] {display: none;}
    .stDeployButton {display: none;}
    
    /* Force Full Screen & Remove Padding */
    .main .block-container {
        padding: 0 !important;
        max-width: 100vw !important;
        height: 100vh !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .stApp { background-color: #020205; }

    /* --- ULTRA MODERN SQUARE BUTTONS CSS --- */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap');

    /* Container for the side-by-side layout */
    .button-row {
        display: flex;
        gap: 40px;
        justify-content: center;
        align-items: center;
        width: 100%;
        padding: 20px;
    }

    /* Targeting Streamlit Link Buttons to make them Square Modules */
    div.stButton > button {
        width: 250px !important;
        height: 250px !important;
        background: rgba(255, 255, 255, 0.03) !important;
        border: 2px solid rgba(0, 242, 255, 0.3) !important;
        color: #00f2ff !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 1.2rem !important;
        letter-spacing: 2px !important;
        border-radius: 20px !important;
        backdrop-filter: blur(15px) !important;
        transition: 0.5s cubic-bezier(0.16, 1, 0.3, 1) !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-transform: uppercase;
        box-shadow: inset 0 0 20px rgba(0, 242, 255, 0.05);
    }

    div.stButton > button:hover {
        transform: scale(1.05) translateY(-10px) !important;
        border-color: #00f2ff !important;
        background: rgba(0, 242, 255, 0.1) !important;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.3), inset 0 0 20px rgba(0, 242, 255, 0.2) !important;
        color: #fff !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. BOOT LOGIC
if 'booted' not in st.session_state:
    st.session_state.booted = False

# --- PHASE 1: STUNNING 3-SEC INTRO ---
if not st.session_state.booted:
    components.html("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap');
            body { background: #000; margin: 0; overflow: hidden; display: flex; justify-content: center; align-items: center; height: 100vh; }
            .title { 
                font-family: 'Orbitron'; color: #00f2ff; font-size: 3rem; letter-spacing: 15px; 
                text-shadow: 0 0 30px #00f2ff; animation: pulse 1.5s infinite alternate; 
            }
            @keyframes pulse { from { opacity: 0.2; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }
        </style>
        <div class="title">NEXUS</div>
        <canvas id="warp" style="position:fixed; top:0; left:0; z-index:-1;"></canvas>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(60, window.innerWidth/window.innerHeight, 1, 1000);
            camera.position.z = 1; camera.rotation.x = Math.PI/2;
            const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('warp'), alpha: true});
            renderer.setSize(window.innerWidth, window.innerHeight);
            const geo = new THREE.BufferGeometry();
            const pos = [];
            for (let i = 0; i < 10000; i++) { pos.push(Math.random()*600-300, Math.random()*600-300, Math.random()*600-300); }
            geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
            const points = new THREE.Points(geo, new THREE.PointsMaterial({color: 0xffffff, size: 0.5}));
            scene.add(points);
            function animate() {
                const p = geo.attributes.position.array;
                for(let i=0; i<10000; i++) { p[i*3+1] -= 20; if(p[i*3+1] < -300) p[i*3+1] = 300; }
                geo.attributes.position.needsUpdate = true;
                renderer.render(scene, camera);
                requestAnimationFrame(animate);
            }
            animate();
        </script>
    """, height=1000)
    time.sleep(3.2)
    st.session_state.booted = True
    st.rerun()

# --- PHASE 2: SIDE-BY-SIDE SQUARE HUB ---
else:
    # Starfield Background
    components.html("""
        <canvas id="stars" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1;"></canvas>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('stars'), alpha: true});
            renderer.setSize(window.innerWidth, window.innerHeight);
            const geo = new THREE.BufferGeometry();
            const pos = [];
            for (let i = 0; i < 4000; i++) { pos.push(Math.random()*2000-1000, Math.random()*2000-1000, Math.random()*2000-1000); }
            geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
            const points = new THREE.Points(geo, new THREE.PointsMaterial({color: 0xffffff, size: 0.8}));
            scene.add(points);
            camera.position.z = 1;
            function animate() {
                requestAnimationFrame(animate);
                points.rotation.y += 0.0004;
                renderer.render(scene, camera);
            }
            animate();
        </script>
    """, height=0)

    # Content
    st.markdown('<h1 style="font-family:Orbitron; color:#00f2ff; letter-spacing:20px; text-align:center; font-size:4rem; margin-bottom:0;">NEXUS</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#bc13fe; letter-spacing:10px; font-weight:bold; margin-bottom:50px;">PORTAL ACTIVE</p>', unsafe_allow_html=True)

    # Side-by-Side Columns
    col1, col2 = st.columns(2)
    
    with col1:
        # The CSS targets the button based on it being in a column
        st.link_button("◈ AI CODE FLAT", "https://aicodeflat.streamlit.app/")

    with col2:
        st.link_button("◈ MOVIE VOID", "https://movievoidup.streamlit.app/")

    st.write("")
    st.caption("🔒 SYSTEM SECURE | DEK-I ENCRYPTION ACTIVE")
