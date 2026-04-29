import streamlit as st
import streamlit.components.v1 as components
import time

# 1. PAGE SETUP (Wide mode is the first step to full screen)
st.set_page_config(page_title="NEXUS COMMAND", layout="wide", initial_sidebar_state="collapsed")

# 2. HIDE MENU & FORCE FULL SCREEN CSS
st.markdown("""
    <style>
    /* 1. Hide the Streamlit Menu, Header, and Footer */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    
    /* 2. Remove all margins and padding from the app container */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100vw !important;
    }
    
    /* 3. Force the background of the whole page to black */
    .stApp {
        background-color: #020205;
    }

    /* 4. Fix Iframe behavior - making sure it fills the background */
    iframe {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw !important;
        height: 100vh !important;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 3. SESSION STATE FOR BOOT LOGIC
if 'booted' not in st.session_state:
    st.session_state.booted = False

# --- PHASE 1: THE FULL SCREEN INTRO ---
if not st.session_state.booted:
    components.html("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap');
            body { background: #000; margin: 0; overflow: hidden; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; width: 100vw; }
            .loader-container { z-index: 10; width: 300px; text-align: center; font-family: 'Orbitron', sans-serif; }
            .title { color: #00f2ff; font-size: 2.5rem; letter-spacing: 12px; margin-bottom: 20px; text-shadow: 0 0 20px #00f2ff; }
            .bar-bg { width: 100%; height: 2px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; }
            .bar-fill { width: 0%; height: 100%; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; animation: progress 3s forwards; }
            @keyframes progress { 0% { width: 0%; } 100% { width: 100%; } }
        </style>
        <div class="loader-container">
            <div class="title">NEXUS</div>
            <div class="bar-bg"><div class="bar-fill"></div></div>
        </div>
        <canvas id="intro-warp" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:1;"></canvas>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(60, window.innerWidth/window.innerHeight, 1, 1000);
            camera.position.z = 1; camera.rotation.x = Math.PI/2;
            const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('intro-warp'), alpha: true});
            renderer.setSize(window.innerWidth, window.innerHeight);
            const geo = new THREE.BufferGeometry();
            const pos = [];
            for (let i = 0; i < 8000; i++) { pos.push(Math.random()*600-300, Math.random()*600-300, Math.random()*600-300); }
            geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
            const points = new THREE.Points(geo, new THREE.PointsMaterial({color: 0xffffff, size: 0.6}));
            scene.add(points);
            function animate() {
                const p = geo.attributes.position.array;
                for(let i=0; i<8000; i++) { p[i*3+1] -= 12; if(p[i*3+1] < -300) p[i*3+1] = 300; }
                geo.attributes.position.needsUpdate = true;
                renderer.render(scene, camera);
                requestAnimationFrame(animate);
            }
            animate();
        </script>
    """, height=2000) # Large height ensures it covers screen
    
    time.sleep(3.2)
    st.session_state.booted = True
    st.rerun()

# --- PHASE 2: THE MAIN HUB (CLEAN FULL SCREEN) ---
else:
    # 1. UI CSS (Forces text white and cards neon)
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500&display=swap');

        /* Hub Content Positioning */
        .hub-content {
            margin-top: 10vh;
            padding: 0 10vw;
        }

        .hub-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 5rem;
            text-align: center;
            color: #00f2ff !important;
            letter-spacing: 20px;
            text-shadow: 0 0 40px rgba(0, 242, 255, 0.7);
        }

        .card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(0, 242, 255, 0.2);
            padding: 50px;
            border-radius: 30px;
            text-align: center;
            backdrop-filter: blur(20px);
            transition: 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .card:hover {
            transform: translateY(-20px);
            border-color: #00f2ff;
            box-shadow: 0 0 60px rgba(0, 242, 255, 0.3);
        }

        .card h2 { color: #00f2ff !important; font-family: 'Orbitron'; margin-bottom: 20px; font-size: 2rem; }
        .card p { color: #cfcfcf !important; font-family: 'Rajdhani'; font-size: 1.2rem; }

        /* Button Customization */
        div.stButton > button {
            background: transparent !important;
            border: 1px solid #00f2ff !important;
            color: #00f2ff !important;
            font-family: 'Orbitron';
            letter-spacing: 5px;
            width: 100%;
            height: 60px;
            margin-top: 20px;
            transition: 0.4s !important;
        }
        div.stButton > button:hover {
            background: #00f2ff !important;
            color: #000 !important;
            box-shadow: 0 0 30px #00f2ff;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. PERSISTENT STARFIELD BACKGROUND
    components.html("""
        <canvas id="bg-stars" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1;"></canvas>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('bg-stars'), alpha: true});
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

    # 3. MAIN CONTENT
    st.markdown('<div class="hub-content">', unsafe_allow_html=True)
    st.markdown('<h1 class="hub-title">NEXUS</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#bc13fe; letter-spacing:10px; font-weight:bold; margin-bottom:80px;">COMMAND INTERFACE ACTIVE</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""<div class="card"><h2>AICodeFlat</h2><p>AI Neural Interface</p></div>""", unsafe_allow_html=True)
        st.link_button("LAUNCH MODULE", "https://aicodeflat.streamlit.app/")

    with col2:
        st.markdown("""<div class="card"><h2>MovieVoid</h2><p>Predictive Data Engine</p></div>""", unsafe_allow_html=True)
        st.link_button("LAUNCH MODULE", "https://movievoidup.streamlit.app/")
    
    st.markdown('</div>', unsafe_allow_html=True)
