import streamlit as st
import streamlit.components.v1 as components
import time

# 1. PAGE SETUP
st.set_page_config(page_title="NEXUS COMMAND", layout="wide", initial_sidebar_state="collapsed")

# 2. SESSION STATE (Handles the 3-second boot timer)
if 'booted' not in st.session_state:
    st.session_state.booted = False

# --- PHASE 1: THE STUNNING INTRO ---
if not st.session_state.booted:
    # This is the "Boot-up" screen with high-speed warp drive
    components.html("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap');
            body { background: #000; margin: 0; overflow: hidden; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; }
            
            /* Loading Bar */
            .loader-container { width: 300px; text-align: center; font-family: 'Orbitron', sans-serif; }
            .title { color: #00f2ff; font-size: 2.5rem; letter-spacing: 10px; margin-bottom: 20px; text-shadow: 0 0 20px #00f2ff; }
            .bar-bg { width: 100%; height: 4px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; }
            .bar-fill { width: 0%; height: 100%; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; animation: progress 3s forwards; }
            .status { color: #bc13fe; font-size: 0.7rem; margin-top: 10px; letter-spacing: 3px; text-transform: uppercase; }

            @keyframes progress { 0% { width: 0%; } 100% { width: 100%; } }
        </style>
        
        <div class="loader-container">
            <div class="title">NEXUS</div>
            <div class="bar-bg"><div class="bar-fill"></div></div>
            <div class="status">Initializing Quantum Link...</div>
        </div>

        <canvas id="intro-warp" style="position:fixed; top:0; left:0; z-index:-1;"></canvas>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(60, window.innerWidth/window.innerHeight, 1, 1000);
            camera.position.z = 1; camera.rotation.x = Math.PI/2;
            const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('intro-warp'), alpha: true});
            renderer.setSize(window.innerWidth, window.innerHeight);
            
            const geo = new THREE.BufferGeometry();
            const pos = [];
            for (let i = 0; i < 6000; i++) { pos.push(Math.random()*600-300, Math.random()*600-300, Math.random()*600-300); }
            geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
            const points = new THREE.Points(geo, new THREE.PointsMaterial({color: 0xffffff, size: 0.7}));
            scene.add(points);

            function animate() {
                const p = geo.attributes.position.array;
                for(let i=0; i<6000; i++) {
                    p[i*3+1] -= 15; // WARP SPEED
                    if(p[i*3+1] < -300) p[i*3+1] = 300;
                }
                geo.attributes.position.needsUpdate = true;
                renderer.render(scene, camera);
                requestAnimationFrame(animate);
            }
            animate();
        </script>
    """, height=800)
    
    time.sleep(3.5) # The stunning 3-second wait
    st.session_state.booted = True
    st.rerun()

# --- PHASE 2: THE MAIN HUB ---
else:
    # 1. THE CSS (Stops black text, forces Neon UI)
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500&display=swap');

        /* Force App Background */
        .stApp { background: #020205; color: #ffffff !important; }
        header, footer { visibility: hidden; }

        /* The Hub Title */
        .hub-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 4.5rem;
            text-align: center;
            color: #00f2ff !important;
            letter-spacing: 15px;
            margin-top: 50px;
            text-shadow: 0 0 30px rgba(0, 242, 255, 0.6);
        }

        /* Module Cards */
        .card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(0, 242, 255, 0.2);
            padding: 40px;
            border-radius: 25px;
            text-align: center;
            backdrop-filter: blur(10px);
            transition: 0.5s cubic-bezier(0.2, 1, 0.3, 1);
        }
        .card:hover {
            transform: translateY(-15px);
            border-color: #00f2ff;
            box-shadow: 0 0 50px rgba(0, 242, 255, 0.2);
        }

        .card h2 { color: #00f2ff !important; font-family: 'Orbitron'; font-size: 1.8rem; }
        .card p { color: #a0a0a0 !important; font-family: 'Rajdhani'; font-size: 1.1rem; }

        /* Target Streamlit Link Buttons to make them Ultra Modern */
        div.stButton > button {
            background: transparent !important;
            border: 1px solid #00f2ff !important;
            color: #00f2ff !important;
            font-family: 'Orbitron';
            letter-spacing: 3px;
            width: 100%;
            height: 55px;
            border-radius: 10px;
            transition: 0.4s !important;
            text-transform: uppercase;
        }

        div.stButton > button:hover {
            background: #00f2ff !important;
            color: #000 !important;
            box-shadow: 0 0 25px #00f2ff;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. THE BACKGROUND (Calm Floating Stars)
    components.html("""
        <canvas id="starfield" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1;"></canvas>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('starfield'), alpha: true});
            renderer.setSize(window.innerWidth, window.innerHeight);
            const geo = new THREE.BufferGeometry();
            const pos = [];
            for (let i = 0; i < 5000; i++) { pos.push(Math.random()*2000-1000, Math.random()*2000-1000, Math.random()*2000-1000); }
            geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
            const points = new THREE.Points(geo, new THREE.PointsMaterial({color: 0xffffff, size: 0.8}));
            scene.add(points);
            camera.position.z = 1;
            function animate() {
                requestAnimationFrame(animate);
                points.rotation.y += 0.0006;
                renderer.render(scene, camera);
            }
            animate();
        </script>
    """, height=0)

    # 3. HUB CONTENT
    st.markdown('<h1 class="hub-title">NEXUS</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#bc13fe; letter-spacing:8px; font-weight:bold;">COMMAND INTERFACE OPERATIONAL</p>', unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div class="card">
                <h2>AICodeFlat</h2>
                <p>Neural Processing Interface for Spatial Logic & Code Generation.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("🚀 LAUNCH MODULE", "https://aicodeflat.streamlit.app/")

    with col2:
        st.markdown("""
            <div class="card">
                <h2>MovieVoid</h2>
                <p>Cinematic Predictive Analytics & Dataset Visualization Engine.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("🚀 LAUNCH MODULE", "https://movievoidup.streamlit.app/")

    st.write("")
    st.write("")
    st.caption("🔒 SYSTEM: DEK-I ENCRYPTED | STATUS: SECURE")
