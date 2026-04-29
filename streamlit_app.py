import streamlit as st
import streamlit.components.v1 as components
import time

# 1. PAGE SETUP
st.set_page_config(page_title="NEXUS COMMAND", layout="wide", initial_sidebar_state="collapsed")

# 2. GLOBAL CSS
st.markdown("""
    <style>
    #MainMenu, header, footer, [data-testid="stHeader"] { display: none !important; }
    .stApp { background-color: #020205 !important; }
    .main .block-container { padding: 0 !important; max-width: 100vw !important; }

    .nexus-wrapper { display: flex; flex-direction: column; align-items: center; padding-top: 50px; font-family: 'Orbitron', sans-serif; }
    .nexus-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; width: 90%; max-width: 500px; margin-top: 30px; }
    
    .nexus-btn {
        aspect-ratio: 1 / 1;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 242, 255, 0.3);
        border-radius: 20px;
        display: flex; flex-direction: column;
        justify-content: center; align-items: center;
        text-decoration: none; color: #00f2ff !important;
        transition: 0.3s; backdrop-filter: blur(10px);
    }
    .nexus-btn:hover { background: rgba(0, 242, 255, 0.1); border-color: #00f2ff; }
    
    .title { color: #00f2ff; font-size: 3rem; letter-spacing: 15px; margin: 0; }
    .subtitle { color: #bc13fe; font-size: 0.7rem; letter-spacing: 5px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# 3. BOOT LOGIC
if 'booted' not in st.session_state:
    st.session_state.booted = False

if not st.session_state.booted:
    components.html("""
        <style>
            body { background: #000; margin: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; font-family: 'Orbitron'; }
            .t { color: #00f2ff; font-size: 3rem; letter-spacing: 15px; }
            .l { width: 200px; height: 2px; background: #333; margin-top: 20px; }
            .f { width: 0%; height: 100%; background: #00f2ff; animation: p 3s forwards; }
            @keyframes p { to { width: 100%; } }
        </style>
        <div class="t">NEXUS</div>
        <div class="l"><div class="f"></div></div>
    """, height=600)
    time.sleep(3.2)
    st.session_state.booted = True
    st.rerun()

else:
    # 4. STARFIELD BACKGROUND
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

    # 5. MAIN INTERFACE
    st.markdown("""
        <div class="nexus-wrapper">
            <h1 class="title">NEXUS</h1>
            <p class="subtitle">PORTAL OPERATIONAL</p>
            
            <div class="nexus-grid">
                <a href="https://aicodeflat.streamlit.app/" class="nexus-btn">
                    <div style="font-size: 2rem;">🧠</div>
                    <div style="font-size: 0.7rem; margin-top:10px;">AI CODE</div>
                </a>
                <a href="https://movievoidup.streamlit.app/" class="nexus-btn">
                    <div style="font-size: 2rem;">🎬</div>
                    <div style="font-size: 0.7rem; margin-top:10px;">MOVIE VOID</div>
                </a>
            </div>
            
            <p style="margin-top: 50px; font-size: 0.5rem; color: rgba(0,242,255,0.4); letter-spacing: 3px;">
                SYSTEM SECURE
            </p>
        </div>
    """, unsafe_allow_html=True)
