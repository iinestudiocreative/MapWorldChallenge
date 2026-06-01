#!/usr/bin/env python3
"""
Script to add Spain (50 provinces + Ceuta/Melilla) to the Ride the World app.
Modifies update_app.py to inject all Spain-related code.
"""
import re

FILE = "update_app.py"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ═══════════════════════════════════════════════════════════
# 1. Add PROVINCES_ES dictionary after DEPARTEMENTS_FR
# ═══════════════════════════════════════════════════════════
PROVINCES_ES_BLOCK = """
const PROVINCES_ES = {
  "01": "Araba/Álava", "02": "Albacete", "03": "Alacant/Alicante", "04": "Almería",
  "05": "Ávila", "06": "Badajoz", "07": "Illes Balears", "08": "Barcelona",
  "09": "Burgos", "10": "Cáceres", "11": "Cádiz", "12": "Castelló/Castellón",
  "13": "Ciudad Real", "14": "Córdoba", "15": "A Coruña", "16": "Cuenca",
  "17": "Girona", "18": "Granada", "19": "Guadalajara", "20": "Gipuzkoa/Guipúzcoa",
  "21": "Huelva", "22": "Huesca", "23": "Jaén", "24": "León",
  "25": "Lleida", "26": "La Rioja", "27": "Lugo", "28": "Madrid",
  "29": "Málaga", "30": "Murcia", "31": "Navarra", "32": "Ourense",
  "33": "Asturias", "34": "Palencia", "35": "Las Palmas", "36": "Pontevedra",
  "37": "Salamanca", "38": "Santa Cruz De Tenerife", "39": "Cantabria", "40": "Segovia",
  "41": "Sevilla", "42": "Soria", "43": "Tarragona", "44": "Teruel",
  "45": "Toledo", "46": "València/Valencia", "47": "Valladolid", "48": "Bizkaia/Vizcaya",
  "49": "Zamora", "50": "Zaragoza", "51": "Ceuta", "52": "Melilla"
};
"""

# Insert after the FR_GRID closing ];
# Find the end of FR_GRID
fr_grid_end = content.find("];\n\nconst COLORS")
if fr_grid_end == -1:
    print("ERROR: Could not find FR_GRID end marker")
    exit(1)

insert_pos = content.find("];\n\nconst COLORS") + 2  # After the ];
content = content[:insert_pos] + "\n" + PROVINCES_ES_BLOCK + content[insert_pos:]

# ═══════════════════════════════════════════════════════════
# 2. Add ES_GRID after PROVINCES_ES (cartogram grid layout)
# ═══════════════════════════════════════════════════════════
# Spain grid layout - positioned to roughly match geography
# Row structure: N→S, columns W→E
ES_GRID_BLOCK = """
const ES_GRID = [
  // Row 1 - North (Galicia, Asturias, Cantabria, Basque, Navarra)
  { code: '15', x: 38, y: 45, w: 38, h: 38 },   // A Coruña
  { code: '27', x: 78, y: 45, w: 38, h: 38 },   // Lugo
  { code: '32', x: 38, y: 85, w: 38, h: 38 },   // Ourense
  { code: '36', x: 38, y: 125, w: 38, h: 38 },  // Pontevedra
  { code: '33', x: 118, y: 45, w: 38, h: 38 },  // Asturias
  { code: '24', x: 118, y: 85, w: 38, h: 38 },  // León
  { code: '39', x: 158, y: 45, w: 38, h: 38 },  // Cantabria
  { code: '34', x: 158, y: 85, w: 38, h: 38 },  // Palencia
  { code: '09', x: 198, y: 85, w: 38, h: 38 },  // Burgos
  { code: '48', x: 198, y: 45, w: 38, h: 38 },  // Bizkaia/Vizcaya
  { code: '20', x: 238, y: 45, w: 38, h: 38 },  // Gipuzkoa/Guipúzcoa
  { code: '01', x: 238, y: 85, w: 38, h: 38 },  // Araba/Álava
  { code: '31', x: 278, y: 45, w: 38, h: 38 },  // Navarra
  { code: '26', x: 278, y: 85, w: 38, h: 38 },  // La Rioja
  // Row 2 - Castilla y León, Aragón, Cataluña
  { code: '49', x: 78, y: 125, w: 38, h: 38 },  // Zamora
  { code: '37', x: 78, y: 165, w: 38, h: 38 },  // Salamanca
  { code: '47', x: 118, y: 125, w: 38, h: 38 },  // Valladolid
  { code: '05', x: 118, y: 165, w: 38, h: 38 },  // Ávila
  { code: '42', x: 198, y: 125, w: 38, h: 38 },  // Soria
  { code: '40', x: 158, y: 125, w: 38, h: 38 },  // Segovia
  { code: '50', x: 278, y: 125, w: 38, h: 38 },  // Zaragoza
  { code: '22', x: 318, y: 45, w: 38, h: 38 },  // Huesca
  { code: '25', x: 358, y: 45, w: 38, h: 38 },  // Lleida
  { code: '44', x: 318, y: 125, w: 38, h: 38 },  // Teruel
  { code: '17', x: 398, y: 45, w: 38, h: 38 },  // Girona
  { code: '08', x: 398, y: 85, w: 38, h: 38 },  // Barcelona
  { code: '43', x: 358, y: 85, w: 38, h: 38 },  // Tarragona
  // Row 3 - Madrid, C-LM, Valencia, Extremadura
  { code: '28', x: 158, y: 165, w: 38, h: 38 },  // Madrid
  { code: '19', x: 198, y: 165, w: 38, h: 38 },  // Guadalajara
  { code: '16', x: 238, y: 165, w: 38, h: 38 },  // Cuenca
  { code: '12', x: 318, y: 165, w: 38, h: 38 },  // Castelló/Castellón
  { code: '46', x: 318, y: 205, w: 38, h: 38 },  // València/Valencia
  { code: '03', x: 318, y: 245, w: 38, h: 38 },  // Alacant/Alicante
  { code: '45', x: 198, y: 205, w: 38, h: 38 },  // Toledo
  { code: '13', x: 198, y: 245, w: 38, h: 38 },  // Ciudad Real
  { code: '02', x: 238, y: 205, w: 38, h: 38 },  // Albacete
  { code: '10', x: 78, y: 205, w: 38, h: 38 },  // Cáceres
  { code: '06', x: 78, y: 245, w: 38, h: 38 },  // Badajoz
  // Row 4 - Andalucía, Murcia
  { code: '30', x: 278, y: 245, w: 38, h: 38 },  // Murcia
  { code: '21', x: 78, y: 285, w: 38, h: 38 },  // Huelva
  { code: '41', x: 118, y: 285, w: 38, h: 38 },  // Sevilla
  { code: '14', x: 158, y: 285, w: 38, h: 38 },  // Córdoba
  { code: '23', x: 198, y: 285, w: 38, h: 38 },  // Jaén
  { code: '18', x: 238, y: 285, w: 38, h: 38 },  // Granada
  { code: '04', x: 278, y: 285, w: 38, h: 38 },  // Almería
  { code: '11', x: 118, y: 325, w: 38, h: 38 },  // Cádiz
  { code: '29', x: 158, y: 325, w: 38, h: 38 },  // Málaga
  // Islands (inset-style)
  { code: '07', x: 398, y: 205, w: 38, h: 38 },  // Illes Balears
  { code: '35', x: 38, y: 405, w: 38, h: 38 },  // Las Palmas (Canarias)
  { code: '38', x: 78, y: 405, w: 38, h: 38 },  // S.C. Tenerife (Canarias)
  // Autonomous cities
  { code: '51', x: 158, y: 365, w: 38, h: 38 },  // Ceuta
  { code: '52', x: 198, y: 365, w: 38, h: 38 },  // Melilla
];
"""

# Insert after PROVINCES_ES
provinces_end = content.find("};\n\n\nconst COLORS")
if provinces_end == -1:
    # Try alternate pattern
    provinces_end = content.find("};\n\nconst COLORS")
if provinces_end == -1:
    print("ERROR: Could not find insertion point for ES_GRID")
    exit(1)
insert_pos = provinces_end + 2
content = content[:insert_pos] + "\n" + ES_GRID_BLOCK + content[insert_pos:]

# ═══════════════════════════════════════════════════════════
# 3. Add esLevels to state
# ═══════════════════════════════════════════════════════════
content = content.replace(
    "  frLevels: {}\n};",
    "  frLevels: {},\n  esLevels: {}\n};"
)

# Also add spainProvincesData cache variable
content = content.replace(
    "let franceDomTomData = null;",
    "let franceDomTomData = null;\nlet spainProvincesData = null;"
)

# ═══════════════════════════════════════════════════════════
# 4. Add Spain translations to all 7 languages
# ═══════════════════════════════════════════════════════════
# For each language, add subtitleSpain, exploredSpain, bgWatermarkSpain, countryModal.es
spain_translations = {
    "en": {
        "subtitleSpain": "How much of Spain have you explored?",
        "exploredSpain": '(nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`',
        "bgWatermarkSpain": "SPAIN",
        "countryModal_es": '🇪🇸 Spain',
    },
    "ja": {
        "subtitleSpain": "スペインのどこを旅しましたか？",
        "exploredSpain": '(nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`',
        "bgWatermarkSpain": "スペイン",
        "countryModal_es": '🇪🇸 スペイン',
    },
    "fr": {
        "subtitleSpain": "Combien de provinces d'Espagne as-tu exploré ?",
        "exploredSpain": '(nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`',
        "bgWatermarkSpain": "ESPAGNE",
        "countryModal_es": '🇪🇸 Espagne',
    },
    "es": {
        "subtitleSpain": "¿Cuánto de España has explorado?",
        "exploredSpain": '(nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} provincias</strong></span></div>`',
        "bgWatermarkSpain": "ESPAÑA",
        "countryModal_es": '🇪🇸 España',
    },
    "ko": {
        "subtitleSpain": "스페인의 어디를 여행하셨나요?",
        "exploredSpain": '(nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 주</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`',
        "bgWatermarkSpain": "스페인",
        "countryModal_es": '🇪🇸 스페인',
    },
    "zh": {
        "subtitleSpain": "你探索了多少西班牙？",
        "exploredSpain": '(nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个省份</strong></span></div>`',
        "bgWatermarkSpain": "西班牙",
        "countryModal_es": '🇪🇸 西班牙',
    },
    "hi": {
        "subtitleSpain": "आपने स्पेन का कितना हिस्सा खोजा है?",
        "exploredSpain": '(nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} प्रांतों</strong><span style="opacity:0.7; font-weight:400;"> का दौरा किया है</span></span></div>`',
        "bgWatermarkSpain": "स्पेन",
        "countryModal_es": '🇪🇸 स्पेन',
    },
}

# Add subtitleSpain after subtitleFrance for each lang
for lang, trans in spain_translations.items():
    # subtitleSpain
    old_sf = f'subtitleFrance: "{content.split(lang + ": {")[1].split("subtitleFrance: ")[1].split(chr(34))[1]}"'
    # This is fragile — let's use a different approach
    pass

# Let me use a more robust approach: find each language block and insert after subtitleFrance line
lines = content.split('\n')
new_lines = []
current_lang = None
i = 0
while i < len(lines):
    line = lines[i]
    new_lines.append(line)
    
    # Track which language block we're in
    for lang in ['en', 'ja', 'fr', 'es', 'ko', 'zh', 'hi']:
        if f'  {lang}: {{' == line.strip() or f'{lang}: {{' == line.strip():
            current_lang = lang
    
    # Add subtitleSpain after subtitleFrance
    if current_lang and 'subtitleFrance:' in line and 'subtitleSpain' not in lines[i+1] if i+1 < len(lines) else True:
        trans = spain_translations.get(current_lang)
        if trans:
            indent = '    '
            new_lines.append(f'{indent}subtitleSpain: "{trans["subtitleSpain"]}",')
    
    # Add exploredSpain after exploredFrance
    if current_lang and 'exploredFrance:' in line and '=>' in line and 'exploredSpain' not in lines[i+1] if i+1 < len(lines) else True:
        trans = spain_translations.get(current_lang)
        if trans:
            indent = '    '
            new_lines.append(f'{indent}exploredSpain: {trans["exploredSpain"]},')
    
    # Add bgWatermarkSpain after bgWatermarkFrance
    if current_lang and 'bgWatermarkFrance:' in line and 'bgWatermarkSpain' not in lines[i+1] if i+1 < len(lines) else True:
        trans = spain_translations.get(current_lang)
        if trans:
            indent = '    '
            new_lines.append(f'{indent}bgWatermarkSpain: "{trans["bgWatermarkSpain"]}",')
    
    # Add es entry to countryModal - find the 'it:' line in countryModal and add es after it
    if current_lang and 'it: "🇮🇹' in line and 'countryModal' in '\n'.join(lines[max(0,i-5):i]):
        trans = spain_translations.get(current_lang)
        if trans:
            # The it line is usually part of a multi-entry line like: world: "...", fr: "...", it: "...", jp: "...", us: "..."
            # We need to add es to this line. Let's modify the current line instead.
            # Actually the countryModal entries are on one line. We need to add es: to it
            # Let's modify the line we just added
            last_line = new_lines[-1]
            if 'it:' in last_line and 'es:' not in last_line:
                # Add es: after it: entry
                last_line = last_line.replace('jp:', f'es: "{trans["countryModal_es"]}", jp:')
                new_lines[-1] = last_line
    
    i += 1

content = '\n'.join(new_lines)

# ═══════════════════════════════════════════════════════════
# 5. Update loadState to handle esLevels
# ═══════════════════════════════════════════════════════════
content = content.replace(
    "    state.frLevels = s.frLevels || {};",
    "    state.frLevels = s.frLevels || {};\n    state.esLevels = s.esLevels || {};"
)

content = content.replace(
    '    if (state.currentMap === "jp") state.levels = state.jpLevels;\n    else if (state.currentMap === "fr") state.levels = state.frLevels;\n    else state.levels = state.worldLevels;',
    '    if (state.currentMap === "jp") state.levels = state.jpLevels;\n    else if (state.currentMap === "fr") state.levels = state.frLevels;\n    else if (state.currentMap === "es") state.levels = state.esLevels;\n    else state.levels = state.worldLevels;'
)

# Init es provinces in loadState
content = content.replace(
    '  } else if (state.currentMap === "fr") {\n    Object.keys(DEPARTEMENTS_FR).forEach(c => {\n      if (state.levels[c] == null) state.levels[c] = 0;\n    });\n  }\n\n  // Select active country button',
    '  } else if (state.currentMap === "fr") {\n    Object.keys(DEPARTEMENTS_FR).forEach(c => {\n      if (state.levels[c] == null) state.levels[c] = 0;\n    });\n  } else if (state.currentMap === "es") {\n    Object.keys(PROVINCES_ES).forEach(c => {\n      if (state.levels[c] == null) state.levels[c] = 0;\n    });\n  }\n\n  // Select active country button'
)

# ═══════════════════════════════════════════════════════════
# 6. Update saveState to handle esLevels
# ═══════════════════════════════════════════════════════════
content = content.replace(
    '  if (state.currentMap === "jp") {\n    state.jpLevels = state.levels;\n  } else if (state.currentMap === "fr") {\n    state.frLevels = state.levels;\n  } else {\n    state.worldLevels = state.levels;\n  }',
    '  if (state.currentMap === "jp") {\n    state.jpLevels = state.levels;\n  } else if (state.currentMap === "fr") {\n    state.frLevels = state.levels;\n  } else if (state.currentMap === "es") {\n    state.esLevels = state.levels;\n  } else {\n    state.worldLevels = state.levels;\n  }'
)

# ═══════════════════════════════════════════════════════════
# 7. Update updateUITranslations - subtitle
# ═══════════════════════════════════════════════════════════
content = content.replace(
    '''    if (state.currentMap === "jp") {
      subtitle.textContent = t.subtitle;
    } else if (state.currentMap === "fr") {
      subtitle.textContent = t.subtitleFrance;
    } else {
      subtitle.textContent = t.subtitleWorld;
    }''',
    '''    if (state.currentMap === "jp") {
      subtitle.textContent = t.subtitle;
    } else if (state.currentMap === "fr") {
      subtitle.textContent = t.subtitleFrance;
    } else if (state.currentMap === "es") {
      subtitle.textContent = t.subtitleSpain;
    } else {
      subtitle.textContent = t.subtitleWorld;
    }'''
)

# ═══════════════════════════════════════════════════════════
# 8. Update country selector button text
# ═══════════════════════════════════════════════════════════
content = content.replace(
    '''    if (state.currentMap === "jp") {
      btnCountry.innerHTML = `${t.countryModal.jp} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
    } else if (state.currentMap === "fr") {
      btnCountry.innerHTML = `${t.countryModal.fr} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
    } else {
      btnCountry.innerHTML = `${t.countryModal.world} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
    }''',
    '''    if (state.currentMap === "jp") {
      btnCountry.innerHTML = `${t.countryModal.jp} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
    } else if (state.currentMap === "fr") {
      btnCountry.innerHTML = `${t.countryModal.fr} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
    } else if (state.currentMap === "es") {
      btnCountry.innerHTML = `${t.countryModal.es} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
    } else {
      btnCountry.innerHTML = `${t.countryModal.world} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
    }'''
)

# ═══════════════════════════════════════════════════════════
# 9. Update bgWatermark
# ═══════════════════════════════════════════════════════════
content = content.replace(
    '    if (state.currentMap === "jp") text = t.bgWatermark || "JAPAN";\n    else if (state.currentMap === "fr") text = t.bgWatermarkFrance || "FRANCE";\n    else text = t.bgWatermarkWorld || "WORLD";',
    '    if (state.currentMap === "jp") text = t.bgWatermark || "JAPAN";\n    else if (state.currentMap === "fr") text = t.bgWatermarkFrance || "FRANCE";\n    else if (state.currentMap === "es") text = t.bgWatermarkSpain || "SPAIN";\n    else text = t.bgWatermarkWorld || "WORLD";'
)

# ═══════════════════════════════════════════════════════════
# 10. Update updateHeader - explored text
# ═══════════════════════════════════════════════════════════
content = content.replace(
    '''    if (state.currentMap === "jp") {
      floatingName.innerHTML = t.explored(nameHtml, exploredCount);
    } else if (state.currentMap === "fr") {
      floatingName.innerHTML = t.exploredFrance(nameHtml, exploredCount);
    } else {
      floatingName.innerHTML = t.exploredWorld(nameHtml, exploredCount);
    }''',
    '''    if (state.currentMap === "jp") {
      floatingName.innerHTML = t.explored(nameHtml, exploredCount);
    } else if (state.currentMap === "fr") {
      floatingName.innerHTML = t.exploredFrance(nameHtml, exploredCount);
    } else if (state.currentMap === "es") {
      floatingName.innerHTML = t.exploredSpain(nameHtml, exploredCount);
    } else {
      floatingName.innerHTML = t.exploredWorld(nameHtml, exploredCount);
    }'''
)

# ═══════════════════════════════════════════════════════════
# 11. Update updateHeader - maxPoints
# ═══════════════════════════════════════════════════════════
content = content.replace(
    '  let maxPoints = 235; // Japan\n  if (state.currentMap === "fr") {\n    maxPoints = 505; // France (101 departments * 5)',
    '  let maxPoints = 235; // Japan\n  if (state.currentMap === "fr") {\n    maxPoints = 505; // France (101 departments * 5)\n  } else if (state.currentMap === "es") {\n    maxPoints = 260; // Spain (52 provinces * 5)'
)

# ═══════════════════════════════════════════════════════════
# 12. Update getCountryDisplayName for Spain
# ═══════════════════════════════════════════════════════════
content = content.replace(
    '''  } else if (state.currentMap === "fr") {
    return `${code} - ${DEPARTEMENTS_FR[code] || code}`;
  } else {''',
    '''  } else if (state.currentMap === "fr") {
    return `${code} - ${DEPARTEMENTS_FR[code] || code}`;
  } else if (state.currentMap === "es") {
    return PROVINCES_ES[code] || code;
  } else {'''
)

# ═══════════════════════════════════════════════════════════
# 13. Update buildMap to handle "es"
# ═══════════════════════════════════════════════════════════
# Add es case in buildMap between fr and world
content = content.replace(
    '''  } else if (state.currentMap === "fr") {
    if (franceDepsData && franceDomTomData) {
      drawFranceMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      Promise.all([
        fetch("france_departements.geojson").then(res => res.json()),
        fetch("france_domtom.geojson").then(res => res.json())
      ]).then(([deps, domtom]) => {
        franceDepsData = deps;
        franceDomTomData = domtom;
        drawFranceMap();
        updateHeader();
      }).catch(err => {
        console.error("Error loading France map data:", err);
        toast("Erreur de chargement de la carte de France.");
        document.getElementById("map-loading").style.display = "none";
      });
    }
  } else {''',
    '''  } else if (state.currentMap === "fr") {
    if (franceDepsData && franceDomTomData) {
      drawFranceMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      Promise.all([
        fetch("france_departements.geojson").then(res => res.json()),
        fetch("france_domtom.geojson").then(res => res.json())
      ]).then(([deps, domtom]) => {
        franceDepsData = deps;
        franceDomTomData = domtom;
        drawFranceMap();
        updateHeader();
      }).catch(err => {
        console.error("Error loading France map data:", err);
        toast("Erreur de chargement de la carte de France.");
        document.getElementById("map-loading").style.display = "none";
      });
    }
  } else if (state.currentMap === "es") {
    if (spainProvincesData) {
      drawSpainMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("spain_provinces.geojson")
        .then(res => res.json())
        .then(data => {
          spainProvincesData = data;
          drawSpainMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading Spain map data:", err);
          toast("Error loading Spain map.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else {'''
)

# ═══════════════════════════════════════════════════════════
# 14. Add drawSpainMap function (before drawWorldMap)
# ═══════════════════════════════════════════════════════════
DRAW_SPAIN_MAP = '''
function drawSpainMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  // Initialize missing levels for Spain provinces
  Object.keys(PROVINCES_ES).forEach(code => {
    if (state.levels[code] == null) {
      state.levels[code] = 0;
    }
  });

  // Separate mainland from Canary Islands
  const mainlandFeatures = spainProvincesData.features.filter(f => {
    const code = f.properties.cod_prov;
    return code !== "35" && code !== "38"; // Exclude Las Palmas and S.C. Tenerife
  });
  const canaryFeatures = spainProvincesData.features.filter(f => {
    const code = f.properties.cod_prov;
    return code === "35" || code === "38";
  });

  const mainlandGeoJSON = {
    type: "FeatureCollection",
    features: mainlandFeatures
  };

  // 1. Draw Mainland Spain inside a zoomable group
  const mapG = svg.append("g")
    .attr("id", "spain-group");

  const projection = d3.geoConicConformal()
    .center([-3.7, 40.0])
    .fitExtent([[110, 25], [550, 520]], mainlandGeoJSON);

  const pathGenerator = d3.geoPath().projection(projection);

  // Render mainland provinces
  mapG.selectAll(".spain-path")
    .data(mainlandFeatures)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path spain-path")
    .attr("data-code", d => d.properties.cod_prov)
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[d.properties.cod_prov] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return;
      openModal(d.properties.cod_prov);
    });

  // Draw province labels
  mapG.selectAll(".spain-label")
    .data(mainlandFeatures)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => d.properties.cod_prov)
    .attr("x", d => {
      const centroid = pathGenerator.centroid(d);
      return centroid ? centroid[0] : 0;
    })
    .attr("y", d => {
      const centroid = pathGenerator.centroid(d);
      return centroid ? centroid[1] : 0;
    })
    .attr("text-anchor", "middle")
    .attr("dominant-baseline", "middle")
    .attr("font-family", "'Outfit', sans-serif")
    .attr("font-size", "4.5px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => {
      // Use short name for display
      const name = d.properties.name;
      // Shorten dual-language names
      if (name.includes('/')) return name.split('/')[1] || name.split('/')[0];
      return name;
    });

  // 2. Setup D3 Zoom & Pinch for mainland
  const zoomBehavior = d3.zoom()
    .scaleExtent([1, 8])
    .filter((event) => {
      const svgNode = document.getElementById("map-svg");
      if (!svgNode) return false;
      let clientX = 0;
      if (event.touches && event.touches.length > 0) {
        clientX = event.touches[0].clientX;
      } else if (event.changedTouches && event.changedTouches.length > 0) {
        clientX = event.changedTouches[0].clientX;
      } else {
        clientX = event.clientX;
      }
      const rect = svgNode.getBoundingClientRect();
      const xInSvg = ((clientX - rect.left) / rect.width) * 560;
      return !event.ctrlKey && (!event.type.startsWith("mouse") || event.button === 0) && xInSvg >= 92;
    })
    .on("zoom", (event) => {
      mapG.attr("transform", event.transform);
    });

  svg.call(zoomBehavior);

  // 3. Draw Canary Islands as insets (fixed, not zoomed)
  const canaries = [
    { code: "35", name: "Las Palmas", y: 420 },
    { code: "38", name: "S.C. Tenerife", y: 420 }
  ];

  canaries.forEach((island, idx) => {
    const OX = 12 + idx * 50, OY = island.y, OW = 45, OH = 80;
    
    // Inset box
    svg.append("rect")
      .attr("x", OX).attr("y", OY).attr("width", OW).attr("height", OH)
      .attr("fill", "rgba(255, 255, 255, 0.05)")
      .attr("stroke", "rgba(255, 255, 255, 0.35)")
      .attr("stroke-width", 1.2)
      .attr("rx", 4);

    // Inset label
    svg.append("text")
      .attr("x", OX + OW / 2)
      .attr("y", OY + OH - 7)
      .attr("text-anchor", "middle")
      .attr("font-family", "'Outfit', sans-serif")
      .attr("font-size", "6px")
      .attr("font-weight", "800")
      .attr("fill", "rgba(255, 255, 255, 0.8)")
      .text(island.name);

    const feature = spainProvincesData.features.find(f => f.properties.cod_prov === island.code);
    if (feature) {
      const gInset = svg.append("g")
        .attr("class", "cell-group")
        .attr("data-code", island.code)
        .style("cursor", "pointer")
        .on("click", () => {
          openModal(island.code);
        });

      const localProjection = d3.geoMercator()
        .fitExtent([[OX + 4, OY + 4], [OX + OW - 4, OY + OH - 18]], feature);
      const localPath = d3.geoPath().projection(localProjection);

      gInset.append("path")
        .attr("class", "cell-path")
        .attr("data-code", island.code)
        .attr("d", localPath(feature))
        .attr("fill", COLORS[state.levels[island.code] || 0])
        .attr("stroke", "#ffffff")
        .attr("stroke-width", 0.7);

      gInset.append("rect")
        .attr("x", OX).attr("y", OY)
        .attr("width", OW).attr("height", OH)
        .attr("fill", "rgba(0,0,0,0)")
        .attr("pointer-events", "all")
        .style("cursor", "pointer");
    }
  });

  document.getElementById("map-loading").style.display = "none";
}

'''

content = content.replace(
    "function drawWorldMap() {",
    DRAW_SPAIN_MAP + "function drawWorldMap() {"
)

# ═══════════════════════════════════════════════════════════
# 15. Update country switch handler to save/restore esLevels
# ═══════════════════════════════════════════════════════════
content = content.replace(
    '''        if (newMap !== state.currentMap) {
        if (state.currentMap === "jp") {
          state.jpLevels = state.levels;
        } else {
          state.worldLevels = state.levels;
        }
        
        state.currentMap = newMap;
        state.levels = newMap === "jp" ? state.jpLevels : state.worldLevels;''',
    '''        if (newMap !== state.currentMap) {
        if (state.currentMap === "jp") {
          state.jpLevels = state.levels;
        } else if (state.currentMap === "fr") {
          state.frLevels = state.levels;
        } else if (state.currentMap === "es") {
          state.esLevels = state.levels;
        } else {
          state.worldLevels = state.levels;
        }
        
        state.currentMap = newMap;
        if (newMap === "jp") state.levels = state.jpLevels;
        else if (newMap === "fr") state.levels = state.frLevels;
        else if (newMap === "es") state.levels = state.esLevels;
        else state.levels = state.worldLevels;'''
)

# ═══════════════════════════════════════════════════════════
# 16. Update country modal rendering to add Spain button + enable it
# ═══════════════════════════════════════════════════════════
# The country modal has 5 buttons (world, fr, it, jp, us). We need to add es.
# The updateUITranslations function updates cOpts[0-4]. We need to add cOpts[5] for es.
# But first let's update to handle 6+ buttons.

# Replace the country modal rendering in updateUITranslations
content = content.replace(
    '''  const cOpts = document.querySelectorAll("#country-modal .opt-btn");
  if (cOpts.length >= 5) {
    cOpts[0].querySelector("div").innerHTML = `<strong>${t.countryModal.world}</strong><small>${t.countryModal.soon}</small>`;
    cOpts[0].setAttribute("disabled", "true");
    cOpts[0].style.opacity = "0.5";
    cOpts[0].style.cursor = "not-allowed";
    
    cOpts[1].querySelector("div").innerHTML = `<strong>${t.countryModal.fr}</strong><small>${t.countryModal.avail}</small>`;
    cOpts[1].removeAttribute("disabled");
    cOpts[1].removeAttribute("style");
    
    cOpts[2].querySelector("div").innerHTML = `<strong>${t.countryModal.it}</strong><small>${t.countryModal.soon}</small>`;
    cOpts[3].querySelector("div").innerHTML = `<strong>${t.countryModal.jp}</strong><small>${t.countryModal.avail}</small>`;
    cOpts[4].querySelector("div").innerHTML = `<strong>${t.countryModal.us}</strong><small>${t.countryModal.soon}</small>`;
  }''',
    '''  const cOpts = document.querySelectorAll("#country-modal .opt-btn");
  if (cOpts.length >= 6) {
    cOpts[0].querySelector("div").innerHTML = `<strong>${t.countryModal.world}</strong><small>${t.countryModal.soon}</small>`;
    cOpts[0].setAttribute("disabled", "true");
    cOpts[0].style.opacity = "0.5";
    cOpts[0].style.cursor = "not-allowed";
    
    cOpts[1].querySelector("div").innerHTML = `<strong>${t.countryModal.es}</strong><small>${t.countryModal.avail}</small>`;
    cOpts[1].removeAttribute("disabled");
    cOpts[1].removeAttribute("style");
    
    cOpts[2].querySelector("div").innerHTML = `<strong>${t.countryModal.fr}</strong><small>${t.countryModal.avail}</small>`;
    cOpts[2].removeAttribute("disabled");
    cOpts[2].removeAttribute("style");
    
    cOpts[3].querySelector("div").innerHTML = `<strong>${t.countryModal.it}</strong><small>${t.countryModal.soon}</small>`;
    cOpts[3].setAttribute("disabled", "true");
    cOpts[3].style.opacity = "0.5";
    cOpts[3].style.cursor = "not-allowed";
    
    cOpts[4].querySelector("div").innerHTML = `<strong>${t.countryModal.jp}</strong><small>${t.countryModal.avail}</small>`;
    cOpts[4].removeAttribute("disabled");
    cOpts[4].removeAttribute("style");
    
    cOpts[5].querySelector("div").innerHTML = `<strong>${t.countryModal.us}</strong><small>${t.countryModal.soon}</small>`;
    cOpts[5].setAttribute("disabled", "true");
    cOpts[5].style.opacity = "0.5";
    cOpts[5].style.cursor = "not-allowed";
  }'''
)

# ═══════════════════════════════════════════════════════════
# Write the modified file
# ═══════════════════════════════════════════════════════════
with open(FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ update_app.py has been modified with Spain support!")
print("Now run: python3 update_app.py")
