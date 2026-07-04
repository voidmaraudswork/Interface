from flask import Flask

app = Flask(__name__)

# VOID CORE UI - Condensed 5-Box Grid Layout
VOID_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>lloingex core</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #020205; color: white; font-family: 'Orbitron'; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; width: 100vw; overflow: hidden; }
        canvas { position: fixed; top: 0; left: 0; z-index: -1; }
        
        #boot-screen { position: fixed; inset: 0; background: #000; z-index: 9999; display: flex; flex-direction: column; justify-content: center; align-items: center; }
        .boot-bar { width: 200px; height: 2px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; margin-top: 20px; }
        .boot-fill { width: 0%; height: 100%; background: #bc13fe; animation: boot-load 3s forwards ease-in-out; }
        @keyframes boot-load { to { width: 100%; } }

        /* GRID SYSTEM: 5 boxes in area of 4 */
        .grid { 
            display: grid; 
            grid-template-columns: repeat(3, 1fr); 
            gap: 10px; 
            width: 95%; 
            max-width: 480px; 
            margin-top: 10px; 
        }

        .btn-container { 
            position: relative; 
            aspect-ratio: 1.1 / 1; 
            border-radius: 12px; 
            padding: 2px; 
            background: linear-gradient(0deg, #00f2ff, #bc13fe, #00f2ff); 
            background-size: 100% 200%; 
            animation: flow 3s linear infinite; 
            overflow: hidden; 
            cursor: pointer; 
        }
        
        /* Adjusting btn-4 (Classified) to span if needed, but keeping them all uniform looks cleaner */
        #btn-4 { grid-column: span 1; } 

        @keyframes flow { 0% { background-position: 0% 0%; } 100% { background-position: 0% 200%; } }
        
        .btn-inner { 
            width: 100%; 
            height: 100%; 
            background: #08080a; 
            border-radius: 10px; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center; 
            text-align: center; 
            padding: 5px;
            box-sizing: border-box;
        }

        .btn-inner b { font-size: 0.5rem; letter-spacing: 1px; line-height: 1.2; }

        .modal { position: fixed; inset: 0; background: rgba(0,0,0,0.97); z-index: 8000; display: none; flex-direction: column; justify-content: center; align-items: center; backdrop-filter: blur(25px); text-align: center; }
        .modal-box { width: 85%; max-width: 400px; padding: 25px; border: 2px solid #00f2ff; background: #050505; border-radius: 25px; box-shadow: 0 0 40px rgba(0, 242, 255, 0.4); }
        
        .locked-overlay { position: absolute; inset: 0; background: rgba(255, 0, 0, 0.15); backdrop-filter: grayscale(1) blur(2px); z-index: 100; display: flex; justify-content: center; align-items: center; }
        .locked-overlay::before, .locked-overlay::after { content: ''; position: absolute; width: 80%; height: 4px; background: #ff0055; box-shadow: 0 0 15px #ff0055; border-radius: 10px; }
        .locked-overlay::before { transform: rotate(45deg); } .locked-overlay::after { transform: rotate(-45deg); }

        #warp-overlay { position: fixed; inset: 0; background: #000; display: none; flex-direction: column; justify-content: center; align-items: center; z-index: 7000; }
        .warp-fill { width: 0%; height: 3px; background: #00f2ff; box-shadow: 0 0 15px #00f2ff; }
        #override-input { width: 80%; background: transparent; border: none; border-bottom: 2px solid #ff0055; color: #ff0055; font-family: 'Orbitron'; text-align: center; margin: 20px 0; outline: none; }
    </style>
</head>
<body>
    <canvas id="bg-stars"></canvas>
    <div id="boot-screen">
        <div style="color:#00f2ff; letter-spacing:15px; font-size:1.8rem;">LLOINGEX</div>
        <div class="boot-bar"><div class="boot-fill"></div></div>
    </div>

    <div id="selection-popup" class="modal">
        <div class="modal-box">
            <h2 style="color:#00f2ff; font-size:1rem;">SELECT 2 MODULES</h2>
            <div style="display:flex; flex-direction:column; gap:10px; margin:20px 0; text-align:left;">
                <div id="sel-btn-1" style="padding:10px; border:1px solid #333; border-radius:10px;" onclick="toggleSelect('sel-btn-1', 'btn-1')">AI CODE FLATTENER</div>
                <div id="sel-btn-2" style="padding:10px; border:1px solid #333; border-radius:10px;" onclick="toggleSelect('sel-btn-2', 'btn-2')">MOVIE UPDATES</div>
                <div id="sel-btn-3" style="padding:10px; border:1px solid #333; border-radius:10px;" onclick="toggleSelect('sel-btn-3', 'btn-3')">VIBE SEARCH</div>
            </div>
            <button id="confirm-protocol" style="width:100%; padding:15px; background:none; border:1px solid #00f2ff; color:#00f2ff; font-family:Orbitron; opacity:0.3;" onclick="finalizeChoices()">LOCK SELECTION</button>
        </div>
    </div>

    <div id="override-modal" class="modal">
        <div class="modal-box" style="border-color:#ff0055;">
            <h2 style="color:#ff0055; font-size:0.9rem;">OVERRIDE REQUIRED</h2>
            <input type="text" id="override-input" placeholder="ACCESS CODE..." autocomplete="off">
            <button style="width:100%; padding:10px; background:none; border:1px solid #ff0055; color:#ff0055; font-family:Orbitron;" onclick="checkOverride()">BYPASS</button>
        </div>
    </div>

    <div id="warp-overlay">
        <p style="color:#bc13fe; font-size:0.6rem; letter-spacing:4px;">PORTAL TO LLOINGEX SUB IS OPENING...</p>
        <h1 id="warp-title" style="color:#00f2ff; font-size:1.2rem;"></h1>
        <div style="width:200px; height:2px; background:rgba(255,255,255,0.1); margin-top:20px;"><div id="fill" class="warp-fill"></div></div>
    </div>

    <h1 style="color:#00f2ff; letter-spacing:12px; font-size: 1.8rem; margin:0;">LLOINGEX</h1>
    <p style="color:#bc13fe; font-size:0.4rem; letter-spacing:5px; margin-bottom:15px;">TERMINAL ACCESS</p>

    <div class="grid">
        <div class="btn-container" id="btn-1" onclick="handleInteraction('btn-1', 'AI CODE FLATTENER', 'https://ai-code-flattener-m8e4.onrender.com')">
            <div class="btn-inner"><b>AI CODE<br>FLATTENER</b></div>
        </div>
        <div class="btn-container" id="btn-2" onclick="handleInteraction('btn-2', 'MOVIE UPDATES', 'https://lloingexmovieup.onrender.com')">
            <div class="btn-inner"><b>MOVIE<br>UPDATES</b></div>
        </div>
        <div class="btn-container" id="btn-3" onclick="handleInteraction('btn-3', 'VIBE SEARCH', 'https://lloingexmovievibe.onrender.com')">
            <div class="btn-inner"><b>VIBE<br>SEARCH</b></div>
        </div>
        <div class="btn-container" id="btn-5" onclick="handleInteraction('btn-5', 'TYPING MASTER', 'https://sunny-unicorn-193ae9.netlify.app/')">
            <div class="btn-inner"><b>TYPING<br>MASTER</b></div>
        </div>
        <div class="btn-container" id="btn-4" onclick="handleInteraction('btn-4', 'AUTOVOID', 'https://voidauto.onrender.com')">
            <div class="btn-inner" id="btn-4-content"><b style="color:#ff0055;">CLASSIFIED</b></div>
        </div>
    </div>

    <div style="position:fixed; bottom:20px; color:#bc13fe; font-size:0.6rem; font-weight:bold; letter-spacing:6px;">LLOINGEX</div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const sS=new THREE.Scene(), sC=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
        const sR=new THREE.WebGLRenderer({canvas:document.getElementById('bg-stars'), alpha:true});
        sR.setSize(window.innerWidth,window.innerHeight);
        const sG=new THREE.BufferGeometry(), sP=[];
        for(let i=0;i<2500;i++) sP.push(Math.random()*2000-1000,Math.random()*2000-1000,Math.random()*2000-1000);
        sG.setAttribute('position', new THREE.Float32BufferAttribute(sP,3));
        sS.add(new THREE.Points(sG, new THREE.PointsMaterial({color:0xffffff, size:0.8})));
        sC.position.z=1;
        function anim(){ requestAnimationFrame(anim); sS.rotation.y+=0.0004; sR.render(sS,sC); } anim();

        let storage = JSON.parse(localStorage.getItem('void_render_v1')) || { active: [], locked: ['btn-4'], expiry: null, auto_unlocked: false };
        if(storage.expiry && Date.now() > storage.expiry) { storage = { active: [], locked: ['btn-4'], expiry: null, auto_unlocked: storage.auto_unlocked }; }
        
        window.onload = () => { if(storage.auto_unlocked) unlockAutoUI(); setTimeout(() => { document.getElementById('boot-screen').style.display = 'none'; if(storage.expiry) applyLocks(); }, 3200); };
        
        let currentId = '';
        function handleInteraction(id, title, url) {
            currentId = id;
            if(storage.locked.includes(id) || (id === 'btn-4' && !storage.auto_unlocked)) { document.getElementById('override-modal').style.display='flex'; return; }
            // Journal Formatter is always open, others require selection if expiry not set
            if(!storage.expiry && id !== 'btn-5' && id !== 'btn-4') { document.getElementById('selection-popup').style.display='flex'; return; }
            runWarp(title, url);
        }

        function checkOverride() {
            let val = document.getElementById('override-input').value;
            if(val === 'ifollowedvoidmarauds' || (storage.auto_unlocked && val === '345')) {
                if(currentId === 'btn-4') storage.auto_unlocked = true;
                storage.active.push(currentId);
                storage.locked = storage.locked.filter(i => i !== currentId);
                localStorage.setItem('void_render_v1', JSON.stringify(storage));
                location.reload();
            } else { alert('ACCESS DENIED'); }
        }

        let selected = [];
        function toggleSelect(elId, id) {
            const el = document.getElementById(elId);
            if(selected.includes(id)) { selected = selected.filter(i => i !== id); el.style.borderColor = '#333'; }
            else if(selected.length < 2) { selected.push(id); el.style.borderColor = '#bc13fe'; }
            document.getElementById('confirm-protocol').style.opacity = (selected.length === 2) ? '1' : '0.3';
        }

        function finalizeChoices() {
            storage.active = selected; 
            storage.locked = ['btn-1','btn-2','btn-3'].filter(i => !selected.includes(i));
            if(!storage.auto_unlocked) storage.locked.push('btn-4');
            storage.expiry = Date.now() + 86400000;
            localStorage.setItem('void_render_v1', JSON.stringify(storage));
            location.reload();
        }

        function unlockAutoUI() { document.getElementById('btn-4-content').innerHTML = '<b>AUTOVOID</b>'; }
        function applyLocks() { storage.locked.forEach(id => { const b = document.getElementById(id); if(!b.querySelector('.locked-overlay')){ const o=document.createElement('div'); o.className='locked-overlay'; b.appendChild(o); } }); }

        function runWarp(title, url) {
            document.getElementById('warp-title').innerText = title;
            document.getElementById('warp-overlay').style.display = 'flex';
            let start = null;
            function step(t) {
                if (!start) start = t;
                let p = (t - start) / 2000;
                document.getElementById('fill').style.width = Math.min(p * 100, 100) + '%';
                if (p < 1) requestAnimationFrame(step);
                else { window.open(url, '_blank'); setTimeout(() => { document.getElementById('warp-overlay').style.display='none'; }, 1000); }
            }
            requestAnimationFrame(step);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return VOID_UI

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
