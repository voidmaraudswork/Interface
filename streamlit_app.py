import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NEXUS COMMAND", layout="wide")

# Hide Streamlit UI
st.markdown("<style>#MainMenu, header, footer { visibility: hidden; } .stApp { background: #020205 !important; }</style>", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #020205; font-family: 'Orbitron'; color: white; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; width: 90%; max-width: 600px; margin-top: 50px; }
        .btn { aspect-ratio: 1/1; border: 1px solid #00f2ff; border-radius: 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; color: #00f2ff; transition: 0.3s; padding: 10px; text-align: center; }
        .btn:hover { background: rgba(0,242,255,0.1); box-shadow: 0 0 20px #00f2ff; }
        
        /* Lightning Overlay */
        #warp { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: radial-gradient(circle, #ff00ff, #800080, #000); 
                display: none; justify-content: center; align-items: center; z-index: 99; flex-direction: column; }
        .lightning { font-size: 3rem; animation: flash 0.2s infinite; }
        @keyframes flash { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    </style>
</head>
<body>
    <div id="warp">
        <div class="lightning">⚡⚡⚡</div>
        <h2 id="warp-title">LAUNCHING...</h2>
        <p id="warp-desc" style="font-size:0.8rem;"></p>
    </div>

    <h1 style="color:#00f2ff; margin-top:50px;">NEXUS</h1>
    <div class="grid">
        <div class="btn" onclick="warp('AI CODE FLATTENER', 'Flattening zip codes to MD files', 'https://aicodeflat.streamlit.app/')">
            <div style="font-size:0.8rem;">AI CODE FLATTENER</div>
        </div>
        <div class="btn" onclick="warp('MOVIE UPDATES', 'Movie updates every 5 mins', 'https://movievoidup.streamlit.app/')">
            <div style="font-size:0.8rem;">MOVIE UPDATES</div>
        </div>
        <div class="btn" onclick="warp('MOVIE VIBE SEARCH', 'Search by genre, vibe, type', 'https://getmoviewithvoid.streamlit.app/')">
            <div style="font-size:0.8rem;">MOVIE VIBE SEARCH</div>
        </div>
    </div>

    <script>
        function warp(title, desc, url) {
            document.getElementById('warp-title').innerText = title;
            document.getElementById('warp-desc').innerText = desc;
            document.getElementById('warp').style.display = 'flex';
            setTimeout(() => { window.open(url, '_blank'); location.reload(); }, 2000);
        }
    </script>
</body>
</html>
""", height=800)
