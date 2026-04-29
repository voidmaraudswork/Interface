let scene, camera, renderer, stars;

function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('canvas-container').appendChild(renderer.domElement);

    // Create Starfield
    const starGeometry = new THREE.BufferGeometry();
    const starCount = 15000;
    const posArray = new Float32Array(starCount * 3);

    for(let i=0; i < starCount * 3; i++) {
        posArray[i] = (Math.random() - 0.5) * 1500;
    }
    starGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

    const starMaterial = new THREE.PointsMaterial({
        size: 0.7,
        color: 0xffffff,
        transparent: true
    });

    stars = new THREE.Points(starGeometry, starMaterial);
    scene.add(stars);
    camera.position.z = 1;
}

function animate() {
    requestAnimationFrame(animate);
    stars.rotation.y += 0.0005;
    stars.rotation.x += 0.0002;
    renderer.render(scene, camera);
}

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

init();
animate();