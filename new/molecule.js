// molecule.js â€” 3D rotating molecular lattice for the hero.
// Pure SVG + requestAnimationFrame. ~12 vertices, ~30 edges (icosahedron).

(function () {
    const svg = document.querySelector('.mol-svg');
    if (!svg) return;
    const nodesG = svg.querySelector('#mol-nodes');
    const edgesG = svg.querySelector('#mol-edges');

    // Icosahedron vertices (golden-ratio based) -------------
    const phi = (1 + Math.sqrt(5)) / 2;
    const V = [
        [0, 1, phi], [0, -1, phi],
        [0, 1, -phi], [0, -1, -phi],
        [1, phi, 0], [-1, phi, 0],
        [1, -phi, 0], [-1, -phi, 0],
        [phi, 0, 1], [-phi, 0, 1],
        [phi, 0, -1], [-phi, 0, -1],
    ];

    // Compute edges: any pair with distÂ² â‰ˆ 4 is an edge ------
    const E = [];
    for (let i = 0; i < V.length; i++) {
        for (let j = i + 1; j < V.length; j++) {
            const dx = V[i][0] - V[j][0], dy = V[i][1] - V[j][1], dz = V[i][2] - V[j][2];
            const d2 = dx * dx + dy * dy + dz * dz;
            if (Math.abs(d2 - 4) < 0.01) E.push([i, j]);
        }
    }

    // Create SVG elements -----------------------------------
    const NS = 'http://www.w3.org/2000/svg';
    const nodeEls = V.map(() => {
        const c = document.createElementNS(NS, 'circle');
        c.setAttribute('r', '0');
        c.setAttribute('fill', 'url(#molNode)');
        nodesG.appendChild(c);
        return c;
    });
    const edgeEls = E.map(() => {
        const l = document.createElementNS(NS, 'line');
        edgesG.appendChild(l);
        return l;
    });

    // Add a soft inner glow halo (sits behind nodes) --------
    const halo = document.createElementNS(NS, 'circle');
    halo.setAttribute('cx', '0');
    halo.setAttribute('cy', '0');
    halo.setAttribute('r', '110');
    halo.setAttribute('fill', 'rgba(255, 220, 150, 0.10)');
    halo.setAttribute('filter', 'url(#molGlow)');
    svg.insertBefore(halo, edgesG);

    // Rotation/projection -----------------------------------
    const RADIUS = 110;         // SVG-space radius
    const PERSPECTIVE = 5;
    let ax = 0.4, ay = 0;
    let lastT = performance.now();

    function project(p) {
        // p = [x,y,z] in unit space; map to SVG with depth-based fade
        const f = PERSPECTIVE / (PERSPECTIVE + p[2]);
        return {
            x: p[0] * RADIUS * f / phi,
            y: p[1] * RADIUS * f / phi,
            // depth signal 0..1 (1 = nearest, 0 = farthest)
            d: (p[2] + phi) / (2 * phi),
            f
        };
    }
    function rotate(p, ay, ax) {
        let [x, y, z] = p;
        // rotate around Y
        let cy = Math.cos(ay), sy = Math.sin(ay);
        let x1 = x * cy + z * sy;
        let z1 = -x * sy + z * cy;
        // rotate around X
        let cx = Math.cos(ax), sx = Math.sin(ax);
        let y1 = y * cx - z1 * sx;
        let z2 = y * sx + z1 * cx;
        return [x1, y1, z2];
    }

    function tick(t) {
        const dt = Math.min(80, t - lastT) / 1000;
        lastT = t;
        ay += dt * 0.32;   // smooth Y rotation
        ax += dt * 0.06;   // very slight X drift

        // gentle additional sine wobble on X
        const axEff = ax + Math.sin(t / 4000) * 0.08;

        const projected = V.map(p => project(rotate(p, ay, axEff)));

        // update nodes â€” sized & faded by depth
        projected.forEach((p, i) => {
            const r = 4.2 + p.d * 4.8;          // 4.2 â†’ 9.0
            const op = 0.45 + p.d * 0.55;       // 0.45 â†’ 1
            const el = nodeEls[i];
            el.setAttribute('cx', p.x.toFixed(2));
            el.setAttribute('cy', p.y.toFixed(2));
            el.setAttribute('r', r.toFixed(2));
            el.setAttribute('opacity', op.toFixed(2));
        });

        // update edges â€” opacity averages of two endpoints
        E.forEach(([a, b], i) => {
            const pa = projected[a], pb = projected[b];
            const op = (0.18 + Math.min(pa.d, pb.d) * 0.65);
            const sw = 0.6 + Math.min(pa.d, pb.d) * 1.4;
            const el = edgeEls[i];
            el.setAttribute('x1', pa.x.toFixed(2));
            el.setAttribute('y1', pa.y.toFixed(2));
            el.setAttribute('x2', pb.x.toFixed(2));
            el.setAttribute('y2', pb.y.toFixed(2));
            el.setAttribute('opacity', op.toFixed(2));
            el.setAttribute('stroke-width', sw.toFixed(2));
        });

        requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
})();
