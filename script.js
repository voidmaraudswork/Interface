let scene, camera, renderer, stars, starGeo;
let warpActive = false;

function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
    camera.position.z = 1;
    camera.rotation.x = Math.PI/2;

    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('canvas-container').appendChild(renderer.domElement);

    starGeo = new THREE.BufferGeometry();
    const starCount = 6000;
    const positions = new Float32Array(starCount * 3);
    for(let i=0; i<starCount; i++) {
        positions[i*3] = Math.random() * 600 - 300;
        positions[i*3+1] = Math.random() * 600 - 300;
        positions[i*3+2] = Math.random() * 600 - 300;
    }
    starGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    let starMaterial = new THREE.PointsMaterial({ color: 0xffffff, size: 0.7 });
    stars = new THREE.Points(starGeo, starMaterial);
    scene.add(stars);

    animate();
}

function animate() {
    const positions = starGeo.attributes.position.array;
    let speed = warpActive ? 15.0 : 0.5; // GO FAST ON CLICK

    for(let i=0; i<6000; i++) {
        positions[i*3+1] -= speed;
        if(positions[i*3+1] < -300) positions[i*3+1] = 300;
    }
    starGeo.attributes.position.needsUpdate = true;
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
}

// THE USER INTERFACE LOGIC
document.querySelectorAll('.launch-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        warpActive = true; // Trigger Warp speed in background
        document.getElementById('warp-loader').classList.remove('hidden');
        
        // Let the animation play for 1.5 seconds before opening link
        setTimeout(() => {
            warpActive = false;
            document.getElementById('warp-loader').classList.add('hidden');
        }, 3000);
    });
});

init();
