import streamlit as st
import streamlit.components.v1 as components

# Hide Streamlit UI
st.markdown("""
    <style>
        #MainMenu, header, footer { visibility: hidden; }
        .stApp { background: #020205 !important; }
    </style>
""", unsafe_allow_html=True)

# Full Screen Portal
components.html("""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #020205; color: white; font-family: 'Orbitron'; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; width: 90%; max-width: 600px; }
        .btn { 
            aspect-ratio: 1/1; border: 1px solid #00f2ff; border-radius: 20px; 
            display: flex; flex-direction: column; align-items: center; justify-content: center; 
            text-decoration: none; color: #00f2ff; transition: 0.3s; padding: 10px; text-align: center;
        }
        .btn:hover { background: rgba(0,242,255,0.1); box-shadow: 0 0 20px #00f2ff; transform: scale(1.02); }
        .title { font-size: 0.9rem; font-weight: 900; margin-bottom: 5px; }
        .desc { font-family: 'Rajdhani'; font-size: 0.7rem; color: #ccc; margin-top: 5px; line-height: 1.2; }
        #s { position: fixed; top: 0; left: 0; z-index: -1; }
    </style>
</head>
<body>
    <canvas id="s"></canvas>
    <h1 style="color:#00f2ff; letter-spacing:10px; margin-bottom:30px;">NEXUS</h1>
    
    <div class="grid">
        <!-- Button 1 -->
        <a href="https://aicodeflat.streamlit.app/" class="btn">
            <div class="title">AI CODE FLATTENER</div>
            <div class="desc">Flattening zip codes to MD files</div>
        </a>
        <!-- Button 2 -->
        <a href="https://movievoidup.streamlit.app/" class="btn">
            <div class="title">MOVIE UPDATES</div>
            <div class="desc">Movie updates every 5 mins with search</div>
        </a>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const scene=new THREE.Scene(), cam=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
        const ren=new THREE.WebGLRenderer({canvas:document.getElementById('s'), alpha:true});
        ren.setSize(window.innerWidth,window.innerHeight);
        const geo=new THREE.BufferGeometry(), pos=[];
        for(let i=0;i<3000;i++) pos.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
        geo.setAttribute('position', new THREE.Float32BufferAttribute(pos,3));
        scene.add(new THREE.Points(geo, new THREE.PointsMaterial({color:0xffffff, size:0.5})));
        cam.position.z=1;
        function anim(){ requestAnimationFrame(anim); scene.rotation.y+=0.0005; ren.render(scene,cam); } anim();
    </script>
</body>
</html>
""", height=800)
