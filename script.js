let scene, camera, renderer, stars;

function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('canvas-container').appendChild(renderer.domElement);

    const starGeometry = new THREE.BufferGeometry();
    const posArray = new Float32Array(5000 * 3);
    for(let i=0; i < 5000 * 3; i++) { posArray[i] = (Math.random() - 0.5) * 1000; }
    starGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
    
    stars = new THREE.Points(starGeometry, new THREE.PointsMaterial({size: 0.7, color: 0xffffff}));
    scene.add(stars);
    camera.position.z = 1;
}

function animate() {
    requestAnimationFrame(animate);
    stars.rotation.y += 0.0007;
    renderer.render(scene, camera);
}

init();
animate();
