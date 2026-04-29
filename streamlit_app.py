import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(page_title="NEXUS COMMAND", layout="wide", initial_sidebar_state="collapsed")

# 2. Ultra Modern CSS (The "Space" Style)
st.markdown("""
    <style>
    /* Global Background */
    .stApp {
        background: #020205;
        color: #ffffff;
    }

    /* Hide Streamlit Header/Footer */
    header, footer {visibility: hidden;}

    /* Glassmorphism Card Container */
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(0, 242, 255, 0.2);
        padding: 30px;
        transition: 0.4s;
        text-align: center;
        margin-bottom: 20px;
    }

    .project-card:hover {
        border-color: #00f2ff;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.2);
        transform: translateY(-10px);
    }

    /* Neon Titles */
    .neon-title {
        font-family: 'Orbitron', sans-serif;
        color: #00f2ff;
        text-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
        text-align: center;
        font-size: 3rem;
        letter-spacing: 10px;
        margin-bottom: 0px;
    }

    .neon-subtitle {
        color: #bc13fe;
        text-align: center;
        letter-spacing: 5px;
        font-size: 0.8rem;
        margin-bottom: 50px;
    }

    /* Target buttons specifically */
    div.stButton > button {
        background-color: transparent !important;
        color: #00f2ff !important;
        border: 1px solid #00f2ff !important;
        width: 100%;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        background-color: #00f2ff !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00f2ff;
    }
    </style>
    
    <!-- Load Sci-Fi Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Background Starfield Animation (Injected via Components)
# This stays in the background while Streamlit runs on top
components.html("""
    <canvas id="stars" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1;"></canvas>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('stars'), alpha: true});
        renderer.setSize(window.innerWidth, window.innerHeight);
        
        const geometry = new THREE.BufferGeometry();
        const vertices = [];
        for (let i = 0; i < 5000; i++) {
            vertices.push(Math.random() * 2000 - 1000, Math.random() * 2000 - 1000, Math.random() * 2000 - 1000);
        }
        geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
        const material = new THREE.PointsMaterial({color: 0xffffff, size: 0.7});
        const points = new THREE.Points(geometry, material);
        scene.add(points);
        camera.position.z = 1;

        function animate() {
            requestAnimationFrame(animate);
            points.rotation.y += 0.0005;
            renderer.render(scene, camera);
        }
        animate();
    </script>
    """, height=0) # Height 0 because it's fixed background

# 4. Main UI Content (Pure Python)
st.markdown('<h1 class="neon-title">NEXUS</h1>', unsafe_allow_html=True)
st.markdown('<p class="neon-subtitle">COMMAND INTERFACE v1.0</p>', unsafe_allow_html=True)

# Create 2 Columns for your apps
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="project-card">
            <h3 style="color:#00f2ff; font-family:'Orbitron';">AICodeFlat</h3>
            <p style="color:#a0a0a0;">Neural Processing Interface for Spatial Logic.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Python Link Button
    st.link_button("🚀 LAUNCH MODULE", "https://aicodeflat.streamlit.app/")

with col2:
    st.markdown("""
        <div class="project-card">
            <h3 style="color:#00f2ff; font-family:'Orbitron';">MovieVoid</h3>
            <p style="color:#a0a0a0;">Cinematic Data Visualizer & Predictive Engine.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Python Link Button
    st.link_button("🚀 LAUNCH MODULE", "https://movievoidup.streamlit.app/")

# 5. Dynamic Footer
st.write("---")
st.caption("DEK-I System Status: Operational | Connection: Secure")
