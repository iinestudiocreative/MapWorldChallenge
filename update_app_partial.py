1: 1: import os
2: 2:   "242": { en: "Fiji", fr: "Fidji", ja: "フィジー", es: "Fiyi", ko: "피지", zh: "斐济", hi: "Fiji" },
3: 3: I have successfully updated **both France and Japan maps** to be highly detailed, realistic **Geographic Maps** (prefectures and departments layouts) with fully integrated **pinch-to-zoom, scroll-zoom, double-tap-to-zoom, and pan** gestures using D3.js. Both maps employ elegant isolated overseas insets and gesture filtering for a premium and seamless experience.
4: 4: Un service web où les utilisateurs créent et partagent leur **carte de voyage personnalisée** (par pays ou par région), exportable en image pour Instagram. Le service démarre avec le Japon et s'étend à tous les pays du monde.
5: 5: L'application est inspirée du concept original **JapanEx / 制縣傳說 (Japan Experience Level)** et intègre des fonctionnalités premium, un design néobrutaliste soigné et une navigation ultra-fluide.
6: 6:   "840": { en: "United States", fr: "États-Unis", ja: "アメリカ合衆国", es: "Estados Unidos", ko: "미국", zh: "美国", hi: "United States of America" },
7: 7:   "398": { en: "Kazakhstan", fr: "Kazakhstan", ja: "カザフスタン", es: "Kazajistán", ko: "카자흐스탄", zh: "哈萨克斯坦", hi: "Kazakhstan" },
8: 8:   "860": { en: "Uzbekistan", fr: "Ouzbékistan", ja: "ウズベキスタン", es: "Uzbekistán", ko: "우즈베키스탄", zh: "乌兹别克斯坦", hi: "Uzbekistan" },
9:   "598": { en: "Papua New Guinea", fr: "Papouasie-Nouvelle-Guinée", ja: "パプアニューギニア", es: "Papúa Nueva Guinea", ko: "파푸아뉴기니", zh: "巴布亚新几内亚", hi: "Papua New Guinea" },
10: - **Transition from Grid to Realistic Shape**: Switched Japan from the stylized square grid map to a highly realistic geographic map of the 47 prefectures by loading and parsing `japan.json` (TopoJSON) dynamically.
11: Les blocs (CSS grid) sont lisibles mais non reconnaissables pour la majorité des pays. Pour que l'image partagée sur Instagram soit immédiatement identifiable comme "carte du Japon / USA / France", il faut des **vraies frontières géographiques**.
12: - **Main Island Projection**: Honshu, Hokkaido, Kyushu, and Shikoku are projected beautifully using D3 Mercator projection and fitted inside the main SVG area (`[110, 25] to [550, 545]`), ensuring perfect proportions and framing.
13: - Restored `drawFranceMap()` in [update_app.py](file:///Users/willkyandi/Documents/AI%20-%20Random%20Project/carte-japon/update_app.py) to render metropolitan France via D3's Conic Conformal projection, with precise centroids for department number labels.
14: { "type": "Feature", "properties": { "ID_0": 105, "ISO": "IND", "NAME_0": "India", "ID_1": 1, "NAME_1": "Andaman and Nicobar", "NL_NAME_1": null, "VARNAME_1": "Andaman & Nicobar Islands|Andaman et Nicobar|Iihas de Andama e Nicobar|Inseln Andamanen und Nikobare", "TYPE_1": "Union Territor", "ENGTYPE_1": "Union Territory" }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ 93.787727355957088, 6.85264015197771 ], [ 93.788490295410213, 6.8525710105896 ], [ 93.789047241210994, 6.8525710105896 ], [ 93.789047241210994, 6.852291107177678 ], [ 93.789672851562784, 6.852291107177678 ], [ 93.789878845215128, 6.852013111114729 ], [ 93.790153503418139, 6.851944923400936 ], [ 93.790641784668253, 6.851666927337817 ], [ 93.790779113769588, 6.851388931274641 ], [ 93.790916442871264, 6.851041793823242 ], [ 93.790504455566577, 6.850625038147029 ], [ 93.790290832519474, 6.85034704208374 ], [ 93.790000915527401, 6.850278854370117 ], [ 93.789482116699503, 6.84990310668968 ], [ 93.789001464843921, 6.849484920501766 ], [ 93.788375854492131, 6.849136829376448 ], [ 93.788017272949389, 6.848720073700065 ], [ 93.787780761719034, 6.84
15: - `[x]` Step 13: Replace Japan emoji flag `🗾` next to the card title with custom white inline SVG silhouette map of Japan for complete graphic coherence.
16: 3. Scannez-le simplement avec l'appareil photo de votre téléphone (connecté au **même WiFi** que le Mac) pour l'ouvrir instantanément !
17: - Configured a D3 zoom behavior (`d3.zoom()`) targeting the metropolitan France map group (`#metro-group` / `mapG`):
18: | **Monde (50m)** | `cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json` | ~200KB | Carte mondiale (plus détaillée) |
19:   "260": { en: "French Southern and Antarctic Lands", fr: "Terres australes et antarctiques françaises", ja: "フランス領南方・南極地域", es: "Tierras Australes y Antárticas Francesas", ko: "프랑스령 남부와 남극 지역", zh: "法国南部和南极土地", hi: "Fr. S. Antarctic Lands" },
20:                             # Ensure we don't accidentally get other files' lines if any
21: - **France Country Shape Icon**: Designed a custom inline SVG silhouette of metropolitan France to replace the generic `🇫🇷` emoji flag next to the card title, matching how `🗾` represents Japan.
22:           [ [ [ 159.105420, -31.563994 ], [ 159.097750, -31.564275 ], [ 159.099634, -31.573372 ], [ 159.094217, -31.570970 ], [ 159.074599, -31.597285 ], [ 159.068740, -31.595697 ], [ 159.077238, -31.543533 ], [ 159.056995, -31.519772 ], [ 159.038463, -31.522425 ], [ 159.037960, -31.512156 ], [ 159.064657, -31.509666 ], [ 159.063790, -31.517379 ], [ 159.081178, -31.526607 ], [ 159.081913, -31.539767 ], [ 159.094678, -31.545036 ], [ 159.105420, -31.563994 ] ] ], [ [ [ 151.145550, -33.824079 ], [ 151.143844, -33.829174 ], [ 151.169325, -33.839309 ], [ 151.180206, -33.836165 ], [ 151.174277, -33.843006 ], [ 151.143088, -33.835565 ], [ 151.135902, -33.836469 ], [ 151.148783, -33.839386 ], [ 151.133837, -33.844837 ], [ 151.112863, -33.829724 ], [ 151.108625, -33.835555 ], [ 151.092828, -33.819609 ], [ 151.070345, -33.816445 ], [ 151.051336, -33.823662 ], [ 151.084007, -33.822080 ], [ 151.075192, -33.832683 ], [ 151.080873, -33.845750 ], [ 151.083228, -33.827897 ], [ 151.093817, -33.824443 ], [ 151.089778, -33.833044 ], [ 151.098921,
23:   "21": "Huelva", "22": "Huesca", "23": "Jaén", "24": "León",
24: - **Flag Updates**: Fixed a bug in `updateUITranslations()` where switching to the France map did not update the card's flag icon. It now correctly switches to `🇫🇷` (the flag of France).
25: - **Overlap Prevention**: This significant reduction prevents long prefecture/department names (such as "Hokkaido", "Kagoshima", "Alpes-Maritimes", etc.) from overlapping neighboring regions at default zoom levels, resulting in an exceptionally clean, readable, and professional map overview.
26:   "33": "Asturias", "34": "Palencia", "35": "Las Palmas", "36": "Pontevedra",
27: *   **📍 Grille de Préfectures Stylisée (JIS X 0401) :** Une carte en blocs de grille
28: - **Automatic Display on Page Load**: Implemented a modern welcome popup overlay that appears automatically every time a user arrives on the website.
29: - **Premium Interface**: Designed a gorgeous CSS card with a blurred glassmorphic backdrop (`backdrop-filter: blur(10px)`), elegant modern typography (Outfit), rounded buttons with custom gradients, and clear feature iconography.
30:   - Utilisation d'une projection `d3.geoMercator()` centrée précisément sur l'Italie et ajustée automatiquement avec `.fitExtent()` pour intégrer harmonieusement la péninsule, la Sicile et la Sardaigne.
31: 4. **DOM-TOM Box Stability**: Verify that dragging or pinching directly over the 5 DOM-TOM boxes on the left column (`x < 92`) does **not** zoom the map, keeping them fixed and perfectly clickable.
32:   - Placement précis des étiquettes (labels) sur la carte au centroïde de chaque province en affichant leur code unique de 2 lettres en majuscules (ex: "RM", "MI") pour un rendu esthétique, propre et professionnel même sur smartphone.
33: 3. **Pinch or Double-Tap**: On a mobile device, pinch with two fingers or double-tap to zoom into metropolitan France. On a desktop, use your mouse wheel or trackpad scroll gesture.
34: 4. **DOM-TOM Isolation Test**: Try to zoom or drag with your fingers **directly over the DOM-TOM boxes on the left column** (x < 92). Verify that **no zoom or pan is triggered**, keeping the left column perfectly static.
35: 5. **Metropolitan Zoom Test**: Zoom or drag over **metropolitan France** (x >= 92), and verify that it zooms and pans smoothly.
36: 6. **Selection**: Tap on a zoomed-in department (e.g. *Paris 75*), and verify that it opens the visitation level modal smoothly without accidental triggers during panning.
37: - **100% Tactile Okinawa Touch Target**: Replaced the thin island paths with a top-level invisible box covering the *entire* Okinawa inset box (`[OX, OY, OW, OH]`). By placing the transparent click layer *last* in the group and configuring `pointer-events="all"`, touch gestures and taps are perfectly captured anywhere within the box, resolving the finger touch issue.
38: - **Unified DOM-TOM French Inset Tapping**: For strict graphic coherence, applied the same transparent full-box click helper to all 5 French overseas departments insets. Clicking anywhere inside the bounds of Guadeloupe, Martinique, Guyane, La Réunion, or Mayotte boxes immediately captures the click on mobile.
39: - **Realistic Japan Silhouette Outline**: Replaced the old pixelated/blocky hardcoded Japan SVG flag silhouette in the card title bar with a highly realistic, geographically precise outline of Japan (Honshu, Hokkaido, Kyushu, Shikoku, and Okinawa). Generated directly from true GeoJSON 
40: - **Unified Pop-up Tutoriel Design**: Redesigned the tutorial popup to match the other native modals in the application (Country, Language, and Level modals). It now inherits `.custom-modal` with its sharp corners (`border-radius: 0;`), has a `.modal-header` with uppercase bold typography and a top-right `✕` close button, lists step items inside `.modal-opts` using `.opt-btn` layout styles, and features a flat solid `#111111` action button at the bottom.
41: - **Tutorial Modal Display Fix**: Replaced the CSS opacity transition for hiding the popup modal with a robust `display: none !important;` rule when `.hidden` is present. This completely eliminates layout shifts or rendering bugs on mobile devices, ensuring the overlay displays perfectly centered on load and is fully dismissed when clicking either the bottom button or top-right `✕`.
42:   - Refonte visuelle complète de ce bouton d'export : le bouton est désormais **jaune** (`#FFDE00`) avec une écriture **noire**, respectant le thème premium, avec un effet de survol dynamique jaune plus foncé (`#f0cf00`).
43:   "40": "Landes", "41": "Loir-et-Cher", "42": "Loire", "43": "Haute-Loire", "44": "Loire-Atlantique",
44: 4. **Pinch or Scroll**: Double-tap or pinch over metropolitan France (`x >= 92`) to zoom and pan.
45: 5. **DOM-TOM Box Stability**: Verify that dragging or pinching directly over the 5 DOM-TOM boxes on the left column (`x < 92`) does **not** zoom the map, keeping them fixed and perfectly clickable.
46: 6. **Silhouette Icon**: Check that the title bar next to "Ride the world" displays a premium **white SVG outline representing the geographic shape of France** instead of a flat flag emoji.
47: 2. **Tutorial Popup**: Verify that a gorgeous **Welcome & Tutorial Popup** modal appears on load. Dismiss it by clicking **"C'est parti !"** or **"Let's go!"**.
48: 2. **Tutorial Popup**: Verify that a gorgeous **Welcome & Tutorial Popup** modal appears on load. Dismiss it by clicking **"C'est parti !"** or **"Let's go!"**.
49: - **Zoom & Déplacement** : Utilisez le défilement de la souris ou pincez sur mobile pour zoomer sur les provinces du nord (comme Milan, Bergame, Côme) et vérifiez que les étiquettes en 2 lettres (ex: `MI`, `BG`, `CO`) restent lisibles et bien centrées.
50: 5. **DOM-TOM Box Stability**: Verify that dragging or pinching directly over the 5 DOM-TOM boxes on the left column (`x < 92`) does **not** zoom the map, keeping them fixed and perfectly clickable.
51: 5. **DOM-TOM Box Stability**: Verify that dragging or pinching directly over the 5 DOM-TOM boxes on the left column (`x < 92`) does **not** zoom the map, keeping them fixed and perfectly clickable.
52: 5. **DOM-TOM Box Stability**: Verify that dragging or pinching directly over the 5 DOM-TOM boxes on the left column (`x < 92`) does **not** zoom the map, keeping them fixed and perfectly clickable.
53: 6. **Silhouette Icon**: Check that the title bar next to "Ride the world" displays a premium **white SVG outline representing the geographic shape of France** instead of a flat flag emoji.
54: - **Titre flottant** : Vérifiez que le sous-titre de profil s'affiche correctement en français avec la césure appropriée.
55: 1.  **[index.html](file:///Users/willkyandi/Documents/AI%20-%20Random%20Project/carte-japon/index.html) :** Structure HTML5 sémantique, avec intégration des CDNs requis (html2canvas, qrcodejs et FontAwesome) et des tiroirs de sélection tactiles.
56: 2.  **[styles.css](file:///Users/willkyandi/Documents/AI%20-%20Random%20Project/carte-japon/styles.css) :** Design system complet avec une palette de couleurs riches et harmonieuses, des animations douces pour les popups, des boutons néobrutalistes premium et un affichage 100% adapté aux mobiles.
57: 3.  **[app.js](file:///Users/willkyandi/Documents/AI%20-%20Random%20Project/carte-japon/app.js) :** Coeur applicatif. Il gère l'état de la carte, les calculs des points, le basculement des langues, le rendu dynamique de la grille, le stockage local et le pont html2canvas pour la capture PNG.
58: 4.  **[server.js](file:///Users/willkyandi/Documents/AI%20-%20Random%20Project/carte-japon/server.js) :** Serveur Node.js léger en cas d'utilisation future de Node, tandis que le serveur actif actuel est propulsé par Python 3 natif pour une compatibilité immédiate sans dépendances.
59: 4. **Okinawa Inset Stability**: Verify that the Okinawa inset box in the top-left corner (`x < 110`) remains completely static and does not scale or pan when zooming the rest of the map.
60: 6. **Centroid Labels & Clean Typography**: Verify that prefecture labels are perfectly placed in the middle of each prefecture, and rendered at a very compact `3.8px` size preventing overlaps.
61: 6. **Centroid Labels & Clean Typography**: Verify that prefecture labels are perfectly placed in the middle of each prefecture, and rendered at a very compact `3.8px` size preventing overlaps.
62: 6. **Centroid Labels & Clean Typography**: Verify that prefecture labels are perfectly placed in the middle of each prefecture, and rendered at a very compact `3.8px` size preventing overlaps.
63: > **Astuce de partage :** Lorsque vous ouvrez l'application sur votre téléphone portable, vous pouvez l'ajouter à votre écran d'accueil (option "Sur l'écran d'accueil" de Safari/Chrome) pour y accéder comme s'il s'agissait d'une application native installée !
64:   { code: "04", x: 460, y: 265, w: 60, h: 55 },
65:         res.writeHead(500, { 'Content-Type': 'text/plain' });
66:         res.end('Sorry, check with the site admin for error: ' + error.code + ' ..\n');
67:   { code: "08", x: 460, y: 375, w: 50, h: 50 },
68:   { code: "09", x: 415, y: 375, w: 40, h: 45 },
69:       res.writeHead(200, { 'Content-Type': contentType });
70:   { code: "11", x: 370, y: 420, w: 60, h: 35 },
71: /* Header (Obsidian Indigo-Teal Premium Gradient) */
72:   { code: "13", x: 370, y: 460, w: 65, h: 35 },
73:   background: linear-gradient(135deg, #1a2238 0%, #204d5b 100%); /* Gorgeous dark gradient from image */
74:   { code: "15", x: 310, y: 285, w: 80, h: 45 },
75:   <button id="btn-lang-select">🌐 English <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i></button>
76:   <button id="btn-export" class="btn-accent"><i class="fa fa-download"></i> Exporter</button>
77:   <button id="btn-reset" class="btn-muted"><i class="fa fa-rotate-left"></i></button>
78:   console.log('                 JAPANEX - SERVEUR LOCAL RUNNING             ');
79:   console.log('=============================================================');
80: <!-- ═══════════════════════════════════════════ COUNTRY MODAL -->
81:   console.log(`  👉 Sur votre Téléphone (même WiFi) : http://${localIp}:${PORT}`);
82:   console.log('\n-------------------------------------------------------------');
83:   console.log('   Pressez [Ctrl + C] dans ce terminal pour arrêter le serveur');
84:   console.log('=============================================================\n');
85:       <button id="country-close" class="modal-close">✕</button>
86:   { code: "27", x: 200, y: 435, w: 30, h: 30 },
87:   { code: "29", x: 205, y: 470, w: 25, h: 40 },
88:       <a href="https://www.instagram.com/french_rider_in_japan/" target="_blank" rel="noopener" style="text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 8px; background: #FFDE00; color: #111111; padding: 14px 16px; font-size: 0.8rem; font-weight: 800; text-align: center; font-family: var(--font); line-height: 1.3; transition: background 0.15s ease; width: 100%; margin-bottom: -1.5px; position: relative; z-index: 1; cursor: pointer;" onmouseover="this.style.background='#f0cf00'" onmouseout="this.style.background='#FFDE00'">
89:         <i class="fa-brands fa-instagram" style="font-size: 1.15rem;"></i>
90:         <span>Un autre pays en tête ? Suggère-le en DM !</span>
91:       <button class="opt-btn country-btn" data-val="fr" disabled style="opacity:0.5;cursor:not-allowed">
92:         <div><strong>🇪🇸 Espagne</strong><small>Disponible</small></div>
93:       <button class="opt-btn country-btn" data-val="world">
94:       <button class="opt-btn country-btn" data-val="it" disabled style="opacity:0.5;cursor:not-allowed">
95:         <div><strong>🇫🇷 France</strong><small>Disponible</small></div>
96:     <div><strong>🇦🇺 Australie</strong><small>Disponible</small></div>
97:       <button class="opt-btn country-btn" data-val="it" disabled style="opacity:0.5;cursor:not-allowed">
98:         <div><strong>🇯🇵 Japon</strong><small>Disponible</small></div>
99:     <div><strong>🇮🇳 Inde</strong><small>Disponible</small></div>
100:       <button class="opt-btn country-btn" data-val="us" disabled style="opacity:0.5;cursor:not-allowed">
101:   "840": { en: "United States", fr: "États-Unis", ja: "アメリカ", es: "Estados Unidos", ko: "미국", zh: "美国", hi: "अमेरिका" },
102:   "250": { en: "France", fr: "France", ja: "フランス", es: "Francia", ko: "프랑스", zh: "法国", hi: "फ्रांस" },
103:       <button class="opt-btn country-btn" data-val="us" disabled style="opacity:0.5;cursor:not-allowed">
104:   "380": { en: "Italy", fr: "Italie", ja: "イタリア", es: "Italia", ko: "이탈리아", zh: "イタリア", hi: "इटली" },
105: Ajout des fonctions de dessin dans `update_app.py` utilisant `d3.geoMercator()` ajusté automatiquement avec `.fitExtent()` :
106:   "124": { en: "Canada", fr: "Canada", ja: "カナダ", es: "Canadá", ko: "캐나다", zh: "加拿大", hi: "कनाडा" },
107:   "276": { en: "Germany", fr: "Allemagne", ja: "ドイツ", es: "Alemania", ko: "독일", zh: "德国", hi: "जर्मनी" },
108:   "826": { en: "United Kingdom", fr: "Royaume-Uni", ja: "イギリス", es: "Reino Unido", ko: "영국", zh: "英国", hi: "यूके" },
109:   "036": { en: "Australia", fr: "Australie", ja: "オーストラリア", es: "Australia", ko: "호주", zh: "澳大利亚", hi: "ऑस्ट्रेलिया" },
110:   "156": { en: "China", fr: "Chine", ja: "中国", es: "China", ko: "중국", zh: "中国", hi: "चीन" },
111:   "356": { en: "India", fr: "Inde", ja: "インド", es: "India", ko: "인도", zh: "印度", hi: "भारत" },
112:   { code: '03', x: 278, y: 285, w: 38, h: 38, isDom: false },
113:   { code: '04', x: 398, y: 405, w: 38, h: 38, isDom: false },
114:   { code: '05', x: 358, y: 365, w: 38, h: 38, isDom: false },
115: <!-- ═══════════════════════════════════════════ LANGUAGE MODAL -->
116:   { code: '07', x: 278, y: 365, w: 38, h: 38, isDom: false },
117:   - Masquage des abréviations textuelles pour CH, DN, DD, DL, LD.
118:   { code: '09', x: 158, y: 445, w: 38, h: 38, isDom: false },
119:   { code: '10', x: 318, y: 165, w: 38, h: 38, isDom: false },
120:   "704": { en: "Vietnam", fr: "Viêt Nam", ja: "ベトナム", es: "Vietnam", ko: "베트남", zh: "越南", hi: "वियतनाम" },
121:   "360": { en: "Indonesia", fr: "Indonésie", ja: "インドネシア", es: "Indonesia", ko: "인도네시아", zh: "印度尼西亚", hi: "इंडोनेशिया" },
122:   "554": { en: "New Zealand", fr: "Nouvelle-Zélande", ja: "ニュージーランド", es: "Nueva Zelanda", ko: "뉴질랜드", zh: "新西兰", hi: "न्यूजीलैंड" }
123:   { code: '14', x: 78, y: 125, w: 38, h: 38, isDom: false },
124: - Lancer le compilateur `python3 update_app.py` pour régénérer `app.js`.
125:   "840": { en: "United States", fr: "États-Unis", ja: "アメリカ", es: "Estados Unidos", ko: "미국", zh: "美国", hi: "अमेरिका" },
126:   "250": { en: "France", fr: "France", ja: "フランス", es: "Francia", ko: "프랑스", zh: "法国", hi: "फ्रांस" },
127:   "392": { en: "Japan", fr: "Japon", ja: "日本", es: "Japón", ko: "일본", zh: "日本", hi: "जापान" },
128:   "380": { en: "Italy", fr: "Italie", ja: "イタリア", es: "Italia", ko: "이탈리아", zh: "イタリア", hi: "इटली" },
129:   "724": { en: "Spain", fr: "Espagne", ja: "スペイン", es: "España", ko: "스페인", zh: "西班牙", hi: "स्पेन" },
130:   "124": { en: "Canada", fr: "Canada", ja: "カナダ", es: "Canadá", ko: "캐나다", zh: "加拿大", hi: "कनाडा" },
131:   "276": { en: "Germany", fr: "Allemagne", ja: "ドイツ", es: "Alemania", ko: "독일", zh: "德国", hi: "जर्मनी" },
132:   "826": { en: "United Kingdom", fr: "Royaume-Uni", ja: "イギリス", es: "Reino Unido", ko: "영국", zh: "英国", hi: "यूके" },
133:   "036": { en: "Australia", fr: "Australie", ja: "オーストラリア", es: "Australia", ko: "호주", zh: "澳大利亚", hi: "ऑस्ट्रेलिया" },
134:   "156": { en: "China", fr: "Chine", ja: "中国", es: "China", ko: "중국", zh: "中国", hi: "चीन" },
135:   "826": { en: "United Kingdom", fr: "Royaume-Uni", ja: "イギリス", es: "Reino Unido", ko: "영국", zh: "英国", hi: "यूके" },
136:   "036": { en: "Australia", fr: "Australie", ja: "オーストラリア", es: "Australia", ko: "호주", zh: "澳大利亚", hi: "ऑस्ट्रेलिया" },
137:   "156": { en: "China", fr: "Chine", ja: "中国", es: "China", ko: "중국", zh: "中国", hi: "चीन" },
138:   "356": { en: "India", fr: "Inde", ja: "インド", es: "India", ko: "인도", zh: "印度", hi: "भारत" },
139:   "076": { en: "Brazil", fr: "Brésil", ja: "Brésil", es: "Brasil", ko: "브라질", zh: "巴西", hi: "ब्राजील" },
140:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} regions</strong></span></div>`,
141:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} countries</strong></span></div>`,
142:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} regions</strong></span></div>`,
143:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} countries</strong></span></div>`,
144:       desc: "This application is <strong>100% free</strong>!<br>A simple follow on Instagram helps me<br>tremendously to continue this adventure.<br>🏍️🇯🇵 <strong>Thank you for your support!</strong>",
145:   "056": { en: "Belgium", fr: "Belgique", ja: "ベルギー", es: "Bélgica", ko: "벨기에", zh: "比利时", h
146:       desc: "This application is <strong>100% free</strong>!<br>A simple follow on Instagram helps me<br>tremendously to continue this adventure.<br>🏍️🇯🇵 <strong>Thank you for your support!</strong>",
147:       follow: `<i class="fa-brands fa-instagram"></i> Follow @french_rider_in
148: | **GitHub Pages** | Gratuit | ⭐⭐⭐⭐ | MVP simple |
149:       <button class="opt-btn" data-level="5">
150:       subtitle: "What is your exploration level?",
151:         <div><strong>Lived there</strong><small>J'y ai habité (+5 pts)</small></div>
152: > **Vercel est la recommandation.** `vercel deploy` dans le terminal et c'est en ligne en 30 secondes avec un URL HTTPS automatique. Zéro configuration.
153:       l3: { main: "Visited there", sub: "Day trip (+3 pts)" },
154:       l2: { main: "Alighted there", sub: "Stopover / Transit (+2 pts)" },
155:         <div><strong>Stayed there</strong><small>Séjour ≥ 1 nuit (+4 pts)</small></div>
156:       l0: { main: "Never been", sub: "Never been (0 pt)" }
157:     return COUNTRY_NAMES[id][lang] || COUNTRY_NAMES[id].en;
158:         <span class="opt-dot" data-l="3"></span>
159:         <div><strong>Visited there</strong><small>Visite de journée (+3 pts)</small></div>
160:       world: "🌍 World", fr: "🇫🇷 France", it: "🇮🇹 Italy", jp: "🇯🇵 Japan", us: "🇺🇸 USA",
161:       <button class="opt-btn" data-level="2">
162:       world: "🌍 World", fr: "🇫🇷 France", it: "🇮🇹 Italy", jp: "🇯🇵 Japan", us: "🇺🇸 USA",
163:   "818": { en: "Egypt", fr: "Égypte", ja: "エジプト", es: "Egipto", ko: "이집트", zh: "埃及", hi: "Egypt" },
164:   "434": { en: "Libya", fr: "Libye", ja: "リビア", es: "Libia", ko: "리비아", zh: "利比亚", hi: "Libya" },
165:   "231": { en: "Ethiopia", fr: "Éthiopie", ja: "エチオピア", es: "Etiopía", ko: "에티오피아", zh: "埃塞俄比亚", hi: "Ethiopia" },
166:   "262": { en: "Djibouti", fr: "Djibouti", ja: "ジブチ", es: "Djibouti", ko: "지부티", zh: "吉布提", hi: "Djibouti" },
167:   "800": { en: "Uganda", fr: "Ouganda", ja: "ウガンダ", es: "Uganda", ko: "우간다", zh: "乌干达", hi: "Uganda" },
168:   "646": { en: "Rwanda", fr: "Rwanda", ja: "ルワンダ", es: "Ruanda", ko: "르완다", zh: "卢旺达", hi: "Rwanda" },
169:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} regions</strong></span></div>`,
170:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} countries</strong></span></div>`,
171:   "688": { en: "Serbia", fr: "Serbie", ja: "セルビア", es: "Serbia", ko: "세르비아", zh: "塞尔维亚", hi: "Serbia" },
172:   "499": { en: "Montenegro", fr: "Monténégro", ja: "モンテネグロ", es: "Montenegro", ko: "몬테네그로", zh: "黑山", hi: "Montenegro" },
173:       desc: "This application is <strong>100% free</strong>!<br>A simple follow on Instagram helps me<br>tremendously to continue this adventure.<br>🏍️🇯🇵 <strong>Thank you for your support!</strong>",
174:   "728": { en: "South Sudan", fr: "Soudan du Sud", ja: "南スーダン", es: "Sudán del Sur", ko: "남수단", zh: "南苏丹", hi: "S. Sudan" }
175:   { code: '65', x: 78, y: 445, w: 38, h: 38, isDom: false },
176:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 地域</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
177:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} ヶ国</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
178:   { code: '68', x: 398, y: 125, w: 38, h: 38, isDom: false },
179:   { code: '69', x: 278, y: 325, w: 38, h: 38, isDom: false },
180:       desc: "このアプリは<strong>100%無料</strong>です！<br>Instagramをフォローして応援していただけると<br>旅の励みになります。よろしくお願いします！🏍️🇯🇵",
181:       follow: `<i class="fa-brands fa-instagram"></i> @french_rider_in_japan をフォロー`,
182:     <p id="export-desc">Cette application est <strong>100% gratuite</strong> !<br>Un simple abonnement sur Instagram m'aide<br>énormément à continuer cette aventure.<br>🏍️🇯🇵 <strong>Merci pour ton soutien !</strong></p>
183:     <a id="btn-follow" href="https://www.instagram.com/french_rider_in_japan/" target="_blank" rel="noopener">
184:       <i class="fa-brands fa-instagram"></i> Suivre @french_rider_in_japan
185:     <p id="export-desc">Cette application est <strong>100% gratuite</strong> !<br>Un simple abonnement sur Instagram m'aide<br>énormément à continuer cette aventure.<br>🏍️🇯🇵 <strong>Merci pour ton soutien !</strong></p>
186:     <a id="btn-follow" href="https://www.instagram.com/french_rider_in_japan/" target="_blank" rel="noopener">
187:     <button id="btn-dl-shared">J'ai partagé ! Télécharger en HD 🎉</button>
188:   { code: '78', x: 198, y: 165, w: 38, h: 38, isDom: false },
189:     <button id="btn-dl-anyway">Télécharger quand même</button>
190:     <p id="export-desc">Cette application est <strong>100% gratuite</strong> !<br>Un simple abonnement sur Instagram m'aide<br>énormément à continuer cette aventure.<br>🏍️🇯🇵 <strong>Merci pour ton soutien !</strong></p>
191:     <a id="btn-follow" href="https://www.instagram.com/french_rider_in_japan/" target="_blank" rel="noopener">
192:       <i class="fa-brands fa-instagram"></i> Suivre french_rider_in_japan
193:   { code: '83', x: 358, y: 445, w: 38, h: 38, isDom: false },
194: <!-- ═══════════════════════════════════════════ TUTORIAL POPUP MODAL -->
195:     <button id="btn-dl-shared">J'ai partagé ! Télécharger en HD 🎉</button>
196: **Action 1** : Tester le rendu D3.js avec les vraies formes — je peux coder ça maintenant.
197:         <div class="tuto-icon"><i class="fa-solid fa-maximize"></i></div>
198:     <p id="tuto-subtitle" style="margin-top: -6px; margin-bottom: 20px;">Comment utiliser l'application</p>
199: <!-- ═══════════════════════════════════════════ TUTORIAL POPUP MODAL -->
200: <div id="tutorial-overlay" class="hidden" style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
201:   <div id="tutorial-modal" class="custom-modal">
202:       <div class="opt-btn" style="cursor: default; pointer-events: none;">
203:         <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-maximize"></i></span>
204:         <div class="tuto-icon"><i class="fa-solid fa-location-dot"></i></div>
205:           <strong id="tuto-step1-title">Zoomer & Déplacer</strong>
206:           <small id="tuto-step1-desc">Pincez avec 2 doigts ou utilisez la molette de la souris pour naviguer sur la carte.</small>
207:           <span id="tuto-step2-desc">Cliquez sur une région ou un département pour enregistrer votre niveau d'exploration.</span>
208:     legend: ["Habité", "Séjourné", "Visité", "Escale", "Passé", "Jamais"],
209:         <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-maximize"></i></span>
210:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} régions</strong></span></div>`,
211:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} pays</strong></span></div>`,
212:         <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-location-dot"></i></span>
213: const COLORS = ["#f3f4f6", "#bfdbfe", "#a7f3d0", "#fef08a", "#fed7aa", "#fda4af"];
214:       desc: "Cette application est <strong>100% gratuite</strong> !<br>Un simple abonnement sur Instagram m'aide<br>énormément à continuer cette aventure.<br>🏍️🇯🇵 <strong>Merci pour ton soutien !</strong>",
215:         <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-location-dot"></i></span>
216:   "09": "Burgos", "10": "Cáceres", "11": "Cádiz", "12": "Castelló/Castellón",
217:       <div class="opt-btn" style="cursor: default; pointer-events: none;">
218:         <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-location-dot"></i></span>
219:   "21": "Huelva", "22": "Huesca", "23": "Jaén", "24": "León",
220:       <div class="opt-btn" style="cursor: default; pointer-events: none;">
221:         <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-share-nodes"></i></span>
222:   "33": "Asturias", "34": "Palencia", "35": "Las Palmas", "36": "Pontevedra",
223:   "37": "Salamanca", "38": "Santa Cruz De Tenerife", "39": "Cantabria", "40": "Segovia",
224:         <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-share-nodes"></i></span>
225:   "45": "Toledo", "46": "València/Valencia", "47": "Valladolid", "48": "Bizkaia/Vizcaya",
226:       <div class="opt-btn" style="cursor: default; pointer-events: none;">
227:         <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-share-nodes"></i></span>
228: let franceDomTomData = null;
229:           <strong id="tuto-step3-title">Exporter & Partager</strong>
230:       <button id="btn-tuto-close" style="width: 100%; border: 1.5px solid #111111; background: #111111; color: #ffffff; border-radius: 0; padding: 14px; font-size: 0.9rem; font-weight: 900; text-transform: uppercase; font-family: var(--font); cursor: pointer; transition: all 0.15s ease;">C'est parti !</button>
231:   "AP": "Ascoli Piceno", "AQ": "L'Aquila", "AR": "Arezzo", "AT": "Asti", "AV": "Avellino",
232:           <small id="tuto-step3-desc">Cliquez sur le bouton d'export pour télécharger une superbe carte prête pour vos réseaux sociaux !</small>
233:       <button id="btn-tuto-close" style="width: 100%; border: 1.5px solid #111111; background: #111111; color: #ffffff; border-radius: 0; padding: 14px; font-size: 0.9rem; font-weight: 900; text-transform: uppercase; font-family: var(--font); cursor: pointer; transition: all 0.15s ease;">C'est parti !</button>
234:   "392": { en: "Japan", fr: "Japon", ja: "日本", es: "Japón", ko: "일본", zh: "日本", hi: "जापान" },
235:   "380": { en: "Italy", fr: "Italie", ja: "イタリア", es: "Italia", ko: "이탈리아", zh: "イタリア", hi: "इटली" },
236:       <button id="btn-tuto-close" style="width: 100%; border: 1.5px solid #111111; background: #111111; color: #ffffff; border-radius: 0; padding: 14px; font-size: 0.9rem; font-weight: 900; text-transform: uppercase; font-family: var(--font); cursor: pointer; transition: all 0.15s ease;">C'est parti !</button>
237:       <a href="https://www.instagram.com/french_rider_in_japan/" target="_blank" rel="noopener" style="text-decoration: none; display: block; margin-top: 12px; background: #FFDE00; color: #111111; border: 1.5px solid #111111; padding: 10px 12px; font-size: 0.8rem; font-weight: 700; text-align: center; font-family: var(--font); line-height: 1.3; border-radius: 0; transition: transform 0.15s ease;">
238:       <button id="btn-tuto-close" style="width: 100%; border: 1.5px solid #111111; background: #111111; color: #ffffff; border-radius: 0; padding: 14px; font-size: 0.9rem; font-weight: 900; text-transform: uppercase; font-family: var(--font); cursor: pointer; transition: all 0.15s ease;">C'est parti !</button>
239:   "826": { en: "United Kingdom", fr: "Royaume-Uni", ja: "イギリス", es: "Reino Unido", ko: "영국", zh: "英国", hi: "यूके" },
240:     <a href="https://www.instagram.com/french_rider_in_japan/" target="_blank" rel="noopener" style="text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 8px; background: #FFDE00; color: #111111; padding: 14px 16px; font-size: 0.8rem; font-weight: 800; text-align: center; font-family: var(--font); line-height: 1.3; transition: background 0.15s ease; width: 100%; cursor: pointer; border-top: 3px solid #111111;" onmouseover="this.style.background='#f0cf00'" onmouseout="this.style.background='#FFDE00'">
241:   <a href="https://www.instagram.com/french_rider_in_japan/" target="_blank" rel="noopener" style="text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 8px; background: #FFDE00; color: #111111; padding: 14px 16px; font-size: 0.8rem; font-weight: 800; text-align: center; font-family: var(--font); line-height: 1.3; transition: background 0.15s ease; width: 100%; max-width: 420px; cursor: pointer; margin-top: 3px;" onmouseover="this.style.background='#f0cf00'" onmouseout="this.style.background='#FFDE00'">
242:   "356": { en: "India", fr: "Inde", ja: "インド", es: "India", ko: "인도", zh: "印度", hi: "भारत" },
243:   "076": { en: "Brazil", fr: "Brésil", ja: "Brésil", es: "Brasil", ko: "브라질", zh: "巴西", hi: "ब्राजील" },
244:   "484": { en: "Mexico", fr: "Mexique", ja: "メキシコ", es: "México", ko: "México", zh: "墨西哥", hi: "मेक्सिको" },
245:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} países</strong></span></div>`,
246:   "410": { en: "South Korea", fr: "Corée du Sud", ja: "韓国", es: "Corea del Sur", ko: "대한민국", zh: "韩国", hi: "दक्षिण कोरिया" },
247:   "410": { en: "South Korea", fr: "Corée du Sud", ja: "韓国", es: "Corea del Sur", ko: "대한민국", zh: "韩国", hi: "दक्षिण कोरिया" },
248:       desc: "Esta aplicación es <strong>100% gratuita</strong>.<br>Un simple seguimiento en Instagram me ayuda<br>muchísimo a continuar esta aventura.<br>🏍️🇯🇵 <strong>¡Gracias por tu apoyo!</strong>",
249:   "040": { en: "Austria", fr: "Autriche", ja: "オーストリア", es: "Austria", ko: "오스트리아", zh: "奥地利", hi: "ऑस्ट्रिया" },
250:   "528": { en: "Netherlands", fr: "Pays-Bas", ja: "オランダ", es: "Países Bajos", ko: "네덜란드", zh: "荷兰", hi: "नीदरलैंड" },
251:   "528": { en: "Netherlands", fr: "Pays-Bas", ja: "オランダ", es: "Países Bajos", ko: "네덜란드", zh: "荷兰", hi: "नीदरलैंड" },
252:   "702": { en: "Singapore", fr: "Singapour", ja: "シンガポール", es: "Singapur", ko: "싱가포르", zh: "新加坡", hi: "सिंगापुर" },
253:   "764": { en: "Thailand", fr: "Thaïlande", ja: "タイ", es: "Tailandia", ko: "태국", zh: "ไทย", hi: "थाईलैंड" },
254:   "704": { en: "Vietnam", fr: "Viêt Nam", ja: "ベトナム", es: "Vietnam", ko: "베트남", zh: "越南", hi: "वियतनाम" },
255:   "360": { en: "Indonesia", fr: "Indonésie", ja: "インドネシア", es: "Indonesia", ko: "인도네시아", zh: "印度尼西亚", hi: "इंडोनेशिया" },
256:   "554": { en: "New Zealand", fr: "Nouvelle-Zélande", ja: "ニュージーランド", es: "Nueva Zelanda", ko: "뉴질랜드", zh: "新西兰", hi: "न्यूजीलैंड" }
257:   "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia", "FL": "Florida",
258:   "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana",
259:   "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine",
260:   "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
261:   "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire",
262:   "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota",
263:   "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island",
264:   "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
265:   "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin",
266:   { code: '48', x: 198, y: 45, w: 38, h: 38 },  // Bizkaia/Vizcaya
267:   { code: '20', x: 238, y: 45, w: 38, h: 38 },  // Gipuzkoa/Guipúzcoa
268:   { code: '01', x: 238, y: 85, w: 38, h: 38 },  // Araba/Álava
269:   { code: '10', x: 78, y: 205, w: 38, h: 38 },  // Cáceres
270:   "11": "Beijing", "12": "Tianjin", "13": "Hebei", "14": "Shanxi", "15": "Inner Mongolia",
271:   "21": "Liaoning", "22": "Jilin", "23": "Heilongjiang", "31": "Shanghai", "32": "Jiangsu",
272:   "33": "Zhejiang", "34": "Anhui", "35": "Fujian", "36": "Jiangxi", "37": "Shandong",
273:   "41": "Henan", "42": "Hubei", "43": "Hunan", "44": "Guangdong", "45": "Guangxi",
274:   "46": "Hainan", "50": "Chongqing", "51": "Sichuan", "52": "Guizhou", "53": "Yunnan",
275:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} regions</strong></span></div>`,
276:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} countries</strong></span></div>`,
277:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} departments</strong></span></div>`,
278: 278:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 지역</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
279: 279:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개국</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
280: 280:   { code: '48', x: 198, y: 45, w: 38, h: 38 },  // Bizkaia/Vizcaya
281: 281:   "21": "LN", "22": "JL", "23": "HL", "31": "SH", "32": "JS",
282: 282:       desc: "이 앱은 <strong>100% 무료</strong>입니다!<br>인스타그램 팔로우 하나로<br>이 모험을 이어갈 수 있습니다.<br>🏍️🇯🇵 <strong>응원 감사합니다!</strong>",
283: 283:       follow: `<i class="fa-brands fa-instagram"></i> @french_rider_in_japan 팔로우`,
284: 284:   "46": "HI", "50": "CQ", "51": "SC", "52": "GZ", "53": "YN",
285: 285:   "54": "XZ", "61": "SN", "62": "GS", "63": "QH", "64": "NX",
286: 286:   "65": "XJ", "71": "TW", "81": "HK", "82": "MC"
287: 287: };
288: 288: 
289: 289: const PROVINCES_KR = {
290:   "1": "Busan", "2": "Chungcheongbuk-do", "3": "Chungcheongnam-do", "4": "Daegu", "5": "Daejeon",
291:   "6": "Gangwon-do", "7": "Gwangju", "8": "Gyeonggi-do", "9": "Gyeongsangbuk-do", "10": "Gyeongsangnam-do",
292:   "11": "Incheon", "12": "Jeju", "13": "Jeollabuk-do", "14": "Jeollanam-do", "15": "Seoul",
293:   { code: '13', x: 198, y: 245, w: 38, h: 38 },  // Ciudad Real
294:       world: "🌍 World", fr: "🇫🇷 France", it: "🇮🇹 Italy", jp: "🇯🇵 Japan", us: "🇺🇸 USA",
295:   { code: '33', x: 118, y: 45, w: 38, h: 38 },  // Asturias
296:       world: "🌍 World", fr: "🇫🇷 France", it: "🇮🇹 Italy", jp: "🇯🇵 Japan", us: "🇺🇸 USA",
297:   { code: '39', x: 158, y: 45, w: 38, h: 38 },  // Cantabria
298:   { code: '34', x: 158, y: 85, w: 38, h: 38 },  // Palencia
299:   "11": "IC", "12": "JJ", "13": "JB", "14": "JN", "15": "SU",
300:   { code: '48', x: 198, y: 45, w: 38, h: 38 },  // Bizkaia/Vizcaya
301:   { code: '20', x: 238, y: 45, w: 38, h: 38 },  // Gipuzkoa/Guipúzcoa
302:   { code: '01', x: 238, y: 85, w: 38, h: 38 },  // Araba/Álava
303:   { code: '18', x: 238, y: 285, w: 38, h: 38 },  // Granada
304:   // Row 1 - North (Galicia, Asturias, Cantabria, Basque, Navarra)
305:       step1Desc: "Pinch with 2 fingers or use mouse scroll to navigate the map.",
306:   { code: '29', x: 158, y: 325, w: 38, h: 38 },  // Málaga
307:       step2Desc: "Click on a region or department to record your exploration level.",
308:   { code: '07', x: 398, y: 205, w: 38, h: 38 },  // Illes Balears
309:       step3Desc: "Click the export button to download a beautiful map ready for social networks!",
310:   { code: '38', x: 78, y: 405, w: 38, h: 38 },  // S.C. Tenerife (Canarias)
311:       step3Desc: "Click the export button to download a beautiful map ready for social networks!",
312:   { code: '51', x: 158, y: 365, w: 38, h: 38 },  // Ceuta
313:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 地域</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
314:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} ヶ国</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
315:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
316:     subtitleFrance: "フランスのどこを旅しましたか？",
317:     subtitleFrance: "フランス의 어디를 여행하셨나요? France?",
318:       desc: "このアプリは<strong>100%無料</strong>です！<br>Instagramをフォローして応援していただけると<br>旅の励みになります。よろしくお願いします！🏍️🇯🇵",
319:       follow: `<i class="fa-brands fa-instagram"></i> @french_rider_in_japan をフォロー`,
320:     legend: ["住んだ", "泊まった", "訪れた", "立ち寄り", "通過", "未踏"],
321:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 地域</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
322:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} ヶ国</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
323:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${name
324:       subtitle: "訪問レベルを選択してください",
325:       l5: { main: "Lived there", sub: "住んだことがある (+5 pts)" },
326:       l4: { main: "Stayed there", sub: "1泊以上した (+4 pts)" },
327:       l3: { main: "Visited there", sub: "日帰り旅行 (+3 pts)" },
328:       l2: { main: "Alighted there", sub: "乗り換え / 立ち寄り (+2 pts)" },
329:       l1: { main: "Passed there", sub: "通過しただけ (+1 pt)" },
330:   "040": { en: "Austria", fr: "Autriche", ja: "オーストリア", es: "Austria", ko: "오스트리아", zh: "奥地利", hi: "ऑस्ट्रिया" },
331:   "056": { en: "Belgium", fr: "Belgique", ja: "ベルギー", es: "Bélgica", ko: "벨기에", zh: "比利时", hi: "बेल्जियम" },
332:   "528": { en: "Netherlands", fr: "Pays-Bas", ja: "オランダ", es: "Países Bajos", ko: "네덜란드", zh: "荷兰", hi: "नीदरलैंड" },
333:   "702": { en: "Singapore", fr: "Singapour", ja: "シンガポール", es: "Singapur", ko: "싱가포르", zh: "新加坡", hi: "सिंगापुर" },
334:   "764": { en: "Thailand", fr: "Thaïlande", ja: "タイ", es: "Tailandia", ko: "태국", zh: "ไทย", hi: "थाईलैंड" },
335:   "704": { en: "Vietnam", fr: "Viêt Nam", ja: "ベトナム", es: "Vietnam", ko: "베트남", zh: "越南", hi: "वियतनाम" },
336:   "360": { en: "Indonesia", fr: "Indonésie", ja: "インドネシア", es: "Indonesia", ko: "인도네시아", zh: "印度尼西亚", hi: "इंडोनेशिया" },
337:   "554": { en: "New Zealand", fr: "Nouvelle-Zélande", ja: "ニュージーランド", es: "Nueva Zelanda", ko: "뉴질랜드", zh: "新西兰", hi: "न्यूजीलैंड" }
338:       l0: { main: "Never been", sub: "行ったことがない (0 pt)" }
339: const COUNTRY_NAMES = {
340:   "242": { en: "Fiji", fr: "Fidji", ja: "フィジー", es: "Fiyi", ko: "피지", zh: "斐济", hi: "Fiji" },
341:   "834": { en: "Tanzania", fr: "Tanzanie", ja: "タンザニア", es: "Tanzania", ko: "탄자니아", zh: "坦桑尼亚", hi: "Tanzania" },
342:   "732": { en: "Western Sahara", fr: "Sahara Occidental", ja: "西サハラ", es: "Sahara Occidental", ko: "서사하라", zh: "西撒哈拉", hi: "W. Sahara" },
343:   "834": { en: "Tanzania", fr: "Tanzanie", ja: "タンザニア", es: "Tanzania", ko: "탄자니아", zh: "坦桑尼亚", hi: "Tanzania" },
344:   "840": { en: "United States", fr: "États-Unis", ja: "アメリカ合衆国", es: "Estados Unidos", ko: "미국", zh: "美国", hi: "United States of America" },
345:   "398": { en: "Kazakhstan", fr: "Kazakhstan", ja: "カザフスタン", es: "Kazajistán", ko: "카자흐스탄", zh: "哈萨克斯坦", hi: "Kazakhstan" },
346:   "840": { en: "United States", fr: "États-Unis", ja: "アメリカ合衆国", es: "Estados Unidos", ko: "미국", zh: "美国", hi: "United States of America" },
347:   "598": { en: "Papua New Guinea", fr: "Papouasie-Nouvelle-Guinée", ja: "パプアニューギニア", es: "Papúa Nueva Guinea", ko: "파푸아뉴기니", zh: "巴布亚新几内亚", hi: "Papua New Guinea" },
348:   "860": { en: "Uzbekistan", fr: "Ouzbékistan", ja: "ウズベキスタン", es: "Uzbekistán", ko: "우즈베키스탄", zh: "乌兹别克斯坦", hi: "Uzbekistan" },
349:   "598": { en: "Papua New Guinea", fr: "Papouasie-Nouvelle-Guinée", ja: "パプアニューギニア", es: "Papúa Nueva Guinea", ko: "파푸아뉴기니", zh: "巴布亚新几内亚", hi: "Papua New Guinea" },
350:   "360": { en: "Indonesia", fr: "Indonésie", ja: "インドネシア", es: "Indonesia", ko: "인도네시아", zh: "印度尼西亚", hi: "Indonesia" },
351:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} pays</strong></span></div>`,
352:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} départements</strong></span></div>`,
353:       step1Desc: "2本の指でピンチするか、マウスホイールを使用してマップをナビゲートします。",
354:     subtitle: "À quel point as-tu exploré le Japon ?",
355:       desc: "Cette application est <strong>100% gratuite</strong> !<br>Un simple abonnement sur Instagram m'aide<br>énormément à continuer cette aventure.<br>🏍️🇯🇵 <strong>Merci pour ton soutien !</strong>",
356:   "242": { en: "Fiji", fr: "Fidji", ja: "フィジー", es: "Fiyi", ko: "피지", zh: "斐济", hi: "Fiji" },
357:   "834": { en: "Tanzania", fr: "Tanzanie", ja: "タンザニア", es: "Tanzania", ko: "탄자니아", zh: "坦桑尼亚", hi: "Tanzania" },
358:   "732": { en: "Western Sahara", fr: "Sahara Occidental", ja: "西サハラ", es: "Sahara Occidental", ko: "서사하라", zh: "西撒哈拉", hi: "W. Sahara" },
359:   "124": { en: "Canada", fr: "Canada", ja: "カナダ", es: "Canadá", ko: "캐나다", zh: "加拿大", hi: "कनाडा" },
360:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} régions</strong></span></div>`,
361:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} pays</strong></span></div>`,
362:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} départements</strong></span></div>`,
363:       l4: { main: "Stayed there", sub: "Séjour ≥ 1 nuit (+4 pts)" },
364:     subtitleFrance: "Combien de départements de France as-tu exploré ?",
365:       desc: "Cette application est <strong>100% gratuite</strong> !<br>Un simple abonnement sur Instagram m'aide<br>énormément à continuer cette aventure.<br>🏍️🇯🇵 <strong>Merci pour ton soutien !</strong>",
366:       world: "🌍 विश्व", fr: "🇫🇷 फ़्रांस", it: "🇮🇹 इटली", jp: "🇯🇵 जापान", us: "🇺🇸 अमेरिका",
367:       l0: { main: "Never been", sub: "Jamais allé (0 pt)" }
368: let japanData = null;
369: let worldData = null; // Cache for parsed topojson data
370:     tapName: "👉 अपना नाम लिखें",
371: let franceDomTomData = null;
372:     bgWatermarkWorld: "दुनिया"
373:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} départements</strong></span></div>`,
374: let usaStatesData = null;
375:       title: "Exporter ta carte !",
376:       desc: "Cette application est <strong>100% gratuite</strong> !<br>Un simple abonnement sur Instagram m'aide<br>énormément à continuer cette aventure.<br>🏍️🇯🇵 <strong>Merci pour ton soutien !</strong>",
377:       follow: `<i class="fa-brands fa-instagram"></i> Suivre @french_rider_in_japan`,
378:   "242": { en: "Fiji", fr: "Fidji", ja: "フィジー", es: "Fiyi", ko: "피지", zh: "斐济", hi: "Fiji" },
379:   "834": { en: "Tanzania", fr: "Tanzanie", ja: "タンザニア", es: "Tanzania", ko: "탄자니아", zh: "坦桑尼亚", hi: "Tanzania" },
380:   "732": { en: "Western Sahara", fr: "Sahara Occidental", ja: "西サハラ", es: "Sahara Occidental", ko: "서사하라", zh: "西撒哈拉", hi: "W. Sahara" },
381:       l4: { main: "Stayed there", sub: "Séjour ≥ 1 nuit (+4 pts)" },
382:       l3: { main: "Visited there", sub: "Visite de journée (+3 pts)" },
383:     subtitle.textContent = state.currentMap === "jp" ? t.subtitle : t.subtitleWorld;
384:       l1: { main: "Passed there", sub: "Simple passage (+1 pt)" },
385:     legend: ["Vivido", "Alojado", "Visitado", "Escala", "Pasado", "Nunca"],
386: #modal-overlay.hidden, #export-overlay.hidden, #country-overlay.hidden, #lang-overlay.hidden {
387:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} regiones</strong></span></div>`,
388:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} países</strong></span></div>`,
389:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weigh
390:       avail: "Disponible", soon: "Bientôt"
391:       world: "🌍 Monde", fr: "🇫🇷 France", it: "🇮🇹 Italie", jp: "🇯🇵 Japon", us: "🇺🇸 USA",
392:       world: "🌍 Monde", fr: "🇫🇷 France", it: "🇮🇹 Italie", jp: "🇯🇵 Japon", us: "🇺🇸 USA",
393:   const exportBtn = document.getElementById("btn-export");
394:   "242": { en: "Fiji", fr: "Fidji", ja: "フィジー", es: "Fiyi", ko: "피지", zh: "斐济", hi: "Fiji" },
395:   "834": { en: "Tanzania", fr: "Tanzanie", ja: "タンザニア", es: "Tanzania", ko: "탄자니아", zh: "坦桑尼亚", hi: "Tanzania" },
396:   "732": { en: "Western Sahara", fr: "Sahara Occidental", ja: "西サハラ", es: "Sahara Occidental", ko: "서사하라", zh: "西撒哈拉", hi: "W. Sahara" },
397:   "834": { en: "Tanzania", fr: "Tanzanie", ja: "タンザニア", es: "Tanzania", ko: "탄자니아", zh: "坦桑尼亚", hi: "Tanzania" },
398:   "840": { en: "United States", fr: "États-Unis", ja: "アメリカ合衆国", es: "Estados Unidos", ko: "미국", zh: "美国", hi: "United States of America" },
399:   "124": { en: "Canada", fr: "Canada", ja: "カナダ", es: "Canadá", ko: "캐나다", zh: "加拿大", hi: "कनाडा" },
400:   "840": { en: "United States", fr: "États-Unis", ja: "アメリカ合衆国", es: "Estados Unidos", ko: "미국", zh: "美国", hi: "United States of America" },
401:   "398": { en: "Kazakhstan", fr: "Kazakhstan", ja: "カザフスタン", es: "Kazajistán", ko: "카자흐스탄", zh: "哈萨克斯
402:       step2Desc: "Cliquez sur une région ou un département pour enregistrer votre niveau d'exploration.",
403:     subtitleFrance: "¿Cuánto de Francia has explorado?",
404:       step3Desc: "Cliquez sur le bouton d'export pour télécharger une superbe carte prête pour vos réseaux sociaux !",
405:     legend: ["Vivido", "Alojado", "Visitado", "Escala", "Pasado", "Nunca"],
406:       step2Desc: "Cliquez sur une région ou un département pour enregistrer votre niveau d'exploration.",
407:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} regiones</strong></span></div>`,
408:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} países</strong></span></div>`,
409:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} departamentos</strong></span></div>`,
410:     subtitleWorld: "¿Cuánto del Mundo has explorado?",
411:     legItems[4].innerHTML = `<span class="leg-dot" data-l="1"></span>${t.legend[4]}`;
412:       desc: "Esta aplicación es <strong>100% gratuita</strong>.<br>Un simple seguimiento en Instagram me ayuda<br>muchísimo a continuar esta aventura.<br>🏍️🇯🇵 <strong>¡Gracias por tu apoyo!</strong>",
413:       follow: `<i class="fa-brands fa-instagram"></i> Seguir @french_rider_in_japan`,
414:     subtitleWorld: "¿Cuánto del Mundo has explorado?",
415:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} regiones</strong></span></div>`,
416:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} países</strong></span></div>`,
417:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} departamentos</strong></span></div>`,
418:   const desc = document.getElementById("export-desc");
419:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} regiones</strong></span></div>`,
420:       desc: "Esta aplicación es <strong>100% gratuita</strong>.<br>Un simple seguimiento en Instagram me ayuda<br>muchísimo a continuar esta aventura.<br>🏍️🇯🇵 <strong>¡Gracias por tu apoyo!</strong>",
421:   "710": { en: "South Africa", fr: "Afrique du Sud", ja: "南アフリカ", es: "Sudáfrica", ko: "남아프리카 공화국", zh: "南非", hi: "South Africa" },
422:   "426": { en: "Lesotho", fr: "Lesotho", ja: "レソト", es: "Lesotho", ko: "레소토", zh: "莱索托", hi: "Lesotho" },
423:   "834": { en: "Tanzania", fr: "Tanzanie", ja: "タンザニア", es: "Tanzania", ko: "탄자니아", zh: "坦桑尼亚", hi: "Tanzania" },
424:   "732": { en: "Western Sahara", fr: "Sahara Occidental", ja: "西サハラ", es: "Sahara Occidental", ko: "서사하라", zh: "西撒哈拉", hi: "W. Sahara" },
425:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개국</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
426:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 부서</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
427:   "398": { en: "Kazakhstan", fr: "Kazakhstan", ja: "カザフスタン", es: "Kazajistán", ko: "카자흐스탄", zh: "哈萨克斯坦", hi: "Kazakhstan" },
428:   "860": { en: "Uzbekistan", fr: "Ouzbékistan", ja: "ウズベキスタン", es: "Uzbekistán", ko: "우즈베키스탄", zh: "乌兹别克斯坦", hi: "Uzbekistan" },
429:       desc: "이 앱은 <strong>100% 무료</strong>입니다!<br>인스타그램 팔로우 하나로<br>이 모험을 이어갈 수 있습니다.<br>🏍️🇯🇵 <strong>응원 감사합니다!</strong>",
430:   "188": { en: "Costa Rica", fr: "Costa Rica", ja: "コスタリカ", es: "Costa Rica", ko: "코스타리카", zh: "哥斯达黎加", hi: "Costa Rica" },
431:       l1: { main: "Passed there", sub: "Solo de paso (+1 pt)" },
432:       l0: { main: "Never been", sub: "Nunca he ido (0 pt)" }
433:   [5,4,3,2,1,0].forEach(lvl => {
434:     const btn = document.querySelector(`#modal-opts .opt-btn[data-level="${lvl}"]`);
435:   padding: 0 16px; /* Inner padding for the subtitle */
436:       world: "🌍 Mundo", fr: "🇫🇷 Francia", it: "🇮🇹 Italia", jp: "🇯🇵 Japón", us: "🇺🇸 EE.UU.",
437:       l4: { main: "Stayed there", sub: "1박 이상 숙박 (+4 pts)" },
438:         div.innerHTML = `<strong>${t.levelModal['l'+lvl].main}</strong><small>${t.levelModal['l'+lvl].sub}</small>`;
439:       l2: { main: "Alighted there", sub: "경유 / 환승 (+2 pts)" },
440:       l1: { main: "Passed there", sub: "지ना간 적 있음 (+1 pt)" },
441:   flex-direction: column;
442:   gap: 0; /* Remove space to fuse buttons together */
443:     bgWatermarkFrance: "FRANCIA"
444:   const countryTitle = document.querySelector("#country-modal .modal-header h3");
445:   if (countryTitle) countryTitle.textContent = t.countryModal.title;
446:     subtitle: "일본을 얼마나 탐험했나요?",
447:   const cOpts = document.querySelectorAll("#country-modal .opt-btn");
448:     subtitleFrance: "프랑스의 어디를 여행하셨나요?",
449:     cOpts[0].querySelector("div").innerHTML = `<strong>${t.countryModal.world}</strong><small>${t.countryModal.avail}</small>`;
450:     cOpts[1].querySelector("div").innerHTML = `<strong>${t.countryModal.fr}</strong><small>${t.countryModal.soon}</small>`;
451:     cOpts[2].querySelector("div").innerHTML = `<strong>${t.countryModal.it}</strong><small>${t.countryModal.soon}</small>`;
452:     cOpts[3].querySelector("div").innerHTML = `<strong>${t.countryModal.jp}</strong><small>${t.countryModal.avail}</small>`;
453:     cOpts[2].querySelector("div").innerHTML = `<strong>${t.countryModal.it}</strong><small>${t.countryModal.soon}</small>`;
454:     cOpts[3].querySelector("div").innerHTML = `<strong>${t.countryModal.jp}</strong><small>${t.countryModal.avail}</small>`;
455:     cOpts[4].querySelector("div").innerHTML = `<strong>${t.countryModal.us}</strong><small>${t.countryModal.soon}</small>`;
456:     exportBtn: '<i class="fa fa-download"></i> Exporter',
457:     legend: ["Habité", "Séjourné", "Visité", "Escale", "Passé", "Jamais"],
458:   // Country selector button text
459:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} régions</strong></span></div>`,
460:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} pays</strong></span></div>`,
461:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} départements</strong></span></div>`,
462:     exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
463:   background: #f9fafb;
464:       btnCountry.innerHTML = `🌍 ${t.countryModal.world} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
465:       desc: "Cette application est <strong>100% gratuite</strong> !<br>Un simple abonnement sur Instagram m'aide<br>énormément à continuer cette aventure.<br>🏍️🇯🇵 <strong>Merci pour ton soutien !</strong>",
466:       follow: `<i class="fa-brands fa-instagram"></i> Suivre @french_rider_in_japan`,
467:   const bgWatermark = document.getElementById("bg-watermark");
468:       dlShared: "Je me suis abonné ! HD 🎉"
469:     const text = state.currentMap === "jp" ? (t.bgWatermark || "JAPAN") : (t.bgWatermarkWorld || "WORLD");
470:     bgWatermark.innerHTML = Array(5).fill(`<div>${text}</div>`).join("");
471:     const text = state.currentMap === "jp" ? (t.bgWatermark || "JAPAN") : (t.bgWatermarkWorld || "WORLD");
472:     bgWatermark.innerHTML = Array(5).fill(`<div>${text}</div>`).join("");
473:       l4: { main: "Séjourné", sub: "Séjour ≥ 1 nuit (+4 pts)" },
474:       l3: { main: "Visité", sub: "Visite de journée (+3 pts)" },
475:       l2: { main: "Escale", sub: "Arrêt / Escale (+2 pts)" },
476:     cOpts[0].querySelector("div").innerHTML = `<strong>${t.countryModal.world}</strong><small>${t.countryModal.soon}</small>`;
477:       l0: { main: "Jamais", sub: "Jamais allé (0 pt)" }
478: // ── State Management ─────────────────────────────────────────
479: // ── State Management ─────────────────────────────────────────
480:     cOpts[1].querySelector("div").innerHTML = `<strong>${t.countryModal.fr}</strong><small>${t.countryModal.soon}</small>`;
481:     cOpts[2].querySelector("div").innerHTML = `<strong>${t.countryModal.it}</strong><small>${t.countryModal.soon}</small>`;
482:     cOpts[3].querySelector("div").innerHTML = `<strong>${t.countryModal.jp}</strong><small>${t.countryModal.avail}</small>`;
483:     cOpts[4].querySelector("div").innerHTML = `<strong>${t.countryModal.us}</strong><small>${t.countryModal.soon}</small>`;
484:     state.currentMap = s.currentMap || "jp";
485:     state.jpLevels = s.jpLevels || s.levels || {};
486:     state.jpLevels = s.jpLevels || s.levels || {};
487:     state.levels = state.currentMap === "jp" ? state.jpLevels : state.worldLevels;
488:     state.levels = state.currentMap === "jp" ? state.jpLevels : state.worldLevels;
489:     if (state.currentMap === "jp") {
490:       btnCountry.innerHTML = `${t.countryModal.jp} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
491:     Object.keys(NAMES_EN).forEach(c => {
492:       btnCountry.innerHTML = `${t.countryModal.world} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
493:       if (state.levels[c] == null) state.levels[c] = 0;
494:     bgWatermarkWorld: "세계",
495:     bgWatermarkFrance: "프랑스",
496:   // Select active country button
497:   const bgWatermark = document.getElementById("bg-watermark");
498:     if (btn.dataset.val === state.currentMap) {
499:     const text = state.currentMap === "jp" ? (t.bgWatermark || "JAPAN") : (t.bgWatermarkWorld || "WORLD");
500:     bgWatermark.innerHTML = Array(5).fill(`<div>${text}</div>`).join("");
501:     subtitleFrance: "How much of France have you explored?",
502:     subtitleSpain: "How much of Spain have you explored?",
503:       step3Desc: "내보내기 버튼을 클릭하여 SNS에 공유할 멋진 지도를 다운로드하세요!",
504:     legend: ["Lived", "Stayed", "Visited", "Alighted", "Passed", "Never"],
505:   const val = state.lang;
506:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} regions</strong></span></div>`,
507:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} countries</strong></span></div>`,
508:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} departments</strong></span></div>`,
509:     exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
510:     if (s.username) state.username = s.username;
511:     if (s.lang) state.lang = s.lang;
512:     state.currentMap = s.currentMap || "jp";
513:     if (state.currentMap === "world") state.currentMap = "jp";
514:   const btnLang = document.getElementById("btn-lang-select");
515:   if (btnLang) btnLang.innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
516:     state.levels = state.currentMap === "jp" ? state.jpLevels : state.worldLevels;
517:   document.querySelectorAll(".lang-btn").forEach(b => {
518:     if(b.dataset.val === val) b.classList.add("selected");
519:     else b.classList.remove("selected");
520:     Object.keys(NAMES_EN).forEach(c => {
521:       if (state.levels[c] == null) state.levels[c] = 0;
522:   updateUITranslations();
523:   text-transform: uppercase;
524:   letter-spacing: -0.8px;
525:   "070": { en: "Bosnia and Herzegovina", fr: "Bosnie-Herzégovine", ja: "ボスニア・ヘルツェゴビナ", es: "Bosnia y Herzegovina", ko: "보스니아 헤르체고비나", zh: "波斯尼亚和黑塞哥维那", hi: "Bosnia and Herz." },
526:   "807": { en: "North Macedonia", fr: "Macédoine du Nord", ja: "北マケドニア ", es: "Macedonia del Norte", ko: "북마케도니아", zh: "北馬其頓", hi: "Macedonia" },
527:   "780": { en: "Trinidad and Tobago", fr: "Trinité-et-Tobago", ja: "トリニダード・トバゴ", es: "Trinidad y Tobago", ko: "트리니다드 토바고", zh: "特立尼达和多巴哥", hi: "Trinidad and Tobago" },
528:   "728": { en: "South Sudan", fr: "Soudan du Sud", ja: "南スーダン", es: "Sudán del Sur", ko: "남수단", zh: "南苏丹", hi: "S. Sudan" }
529:   "780": { en: "Trinidad and Tobago", fr: "Trinité-et-Tobago", ja: "トリニダード・トバゴ", es: "Trinidad y Tobago", ko: "트리니다드 토바고", zh: "特立尼达和多巴哥", hi: "Trinidad and Tobago" },
530:   "728": { en: "South Sudan", fr: "Soudan du Sud", ja: "南スーダン", es: "Sudán del Sur", ko: "남수단", zh: "南苏丹", hi: "S. Sudan" }
531:   const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];
532:   const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];
533:     legend: ["Lived", "Stayed", "Visited", "Alighted", "Passed", "Never"],
534:       follow: `<i class="fa-brands fa-instagram"></i> @french_rider_in_japan फ़ॉलो करें`,
535:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} regions</strong></span></div>`,
536:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} countries</strong></span></div>`,
537:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7;
538:   const total = Object.values(state.levels).reduce((a, b) => a + b, 0);
539:   document.getElementById("card-level").textContent = "Ride the world";
540:       l3: { main: "Visited there", sub: "दिन की यात्रा (+3 pts)" },
541:       l2: { main: "Alighted there", sub: "पड़ाव / रुकावट (+2 pts)" },
542:       l3: { main: "Visited there", sub: "दिन की यात्रा (+3 pts)" },
543:       l2: { main: "Alighted there", sub: "पड़ाव / रुकावट (+2 pts)" },
544:   if (btnLang) btnLang.innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
545:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
546:       const countries = countriesGeoJson.features.filter(d => d.id !== "010");
547:       world: "🌍 विश्व", fr: "🇫🇷 फ़्रांस", it: "🇮🇹 इटली", jp: "🇯🇵 जापान", us: "🇺🇸 अमेरिका",
548:     legend: ["Lived", "Stayed", "Visited", "Alighted", "Passed", "Never"],
549:       world: "🌍 विश्व", fr: "🇫🇷 फ़्रांस", it: "🇮🇹 इटली", jp: "🇯🇵 जापान", us: "🇺🇸 अमेरिका",
550:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color
551:   "008": { en: "Albania", fr: "Albanie", ja: "アルバニア", es: "Albania", ko: "알바니아", zh: "阿尔巴尼亚", hi: "Albania" },
552:       cardFlag.innerHTML = '<svg width="1em" height="1em" viewBox="0 0 100 100" style="vertical-align: middle; fill: #ffffff; display: inline-block; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.25));"><path d="M 65.7 50.5 L 66.6 47.5 L 74.2 48.8 L 70.8 55.4 L 65.7 50.5 Z M 61.2 21.9 L 56.4 26.1 L 55.8 16.6 L 62.3 17.0 L 61.2 21.9 Z M 54.9 45.0 L 60.9 47.9 L 59.0 52.6 L 50.5 48.9 L 54.9 45.0 Z M 71.2 68.0 L 79.0 63.9 L 77.5 71.4 L 71.7 72.1 L 71.2 68.0 Z M 74.8 59.7 L 79.8 63.7 L 71.3 68.0 L 69.6 65.9 L 75.3 62.1 L 74.8 59.7 Z M 78.6 66.5 L 83.7 69.0 L 78.9 74.3 L 78.6 66.5 Z M 63.8 58.8 L 65.6 57.7 L 66.3 61.4 L 64.9 67.3 L 62.5 67.3 L 60.0 63.1 L 63.8 58.8 
553:   "756": { en: "Switzerland", fr: "Suisse", ja: "スイス", es: "Suiza", ko: "스위스", zh: "瑞士", hi: "Switzerland" },
554:   "682": { en: "Saudi Arabia", fr: "Arabie Saoudite", ja: "サウジアラビア", es: "Arabia Saudí", ko: "사우디아라비아", zh: "沙特阿拉伯", hi: "Saudi Arabia" },
555:     exploredItaly: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
556:   "528": { en: "Netherlands", fr: "Pays-Bas", ja: "オランダ", es: "Países Bajos", ko: "네덜란드", zh: "荷兰", hi: "Netherlands" },
557:   "620": { en: "Portugal", fr: "Portugal", ja: "ポルトガル", es: "Portugal", ko: "포르투갈", zh: "葡萄牙", hi: "Portugal" },
558:       desc: "This application is <strong>100% free</strong>!<br>A simple follow on Instagram helps me<br>tremendously to continue this adventure.<br>🏍️🇯🇵 <strong>Thank you for your support!</strong>",
559:   "231": { en: "Ethiopia", fr: "Éthiopie", ja: "エチオピア", es: "Etiopía", ko: "에티오피아", zh: "埃塞俄比亚", hi: "Ethiopia" },
560:     exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
561:   "800": { en: "Uganda", fr: "Ouganda", ja: "ウガンダ
562:   const insetLabel = document.getElementById("inset-label");
563:       desc: "このアプリは<strong>100%無料</strong>です！<br>Instagramをフォローして応援していただけると<br>旅の励みになります。よろしくお願いします！🏍️🇯🇵",
564:       follow: `<i class="fa-brands fa-instagram"></i> @french_rider_in_japan をフォロー`,
565:   const total = Object.values(state.levels).reduce((a, b) => a + b, 0);
566:     insetLabel.style.display = state.currentMap === "jp" ? "block" : "none";
567:     insetLabel.style.display = state.currentMap === "jp" ? "block" : "none";
568:       l2: { main: "Alighted there", sub: "Stopover / Transit (+2 pts)" },
569:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
570:   const legItems = document.querySelectorAll("#card-legend .leg-item");
571:       desc: "这个应用是<strong>100%免费</strong>的！<br>在Instagram上关注我<br>将极大地帮助我继续这段冒险。<br>🏍️🇯🇵 <strong>感谢你的支持！</strong>",
572:     legItems[0].innerHTML = `<span class="leg-dot" data-l="5"></span>${t.legend[0]}`;
573:     legItems[1].innerHTML = `<span class="leg-dot" data-l="4"></span>${t.legend[1]}`;
574:       world: "🌍 World", fr: "🇫🇷 France", it: "🇮🇹 Italy", es: "🇪🇸 Spain", jp: "🇯🇵 Japan", us: "🇺🇸 USA",
575:     const nameHtml = `<span style="${isDefault ? 'border-bottom: 1px dashed rgba(255,255,255,0.7); opacity: 0.9;' : 'font-weight: 800; border-bottom: 1px solid rgba(255,255,255,0.5);'}">${displayName} <i class="fa-solid fa-pen" style="font-size: 0.7em;"></i></span>`;
576:       world: "🌍 World", fr: "🇫🇷 France", it: "🇮🇹 Italy", es: "🇪🇸 Spain", jp: "🇯🇵 Japan", us: "🇺🇸 USA",
577:     legItems[5].innerHTML = `<span class="leg-dot" data-l="0"></span>${t.legend[5]}`;
578:       cardFlag.innerHTML = '<svg width="1em" height="1em" viewBox="0 0 100 100" style="vertical-align: middle; fill: #ffffff; display: inline-block; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.25));"><path d="M 48.0 18.4 L 49.5 9.3 L 56.5 15.1 L 59.2 13.4 L 58.6 15.7 L 60.8 17.0 L 55.5 19.4 L 53.8 23.1 L 45.7 20.9 L 47.9 23.9 L 44.7 25.4 L 43.9 20.8 L 45.3 18.0 L 48.0 18.4 Z M 60.8 14.2 L 59.9 16.0 L 62.5 12.7 L 60.8 14.2 Z M 67.1 9.2 L 63.3 12.7 L 68.4 7.9 L 67.1 9.2 Z M 47.7 27.4 L 47.1 24.9 L 49.5 29.1 L 44.3 29.3 L 45.5 26.0 L 47.7 27.4 Z M 47.4 29.9 L 50.4 30.9 L 48.9 35.6 L 46.9 34.8 L 47.4 29.9 Z M 47.8 37.3 L 47.3 39.5 L 45.5 38.8 L 46.3 35.2 L 49.5 34.8 L 47.8 37.3 Z M 46.8 32.6 L 46.6 35.2 L 44.2 34.4 L 44.3 29.3 L 47.4 29.2 L 46.8 32.6 Z M 45.5 38.5 L 43.5 39.2 L 44.2 34.4 L 46.6 35.7 L 45.5 38.5 Z M 46.2 39.1 L 47.7 42.7 L 42.3 42.9 L 43.7 39.3 L 46.2 39.1 Z M 46.6 45.2 L 47.5 47.5 L 43.8 45.9 L 45.5 42.9 L 46.6 45.2 Z M 44.5 45.2 L 42.6 44.0 L 44.6 42.0 L 44.5 45.2 Z M 42.2 45.5 L 39.7 44.9 L 41.9 42.4 L 43.7 45.7 L 42.2 45.5 Z M 44.3 46.6 L 40.7 46.7 L 44.3 46.6 Z M 46.1 48.5 L 44.1 50.6 L 44.1 46.1 L 47.5 47.5 L 46.1 48.5 Z M 44.1 47.9 L 41.5 47.1 L 44.1 47.9 Z M 43.3 47.9 L 43.8 49.9 L 41.7 49.9 L 43.3 47.9 Z M 43.5 39.1 L 42.4 42.9 L 37.8 43.6 L 43.3 36.6 L 43.5 39.1 Z M 39.3 39.5 L 40.1 37.5 L 39.3 39.5 Z M 36.6 43.4 L
579:       world: "🌍 世界", fr: "🇫🇷 フランス", it: "🇮🇹 イタリア", es: "🇪🇸 スペイン", jp: "🇯🇵 日本", us: "🇺🇸 アメリカ",
580:       cardFlag.innerHTML = '<svg width="1em" height="1em" viewBox="0 0 100 100" style="vertical-align: middle; fill: #ffffff; display: inline-block; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.25));"><path d="M 48.0 18.4 L 49.5 9.3 L 56.5 15.1 L 59.2 13.4 L 58.6 15.7 L 60.8 17.0 L 55.5 19.4 L 53.8 23.1 L 45.7 20.9 L 47.9 23.9 L 44.7 25.4 L 43.9 20.8 L 45.3 18.0 L 48.0 18.4 Z M 60.8 14.2 L 59.9 16.0 L 62.5 12.7 L 60.8 14.2 Z M 67.1 9.2 L 63.3 12.7 L 68.4 7.9 L 67.1 9.2 Z M 47.7 27.4 L 47.1 24.9 L 49.5 29.1 L 44.3 29.3 L 45.5 26.0 L 47.7 27.4 Z M 47.4 29.9 L 50.4 30.9 L 48.9 35.6 L 46.9 34.8 L 47.4 29.9 Z M 47.8 37.3 L 47.3 39.5 L 45.5 38.8 L 46.3 35.2 L 49.5 34.8 L 47.8 37.3 Z M 46.8 32.6 L 46.6 35.2 L 44.2 34.4 L 44.3 29.3 L 47.4 29.2 L 46.8 32.6 Z M 45.5 38.5 L 43.5 39.2 L 44.2 34.4 L 46.6 35.7 L 45.5 38.5 Z M 46.2 39.1 L 47.7 42.7 L 42.3 42.9 L 43.7 39.3 L 46.2 39.1 Z M 46.6 45.2 L 47.5 47.5 L 43.8 45.9 L 45.5 42.9 L 46.6 45.2 Z M 44.5 45.2 L 42.6 44.0 L 44.6 42.0 L 44.5 45.2 Z M 42.2 45.5 L 39.7 44.9 L 41.9 42.4 L 43.7 45.7 L 42.2 45.5 Z M 44.3 46.6 L 40.7 46.7 L 44.3 46.6 Z M 46.1 48.5 L 44.1 50.6 L 44.1 46.1 L 47.5 47.5 L 46.1 48.5 Z M 44.1 47.9 L 41.5 47.1 L 44.1 47.9 Z M 43.3 47.9 L 43.8 49.9 L 41.7 49.9 L 43.3 47.9 Z M 43.5 39.1 L 42.4 42.9 L 37.8 43.6 
581:   const exportBtn = document.getElementById("btn-export");
582:       cardFlag.innerHTML = '<svg width="1em" height="1em" viewBox="0 0 100 100" style="vertical-align: middle; fill: #ffffff; display: inline-block; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.25));"><path d="M 65.7 50.5 L 66.6 47.5 L 74.2 48.8 L 70.8 55.4 L 65.7 50.5 Z M 61.2 21.9 L 56.4 26.1 L 55.8 16.6 L 62.3 17.0 L 61.2 21.9 Z M 54.9 45.0 L 60.9 47.9 L 59.0 52.6 L 50.5 48.9 L 54.9 45.0 Z M 71.2 68.0 L 79.0 63.9 L 77.5 71.4 L 71.7 72.1 L 71.2 68.0 Z M 74.8 59.7 L 79.8 63.7 L 71.3 68.0 L 69.6 65.9 L 75.3 62.1 L 74.8 59.7 Z M 78.6 66.5 L 83.7 69.0 L 78.9 74.3 L 78.6 66.5 Z M 63.8 58.8 L 65.6 57.7 L 66.3 61.4 L 64.9 67.3 L 62.5 67.3 L 60.0 63.1 L 63.8 58.8 Z M 62.3 17.0 L 66.3 15.3 L 66.1 18.5 L 69.4 20.1 L 67.3 23.0 L 61.2 21.9 L 62.3 17.0 Z M 46.7 76.1 L 49.6 81.5 L 41.6 80.1 L 46.7 76.1 Z M 57.3 30.9 L 62.7 28.0 L 66.1 33.1 L 60.3 34.9 L 57.3 30.9 Z M 46.7 76.1 L 56.2 76.6 L 55.0 79.9 L 49.7 81.6 L 46.7 76.1 Z M 49.9 64.2 L 53.9 62.0 L 57.5 69.5 L 55.1 72.4 L 48.0 68.0 L 49.9 64.2 Z M 65.4 70.4 L 71.8 72.3 L 71.1 76.9 L 62.3 74.5 L 65.4 70.4 Z M 29.5 22.4 L 38.1 21.7 L 39.0 25.8 L 29.8 27.5 L 29.5 22.4 Z M 51.7 56.6 L 56.8 59.9 L 54.6 64.0 L 53.1 61.4 L 49.6 64.0 L 51.
583:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 地域</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
584:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} ヶ国</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
585:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
586:     exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center
587:       world: "🌍 世界", fr: "🇫🇷 法国", it: "🇮🇹 意大利", es: "🇪🇸 西班牙", jp: "🇯🇵 日本", us: "🇺🇸 美国",
588:       step1Desc: "Pinch with 2 fingers or use mouse scroll to navigate the map.",
589:   const exportBtn = document.getElementById("btn-export");
590:   "262": { en: "Djibouti", fr: "Djibouti", ja: "ジブチ", es: "Djibouti", ko: "지부티", zh: "吉布提", hi: "Djibouti" },
591:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
592:     exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
593:     exploredItaly: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
594:   "807": { en: "North Macedonia", fr: "Macédoine du Nord", ja: "北マケドニア ", es: "Macedonia del Norte", ko: "북마케도니아", zh: "北馬其頓", hi: "Macedonia" },
595:   "688": { en: "Serbia", fr: "Serbie", ja: "セルビア", es: "Serbia", ko: "세르비아", zh: "塞尔维亚", hi: "Serbia" },
596:   "499": { en: "Montenegro", fr: "Monténégro", ja: "モンテネグロ", es: "Montenegro", ko: "몬테네그로", zh: "黑山", hi: "Montenegro" },
597:   "780": { en: "Trinidad and Tobago", fr: "Trinité-et-Tobago", ja: "トリニダード・トバゴ", es: "Trinidad y Tobago", ko: "트리니다드 토바고", zh: "特立尼达和多巴哥", hi: "Trinidad and Tobago" },
598:   "728": { en: "South Sudan", fr: "Soudan du Sud", ja: "南スーダン", es: "Sudán del Sur", ko: "남수단", zh: "南苏丹", hi: "S. Sudan" }
599:     legItems[2].innerHTML = `<span class="leg-dot" data-l="3"></span>${t.legend[2]}`;
600:       step3Desc: "सोशल मीडिया के लिए तैयार एक सुंदर मानचित्र डाउनलोड करने के लिए निर्यात बटन पर क्लिक करें!",
601: function getCountryName(id, defaultName) {
602:     exportBtn: '<i class="fa fa-download"></i> 書き出し',
603:   const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];
604:         div.innerHTML = `<strong>${t.levelModal['l'+lvl].main}</strong><small>${t.levelModal['l'+lvl].sub}</small>`;
605:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 地域</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
606:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} ヶ国</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
607:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
608:     exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
609:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} ヶ国</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
610:   const countryTitle = document.querySelector("#country-modal .modal-header h3");
611:   if (countryTitle) countryTitle.textContent = t.countryModal.title;
612:       desc: "このアプリは<strong>100%無料</strong>です！<br>Instagramをフォローして応援していただけると<br>旅の励みになります。よろしくお願いします！🏍️🇯🇵",
613:       follow: `<i class="fa-brands fa-instagram"></i> french_rider_in_japan をフォロー`,
614:   const btnAnyway = document.getElementById("btn-dl-anyway");
615:     cOpts[0].querySelector("div").innerHTML = `<strong>${t.countryModal.world}</strong><small>${t.countryModal.soon}</small>`;
616:     cOpts[0].setAttribute("disabled", "true");
617:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
618:       subtitle.textContent = t.subtitleWorld;
619:       l5: { main: "住んだ", sub: "住んだことがある (+5 pts)" },
620:     cOpts[1].querySelector("div").innerHTML = `<strong>${t.countryModal.fr}</strong><small>${t.countryModal.avail}</small>`;
621:   if (btnShared) btnShared.textContent = m.dlShared;
622:     const exploredCount = Object.values(state.levels).filter(l => l >= 3).length;
623:     const nameHtml = `<span style="${isDefault ? 'border-bottom: 1px dashed rgba(255,255,255,0.7); opacity: 0.9;' : 'font-weight: 800; border-bottom: 1px solid rgba(255,255,255,0.5);'}">${displayName} <i class="fa-solid fa-pen" style="font-size: 0.7em;"></i></span>`;
624:     cOpts[2].querySelector("div").innerHTML = `<strong>${t.countryModal.it}</strong><small>${t.countryModal.soon}</small>`;
625:     exploredUS: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} states</strong></span></div>`,
626:     cOpts[4].querySelector("div").innerHTML = `<strong>${t.countryModal.us}</strong><small>${t.countryModal.soon}</small>`;
627:       l0: { main: "未踏", sub: "行ったことがない (0 pt)" }
628:       desc: "This application is <strong>100% free</strong>!<br>A simple follow on Instagram helps me<br>tremendously to continue this adventure.<br>🏍️🇯🇵 <strong>Thank you for your support!</strong>",
629:       follow: `<i class="fa-brands fa-instagram"></i> Follow french_rider_in_japan`,
630:   const btnCountry = document.getElementById("btn-country-select");
631:       world: "🌍 世界", fr: "🇫🇷 フランス", it: "🇮🇹 イタリア", es: "🇪🇸 スペイン", jp: "🇯🇵 日本", us: "🇺🇸 アメリカ",
632:         div.innerHTML = `<strong>${t.levelModal['l'+lvl].main}</strong><small>${t.levelModal['l'+lvl].sub}</small>`;
633:       btnCountry.innerHTML = `${t.countryModal.jp} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
634:       subtitle: "What is your exploration level?",
635:       btnCountry.innerHTML = `${t.countryModal.fr} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
636:       l4: { main: "Stayed there", sub: "Stayed ≥ 1 night (+4 pts)" },
637:       btnCountry.innerHTML = `${t.countryModal.world} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
638:   const countryTitle = document.querySelector("#country-modal .modal-header h3");
639:       l1: { main: "Passed there", sub: "Just passing through (+1 pt)" },
640:   el._t = setTimeout(() => el.classList.remove("show"), 2500);
641:   const legItems = document.querySelectorAll("#card-legend .leg-item");
642:   const bgWatermark = document.getElementById("bg-watermark");
643:     cOpts[0].querySelector("div").innerHTML = `<strong>${t.countryModal.world}</strong><small>${t.countryModal.soon}</small>`;
644:       world: "🌍 World", fr: "🇫🇷 France", it: "🇮🇹 Italy", es: "🇪🇸 Spain", jp: "🇯🇵 Japan", us: "🇺🇸 USA",
645:     legItems[2].innerHTML = `<span class="leg-dot" data-l="3"></span>${t.legend[2]}`;
646:     legItems[3].innerHTML = `<span class="leg-dot" data-l="2"></span>${t.legend[3]}`;
647:     legItems[4].innerHTML = `<span class="leg-dot" data-l="1"></span>${t
648:     cOpts[1].querySelector("div").innerHTML = `<strong>${t.countryModal.fr}</strong><small>${t.countryModal.avail}</small>`;
649:       step3Desc: "書き出しボタンをクリックして、SNSに最適な美しいマップをダウンロードしましょう！",
650:     cOpts[1].removeAttribute("style");
651:     subtitle: "À quel point as-tu exploré <span style='display: inline-block;'>le Japon ?</span>",
652:     subtitleWorld: "À quel point as-tu exploré <span style='display: inline-block;'>le Monde ?</span>",
653:     subtitleFrance: "Combien de départements <span style='display: inline-block;'>de France as-tu exploré ?</span>",
654:     subtitleSpain: "Combien de provinces <span style='display: inline-block;'>d'Espagne as-tu exploré ?</span>",
655:     subtitleItaly: "Combien de provinces de<br><span style='display: inline-block;'>l'Italie as-tu exploré ?</span>",
656:         fs = Math.min((p.h * paddingMultiplier) / L, p.w * paddingMultiplier);
657:     subtitle: "À quel point as-tu exploré <span style='display: inline-block;'>le Japon ?</span>",
658:     subtitleWorld: "À quel point as-tu exploré <span style='display: inline-block;'>le Monde ?</span>",
659:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} régions</strong></span></div>`,
660:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} pays</strong></span></div>`,
661:     subtitleItaly: "Combien de provinces de<br><span style='display: inline-block;'>l'Italie as-tu exploré ?</span>",
662:     exportBtn: '<i class="fa fa-download"></i> Exporter',
663:       step3Desc: "Click the export button to download a beautiful map ready for social networks!",
664:         fs = Math.min((p.h * paddingMultiplier) / (L * charWidthRatio), p.w * paddingMultiplier);
665:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} régions</strong></span></div>`,
666:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} pays</strong></span></div>`,
667:       btnCountry.innerHTML = `${t.countryModal.world} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
668:     else if (state.currentMap === "fr") text = t.bgWatermarkFrance || "FRANCE";
669:     if (state.currentMap === "jp") text = t.bgWatermark || "JAPAN";
670:     else if (state.currentMap === "fr") text = t.bgWatermarkFrance || "FRANCE";
671:     else text = t.bgWatermarkWorld || "WORLD";
672:     bgWatermark.innerHTML = Array(5).fill(`<div>${text}</div>`).join("");
673:       l5: { main: "Habité", sub: "J'y ai habité (+5 pts)" },
674:       l4: { main: "Séjourné", sub: "Séjour ≥ 1 nuit (+4 pts)" },
675:     if (state.currentMap === "jp") text = t.bgWatermark || "JAPAN";
676:     else if (state.currentMap === "fr") text = t.bgWatermarkFrance || "FRANCE";
677:     cOpts[1].querySelector("div").innerHTML = `<strong>${t.countryModal.es}</strong><small>${t.countryModal.avail}</small>`;
678:     bgWatermark.innerHTML = Array(5).fill(`<div>${text}</div>`).join("");
679:     if (tutoStep1T) tutoStep1T.textContent = tuto.step1Title;
680:     const tutoStep1T = document.getElementById("tuto-step1-title");
681:     cOpts[2].querySelector("div").innerHTML = `<strong>${t.countryModal.fr}</strong><small>${t.countryModal.avail}</small>`;
682:       world: "🌍 Monde", fr: "🇫🇷 France", it: "🇮🇹 Italie", es: "🇪🇸 Espagne", jp: "🇯🇵 Japon", us: "🇺🇸 USA",
683:     if (tutoStep2T) tutoStep2T.textContent = tuto.step2Title;
684:     const tutoStep2T = document.getElementById("tuto-step2-title");
685:     cOpts[3].querySelector("div").innerHTML = `<strong>${t.countryModal.it}</strong><small>${t.countryModal.soon}</small>`;
686:     const tutoStep3T = document.getElementById("tuto-step3-title");
687:     if (tutoStep3T) tutoStep3T.textContent = tuto.step3Title;
688:       world: "🌍 Monde", fr: "🇫🇷 France", it: "🇮🇹 Italie", es: "🇪🇸 Espagne", jp: "🇯🇵 Japon", us: "🇺🇸 USA",
689:     if (tutoStep3T) tutoStep3T.textContent = tuto.step3Title;
690:     cOpts[4].querySelector("div").innerHTML = `<strong>${t.countryModal.jp}</strong><small>${t.countryModal.avail}</small>`;
691:     if (tutoStep3D) tutoStep3D.textContent = tuto.step3Desc;
692:     legend: ["Vivido", "Alojado", "Visitado", "Escala", "Pasado", "Nunca"],
693:         txt.attr("transform", `rotate(-90, ${cx}, ${cy})`);
694:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} regiones</strong></span></div>`,
695:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} países</strong></span></div>`,
696:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} departamento
697:     if (tutoClose) tutoClose.textContent = tuto.closeBtn;
698:       step2Desc: "Cliquez sur une région ou un département pour enregistrer votre niveau d'exploration.",
699:       l4: { main: "Alojado", sub: "Estancia ≥ 1 noche (+4 pts)" },
700:       step3Desc: "Cliquez sur le bouton d'export pour télécharger une superbe carte prête pour vos réseaux sociaux !",
701:       l2: { main: "Escala", sub: "Parada / Escala (+2 pts)" },
702:       step1Desc: "Pincez avec 2 doigts ou utilisez la molette de la souris pour naviguer sur la carte.",
703:       .attr("x", OX).attr("y", OY).attr("width", OW).attr("height", OH)
704:       step2Desc: "Cliquez sur une région ou un département pour enregistrer votre niveau d'exploration.",
705:       .attr("stroke", "rgba(255, 255, 255, 0.5)")
706:       step3Desc: "Cliquez sur le bouton d'export pour télécharger une superbe carte prête pour vos réseaux sociaux !",
707:     exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
708:     exploredItaly: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
709:     exploredUS: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} états</strong></span></div>`,
710:     if (state.currentMap === "world") state.currentMap = "jp";
711:     legend: ["Vivido", "Alojado", "Visitado", "Escala", "Pasado", "Nunca"],
712:       desc: "Cette application est <strong>100% gratuite</strong> !<br>Un simple abonnement sur Instagram m'aide<br>énormément à continuer cette aventure.<br>🏍️🇯🇵 <strong>Merci pour ton soutien !</strong>",
713:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} regiones</strong></span></div>`,
714:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} países</strong></span></div>`,
715:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span>
716:     else if (state.currentMap === "fr") state.levels = state.frLevels;
717:       .text(UI_TRANSLATIONS[state.lang || "en"].insetLabel);
718:   localStorage.setItem("maplevel_jp_v5", JSON.stringify(state));
719:     const tutoStep1T = document.getElementById("tuto-step1-title");
720:       step1Desc: "Pellizca con 2 dedos o usa la rueda del ratón para navegar por el mapa.",
721:     const tutoStep1D = document.getElementById("tuto-step1-desc");
722:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} regiones</strong></span></div>`,
723:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} países</strong></span></div>`,
724:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span 
725:     const tutoStep2D = document.getElementById("tuto-step2-desc");
726:     if (tutoStep2D) tutoStep2D.textContent = tuto.step2Desc;
727:     const tutoStep3T = document.getElementById("tuto-step3-title");
728:       world: "🌍 Monde", fr: "🇫🇷 France", it: "🇮🇹 Italie", es: "🇪🇸 Espagne", jp: "🇯🇵 Japon", us: "🇺🇸 USA",
729:     const tutoStep3D = document.getElementById("tuto-step3-desc");
730:       follow: `<i class="fa-brands fa-instagram"></i> Seguir french_rider_in_japan`,
731:     const tutoClose = document.getElementById("btn-tuto-close");
732:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
733:       const countries = countriesGeoJson.features.filter(d => d.id !== "010");
734:     const okName = state.lang === "ja" ? "沖縄" : "Okinawa";
735:       subtitle: "¿Cuál es tu nivel de exploración?",
736:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 지역</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
737:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개국</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
738:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 부서</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
739:     exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line
740:       l1: { main: "Pasado", sub: "Solo de paso (+1 pt)" },
741:       okFs = Math.min((okGrid.w * 0.82) / (okL * 0.52), okGrid.h * 0.82);
742:   const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];
743:       step1Desc: "Pincez avec 2 doigts ou utilisez la molette de la souris pour naviguer sur la carte.",
744:       step2Title: "Sélectionner un Statut",
745:       world: "🌍 Mundo", fr: "🇫🇷 Francia", it: "🇮🇹 Italia", es: "🇪🇸 España", jp: "🇯🇵 Japón", us: "🇺🇸 EE.UU.",
746:       avail: "Disponible", soon: "Próximamente"
747:     userWatermark.innerHTML = `<i class="fa-solid fa-user"></i> ${state.username !== "Votre nom" ? state.username : "French Rider"}`;
748:       avail: "Disponible", soon: "Próximamente"
749:       .attr("y", OY + 8 + okGrid.h / 2)
750:       step1Desc: "Pellizca con 2 dedos o usa la rueda del ratón para navegar por el mapa.",
751:   const floatingName = document.getElementById("lbl-floating-name");
752:       step2Desc: "Pulsa una región o departamento para registrar tu nivel de exploración.",
753:       step3Title: "Exportar y Compartir",
754:       step3Desc: "Pulsa el botón de exportar para descargar un mapa hermoso listo para tus redes sociales.",
755:       .attr("fill", "rgba(26,37,51,0.9)")
756:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
757:       subtitle: "Cómo usar la aplicación",
758:               [1.497077, 39.099212],
759:       step1Desc: "Pellizca con 2 dedos o usa la rueda del ratón para navegar por el mapa.",
760:   document.getElementById("map-loading").style.display = "none";
761:       step2Desc: "Pulsa una región o departamento para registrar tu nivel de exploración.",
762:   } else if (state.currentMap === "fr") {
763:       step3Desc: "Pulsa el botón de exportar para descargar un mapa hermoso listo para tus redes sociales.",
764:     exportBtn: '<i class="fa fa-download"></i> 내보내기',
765:       step3Desc: "Pulsa el botón de exportar para descargar un mapa hermoso listo para tus redes sociales.",
766:       step3Desc: "Pulsa el botón de exportar para descargar un mapa hermoso listo para tus redes sociales.",
767:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 지역</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
768:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개국</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
769:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개
770: // ── UI / Header ──────────────────────────────────────────────
771:   const svg = d3.select("#map-svg");
772:   const total = Object.values(state.levels).reduce((a, b) => a + b, 0);
773:   document.getElementById("card-level").textContent = "Ride the world";
774:   document.getElementById("card-score").textContent = total;
775:   const pathGenerator = d3.geoPath().projection(projection);
776:     exportBtn: '<i class="fa fa-download"></i> 내보내기',
777:     legend: ["거주", "숙박", "방문", "경유", "통과", "미방문"],
778:   el._t = setTimeout(() => el.classList.remove("show"), 2500);
779:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 지역</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
780:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개국</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
781:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
782:       const countries = countriesGeoJson.features.filter(d => d.id !== "010");
783:         fetch("france_domtom.geojson").then(res => res.json())
784:   const countryTitle = document.querySelector("#country-modal .modal-header h3");
785:   if (countryTitle) countryTitle.textContent = t.countryModal.title;
786:       l0: { main: "미방문", sub: "가본 적 없음 (0 pt)" }
787:       follow: `<i class="fa-brands fa-instagram"></i> french_rider_in_japan 팔로우`,
788:   document.getElementById("card-max-score").textContent = `/ ${maxPoints} pts`;
789:     cOpts[0].querySelector("div").innerHTML = `<strong>${t.countryModal.world}</strong><small>${t.countryModal.soon}</small>`;
790:       world: "🌍 세계", fr: "🇫🇷 프랑스", it: "🇮🇹 이탈리아", es: "🇪🇸 스페인", jp: "🇯🇵 일본", us: "🇺🇸 미국",
791:         toast("Erreur de chargement de la carte de France.");
792:         document.getElementById("map-loading").style.display = "none";
793:       document.getElementById("map-loading").style.display = "flex";
794:     cOpts[1].querySelector("div").innerHTML = `<strong>${t.countryModal.es}</strong><small>${t.countryModal.avail}</small>`;
795:         fetch("france_departements.geojson").then(res => res.json()),
796:     userWatermark.innerHTML = `<i class="fa-solid fa-user"></i> ${state.username !== "Votre nom" ? state.username : "French Rider"}`;
797:       l1: { main: "통과", sub: "지나간 적 있음 (+1 pt)" },
798:     cOpts[2].querySelector("div").innerHTML = `<strong>${t.countryModal.fr}</strong><small>${t.countryModal.avail}</small>`;
799:       document.getElementById("map-loading").style.display = "flex";
800:   const floatingName = document.getElementById("lbl-floating-name");
801:       title: "환영합니다! 🌍",
802:     cOpts[3].querySelector("div").innerHTML = `<strong>${t.countryModal.it}</strong><small>${t.countryModal.soon}</small>`;
803:         toast("Erreur de chargement de la carte de France.");
804:         document.getElementById("map-loading").style.display = "none";
805:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
806:       step2Desc: "지역이나 도를 클릭하여 탐험 레벨을 기록하세요.",
807:     cOpts[4].querySelector("div").innerHTML = `<strong>${t.countryModal.jp}</strong><small>${t.countryModal.avail}</small>`;
808:       step3Desc: "내보내기 버튼을 클릭하여 SNS에 공유할 멋진 지도를 다운로드하세요!",
809:     cOpts[4].removeAttribute("style");
810:     const exploredCount = Object.values(state.levels).filter(l => l >= 3).length;
811:     const nameHtml = `<span style="${isDefault ? 'border-bottom: 1px dashed rgba(255,255,255,0.7); opacity: 0.9;' : 'font-weight: 800; border-bottom: 1px solid rgba(255,255,255,0.5);'}">${displayName} <i class="fa-solid fa-pen" style="font-size: 0.7em;"></i></span>`;
812:     cOpts[5].setAttribute("disabled", "true");
813:     if (state.currentMap === "jp") {
814:       floatingName.innerHTML = t.explored(nameHtml, exploredCount);
815:     } else if (state.currentMap === "fr") {
816:       floatingName.innerHTML = t.exploredFrance(nameHtml, exploredCount);
817:           updateHeader(); // Recalculate accurate max score with actual country count
818:       floatingName.innerHTML = t.exploredWorld(nameHtml, exploredCount);
819:     legend: ["居住", "住宿", "游览", "经停", "路过", "未去"],
820:           console.error("Error loading world map data:", err);
821:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个地区</strong></span></div>`,
822:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个国家</strong></span></div>`,
823:     exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 
824:   const el = document.getElementById("toast");
825:       .attr("pointer-events", "none")
826:   el.classList.add("show");
827:   clearTimeout(el._t);
828:   el._t = setTimeout(() => el.classList.remove("show"), 2500);
829:   document.getElementById("map-loading").style.display = "none";
830:     subtitleFrance: "你探索了多少法国？",
831: // ── Build SVG Proportional Cartogram Map ────────────────────
832:   document.getElementById("card-max-score").textContent = `/ ${maxPoints} pts`;
833:   const mainGrid = GRID.filter(p => p.code !== "47");
834:   const okGrid = GRID.find(p => p.code === "47");
835:   const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];
836:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个地区</strong></span></div>`,
837:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个国家</strong></span>
838:   const userWatermark = document.getElementById("card-user-watermark");
839:           document.getElementById("map-loading").style.display = "none";
840:     userWatermark.innerHTML = `<i class="fa-solid fa-user"></i> ${state.username !== "Votre nom" ? state.username : "French Rider"}`;
841:     const g = mapG.append("g")
842:       .attr("class", "cell-group")
843:       desc: "这个应用是<strong>100%免费</strong>的！<br>在Instagram上关注我<br>将极大地帮助我继续这段冒险。<br>🏍️🇯🇵 <strong>感谢你的支持！</strong>",
844:       follow: `<i class="fa-brands fa-instagram"></i> 关注 french_rider_in_japan`,
845:       .on("click", () => openModal(p.code));
846:     let displayName = state.username;
847: function drawFranceMap() {
848:   svg.attr("viewBox", `0 0 ${W} ${H}`);
849:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
850:           toast("Erreur de chargement de la carte du Japon.");
851:           document.getElementById("map-loading").style.display = "none";
852:       l3: { main: "游览", sub: "一日游 (+3 pts)" },
853:       l2: { main: "经停", sub: "中转 / 经停 (+2 pts)" },
854:     const exploredCount = Object.values(state.levels).filter(l => l >= 3).length;
855:     const nameHtml = `<span style="${isDefault ? 'border-bottom: 1px dashed rgba(255,255,255,0.7); opacity: 0.9;' : 'font-weight: 800; border-bottom: 1px solid rgba(255,255,255,0.5);'}">${displayName} <i class="fa-solid fa-pen" style="font-size: 0.7em;"></i></span>`;
856:     const isVertical = p.h >= p.w;
857:     const name = state.lang === "ja" ? NAMES_JA[p.code] : NAMES_EN[p.code];
858:       document.getElementById("map-loading").style.display = "flex";
859:       world: "🌍 世界", fr: "🇫🇷 法国", it: "🇮🇹 意大利", es: "🇪🇸 西班牙", jp: "🇯🇵 日本", us: "🇺🇸 美国",
860:       floatingName.innerHTML = t.exploredFrance(nameHtml, exploredCount);
861:       world: "🌍 世界", fr: "🇫🇷 法国", it: "🇮🇹 意大利", es: "🇪🇸 西班牙", jp: "🇯🇵 日本", us: "🇺🇸 美国",
862:       floatingName.innerHTML = t.exploredWorld(nameHtml, exploredCount);
863:         fs = Math.min((p.h * paddingMultiplier) / L, p.w * paddingMultiplier);
864:       l1: { main: "गुज़रे", sub: "बस गुज़रा (+1 pt)" },
865:         fs = Math.min((p.w * paddingMultiplier) / L, p.h * paddingMultiplier);
866:   // 1. Draw Metropolitan / Main Japan inside a zoomable group
867:       fs = Math.max(9.5, Math.min(fs, 38));
868:         console.error("Error loading France map data:", err);
869:       world: "🌍 विश्व", fr: "🇫🇷 फ़्रांस", it: "🇮🇹 इटली", es: "🇪🇸 स्पेन", jp: "🇯🇵 जापान", us: "🇺🇸 अमेरिका",
870:         document.getElementById("map-loading").style.display = "none";
871:         fs = Math.min((p.h * paddingMultiplier) / (L * charWidthRatio), p.w * paddingMultiplier);
872:       step1Title: "ज़ूम और नेविगेट",
873:       step1Desc: "मानचित्र पर नेविगेट करने के लिए 2 उंगलियों से पिंच करें या माउस स्क्रॉल का उपयोग करें।",
874:       step2Title: "स्तर चुनें",
875:       step2Desc: "अपना अन्वेषण स्तर दर्ज करने के लिए किसी क्षेत्र पर क्लिक करें।",
876:       step3Title: "निर्यात और साझा करें",
877:       step3Desc: "सोशल मीडिया के लिए तैयार एक सुंदर मानचित्र डाउनलोड करने के लिए निर्यात बटन पर क्लिक करें!",
878:       step2Desc: "点击地区或省份以记录您的探索等级。",
879:       step3Desc: "点击导出按钮，下载一张适合社交媒体的精美地图！",
880:         fs = Math.min((p.h * paddingMultiplier) / L, p.w * paddingMultiplier);
881:       step1Title: "ज़ूम और नेविगेट",
882:       step1Desc: "मानचित्र पर नेविगेट करने के लिए 2 उंगलियों से पिंच करें या माउस स्क्रॉल का उपयोग करें।",
883:       follow: `<i class="fa-brands fa-instagram"></i> french_rider_in_japan फ़ॉलो करें`,
884:       step2Desc: "अपना अन्वेषण स्तर दर्ज करने के लिए किसी क्षेत्र पर क्लिक करें।",
885:   const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];
886:     subtitleWorld: "आपने दुनिया का कितना हिस्सा खोजा है?",
887:     subtitleFrance: "आपने फ्रांस का कितना हिस्सा खोजा है?",
888:   const subtitle = document.getElementById("card-subtitle-phrase");
889:     subtitleItaly: "आपने इटली का कितना हिस्सा खोजा है?",
890:       l4: { main: "ठहरे", sub: "1 रात ≥ ठहरा (+4 pts)" },
891:     legend: ["रहे", "ठहरे", "देखा", "रुके", "गुज़रे", "कभी नहीं"],
892:       l2: { main: "रुके", sub: "पड़ाव / रुकावट (+2 pts)" },
893:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:cent
894:  document.getElementById("btn-country-select").addEventListener("click", () => {
895:           document.getElementById("map-loading").style.display = "none";
896:   document.getElementById("map-loading").style.display = "none";
897:         txt.style("writing-mode", "vertical-rl")
898:       world: "🌍 विश्व", fr: "🇫🇷 फ़्रांस", it: "🇮🇹 इटली", es: "🇪🇸 स्पेन", jp: "🇯🇵 जापान", us: "🇺🇸 अमेरिका",
899:   // Initialize missing levels for Japan prefectures
900:       desc: "यह ऐप <strong>100% मुफ़्त</strong> है!<br>Instagram पर फ़ॉलो करना<br>इस यात्रा को जारी रखने में बहुत मदद करता है।<br>🏍️🇯🇵 <strong>आपके समर्थन का धन्यवाद!</strong>",
901:       follow: `<i class="fa-brands fa-instagram"></i> french_rider_in_japan फ़ॉलो करें`,
902:       document.getElementById("map-loading").style.display = "flex";
903:       dlShared: "मैंने फ़ॉलो किया! HD डाउनलोड 🎉"
904:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
905:       const feature = countriesGeoJson.features.find(f => f.id === code);
906:       subtitle: "अपना अन्वेषण स्तर चुनें",
907:         return getCountryName(code, feature.properties.name);
908:   const prefecturesGeoJSON = topojson.feature(japanData, japanData.objects.prefectures);
909:       l3: { main: "देखा", sub: "दिन की यात्रा (+3 pts)" },
910:       .attr("x", OX).attr("y", OY).attr("width", OW).attr("height", OH)
911:     features: prefecturesGeoJSON.features.filter(f => f.id !== "47")
912:         console.error("Error loading France map data:", err);
913:   const okinawaFeature = prefecturesGeoJSON.features.find(f => f.id === "47");
914:         document.getElementById("map-loading").style.display = "none";
915:     .text(d => state.lang === "ja" ? NAMES_JA[d.id] : NAMES_EN[d.id]);
916:       world: "🌍 विश्व", fr: "🇫🇷 फ़्रांस", it: "🇮🇹 इटली", es: "🇪🇸 स्पेन", jp: "🇯🇵 जापान", us: "🇺🇸 अमेरिका",
917:   // 2. Setup D3 Zoom & Pinch support for Honshu/Hokkaido
918:   document.getElementById("modal-title").textContent = `@ ${name}`;
919:       if (event.defaultPrevented) return;
920:   const legItems = document.querySelectorAll("#card-legend .leg-item");
921:     btn.classList.toggle("selected", +btn.dataset.level === cur);
922:   const pathGenerator = d3.geoPath().projection(projection);
923:   document.getElementById("modal-overlay").classList.remove("hidden");
924:       .text(UI_TRANSLATIONS[state.lang || "en"].insetLabel);
925:     .data(honshuGeoJSON.features)
926:     .data(honshuGeoJSON.features)
927:   document.getElementById("modal-overlay").classList.add("hidden");
928:     .attr("class", "cell-label")
929:   const exportBtn = document.getElementById("btn-export");
930:   if (exportBtn) exportBtn.innerHTML = t.exportBtn;
931: // ── Event Setup ──────────────────────────────────────────────
932:       step1Desc: "मानचित्र पर नेविगेट करने के लिए 2 उंगलियों से पिंच करें या माउस स्क्रॉल का उपयोग करें।",
933:   document.getElementById("modal-close").addEventListener("click", closeModal);
934:       step2Desc: "अपना अन्वेषण स्तर दर्ज करने के लिए किसी क्षेत्र पर क्लिक करें।",
935:     if (e.target.id === "modal-overlay") closeModal();
936:       step3Desc: "सोशल मीडिया के लिए तैयार एक सुंदर मानचित्र डाउनलोड करने के लिए निर्यात बटन पर क्लिक करें!",
937:       .attr("width", okGrid.w - (gap * 2))
938:   document.querySelectorAll(".opt-btn").forEach(btn => {
939:       .attr("fill", COLORS[state.levels["47"] || 0]);
940:     .attr("font-family", "'Outfit', sans-serif")
941:       .text(UI_TRANSLATIONS[state.lang || "en"].insetLabel);
942: function updateUITranslations() {
943:     .attr("fill", "rgba(26,37,51,0.85)")
944:   const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];
945:     .text(d => state.lang === "ja" ? NAMES_JA[d.id] : NAMES_EN[d.id]);
946:       document.querySelectorAll(".lang-btn").forEach(b => b.classList.remove("selected"));
947:       .on("click", () => openModal("47"));
948:       okFs = Math.min((okGrid.w * 0.82) / (okL * 0.52), okGrid.h * 0.82);
949:       okFs = Math.max(6.8, Math.min(okFs, 26));
950:     legItems[3].innerHTML = `<span class="leg-dot" data-l="2"></span>${t.legend[3]}`;
951:     legItems[4].innerHTML = `<span class="leg-dot" data-l="1"></span>${t.legend[4]}`;
952:   const prefecturesGeoJSON = topojson.feature(japanData, japanData.objects.prefectures);
953:     subtitle: "आपने जापान का कितना हिस्सा खोजा है?",
954:     subtitleWorld: "आपने दुनिया का कितना हिस्सा खोजा है?",
955:     features: prefecturesGeoJSON.features.filter(f => f.id !== "47")
956:       world: "🌍 विश्व", fr: "🇫🇷 फ़्रांस", it: "🇮🇹 इटली", es: "🇪🇸 स्पेन", jp: "🇯🇵 जापान", us: "🇺🇸 अमेरिका",
957:   const okinawaFeature = prefecturesGeoJSON.features.find(f => f.id === "47");
958:     const okName = state.lang === "ja" ? "沖縄" : "Okinawa";
959:   // 1. Draw Metropolitan / Main Japan inside a zoomable group
960:       document.getElementById("btn-lang-select").innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
961:   const btnShared = document.getElementById("btn-dl-shared");
962:     explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} क्षेत्र</strong><span style="opacity:0.7; font-weight:400;"> खोजे</span></span></div>`,
963:     exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; 
964:   const cardFlag = document.getElementById("card-flag");
965:       okFs = Math.min((okGrid.w * 0.82) / (okL * 0.52), okGrid.h * 0.82);
966:   const pathGenerator = d3.geoPath().projection(projection);
967:   document.getElementById("map-loading").style.display = "none";
968:   // Render main prefectures
969:   const btnFloatingProfile = document.getElementById("btn-floating-profile");
970:       desc: "यह ऐप <strong>100% मुफ़्त</strong> है!<br>Instagram पर फ़ॉलो करना<br>इस यात्रा को जारी रखने में बहुत मदद करता है।<br>🏍️🇯🇵 <strong>आपके समर्थन का धन्यवाद!</strong>",
971:       step1Desc: "मानचित्र पर नेविगेट करने के लिए 2 उंगलियों से पिंच करें या माउस स्क्रॉल का उपयोग करें।",
972:       const n = prompt("Votre prénom/pseudo :", state.username === "Votre nom" ? "" : state.username);
973:       step2Desc: "अपना अन्वेषण स्तर दर्ज करने के लिए किसी क्षेत्र पर क्लिक करें।",
974:         div.innerHTML = `<strong>${t.levelModal['l'+lvl].main}</strong><small>${t.levelModal['l'+lvl].sub}</small>`;
975:       step3Desc: "सोशल मीडिया के लिए तैयार एक सुंदर मानचित्र डाउनलोड करने के लिए निर्यात बटन पर क्लिक करें!",
976:     .attr("fill", d => COLORS[state.levels[d.id] || 0])
977:       l5: { main: "रहे", sub: "वहाँ रहा (+5 pts)" },
978:         div.innerHTML = `<strong>${t.levelModal['l'+lvl].main}</strong><small>${t.levelModal['l'+lvl].sub}</small>`;
979:       l3: { main: "देखा", sub: "दिन की यात्रा (+3 pts)" },
980:   const countryTitle = document.querySelector("#country-modal .modal-header h3");
981:   if (countryTitle) countryTitle.textContent = t.countryModal.title;
982:   const legItems = document.querySelectorAll("#card-legend .leg-item");
983:   const cOpts = document.querySelectorAll("#country-modal .opt-btn");
984:     legItems[0].innerHTML = `<span class="leg-dot" data-l="5"></span>${t.legend[0]}`;
985:     cOpts[0].querySelector("div").innerHTML = `<strong>${t.countryModal.world}</strong><small>${t.countryModal.avail}</small>`;
986:       world: "🌍 विश्व", fr: "🇫🇷 फ़्रांस", it: "🇮🇹 इटली", es: "🇪🇸 स्पेन", jp: "🇯🇵 जापान", us: "🇺🇸 अमेरिका",
987:     legItems[3].innerHTML = `<span class="leg-dot" data-l="2"></span>${t.legend[3]}`;
988:     legItems[4].innerHTML = `<span class="leg-dot" data-l="1"></span>${t.legend[4]}`;
989:     cOpts[1].querySelector("div").innerHTML = `<strong>${t.countryModal.es}</strong><small>${t.countryModal.avail}</small>`;
990:     legItems[4].innerHTML = `<span class="leg-dot" data-l="1"></span>${t.legend[4]}`;
991:     legItems[5].innerHTML = `<span class="leg-dot" data-l="0"></span>${t.legend[5]}`;
992:       mapG.attr("transform", event.transform);
993:     cOpts[2].querySelector("div").innerHTML = `<strong>${t.countryModal.fr}</strong><small>${t.countryModal.avail}</small>`;
994:       const centroid = pathGenerator.centroid(d);
995:       subtitle.innerHTML = t.subtitleItaly;
996:   const title = document.getElementById("export-title");
997:     cOpts[3].querySelector("div").innerHTML = `<strong>${t.countryModal.it}</strong><small>${t.countryModal.soon}</small>`;
998:   const btnFollow = document.getElementById("btn-follow");
999:   const btnAnyway = document.getElementById("btn-dl-anyway");
1000:     .attr("fill", d => COLORS[state.levels[d.properties.code] || 0])
1001:       step1Desc: "मानचित्र पर नेविगेट करने के लिए 2 उंगलियों से पिंच करें या माउस स्क्रॉल का उपयोग करें।",
1002:     cOpts[4].querySelector("div").innerHTML = `<strong>${t.countryModal.jp}</strong><small>${t.countryModal.avail}</small>`;
1003:       step2Desc: "अपना अन्वेषण स्तर दर्ज करने के लिए किसी क्षेत्र पर क्लिक करें।",
1004:     const savedBtnBottom = floatingBtn ? floatingBtn.style.bottom : null;
1005:       step3Desc: "सोशल मीडिया के लिए तैयार एक सुंदर मानचित्र डाउनलोड करने के लिए निर्यात बटन पर क्लिक करें!",
1006:     cOpts[5].querySelector("div").innerHTML = `<strong>${t.countryModal.us}</strong><small>${t.countryModal.soon}</small>`;
1007:     const savedLegendPaddingBottom = legend ? legend.style.paddingBottom : null;
1008:     cOpts[5].style.opacity = "0.5";
1009:     // Temporarily adjust for clean export (no cropping)
1010:   // Draw department label numbers inside centroids for metropolitan departments
1011:   if (exportBtn) exportBtn.innerHTML = t.exportBtn;
1012:       mapSvg.style.transform = "translateY(-35px)";
1013:     const btn = document.querySelector(`#modal-opts .opt-btn[data-level="${lvl}"]`);
1014:   const insetLabel = document.getElementById("inset-label");
1015:     .attr("font-family", "'Outfit', sans-serif")
1016:       btnCountry.innerHTML = `${t.countryModal.jp} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1017:         div.innerHTML = `<strong>${t.levelModal['l'+lvl].main}</strong><small>${t.levelModal['l'+lvl].sub}</small>`;
1018:       btnCountry.innerHTML = `${t.countryModal.fr} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1019:     const s = JSON.parse(localStorage.getItem("maplevel_jp_v5") || "{}");
1020:       btnCountry.innerHTML = `${t.countryModal.es} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1021:       header.style.paddingTop = "75px";
1022:       btnCountry.innerHTML = `${t.countryModal.world} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1023:   const countryTitle = document.querySelector("#country-modal .modal-header h3");
1024:   if (countryTitle) countryTitle.textContent = t.countr
1025:   document.getElementById("map-loading").style.display = "none";
1026:       mapG.attr("transform", event.transform);
1027:     .attr("font-family", "'Outfit', sans-serif")
1028:     // Transparent click helper covering the entire inset box for easy tapping
1029:       .fitExtent([[OX + 6, OY + 6], [OX + OW - 6, OY + OH - 20]], okinawaFeature);
1030:     else if (state.currentMap === "fr") state.levels = state.frLevels;
1031:   // 3. Draw 5 Overseas Insets (Okinawa-style) stacked vertically on the left side (outside mapG so they stay fixed!)
1032:     else state.levels = state.worldLevels;
1033:   const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1034:   const countries = countriesGeoJson.features.filter(d => d.id !== "010"); // Exclude Antarctica
1035:     { code: "973", name: "Guyane", nameJa: "ギアナ", y: 229 },
1036:     { code: "974", name: "La Réunion", nameJa: "レユニオン", y: 326 },
1037:     { code: "976", name: "Mayotte", nameJa: "マヨット", y: 423 }
1038:       // Exclude zoom gestures starting on the left side of the map (x < 92) where DOM-TOMs are located
1039:       const svgNode = document.getElementById("map-svg");
1040:     const localPath = d3.geoPath().projection(localProjection);
1041:       if (state.levels[c] == null) state.levels[c] = 0;
1042:   document.getElementById("map-loading").style.display = "none";
1043:       if (event.touches && event.touches.length > 0) {
1044:     Object.keys(PROVINCES_ES).forEach(c => {
1045:       } else if (event.changedTouches && event.changedTouches.length > 0) {
1046:       .attr("fill", COLORS[state.levels["47"] || 0])
1047:       return centroid ? centroid[1] : 0;
1048:       .attr("font-weight", "800")
1049:       .attr("fill", "rgba(255, 255, 255, 0.8)")
1050:       .text(`${dt.code} - ${state.lang === "ja" ? dt.nameJa : dt.name}`);
1051:   document.getElementById("modal-overlay").classList.add("hidden");
1052:       const xInSvg = ((clientX - rect.left) / rect.width) * 560;
1053:     const feature = franceDomTomData.features.find(f => f.properties.code === dt.code);
1054:       // Keep D3 default filters: no ctrlKey, left click only for mouse events
1055:       return !event.ctrlKey && (!event.type.startsWith("mouse") || event.button === 0) && xInSvg >= 92;
1056:     const tutoClose = document.getElementById("btn-tuto-close");
1057:       btnCountry.innerHTML = `${t.countryModal.jp} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1058:       btnCountry.innerHTML = `${t.countryModal.jp} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1059:       btnCountry.innerHTML = `${t.countryModal.fr} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1060:       btnCountry.innerHTML = `${t.countryModal.fr} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1061:       btnCountry.innerHTML = `${t.countryModal.es} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1062:       btnCountry.innerHTML = `${t.countryModal.es} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1063:       btnCountry.innerHTML = `${t.countryModal.it} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1064:       btnCountry.innerHTML = `${t.countryModal.it} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1065:       btnCountry.innerHTML = `${t.countryModal.world} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1066:       btnCountry.innerHTML = `${t.countryModal.world} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1067:   const btnLang = document.getElementById("btn-lang-select");
1068:   if (btnLang) btnLang.innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1069:     { code: "976", name: "Mayotte", nameJa: "マヨット", y: 423 }
1070:       const g = document.querySelector(`.cell-group[data-code="${activePrefCode}"]`);
1071:   const bgWatermark = document.getElementById("bg-watermark");
1072:   document.getElementById("btn-dl-anyway").addEventListener("click", doExport);
1073:   document.getElementById("btn-dl-shared").addEventListener("click", () => {
1074:     if (state.currentMap === "jp") text = t.bgWatermark || "JAPAN";
1075:         // Also support selection via path selector direct mapping (World Map fallback)
1076:         const cellPath = document.querySelector(`path.cell-path[data-code="${activePrefCode}"]`);
1077:     else if (state.currentMap === "it") text = t.bgWatermarkItaly || "ITALY";
1078:     else if (state.currentMap === "it") text = t.bgWatermarkItaly || "ITALY";
1079:     bgWatermark.innerHTML = Array(5).fill(`<div>${text}</div>`).join("");
1080:     bgWatermark.innerHTML = Array(5).fill(`<div>${text}</div>`).join("");
1081:     Object.keys(state.levels).forEach(c => state.levels[c] = 0);
1082:     .attr("fill", d => COLORS[state.levels[d.properties.code] || 0])
1083:     if (state.currentMap === "jp") state.levels = state.jpLevels;
1084:       const lbls = ["Jamais", "Passé", "Escale", "Visité", "Séjourné", "Habité"];
1085:     document.querySelectorAll(".cell-rect, .cell-path").forEach(r => r.setAttribute("fill", COLORS[0]));
1086:     else if (state.currentMap === "it") state.levels = state.itLevels;
1087:     Object.keys(DEPARTEMENTS_FR).forEach(c => {
1088:     const s = JSON.parse(localStorage.getItem("maplevel_jp_v5") || "{}");
1089:     if (s.username) state.username = s.username;
1090:   const countryOverlay = document.getElementById("country-overlay");
1091: // ── INIT ─────────────────────────────────────────────────────
1092:       // Exclude zoom gestures starting on the left side of the map (x < 92) where DOM-TOMs are located
1093:   const total = Object.values(state.levels).reduce((a, b) => a + b, 0);
1094:   document.getElementById("card-level").textContent = "Ride the world";
1095:     const feature = franceDomTomData.features.find(f => f.properties.code === dt.code);
1096:       if (state.levels[c] == null) state.levels[c] = 0;
1097:     state.itLevels = s.itLevels || {};
1098:     .attr("data-code", d => d.properties.code)
1099:     if (state.currentMap === "jp") state.levels = state.jpLevels;
1100:     else if (state.currentMap === "fr") state.levels = state.frLevels;
1101:     else if (state.currentMap === "es") state.levels = state.esLevels;
1102:     else if (state.currentMap === "it") state.levels = state.itLevels;
1103:     else if (state.currentMap === "it") state.levels = state.itLevels;
1104:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1105:       const countries = countriesGeoJson.features.filter(d => d.id !== "010");
1106:       const localProjection = d3.geoMercator()
1107:         .fitExtent([[OX + 6, OY + 6], [OX + OW - 6, OY + OH - 20]], feature);
1108:       if (state.levels[c] == null) state.levels[c] = 0;
1109:   // 1. Draw Metropolitan France Departments inside a zoomable group
1110:       if (state.levels[c] == null) state.levels[c] = 0;
1111:   document.getElementById("card-max-score").textContent = `/ ${maxPoints} pts`;
1112:       if (state.levels[c] == null) state.levels[c] = 0;
1113:     Object.keys(DEPARTEMENTS_FR).forEach(c => {
1114:       if (state.levels[c] == null) state.levels[c] = 0;
1115:         .attr("fill", COLORS[state.levels[dt.code] || 0])
1116:   } else if (state.currentMap === "es") {
1117:   const pathGenerator = d3.geoPath().projection(projection);
1118:       if (state.levels[c] == null) state.levels[c] = 0;
1119:     Object.keys(PROVINCES_IT).forEach(c => {
1120:       // Exclude zoom gestures starting on the left side of the map (x < 92) where DOM-TOMs are located
1121:       const svgNode = document.getElementById("map-svg");
1122:       if (state.levels[c] == null) state.levels[c] = 0;
1123:   const floatingName = document.getElementById("lbl-floating-name");
1124:     .attr("class", "cell-group cell-path metro-path")
1125:   document.querySelectorAll(".country-btn").forEach(btn => {
1126:   const btnLang = document.getElementById("btn-lang-select");
1127:   if (btnLang) btnLang.innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1128:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
1129:   document.querySelectorAll(".lang-btn").forEach(b => {
1130:     if(b.dataset.val === val) b.classList.add("selected");
1131:     else b.classList.remove("selected");
1132:       // Prevent modal opening if dragging
1133:     const exploredCount = Object.values(state.levels).filter(l => l >= 3).length;
1134:     const nameHtml = `<span style="${isDefault ? 'border-bottom: 1px dashed rgba(255,255,255,0.7); opacity: 0.9;' : 'font-weight: 800; border-bottom: 1px solid rgba(255,255,255,0.5);'}">${displayName} <i class="fa-solid fa-pen" style="font-size: 0.7em;"></i></span>`;
1135:   localStorage.setItem("maplevel_jp_v5", JSON.stringify(state));
1136:       // Keep D3 default filters: no ctrlKey, left click only for mouse events
1137:       return !event.ctrlKey && (!event.type.startsWith("mouse") || event.button === 0) && xInSvg >= 92;
1138: // ── UI / Header ──────────────────────────────────────────────
1139:       floatingName.innerHTML = t.exploredFrance(nameHtml, exploredCount);
1140:   const total = Object.values(state.levels).reduce((a, b) => a + b, 0);
1141:       floatingName.innerHTML = t.exploredSpain(nameHtml, exploredCount);
1142:   const btnLang = document.getElementById("btn-lang-select");
1143:   if (btnLang) btnLang.innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1144:   } else if (state.currentMap === "it") {
1145:   // 3. Draw 5 Overseas Insets (Okinawa-style) stacked vertically on the left side (outside mapG so they stay fixed!)
1146:     if(b.dataset.val === val) b.classList.add("selected");
1147:   // 3. Draw 5 Overseas Insets (Okinawa-style) stacked vertically on the left side (outside mapG so they stay fixed!)
1148:     { code: "972", name: "Martinique", nameJa: "マルティニーク", y: 132 },
1149:     { code: "971", name: "Guadeloupe", nameJa: "グアドループ", y: 35 },
1150:     { code: "972", name: "Martinique", nameJa: "マルティニーク", y: 132 },
1151:     const s = JSON.parse(localStorage.getItem("maplevel_jp_v5") || "{}");
1152:   const total = Object.values(state.levels).reduce((a, b) => a + b, 0);
1153:   document.getElementById("card-level").textContent = "Ride the world";
1154:   const total = Object.values(state.levels).reduce((a, b) => a + b, 0);
1155:   document.getElementById("card-level").textContent = "Ride the world";
1156: // ── Build SVG Proportional Cartogram Map ────────────────────
1157:     const OX = 12, OY = dt.y, OW = 90, OH = 82;
1158:     maxPoints = 505; // France (101 departments * 5)
1159:   } else if (state.currentMap === "es") {
1160:     maxPoints = 505; // France (101 departments * 5)
1161:       .attr("x", OX).attr("y", OY).attr("width", OW).attr("height", OH)
1162:       .attr("fill", "rgba(255, 255, 255, 0.05)")
1163:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1164:       const countries = countriesGeoJson.features.filter(d => d.id !== "010");
1165:       // Exclude zoom gestures starting on the left side of the map (x < 92) where DOM-TOMs are located
1166:     else if (state.currentMap === "it") state.levels = state.itLevels;
1167:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1168:       const countries = countriesGeoJson.features.filter(d => d.id !== "010");
1169:     else if (state.currentMap === "us") state.levels = state.usLevels;
1170:   document.getElementById("card-max-score").textContent = `/ ${maxPoints} pts`;
1171:     else if (state.currentMap === "kr") state.levels = state.krLevels;
1172:       } else if (event.changedTouches && event.changedTouches.length > 0) {
1173:   localStorage.setItem("maplevel_jp_v5", JSON.stringify(state));
1174:   document.getElementById("card-max-score").textContent = `/ ${maxPoints} pts`;
1175:           toast("Erreur de chargement de la carte du Japon.");
1176:       .text(`${dt.code} - ${state.lang === "ja" ? dt.nameJa : dt.name}`);
1177:   const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];
1178:     userWatermark.innerHTML = `<i class="fa-solid fa-user"></i> ${state.username !== "Votre nom" ? state.username : "French Rider"}`;
1179:     const feature = franceDomTomData.features.find(f => f.properties.code === dt.code);
1180:   const userWatermark = document.getElementById("card-user-watermark");
1181:       // Keep D3 default filters: no ctrlKey, left click only for mouse events
1182:     userWatermark.innerHTML = `<i class="fa-solid fa-user"></i> ${state.username !== "Votre nom" ? state.username : "French Rider"}`;
1183:       document.getElementById("map-loading").style.display = "flex";
1184:     maxPoints = 505; // France (101 departments * 5)
1185:         fetch("france_departements.geojson").then(res => res.json()),
1186:   const floatingName = document.getElementById("lbl-floating-name");
1187:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
1188:     maxPoints = 535; // Italy (107 provinces * 5)
1189:       // Setup small local projection for the inset box
1190:   // 3. Draw 5 Overseas Insets (Okinawa-style) stacked vertically on the left side (outside mapG so they stay fixed!)
1191:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
1192:     const exploredCount = Object.values(state.levels).filter(l => l >= 3).length;
1193:     const nameHtml = `<span style="${isDefault ? 'border-bottom: 1px dashed rgba(255,255,255,0.7); opacity: 0.9;' : 'font-weight: 800; border-bottom: 1px solid rgba(255,255,255,0.5);'}">${displayName} <i class="fa-solid fa-pen" style="font-size: 0.7em;"></i></span>`;
1194:         toast("Erreur de chargement de la carte de France.");
1195:         document.getElementById("map-loading").style.display = "none";
1196:     const exploredCount = Object.values(state.levels).filter(l => l >= 3).length;
1197:     const nameHtml = `<span style="${isDefault ? 'border-bottom: 1px dashed rgba(255,255,255,0.7); opacity: 0.9;' : 'font-weight: 800; border-bottom: 1px solid rgba(255,255,255,0.5);'}">${displayName} <i class="fa-solid fa-pen" style="font-size: 0.7em;"></i></span>`;
1198:   document.getElementById("card-max-score").textContent = `/ ${maxPoints} pts`;
1199:         .attr("fill", COLORS[state.levels[dt.code] || 0])
1200:       floatingName.innerHTML = t.exploredSpain(nameHtml, exploredCount);
1201:   const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];
1202:       floatingName.innerHTML = t.exploredFrance(nameHtml, exploredCount);
1203:     const savedBtnBottom = floatingBtn ? floatingBtn.style.bottom : null;
1204:     const savedBtnTransform = floatingBtn ? floatingBtn.style.transform : null;
1205:     const savedHeaderPaddingTop = header ? header.style.paddingTop : null;
1206:     userWatermark.innerHTML = `<i class="fa-solid fa-user"></i> ${state.username !== "Votre nom" ? state.username : "French Rider"}`;
1207:     if (btn.dataset.val === state.currentMap) {
1208:       floatingName.innerHTML = t.exploredWorld(nameHtml, exploredCount);
1209:   // Update floating profile button text dynamically
1210:   const floatingName = document.getElementById("lbl-floating-name");
1211:   const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1212:   const countries = countriesGeoJson.features.filter(d => d.id !== "010"); // Exclude Antarctica
1213:           document.getElementById("map-loading").style.display = "none";
1214:   const el = document.getElementById("toast");
1215:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
1216:   el._t = setTimeout(() => el.classList.remove("show"), 2500);
1217:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
1218:   el._t = setTimeout(() => el.classList.remove("show"), 2500);
1219:       .text(`${dt.code} - ${state.lang === "ja" ? dt.nameJa : dt.name}`);
1220:     const exploredCount = Object.values(state.levels).filter(l => l >= 3).length;
1221: // ── Build SVG Proportional Cartogram Map ────────────────────
1222:     const feature = franceDomTomData.features.find(f => f.properties.code === dt.code);
1223:     const nameHtml = `<span style="${isDefault ? 'border-bottom: 1px dashed rgba(255,255,255,0.7); opacity: 0.9;' : 'font-weight: 800; border-bottom: 1px solid rgba(255,255,255,0.5);'}">${displayName} <i class="fa-solid fa-pen" style="font-size: 0.7em;"></i></span>`;
1224:   if (btnLang) btnLang.innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1225:         .attr("class", "cell-group")
1226:           updateHeader(); // Recalculate accurate max score with actual country count
1227:     if(b.dataset.val === val) b.classList.add("selected");
1228:       floatingName.innerHTML = t.exploredFrance(nameHtml, exploredCount);
1229:           console.error("Error loading world map data:", err);
1230:       floatingName.innerHTML = t.exploredSpain(nameHtml, exploredCount);
1231:           document.getElementById("map-loading").style.display = "none";
1232:       floatingName.innerHTML = t.exploredItaly(nameHtml, exploredCount);
1233:       const localProjection = d3.geoMercator()
1234:         .fitExtent([[OX + 6, OY + 6], [OX + OW - 6, OY + OH - 20]], feature);
1235:   if (state.currentMap === "jp") {
1236:       const localPath = d3.geoPath().projection(localProjection);
1237:           console.error("Error loading Japan map data:", err);
1238:           toast("Erreur de chargement de la carte du Japon.");
1239:           document.getElementById("map-loading").style.display = "none";
1240:           toast("Erreur de chargement de la carte du Japon.");
1241:           document.getElementById("map-loading").style.display = "none";
1242:   // Initialize missing levels for Japan prefectures
1243:         legend.style.paddingBottom = savedLegendPaddingBottom;
1244:   el._t = setTimeout(() => el.classList.remove("show"), 2500);
1245:     if (franceDepsData && franceDomTomData) {
1246:       document.getElementById("map-loading").style.display = "flex";
1247:       const mapName = state.currentMap === "jp" ? "japan" : "world";
1248:       a.download = `maplevel_${mapName}_${state.username.replace(/\\W/g, "_")}.png`;
1249:         fetch("france_domtom.geojson").then(res => res.json())
1250:         fetch("france_departements.geojson").then(res => res.json()),
1251:   const prefecturesGeoJSON = topojson.feature(japanData, japanData.objects.prefectures);
1252:         franceDomTomData = domtom;
1253:   const total = Object.values(state.levels).reduce((a, b) => a + b, 0);
1254:   document.getElementById("card-level").textContent = "Ride the world";
1255:   document.getElementById("card-score").textContent = total;
1256:   const okinawaFeature = prefecturesGeoJSON.features.find(f => f.id === "47");
1257:         toast("Erreur de chargement de la carte de France.");
1258:         document.getElementById("map-loading").style.display = "none";
1259:         floatingBtn.style.transform = savedBtnTransform;
1260:         document.getElementById("map-loading").style.display = "none";
1261:       floatingName.innerHTML = t.exploredWorld(nameHtml, exploredCount);
1262:         header.style.paddingTop = savedHeaderPaddingTop;
1263:     maxPoints = 535; // Italy (107 provinces * 5)
1264:   } else if (state.currentMap === "us") {
1265:       document.getElementById("map-loading").style.display = "flex";
1266:   } else if (state.currentMap === "world") {
1267:       document.getElementById("map-loading").style.display = "flex";
1268:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1269:       const countries = countriesGeoJson.features.filter(d => d.id !== "010");
1270:       maxPoints = countries.length * 5;
1271:   el._t = setTimeout(() => el.classList.remove("show"), 2500);
1272:       maxPoints = 885; // estimate
1273:           updateHeader();
1274: // ── Build SVG Proportional Cartogram Map ────────────────────
1275:   document.getElementById("card-max-score").textContent = `/ ${maxPoints} pts`;
1276:           document.getElementById("map-loading").style.display = "none";
1277:           toast("Error loading Spain map.");
1278:           document.getElementById("map-loading").style.display = "none";
1279:   if (state.currentMap === "jp") {
1280:   // Update traveler watermark dynamically
1281:   const userWatermark = document.getElementById("card-user-watermark");
1282:     if (italyProvincesData) {
1283:     userWatermark.innerHTML = `<i class="fa-solid fa-user"></i> ${state.username !== "Votre nom" ? state.username : "French Rider"}`;
1284:       fetch("world.json")
1285:       document.getElementById("map-loading").style.display = "flex";
1286:   // Update floating profile button text dynamically
1287:   const floatingName = document.getElementById("lbl-floating-name");
1288:           drawWorldMap();
1289:           updateHeader(); // Recalculate accurate max score with actual country count
1290:     let isDefault = false;
1291:           updateHeader();
1292:     if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
1293:           toast("Erreur de chargement de la carte du Japon.");
1294:           document.getElementById("map-loading").style.display = "none";
1295:           toast("Erreur de chargement de la carte d'Italie.");
1296:           document.getElementById("map-loading").style.display = "none";
1297:     const exploredCount = Object.values(state.levels).filter(l => l >= 3).length;
1298:     const nameHtml = `<span style="${isDefault ? 'border-bottom: 1px dashed rgba(255,255,255,0.7); opacity: 0.9;' : 'font-weight: 800; border-bottom: 1px solid rgba(255,255,255,0.5);'}">${displayName} <i class="fa-solid fa-pen" style="font-size: 0.7em;"></i></span>`;
1299:       drawFranceMap();
1300:     if (state.currentMap === "jp") {
1301:       document.getElementById("map-loading").style.display = "flex";
1302:     } else if (state.currentMap === "fr") {
1303:       floatingName.innerHTML = t.exploredFrance(nameHtml, exploredCount);
1304:         fetch("france_domtom.geojson").then(res => res.json())
1305:       floatingName.innerHTML = t.exploredSpain(nameHtml, exploredCount);
1306:     } else if (state.currentMap === "it") {
1307:         const fs = Math.max(5.5, Math.min(8.5, Math.sqrt(area) * 0.15));
1308:     } else if (state.currentMap === "us") {
1309:           updateHeader(); // Recalculate accurate max score with actual country count
1310:           .attr("class", "cell-label-world")
1311:       floatingName.innerHTML = t.exploredWorld(nameHtml, exploredCount);
1312:           console.error("Error loading world map data:", err);
1313:         document.getElementById("map-loading").style.display = "none";
1314:           document.getElementById("map-loading").style.display = "none";
1315:           .attr("font-family", "'Outfit', sans-serif")
1316:   } else if (state.currentMap === "es") {
1317:   const el = document.getElementById("toast");
1318:           .attr("fill", "rgba(26,37,51,0.85)")
1319:           .attr("pointer-events", "none")
1320:   document.getElementById("modal-close").addEventListener("click", closeModal);
1321:   document.getElementById("modal-overlay").addEventListener("click", e => {
1322:     if (e.target.id === "modal-overlay") closeModal();
1323:   svg.attr("viewBox", `0 0 ${W} ${H}`);
1324: // ── Build SVG Proportional Cartogram Map ────────────────────
1325:   document.getElementById("map-loading").style.display = "none";
1326:     btn.addEventListener("click", () => {
1327:     const code = String(i).padStart(2, '0');
1328: function getCountryDisplayName(code) {
1329:           console.error("Error loading Spain map data:", err);
1330:     return state.lang === "ja" ? NAMES_JA[code] : NAMES_EN[code];
1331:           document.getElementById("map-loading").style.display = "none";
1332:     return `${code} - ${DEPARTEMENTS_FR[code] || code}`;
1333:       const g = document.querySelector(`.cell-group[data-code="${activePrefCode}"]`);
1334:   } else if (state.currentMap === "it") {
1335:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1336:       const feature = countriesGeoJson.features.find(f => f.id === code);
1337:           japanData = data;
1338:           const targetElement = g.querySelector(".cell-rect, .cell-path");
1339:           if (targetElement) targetElement.setAttribute("fill", COLORS[lvl]);
1340:         .then(res => res.json())
1341:         .then(data => {
1342:         // Also support selection via path selector direct mapping (World Map fallback)
1343:         const cellPath = document.querySelector(`path.cell-path[data-code="${activePrefCode}"]`);
1344:           document.getElementById("map-loading").style.display = "none";
1345: // ── Modal level selection ────────────────────────────────────
1346: function openModal(code) {
1347:           console.error("Error loading Italy map data:", err);
1348:           toast("Erreur de chargement de la carte d'Italie.");
1349:           document.getElementById("map-loading").style.display = "none";
1350:       const name = getCountryDisplayName(activePrefCode);
1351:       const lbls = ["Jamais", "Passé", "Escale", "Visité", "Séjourné", "Habi
1352:       Promise.all([
1353:         fetch("france_departements.geojson").then(res => res.json()),
1354:         fetch("france_domtom.geojson").then(res => res.json())
1355:       ]).then(([deps, domtom]) => {
1356:       document.getElementById("map-loading").style.display = "flex";
1357:         franceDomTomData = domtom;
1358:         .then(res => res.json())
1359:         .then(data => {
1360:           worldData = data;
1361:           drawWorldMap();
1362:           updateHeader(); // Recalculate accurate max score with actual country count
1363:         })
1364:         .catch(err => {
1365:           console.error("Error loading world map data:", err);
1366:           toast("Error loading map data.");
1367:           document.getElementById("map-loading").style.display = "none";
1368:         });
1369:     }
1370:   }
1371: }
1372: 
1373: function drawJapanMap() {
1374:   const svg = d3.select("#map-svg");
1375:       if (newMap !== state.currentMap) {
1376:         if (state.currentMap === "jp") {
1377:           state.jpLevels = state.levels;
1378:         } else {
1379:           state.worldLevels = state.levels;
1380:         }
1381:         
1382:         state.currentMap = newMap;
1383:         state.levels = newMap === "jp" ? state.jpLevels : state.worldLevels;
1384:         saveState();
1385:         
1386:         updateUITranslations();
1387:         buildMap();
1388:       }
1389:       
1390:       countryOverlay.classList.add("hidden");
1391:     });
1392:   });
1393: 
1394:   // Language Modal
1395:   const langOverlay = document.getElementById("lang-overlay");
1396:   document.getElementById("btn-lang-select").addEventListener("click", () => {
1397:           console.error("Error loading Italy map data:", err);
1398:           toast("Erreur de chargement de la carte d'Italie.");
1399:   document.getElementById("lang-close").addEventListener("click", () => {
1400:     langOverlay.classList.add("hidden");
1401:   const countryOverlay = document.getElementById("country-overlay");
1402:   document.getElementById("btn-country-select").addEventListener("click", () => {
1403:     if (e.target.id === "lang-overlay") langOverlay.classList.add("hidden");
1404:       drawUSAMap();
1405:   document.getElementById("country-close").addEventListener("click", () => {
1406:       document.getElementById("map-loading").style.display = "flex";
1407:     btn.addEventListener("click", () => {
1408:       document.querySelectorAll(".lang-btn").forEach(b => b.classList.remove("selected"));
1409:     if (e.target.id === "country-overlay") countryOverlay.classList.add("hidden");
1410:           usaStatesData = data;
1411:       const val = btn.dataset.val;
1412:   document.querySelectorAll(".country-btn").forEach(btn => {
1413:     btn.addEventListener("click", () => {
1414:       if (btn.hasAttribute("disabled")) return;
1415:       document.querySelectorAll(".country-btn").forEach(b => b.classList.remove("selected"));
1416:           toast("Erreur de chargement de la carte des USA.");
1417:           document.getElementById("map-loading").style.display = "none";
1418:       if(val === "hi") txt = "🇮🇳 हिन्दी";
1419:       if (newMap !== state.currentMap) {
1420:         if (state.currentMap === "jp") {
1421:           state.jpLevels = state.levels;
1422:       document.getElementById("btn-lang-select").innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1423:           state.worldLevels = state.levels;
1424:       document.getElementById("map-loading").style.display = "flex";
1425:       updateUITranslations();
1426:       langOverlay.classList.add("hidden");
1427:         state.levels = newMap === "jp" ? state.jpLevels : state.worldLevels;
1428:           worldData = data;
1429:           drawWorldMap();
1430:           updateHeader(); // Recalculate accurate max score with actual country count
1431:   const btnFloatingProfile = document.getElementById("btn-floating-profile");
1432:   if (btnFloatingProfile) {
1433:           console.error("Error loading world map data:", err);
1434:       const n = prompt("Votre prénom/pseudo :", state.username === "Votre nom" ? "" : state.username);
1435:           document.getElementById("map-loading").style.display = "none";
1436:         state.username = n.trim() || "Votre nom";
1437:         saveState();
1438:         updateHeader();
1439:         toast("Nom mis à jour !");
1440:       }
1441:     langOverlay.classList.remove("hidden");
1442:   const svg = d3.select("#map-svg");
1443:   document.getElementById("lang-close").addEventListener("click", () => {
1444:     langOverlay.classList.add("hidden");
1445:   document.getElementById("btn-export").addEventListener("click", () => {
1446:     document.getElementById("export-overlay").classList.remove("hidden");
1447:     if (e.target.id === "lang-overlay") langOverlay.classList.add("hidden");
1448:   });
1449:   document.getElementById("export-overlay").addEventListener("click", e => {
1450:   document.querySelectorAll(".lang-btn").forEach(btn => {
1451:       document.getElementById("export-overlay").classList.add("hidden");
1452:       document.querySelectorAll(".lang-btn").forEach(b => b.classList.remove("selected"));
1453:         floatingBtn.style.transform = savedBtnTransform;
1454:       }
1455:       const val = btn.dataset.val;
1456:     document.getElementById("export-overlay").classList.add("hidden");
1457:     const card = document.getElementById("export-card");
1458:     const mapSvg = document.getElementById
1459:         legend.style.paddingBottom = savedLegendPaddingBottom;
1460:       if(val === "es") txt = "🇪🇸 Español";
1461:       if(val === "fr") txt = "🇫🇷 Français";
1462:       if(val === "hi") txt = "🇮🇳 हिन्दी";
1463:       if(val === "ja") txt = "🇯🇵 日本語";
1464:       if(val === "ko") txt = "🇰🇷 한국어";
1465:   document.getElementById("btn-dl-anyway").addEventListener("click", doExport);
1466:       document.getElementById("btn-lang-select").innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
1467:     toast("🙏 Merci !");
1468:       buildMap();
1469:       updateUITranslations();
1470:       langOverlay.classList.add("hidden");
1471:   // Reset
1472:   document.getElementById("btn-reset").addEventListener("click", () => {
1473:     if (!confirm("Réinitialiser toute la carte ?")) return;
1474:     Object.keys(state.levels).forEach(c => state.levels[c] = 0);
1475:   const btnFloatingProfile = document.getElementById("btn-floating-profile");
1476:   if (btnFloatingProfile) {
1477:     btnFloatingProfile.addEventListener("click", () => {
1478:     document.querySelectorAll(".cell-rect, .cell-path").forEach(r => r.setAttribute("fill", COLORS[0]));
1479:       if (n !== null) {
1480:         state.username = n.trim() || "Votre nom";
1481:   });
1482: }
1483: 
1484: // ── INIT ─────────────────────────────────────────────────────
1485: document.addEventListener("DOMContentLoaded", () => {
1486:       legend.style.paddingBottom = "51px";
1487:   updateHeader();
1488:   setupEvents();
1489:     html2canvas(card, {
1490:       scale: 3,
1491:       useCORS: true,
1492:       logging: false,
1493: with open("app.js", "w", encoding="utf-8") as f:
1494:     f.write(app_js_content)
1495: print("app.js updated successfully!")
1496:       card.style.width = savedCardWidth;
1497:       mapSvg.style.transform = savedSvgTransform;
1498:       console.error(err);
1499:         floatingBtn.style.bottom = savedBtnBottom;
1500:         floatingBtn.style.transform = savedBtnTransform;
1501:       mapSvg.style.transform = savedSvgTransform;
1502:       if (floatingBtn) {
1503:         header.style.paddingTop = savedHeaderPaddingTop;
1504:         floatingBtn.style.transform = savedBtnTransform;
1505:       if (legend) {
1506:         legend.style.paddingBottom = savedLegendPaddingBottom;
1507:         header.style.paddingTop = savedHeaderPaddingTop;
1508:       }
1509:       const a = document.createElement("a");
1510:       const mapName = state.currentMap === "jp" ? "japan" : (state.currentMap === "fr" ? "france" : "world");
1511:       a.download = `maplevel_${mapName}_${state.username.replace(/\W/g, "_")}.png`;
1512:       a.href = canvas.toDataURL("image/png");
1513:       a.click();
1514:       toast("🎉 Image enregistrée !");
1515:     }).catch((err) => {
1516:   document.getElementById("btn-dl-anyway").addEventListener("click", doExport);
1517:   document.getElementById("btn-dl-shared").addEventListener("click", () => {
1518:       card.style.width = savedCardWidth;
1519:       mapSvg.style.transform = savedSvgTransform;
1520:       if (floatingBtn) {
1521:         floatingBtn.style.bottom = savedBtnBottom;
1522:         floatingBtn.style.transform = savedBtnTransform;
1523:   document.getElementById("btn-reset").addEventListener("click", () => {
1524:     if (!confirm("Réinitialiser toute la carte ?")) return;
1525:     Object.keys(state.levels).forEach(c => state.levels[c] = 0);
1526:     saveState();
1527:       if (legend) {
1528:         legend.style.paddingBottom = savedLegendPaddingBottom;
1529:     document.querySelectorAll(".cell-rect, .cell-path").forEach(r => r.setAttribute("fill", COLORS[0]));
1530:       toast("Erreur d'export.");
1531:     toast("Carte réinitialisée !");
1532:   });
1533: }
1534:   document.getElementById("btn-dl-anyway").addEventListener("click", doExport);
1535:   document.getElementById("btn-dl-shared").addEventListener("click", () => {
1536: document.addEventListener("DOMContentLoaded", () => {
1537:     doExport();
1538:   updateHeader();
1539:   setupEvents();
1540:   buildMap();
1541:   document.getElementById("btn-reset").addEventListener("click", () => {
1542:     if (!confirm("Réinitialiser toute la carte ?")) return;
1543:     Object.keys(state.levels).forEach(c => state.levels[c] = 0);
1544: with open("app.js", "w", encoding="utf-8") as f:
1545:     f.write(app_js_content)
1546: print("app.js updated successfully!")
1547:     document.querySelectorAll(".cell-rect, .cell-path").forEach(r => r.setAttribute("fill", COLORS[0]));
1548:     updateHeader();
1549:     toast("Carte réinitialisée !");
1550:         .attr("height", OH)
1551:         .attr("fill", "rgba(0,0,0,0)")
1552:   const tutoOverlay = document.getElementById("tutorial-overlay");
1553: // ── INIT ─────────────────────────────────────────────────────
1554: document.addEventListener("DOMContentLoaded", () => {
1555:     const closeBtn = document.getElementById("btn-tuto-close");
1556:     if (closeBtn) {
1557:   document.getElementById("map-loading").style.display = "none";
1558:         tutoOverlay.classList.add("hidden");
1559:       });
1560:   // Show tutorial modal on load
1561:   const tutoOverlay = document.getElementById("tutorial-overlay");
1562:   const svg = d3.select("#map-svg");
1563:     tutoOverlay.classList.remove("hidden");
1564:     const closeBtn = document.getElementById("btn-tuto-close");
1565: with open("app.js", "w", encoding="utf-8") as f:
1566:   // Initialize missing levels for Spain provinces
1567:   Object.keys(PROVINCES_ES).forEach(code => {
1568:     if (state.levels[code] == null) {
1569:       state.levels[code] = 0;
1570:     }
1571:   });
1572: 
1573:   // Separate mainland from Canary Islands
1574:   const mainlandFeatures = spainProvincesData.features.filter(f => {
1575:     const code = f.properties.cod_prov;
1576:     return code !== "35" && code !== "38"; // Exclude Las Palmas and S.C. Tenerife
1577:   });
1578:   const canaryFeatures = spainProvincesData.features.filter(f => {
1579:     const code = f.properties.cod_prov;
1580:   document.getElementById("map-loading").style.display = "none";
1581:   });
1582: function drawWorldMap() {
1583:   const svg = d3.select("#map-svg");
1584:   const svg = d3.select("#map-svg");
1585:   svg.attr("viewBox", `0 0 ${W} ${H}`);
1586:   svg.attr("viewBox", `0 0 ${W} ${H}`);
1587:   const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1588:   const countries = countriesGeoJson.features.filter(d => d.id !== "010"); // Exclude Antarctica
1589:   const countries = countriesGeoJson.features.filter(d => d.id !== "010"); // Exclude Antarctica
1590:     .attr("id", "spain-group");
1591:   const projection = d3.geoMercator()
1592:     .fitExtent([[10, 50], [550, 530]], countriesGeoJson);
1593:     .fitExtent([[10, 50], [550, 530]], countriesGeoJson);
1594:   const pathGenerator = d3.geoPath().projection(projection);
1595:   const pathGenerator = d3.geoPath().projection(projection);
1596:   const pathGenerator = d3.geoPath().projection(projection);
1597:   const mapG = svg.append("g");
1598:   // Initialize missing levels
1599:   mapG.selectAll(".spain-path")
1600:     if (state.levels[d.id] == null) {
1601:     if (state.levels[d.id] == null) {
1602:       state.levels[d.id] = 0;
1603:     .attr("class", "cell-group cell-path spain-path")
1604:   // Show tutorial modal on load
1605:   const tutoOverlay = document.getElementById("tutorial-overlay");
1606:   mapG.selectAll("path")
1607:     tutoOverlay.classList.remove("hidden");
1608:     .data(countries)
1609:     const closeTuto = () => {
1610:       tutoOverlay.classList.add("hidden");
1611:     .attr("class", "cell-group cell-path")
1612:     .attr("data-code", d => d.id)
1613:     const closeBtn = document.getElementById("btn-tuto-close");
1614:     if (closeBtn) closeBtn.addEventListener("click", closeTuto);
1615:     .attr("stroke", "#ffffff")
1616:     const headerCloseBtn = document.getElementById("btn-tuto-header-close");
1617:     if (headerCloseBtn) headerCloseBtn.addEventListener("click", closeTuto);
1618:     .on("click", (event, d) => {
1619:       openModal(d.id);
1620:     });
1621:   // Add labels for larger countries
1622: with open("app.js", "w", encoding="utf-8") as f:
1623:     const area = pathGenerator.area(d);
1624:     const area = pathGenerator.area(d);
1625:       const centroid = pathGenerator.centroid(d);
1626:       if (centroid && !isNaN(centroid[0]) && !isNaN(centroid[1])) {
1627:       if (centroid && !isNaN(centroid[0]) && !isNaN(centroid[1])) {
1628:         const fs = Math.max(5.5, Math.min(8.5, Math.sqrt(area) * 0.15));
1629:         const fs = Math.max(5.5, Math.min(8.5, Math.sqrt(area) * 0.15));
1630:         mapG.append("text")
1631:           .attr("class", "cell-label-world")
1632:           .attr("class", "cell-label-world")
1633:           .attr("x", centroid[0])
1634:           .attr("text-anchor", "middle")
1635:           .attr("dominant-baseline", "middle")
1636:           .attr("font-family", "'Outfit', sans-serif")
1637:           .attr("font-family", "'Outfit', sans-serif")
1638:           .attr("font-size", fs + "px")
1639:           .attr("fill", "rgba(26,37,51,0.85)")
1640:           .attr("fill", "rgba(26,37,51,0.85)")
1641:           .attr("pointer-events", "none")
1642:           .text(name);
1643:       }
1644:     }
1645:   });
1646:   document.getElementById("map-loading").style.display = "none";
1647:   document.getElementById("map-loading").style.display = "none";
1648: }
1649: function getCountryDisplayName(code) {
1650: function getCountryDisplayName(code) {
1651:     return state.lang === "ja" ? NAMES_JA[code] : NAMES_EN[code];
1652:   } else if (state.currentMap === "fr") {
1653:     return `${code} - ${DEPARTEMENTS_FR[code] || code}`;
1654:   } else if (state.currentMap === "es") {
1655:         clientX = event.changedTouches[0].clientX;
1656:       } else {
1657:         clientX = event.clientX;
1658:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1659:       const feature = countriesGeoJson.features.find(f => f.id === code);
1660:       const xInSvg = ((clientX - rect.left) / rect.width) * 560;
1661:       return !event.ctrlKey && (!event.type.startsWith("mouse") || event.button === 0) && xInSvg >= 92;
1662:       }
1663:     .on("zoom", (event) => {
1664:       mapG.attr("transform", event.transform);
1665:     });
1666: }
1667:   svg.call(zoomBehavior);
1668: // ── Modal level selection ────────────────────────────────────
1669:   // 3. Draw Canary Islands as insets (fixed, not zoomed)
1670:   activePrefCode = code;
1671:     { code: "35", name: "Las Palmas", y: 420 },
1672:   document.getElementById("modal-title").textContent = `@ ${name}`;
1673:   const cur = state.levels[code] || 0;
1674:   document.querySelectorAll(".opt-btn").forEach(btn => {
1675:     btn.classList.toggle("selected", +btn.dataset.level === cur);
1676:     const OX = 12 + idx * 50, OY = island.y, OW = 45, OH = 80;
1677:   document.getElementById("modal-overlay").classList.remove("hidden");
1678:     // Inset box
1679:     svg.append("rect")
1680:       .attr("x", OX).attr("y", OY).attr("width", OW).attr("height", OH)
1681:   document.getElementById("modal-overlay").classList.add("hidden");
1682:       .attr("stroke", "rgba(255, 255, 255, 0.35)")
1683:       .attr("stroke-width", 1.2)
1684:       .attr("rx", 4);
1685: // ── Event Setup ──────────────────────────────────────────────
1686: function setupEvents() {
1687:   document.getElementById("modal-close").addEventListener("click", closeModal);
1688:   document.getElementById("modal-overlay").addEventListener("click", e => {
1689:     if (e.target.id === "modal-overlay") closeModal();
1690:       .attr("text-anchor", "middle")
1691:       .attr("font-family", "'Outfit', sans-serif")
1692:   document.querySelectorAll(".opt-btn").forEach(btn => {
1693:     btn.addEventListener("click", () => {
1694:       .attr("fill", "rgba(255, 255, 255, 0.8)")
1695:       const lvl = +btn.dataset.level;
1696:       state.levels[activePrefCode] = lvl;
1697:     const feature = spainProvincesData.features.find(f => f.properties.cod_prov === island.code);
1698:     if (feature) {
1699:       // Update cell rect/path color dynamically
1700:       const g = document.querySelector(`.cell-group[data-code="${activePrefCode}"]`);
1701:         .attr("data-code", island.code)
1702:         .style("cursor", "pointer")
1703:     .attr("class", "cell-label")
1704:     .attr("data-code", d => d.properties.cod_prov)
1705:     .attr("x", d => {
1706:       const centroid = pathGenerator.centroid(d);
1707:       const localProjection = d3.geoMercator()
1708:         .fitExtent([[OX + 4, OY + 4], [OX + OW - 4, OY + OH - 18]], feature);
1709:       const localPath = d3.geoPath().projection(localProjection);
1710:       const centroid = pathGenerator.centroid(d);
1711:       return centroid ? centroid[1] : 0;
1712:         .attr("class", "cell-path")
1713:         .attr("data-code", island.code)
1714:     .attr("dominant-baseline", "middle")
1715:         .attr("fill", COLORS[state.levels[island.code] || 0])
1716:         .attr("stroke", "#ffffff")
1717:         .attr("stroke-width", 0.7);
1718:     .attr("fill", "rgba(26,37,51,0.85)")
1719:     .attr("pointer-events", "none")
1720:         .attr("x", OX).attr("y", OY)
1721:         .attr("width", OW).attr("height", OH)
1722:         .attr("fill", "rgba(0,0,0,0)")
1723:         .attr("pointer-events", "all")
1724:       if (name.includes('/')) return name.split('/')[1] || name.split('/')[0];
1725:       return name;
1726:     });
1727: 
1728:   document.getElementById("map-loading").style.display = "none";
1729:   const zoomBehavior = d3.zoom()
1730:     .scaleExtent([1, 8])
1731: function drawWorldMap() {
1732:       const svgNode = document.getElementById("map-svg");
1733:       if (!svgNode) return false;
1734:   svg.attr("viewBox", `0 0 ${W} ${H}`);
1735:       if (event.touches && event.touches.length > 0) {
1736:   const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1737:   const countries = countriesGeoJson.features.filter(d => d.id !== "010"); // Exclude Antarctica
1738:         clientX = event.changedTouche
1739:   // Project and fit extent
1740:   const projection = d3.geoMercator()
1741:     .fitExtent([[10, 50], [550, 530]], countriesGeoJson);
1742: 
1743:   const pathGenerator = d3.geoPath().projection(projection);
1744: 
1745:   const mapG = svg.append("g");
1746: 
1747:   // Initialize missing levels
1748:   countries.forEach(d => {
1749:     if (state.levels[d.id] == null) {
1750:       state.levels[d.id] = 0;
1751:     }
1752:   });
1753: 
1754:   // Render countries
1755:     { code: "38", name: "S.C. Tenerife", y: 420 }
1756:     .data(countries)
1757:     .enter()
1758:   canaries.forEach((island, idx) => {
1759:     const OX = 12 + idx * 50, OY = island.y, OW = 45, OH = 80;
1760:     .attr("data-code", d => d.id)
1761:     .attr("d", pathGenerator)
1762:     .attr("fill", d => COLORS[state.levels[d.id] || 0])
1763:       .attr("x", OX).attr("y", OY).attr("width", OW).attr("height", OH)
1764:       .attr("fill", "rgba(255, 255, 255, 0.05)")
1765:       .attr("stroke", "rgba(255, 255, 255, 0.35)")
1766:     .on("click", (event, d) => {
1767:       if (event.defaultPrevented) return; // Ignore drag clicks
1768:       openModal(d.id);
1769:     // Inset label
1770:   // Add labels for larger countries
1771:   // Add labels for larger countries
1772:     const area = pathGenerator.area(d);
1773:     const area = pathGenerator.area(d);
1774:       .attr("font-family", "'Outfit', sans-serif")
1775:       if (centroid && !isNaN(centroid[0]) && !isNaN(centroid[1])) {
1776:       if (centroid && !isNaN(centroid[0]) && !isNaN(centroid[1])) {
1777:       const baseFs = Math.max(2.5, Math.min(8.5, Math.sqrt(area) * 0.15));
1778:         const fs = Math.max(5.5, Math.min(8.5, Math.sqrt(area) * 0.15));
1779:         mapG.append("text")
1780:     const feature = spainProvincesData.features.find(f => f.properties.cod_prov === island.code);
1781:           .attr("class", "cell-label-world")
1782:       const gInset = svg.append("g")
1783:           .attr("text-anchor", "middle")
1784:           .attr("dominant-baseline", "middle")
1785:           .attr("font-family", "'Outfit', sans-serif")
1786:           .attr("font-family", "'Outfit', sans-serif")
1787:         .attr("font-family", "'Outfit', sans-serif")
1788:           .attr("fill", "rgba(26,37,51,0.85)")
1789:           .attr("fill", "rgba(26,37,51,0.85)")
1790:       const localProjection = d3.geoMercator()
1791:         .fitExtent([[OX + 4, OY + 4], [OX + OW - 4, OY + OH - 18]], feature);
1792:       const localPath = d3.geoPath().projection(localProjection);
1793:         .text(name);
1794:       gInset.append("path")
1795:   document.getElementById("map-loading").style.display = "none";
1796:         .attr("data-code", island.code)
1797:         .attr("d", localPath(feature))
1798:         .attr("fill", COLORS[state.levels[island.code] || 0])
1799:   if (state.currentMap === "jp") {
1800:     return state.lang === "ja" ? NAMES_JA[code] : NAMES_EN[code];
1801:       if (!svgNode) return false;
1802:       gInset.append("rect")
1803:         .attr("x", OX).attr("y", OY)
1804:       if (event.touches && event.touches.length > 0) {
1805:         clientX = event.touches[0].clientX;
1806:       } else if (event.changedTouches && event.changedTouches.length > 0) {
1807:         clientX = event.changedTouches[0].clientX;
1808:       } else {
1809:         clientX = event.clientX;
1810:       }
1811:   document.getElementById("map-loading").style.display = "none";
1812:       const rect = svgNode.getBoundingClientRect();
1813:       const xInSvg = ((clientX - rect.left) / rect.width) * 560;
1814: function drawWorldMap() {
1815:       return !event.ctrlKey && (!event.type.startsWith("mouse") || event.button === 0) && xInSvg >= 0;
1816:   const svg = d3.select("#map-svg");
1817:   svg.attr("viewBox", `0 0 ${W} ${H}`);
1818:       mapG.attr("transform", event.transform);
1819:   const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1820:   const countries = countriesGeoJson.features.filter(d => d.id !== "010"); // Exclude Antarctica
1821:   Object.keys(PROVINCES_IT).forEach(code => {
1822:     if (state.levels[code] == null) {
1823:   document.getElementById("map-loading").style.display = "none";
1824:     .fitExtent([[10, 50], [550, 530]], countriesGeoJson);
1825:   });
1826:   const pathGenerator = d3.geoPath().projection(projection);
1827:   // Create zoomable group
1828:   const mapG = svg.append("g");
1829:     .attr("id", "italy-group");
1830:   // Initialize missing levels
1831:   // Project and fit extent (covers mainland, Sicily, and Sardinia)
1832:   // Using d3.geoMercator() centered around Rome, fits perfectly
1833:   const projection = d3.geoMercator()
1834:     .center([12.5, 41.9])
1835:     .fitExtent([[60, 30], [500, 520]], italyProvincesData);
1836: 
1837:   const pathGenerator = d3.geoPath().projection(projection);
1838:   mapG.selectAll("path")
1839:   // Render provinces
1840:   mapG.selectAll(".italy-path")
1841:     .data(italyProvincesData.features)
1842:     .attr("class", "cell-group cell-path")
1843:     .attr("data-code", d => d.id)
1844:     .attr("class", "cell-group cell-path italy-path")
1845:     .attr("fill", d => COLORS[state.levels[d.id] || 0])
1846:     .attr("stroke", "#ffffff")
1847:     .attr("fill", d => COLORS[state.levels[d.properties.prov_acr] || 0])
1848:     .style("cursor", "pointer")
1849:     .on("click", (event, d) => {
1850:       if (event.defaultPrevented) return; // Ignore drag clicks
1851:     .on("click", (event, d) => {
1852:       if (event.defaultPrevented) return;
1853:       openModal(d.properties.prov_acr);
1854:   // Manual centroid overrides for countries where the auto-centroid is misleading
1855:   // (due to overseas territories, large landmasses like Alaska, etc.)
1856:   const CENTROID_OVERRIDES = {
1857:     "840": [-97, 38],     // USA → center of contiguous US
1858:     "250": [2.5, 46.5],   // France → metropolitan France
1859:     "643": [55, 60],      // Russia → shifted west for readability
1860:     "578": [10, 62],      // Norway → mainland Norway
1861:     .attr("class", "cell-label")
1862:     .attr("data-code", d => d.properties.prov_acr)
1863:     .attr("x", d => {
1864:       const centroid = pathGenerator.centroid(d);
1865:       return centroid ? centroid[0] : 0;
1866:     })
1867:     .attr("y", d => {
1868:       const centroid = pathGenerator.centroid(d);
1869:       return centroid ? centroid[1] : 0;
1870:     })
1871:     .attr("text-anchor", "middle")
1872:     .attr("dominant-baseline", "middle")
1873:     .attr("font-family", "'Outfit', sans-serif")
1874:     .attr("font-size", "4px")
1875:     .attr("font-weight", "800")
1876:     .attr("fill", "rgba(26,37,51,0.85)")
1877:     .attr("pointer-events", "none")
1878:     .text(d => d.properties.prov_acr);
1879: 
1880:   // Setup D3 Zoom & Pinch
1881:   const zoomBehavior = d3.zoom()
1882:     .scaleExtent([1, 8])
1883:     .filter((event) => {
1884:       const svgNode = document.getElementById("map-svg");
1885:       if (!svgNode) return false;
1886:       let clientX = 0;
1887:       if (event.touches && event.touches.length > 0) {
1888:         clientX = event.touches[0].clientX;
1889:       } else if (event.changedTouches && event.changedTouches.length > 0) {
1890:         clientX = event.changedTouches[0].clientX;
1891: MISSING
1892: MISSING
1893: MISSING
1894: MISSING
1895: MISSING
1896: MISSING
1897: MISSING
1898: MISSING
1899: MISSING
1900:   };
1901: 
1902:   document.getElementById("btn-dl-anyway").addEventListener("click", doExport);
1903:   document.getElementById("btn-dl-shared").addEventListener("click", () => {
1904:     toast("🙏 Merci !");
1905:     doExport();
1906:   });
1907: 
1908:   // Reset
1909:   document.getElementById("btn-reset").addEventListener("click", () => {
1910:     if (!confirm("Réinitialiser toute la carte ?")) return;
1911:     Object.keys(state.levels).forEach(c => state.levels[c] = 0);
1912:     saveState();
1913:     
1914:     // Clear all rects and paths
1915:     document.querySelectorAll(".cell-rect, .cell-path").forEach(r => r.setAttribute("fill", COLORS[0]));
1916:     updateHeader();
1917:     toast("Carte réinitialisée !");
1918:   });
1919: }
1920: 
1921: // ── INIT ─────────────────────────────────────────────────────
1922: document.addEventListener("DOMContentLoaded", () => {
1923:   loadState();
1924:   updateHeader();
1925:   setupEvents();
1926:   buildMap();
1927:   
1928:   // Show tutorial modal on load
1929:   const tutoOverlay = document.getElementById("tutorial-overlay");
1930:   if (tutoOverlay) {
1931:     tutoOverlay.classList.remove("hidden");
1932:     
1933:     const closeTuto = () => {
1934:       tutoOverlay.classList.add("hidden");
1935:     .scaleExtent([1, 8])
1936:     .filter((event) => {
1937:     const closeBtn = document.getElementById("btn-tuto-close");
1938:     if (closeBtn) closeBtn.addEventListener("click", closeTuto);
1939:       let clientX = 0;
1940:     const headerCloseBtn = document.getElementById("btn-tuto-header-close");
1941:     if (headerCloseBtn) headerCloseBtn.addEventListener("click", closeTuto);
1942:       } else if (event.changedTouches && event.changedTouches.length > 0) {
1943:         clientX = event.changedTouches[0].clientX;
1944:       } else {
1945:         clientX = event.clientX;
1946: with open("app.js", "w", encoding="utf-8") as f:
1947:   document.getElementById("map-loading").style.display = "none";
1948:       const xInSvg = ((clientX - rect.left) / rect.width) * 560;
1949:       return !event.ctrlKey && (!event.type.startsWith("mouse") || event.button === 0) && xInSvg >= 92;
1950:     subtitleSpain: "आपने स्पेन का कितना हिस्सा खोजा है?",
1951:     exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} प्रांतों</strong><span style="opacity:0.7; font-weight:400;"> का दौरा किया है</span></span></div>`,
1952:     return state.lang === "ja" ? NAMES_JA[code] : NAMES_EN[code];
1953:   } else if (state.currentMap === "fr") {
1954:     return `${code} - ${DEPARTEMENTS_FR[code] || code}`;
1955:   } else if (state.currentMap === "es") {
1956:     return PROVINCES_ES[code] || code;
1957:   document.getElementById("map-loading").style.display = "none";
1958:     if (worldData) {
1959:       const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
1960:       const feature = countriesGeoJson.features.find(f => f.id === code);
1961: function drawWorldMap() {
1962:         return getCountryName(code, feature.properties.name);
1963:   const W = 560, H = 570;
1964:   svg.attr("viewBox", `0 0 ${W} ${H}`);
1965:     return code;
1966:   }
1967: }
1968: 
1969: // ── Modal level selection ────────────────────────────────────
1970: function openModal(code) {
1971:   activePrefCode = code;
1972:   const name = getCountryDisplayName(code);
1973:   document.getElementById("modal-title").textContent = `@ ${name}`;
1974:   const cur = state.levels[code] || 0;
1975:   document.querySelectorAll(".opt-btn").forEach(btn => {
1976:     btn.classList.toggle("selected", +btn.dataset.level === cur);
1977:   });
1978:   document.getElementById("modal-overlay").classList.remove("hidden");
1979: }
1980: 
1981: function closeModal() {
1982:   document.getElementById("modal-overlay").classList.add("hidden");
1983:   activePrefCode = null;
1984: }
1985: 
1986: // ── Event Setup ──────────────────────────────────────────────
1987: function setupEvents() {
1988:   document.getElementById("modal-close").addEventListener("click", closeModal);
1989:   document.getElementById("modal-overlay").addEventListener("click", e => {
1990:     if (e.target.id === "modal-overlay") closeModal();
1991:   });
1992: 
1993:   document.querySelectorAll(".opt-btn").forEach(btn => {
1994:     btn.addEventListener("click", () => {
1995:       if (!activePrefCode) return;
1996:       const lvl = +btn.dataset.level;
1997:       state.levels[activePrefCode] = lvl;
1998:       saveState();
1999:       
2000:   document.getElementById("modal-overlay").classList.add("hidden");
2001:       const g = document.querySelector(`.cell-group[data-code="${activePrefCode}"]`);
2002:       if (g) {
2003:         if (g.tagName === "path" || g.tagName === "rect") {
2004: // ── Event Setup ──────────────────────────────────────────────
2005: function setupEvents() {
2006:   document.getElementById("modal-close").addEventListener("click", closeModal);
2007:   document.getElementById("modal-overlay").addEventListener("click", e => {
2008:     if (e.target.id === "modal-overlay") closeModal();
2009:   });
2010: 
2011:   document.querySelectorAll(".opt-btn").forEach(btn => {
2012:     btn.addEventListener("click", () => {
2013:       if (!activePrefCode) return;
2014:       const lvl = +btn.dataset.level;
2015:       state.levels[activePrefCode] = lvl;
2016:       saveState();
2017:       
2018:       // Update cell rect/path color dynamically
2019:       const g = document.querySelector(`.cell-group[data-code="${activePrefCode}"]`);
2020:       if (g) {
2021:         if (g.tagName === "path" || g.tagName === "rect") {
2022:           g.setAttribute("fill", COLORS[lvl]);
2023:         } else {
2024:           const targetElement = g.querySelector(".cell-rect, .cell-path");
2025:           if (targetElement) targetElement.setAttribute("fill", COLORS[lvl]);
2026:         }
2027:       } else {
2028:         // Also support selection via path selector direct mapping (World Map fallback)
2029:         const cellPath = document.querySelector(`path.cell-path[data-code="${activePrefCode}"]`);
2030:   const svg = d3.select("#map-svg");
2031:   const W = 560, H = 570;
2032:   svg.attr("viewBox", `0 0 ${W} ${H}`);
2033: 
2034:   const FIPS_TO_US_CODE = {
2035:     "01": "AL", "02": "AK", "04": "AZ", "05": "AR", "06": "CA", "08": "CO", "09": "CT", "10": "DE",
2036:     "11": "DC", "12": "FL", "13": "GA", "15": "HI", "16": "ID", "17": "IL", "18": "IN", "19": "IA",
2037:     "20": "KS", "21": "KY", "22": "LA", "23": "ME", "24": "MD", "25": "MA", "26": "MI", "27": "MN",
2038:     "28": "MS", "29": "MO", "30": "MT", "31": "NE", "32": "NV", "33": "NH", "34": "NJ", "35": "NM",
2039:     "36": "NY", "37": "NC", "38": "ND", "39": "OH", "40": "OK", "41": "OR", "42": "PA", "44": "RI",
2040:     "45": "SC", "46": "SD", "47": "TN", "48": "TX", "49": "UT", "50": "VT", "51": "VA", "53": "WA",
2041:     "54": "WV", "55": "WI", "56": "WY", "72": "PR"
2042:   };
2043: 
2044:   // Filter features to exclude Puerto Rico (72) which pushes map boundaries too far south
2045:   const features = usaStatesData.features.filter(d => d.properties.STATE !== "72");
2046: 
2047:   // Initialize missing levels for US states
2048:   features.forEach(d => {
2049:     const code = FIPS_TO_US_CODE[d.properties.STATE];
2050:     if (code && state.levels[code] == null) {
2051:       state.levels[code] = 0;
2052:     }
2053:   });
2054: 
2055:   // Create zoomable group
2056:   const mapG = svg.append("g")
2057:     .attr("id", "usa-group");
2058: 
2059:   // Project and fit extent using geoAlbersUsa (native Alaska & Hawaii insets)
2060:     } else {
2061:       mapSvg.style.transform = "none";
2062:     }
2063:     if (floatingBtn) {
2064:       floatingBtn.style.bottom = "77px";
2065:       floatingBtn.style.transform = "translateX(-50%) scale(1.5)";
2066:     }
2067:     if (header) {
2068:       header.style.paddingTop = "75px";
2069:     }
2070:     if (legend) {
2071:       legend.style.paddingBottom = "51px";
2072:     }
2073: 
2074:     html2canvas(card, {
2075:       scale: 3,
2076:       useCORS: true,
2077:       logging: false,
2078:       backgroundColor: "#ffffff"
2079:     }).then(canvas => {
2080:       // Restore original styles
2081:       card.style.width = savedCardWidth;
2082:       mapSvg.style.transform = savedSvgTransform;
2083:       if (floatingBtn) {
2084:         floatingBtn.style.bottom = savedBtnBottom;
2085:         floatingBtn.style.transform = savedBtnTransform;
2086:       }
2087:       if (header) {
2088:         header.style.paddingTop = savedHeaderPaddingTop;
2089:       }
2090:       if (legend) {
2091:         legend.style.paddingBottom = savedLegendPaddingBottom;
2092:       }
2093:       
2094:       const a = document.createElement("a");
2095:       const mapName = state.currentMap === "jp" ? "japan" : (state.currentMap === "fr" ? "france" : "world");
2096:       a.download = `maplevel_${mapName}_${state.username.replace(/\\W/g, "_")}.png`;
2097:       a.href = canvas.toDataURL("image/png");
2098:       const centroid = pathGenerator.centroid(d);
2099:       return centroid ? centroid[1] : 0;
2100:     }).catch((err) => {
2101:     .attr("text-anchor", "middle")
2102:     .attr("dominant-baseline", "middle")
2103:     .attr("font-family", "'Outfit', sans-serif")
2104:     .attr("font-size", "6px")
2105:     .attr("font-weight", "800")
2106:     .attr("fill", "rgba(26,37,51,0.85)")
2107:     .attr("pointer-events", "none")
2108:     .text(d => {
2109:       const code = FIPS_TO_US_CODE[d.properties.STATE];
2110:       // Hide label for DC on general view to avoid overlapping with MD/VA
2111:       return code === "DC" ? "" : code;
2112:     });
2113: 
2114:   // Setup D3 Zoom & Pinch
2115:   const zoomBehavior = d3.zoom()
2116:     .scaleExtent([1, 8])
2117:     .filter((event) => {
2118:       const svgNode = document.getElementById("map-svg");
2119:       if (!svgNode) return false;
2120:   document.getElementById("btn-dl-shared").addEventListener("click", () => {
2121:       if (event.touches && event.touches.length > 0) {
2122:         clientX = event.touches[0].clientX;
2123:       } else if (event.changedTouches && event.changedTouches.length > 0) {
2124:         clientX = event.changedTouches[0].clientX;
2125:       } else {
2126:   document.getElementById("btn-reset").addEventListener("click", () => {
2127:     if (!confirm("Réinitialiser toute la carte ?")) return;
2128:     Object.keys(state.levels).forEach(c => state.levels[c] = 0);
2129:       const xInSvg = ((clientX - rect.left) / rect.width) * 560;
2130:       return !event.ctrlKey && (!event.type.startsWith("mouse") || event.button === 0) && xInSvg >= 92;
2131:     // Clear all rects and paths
2132:     document.querySelectorAll(".cell-rect, .cell-path").forEach(r => r.setAttribute("fill", COLORS[0]));
2133:       mapG.attr("transform", event.transform);
2134:     toast("Carte réinitialisée !");
2135:   });
2136:   svg.call(zoomBehavior);
2137: 
2138: // ── INIT ─────────────────────────────────────────────────────
2139: document.addEventListener("DOMContentLoaded", () => {
2140:   loadState();
2141:   updateHeader();
2142:   setupEvents();
2143:   buildMap();
2144:   
2145:   // Show tutorial modal on load
2146:   const tutoOverlay = document.getElementById("tutorial-overlay");
2147:   if (tutoOverlay) {
2148:     tutoOverlay.classList.remove("hidden");
2149:     
2150:     const closeTuto = () => {
2151:       tutoOverlay.classList.add("hidden");
2152:     };
2153:     
2154:     const closeBtn = document.getElementById("btn-tuto-close");
2155:     if (closeBtn) closeBtn.addEventListener("click", closeTuto);
2156:     
2157:     const headerCloseBtn = document.getElementById("btn-tuto-header-close");
2158:     if (headerCloseBtn) headerCloseBtn.addEventListener("click", closeTuto);
2159:   }
2160: });
2161: """
2162: 
2163: with open("app.js", "w", encoding="utf-8") as f:
2164:     f.write(app_js_content)
2165: print("app.js updated successfully!")
2166: MISSING
2167: MISSING
2168: MISSING
2169: MISSING
2170: MISSING
2171: MISSING
2172: MISSING
2173: MISSING
2174: MISSING
2175: MISSING
2176: MISSING
2177: MISSING
2178: MISSING
2179: MISSING
2180: MISSING
2181: MISSING
2182: MISSING
2183: MISSING
2184: MISSING
2185: MISSING
2186: MISSING
2187: MISSING
2188: MISSING
2189: MISSING
2190: MISSING
2191: MISSING
2192: MISSING
2193: MISSING
2194: MISSING
2195: MISSING
2196: MISSING
2197: MISSING
2198: MISSING
2199: MISSING
2200:       toast("🎉 Image enregistrée !");
2201:     }).catch((err) => {
2202:       console.error(err);
2203:       // Restore original styles on error too
2204:       card.style.width = savedCardWidth;
2205:       mapSvg.style.transform = savedSvgTransform;
2206:       if (floatingBtn) {
2207:         floatingBtn.style.bottom = savedBtnBottom;
2208:         floatingBtn.style.transform = savedBtnTransform;
2209:       }
2210:       if (header) {
2211:         header.style.paddingTop = savedHeaderPaddingTop;
2212:       }
2213:       if (legend) {
2214:         legend.style.paddingBottom = savedLegendPaddingBottom;
2215:       }
2216:       toast("Erreur d'export.");
2217:     });
2218:   };
2219: 
2220:   document.getElementById("btn-dl-anyway").addEventListener("click", doExport);
2221:   document.getElementById("btn-dl-shared").addEventListener("click", () => {
2222:     toast("🙏 Merci !");
2223:     doExport();
2224:   });
2225: 
2226:   // Reset
2227:   document.getElementById("btn-reset").addEventListener("click", () => {
2228:     if (!confirm("Réinitialiser toute la carte ?")) return;
2229:     Object.keys(state.levels).forEach(c => state.levels[c] = 0);
2230:     saveState();
2231:     
2232:     // Clear all rects and paths
2233:     document.querySelectorAll(".cell-rect, .cell-path").forEach(r => r.setAttribute("fill", COLORS[0]));
2234:     updateHeader();
2235:     toast("Carte réinitialisée !");
2236:   });
2237: }
2238: 
2239: // ── INIT ─────────────────────────────────────────────────────
2240: document.addEventListener("DOMContentLoaded", () => {
2241:   loadState();
2242:   updateHeader();
2243:   setupEvents();
2244:   buildMap();
2245:   
2246:   // Show tutorial modal on load
2247:   const tutoOverlay = document.getElementById("tutorial-overlay");
2248:   if (tutoOverlay) {
2249:     tutoOverlay.classList.remove("hidden");
2250:     
2251:     const closeTuto = () => {
2252:       tutoOverlay.classList.add("hidden");
2253:     };
2254:     
2255:     const closeBtn = document.getElementById("btn-tuto-close");
2256:     if (closeBtn) closeBtn.addEventListener("click", closeTuto);
2257:     
2258:     const headerCloseBtn = document.getElementById("btn-tuto-header-close");
2259:     if (headerCloseBtn) headerCloseBtn.addEventListener("click", closeTuto);
2260:   }
2261: });
2262: """
2263: 
2264: with open("app.js", "w", encoding="utf-8") as f:
2265:     f.write(app_js_content)
2266: print("app.js updated successfully!")
