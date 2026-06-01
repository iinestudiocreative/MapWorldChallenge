// ═══════════════════════════════════════════════════════════
// MAPLEVEL — app.js
// Modern Proportional Block Cartogram Layout (Self-contained)
// ═══════════════════════════════════════════════════════════

const NAMES_EN = {
  "01":"Hokkaido","02":"Aomori","03":"Iwate","04":"Miyagi","05":"Akita",
  "06":"Yamagata","07":"Fukushima","08":"Ibaraki","09":"Tochigi","10":"Gunma",
  "11":"Saitama","12":"Chiba","13":"Tokyo","14":"Kanagawa","15":"Niigata",
  "16":"Toyama","17":"Ishikawa","18":"Fukui","19":"Yamanashi","20":"Nagano",
  "21":"Gifu","22":"Shizuoka","23":"Aichi","24":"Mie","25":"Shiga",
  "26":"Kyoto","27":"Osaka","28":"Hyogo","29":"Nara","30":"Wakayama",
  "31":"Tottori","32":"Shimane","33":"Okayama","34":"Hiroshima","35":"Yamaguchi",
  "36":"Tokushima","37":"Kagawa","38":"Ehime","39":"Kochi","40":"Fukuoka",
  "41":"Saga","42":"Nagasaki","43":"Kumamoto","44":"Oita","45":"Miyazaki",
  "46":"Kagoshima","47":"Okinawa"
};

const NAMES_JA = {
  "01":"北海道","02":"青森","03":"岩手","04":"宮城","05":"秋田",
  "06":"山形","07":"福島","08":"茨城","09":"栃木","10":"群馬",
  "11":"埼玉","12":"千葉","13":"東京","14":"神奈川","15":"新潟",
  "16":"富山","17":"石川","18":"福井","19":"山梨","20":"長野",
  "21":"岐阜","22":"静岡","23":"愛知","24":"三重","25":"滋賀",
  "26":"京都","27":"大阪","28":"兵庫","29":"奈良","30":"和歌山",
  "31":"鳥取","32":"島根","33":"岡山","34":"広島","35":"山口",
  "36":"徳島","37":"香川","38":"愛媛","39":"高知","40":"福岡",
  "41":"佐賀","42":"長崎","43":"熊本","44":"大分","45":"宮崎",
  "46":"鹿児島","47":"沖縄"
};

const DEPARTEMENTS_FR = {
  "01": "Ain", "02": "Aisne", "03": "Allier", "04": "Alpes-de-Haute-Provence", "05": "Hautes-Alpes",
  "06": "Alpes-Maritimes", "07": "Ardèche", "08": "Ardennes", "09": "Ariège", "10": "Aube",
  "11": "Aude", "12": "Aveyron", "13": "Bouches-du-Rhône", "14": "Calvados", "15": "Cantal",
  "16": "Charente", "17": "Charente-Maritime", "18": "Cher", "19": "Corrèze", "21": "Côte-d'Or",
  "22": "Côtes-d'Armor", "23": "Creuse", "24": "Dordogne", "25": "Doubs", "26": "Drôme",
  "27": "Eure", "28": "Eure-et-Loir", "29": "Finistère", "2A": "Corse-du-Sud", "2B": "Haute-Corse",
  "30": "Gard", "31": "Haute-Garonne", "32": "Gers", "33": "Gironde", "34": "Hérault",
  "35": "Ille-et-Vilaine", "36": "Indre", "37": "Indre-et-Loire", "38": "Isère", "39": "Jura",
  "40": "Landes", "41": "Loir-et-Cher", "42": "Loire", "43": "Haute-Loire", "44": "Loire-Atlantique",
  "45": "Loiret", "46": "Lot", "47": "Lot-et-Garonne", "48": "Lozère", "49": "Maine-et-Loire",
  "50": "Manche", "51": "Marne", "52": "Haute-Marne", "53": "Mayenne", "54": "Meurthe-et-Moselle",
  "55": "Meuse", "56": "Morbihan", "57": "Moselle", "58": "Nièvre", "59": "Nord",
  "60": "Oise", "61": "Orne", "62": "Pas-de-Calais", "63": "Puy-de-Dôme", "64": "Pyrénées-Atlantiques",
  "65": "Hautes-Pyrénées", "66": "Pyrénées-Orientales", "67": "Bas-Rhin", "68": "Haut-Rhin", "69": "Rhône",
  "70": "Haute-Saône", "71": "Saône-et-Loire", "72": "Sarthe", "73": "Savoie", "74": "Haute-Savoie",
  "75": "Paris", "76": "Seine-Maritime", "77": "Seine-et-Marne", "78": "Yvelines", "79": "Deux-Sèvres",
  "80": "Somme", "81": "Tarn", "82": "Tarn-et-Garonne", "83": "Var", "84": "Vaucluse",
  "85": "Vendée", "86": "Vienne", "87": "Haute-Vienne", "88": "Vosges", "89": "Yonne",
  "90": "Territoire de Belfort", "91": "Essonne", "92": "Hauts-de-Seine", "93": "Seine-Saint-Denis", "94": "Val-de-Marne",
  "95": "Val-d'Oise",
  "971": "Guadeloupe", "972": "Martinique", "973": "Guyane", "974": "La Réunion", "976": "Mayotte"
};

// Proportional Cartogram Grid Layout
const GRID = [
  { code: "01", x: 380, y: 15, w: 150, h: 110 },
  { code: "02", x: 420, y: 140, w: 70, h: 45 },
  { code: "03", x: 460, y: 195, w: 60, h: 65 },
  { code: "05", x: 395, y: 195, w: 60, h: 55 },
  { code: "04", x: 460, y: 265, w: 60, h: 55 },
  { code: "06", x: 395, y: 255, w: 60, h: 50 },
  { code: "07", x: 410, y: 310, w: 85, h: 55 },
  { code: "08", x: 460, y: 375, w: 50, h: 50 },
  { code: "09", x: 415, y: 375, w: 40, h: 45 },
  { code: "10", x: 370, y: 375, w: 40, h: 40 },
  { code: "11", x: 370, y: 420, w: 60, h: 35 },
  { code: "12", x: 440, y: 430, w: 50, h: 75 },
  { code: "13", x: 370, y: 460, w: 65, h: 35 },
  { code: "14", x: 370, y: 500, w: 65, h: 35 },
  { code: "15", x: 310, y: 285, w: 80, h: 45 },
  { code: "16", x: 300, y: 335, w: 45, h: 35 },
  { code: "17", x: 275, y: 290, w: 20, h: 60 },
  { code: "18", x: 245, y: 355, w: 35, h: 35 },
  { code: "20", x: 320, y: 375, w: 45, h: 75 },
  { code: "19", x: 320, y: 455, w: 45, h: 40 },
  { code: "22", x: 310, y: 500, w: 55, h: 40 },
  { code: "21", x: 270, y: 400, w: 45, h: 50 },
  { code: "23", x: 270, y: 455, w: 45, h: 40 },
  { code: "25", x: 235, y: 405, w: 30, h: 40 },
  { code: "26", x: 200, y: 380, w: 30, h: 50 },
  { code: "24", x: 235, y: 450, w: 30, h: 55 },
  { code: "27", x: 200, y: 435, w: 30, h: 30 },
  { code: "29", x: 205, y: 470, w: 25, h: 40 },
  { code: "30", x: 180, y: 475, w: 20, h: 45 },
  { code: "28", x: 155, y: 395, w: 40, h: 55 },
  { code: "31", x: 110, y: 395, w: 40, h: 25 },
  { code: "32", x: 65, y: 395, w: 40, h: 25 },
  { code: "33", x: 110, y: 425, w: 40, h: 35 },
  { code: "34", x: 65, y: 425, w: 40, h: 35 },
  { code: "35", x: 20, y: 410, w: 40, h: 35 },
  { code: "37", x: 145, y: 465, w: 30, h: 25 },
  { code: "36", x: 145, y: 495, w: 30, h: 25 },
  { code: "38", x: 105, y: 465, w: 35, h: 25 },
  { code: "39", x: 105, y: 495, w: 35, h: 25 },
  { code: "40", x: 20, y: 455, w: 40, h: 30 },
  { code: "41", x: 10, y: 490, w: 25, h: 25 },
  { code: "42", x: 5, y: 520, w: 25, h: 30 },
  { code: "44", x: 65, y: 455, w: 30, h: 30 },
  { code: "43", x: 40, y: 490, w: 35, h: 35 },
  { code: "45", x: 80, y: 490, w: 20, h: 35 },
  { code: "46", x: 40, y: 530, w: 60, h: 35 },
  { code: "47", x: 25, y: 25, w: 60, h: 45 }
];

const FR_GRID = [
  { code: '01', x: 358, y: 285, w: 38, h: 38, isDom: false },
  { code: '02', x: 238, y: 85, w: 38, h: 38, isDom: false },
  { code: '03', x: 278, y: 285, w: 38, h: 38, isDom: false },
  { code: '04', x: 398, y: 405, w: 38, h: 38, isDom: false },
  { code: '05', x: 358, y: 365, w: 38, h: 38, isDom: false },
  { code: '06', x: 438, y: 405, w: 38, h: 38, isDom: false },
  { code: '07', x: 278, y: 365, w: 38, h: 38, isDom: false },
  { code: '08', x: 278, y: 85, w: 38, h: 38, isDom: false },
  { code: '09', x: 158, y: 445, w: 38, h: 38, isDom: false },
  { code: '10', x: 318, y: 165, w: 38, h: 38, isDom: false },
  { code: '11', x: 198, y: 445, w: 38, h: 38, isDom: false },
  { code: '12', x: 238, y: 405, w: 38, h: 38, isDom: false },
  { code: '13', x: 318, y: 445, w: 38, h: 38, isDom: false },
  { code: '14', x: 78, y: 125, w: 38, h: 38, isDom: false },
  { code: '15', x: 198, y: 365, w: 38, h: 38, isDom: false },
  { code: '16', x: 118, y: 285, w: 38, h: 38, isDom: false },
  { code: '17', x: 78, y: 285, w: 38, h: 38, isDom: false },
  { code: '18', x: 278, y: 245, w: 38, h: 38, isDom: false },
  { code: '19', x: 158, y: 325, w: 38, h: 38, isDom: false },
  { code: '21', x: 358, y: 245, w: 38, h: 38, isDom: false },
  { code: '22', x: 38, y: 165, w: 38, h: 38, isDom: false },
  { code: '23', x: 238, y: 285, w: 38, h: 38, isDom: false },
  { code: '24', x: 118, y: 325, w: 38, h: 38, isDom: false },
  { code: '25', x: 438, y: 245, w: 38, h: 38, isDom: false },
  { code: '26', x: 318, y: 365, w: 38, h: 38, isDom: false },
  { code: '27', x: 118, y: 125, w: 38, h: 38, isDom: false },
  { code: '28', x: 238, y: 205, w: 38, h: 38, isDom: false },
  { code: '29', x: 38, y: 205, w: 38, h: 38, isDom: false },
  { code: '2A', x: 398, y: 485, w: 38, h: 38, isDom: false },
  { code: '2B', x: 438, y: 485, w: 38, h: 38, isDom: false },
  { code: '30', x: 318, y: 405, w: 38, h: 38, isDom: false },
  { code: '31', x: 118, y: 445, w: 38, h: 38, isDom: false },
  { code: '32', x: 118, y: 405, w: 38, h: 38, isDom: false },
  { code: '33', x: 78, y: 325, w: 38, h: 38, isDom: false },
  { code: '34', x: 278, y: 445, w: 38, h: 38, isDom: false },
  { code: '35', x: 78, y: 165, w: 38, h: 38, isDom: false },
  { code: '36', x: 198, y: 285, w: 38, h: 38, isDom: false },
  { code: '37', x: 198, y: 245, w: 38, h: 38, isDom: false },
  { code: '38', x: 318, y: 325, w: 38, h: 38, isDom: false },
  { code: '39', x: 398, y: 245, w: 38, h: 38, isDom: false },
  { code: '40', x: 78, y: 365, w: 38, h: 38, isDom: false },
  { code: '41', x: 238, y: 245, w: 38, h: 38, isDom: false },
  { code: '42', x: 238, y: 325, w: 38, h: 38, isDom: false },
  { code: '43', x: 238, y: 365, w: 38, h: 38, isDom: false },
  { code: '44', x: 118, y: 205, w: 38, h: 38, isDom: false },
  { code: '45', x: 358, y: 205, w: 38, h: 38, isDom: false },
  { code: '46', x: 158, y: 365, w: 38, h: 38, isDom: false },
  { code: '47', x: 118, y: 365, w: 38, h: 38, isDom: false },
  { code: '48', x: 278, y: 405, w: 38, h: 38, isDom: false },
  { code: '49', x: 158, y: 205, w: 38, h: 38, isDom: false },
  { code: '50', x: 38, y: 125, w: 38, h: 38, isDom: false },
  { code: '51', x: 318, y: 125, w: 38, h: 38, isDom: false },
  { code: '52', x: 358, y: 165, w: 38, h: 38, isDom: false },
  { code: '53', x: 118, y: 165, w: 38, h: 38, isDom: false },
  { code: '54', x: 358, y: 125, w: 38, h: 38, isDom: false },
  { code: '55', x: 318, y: 85, w: 38, h: 38, isDom: false },
  { code: '56', x: 78, y: 205, w: 38, h: 38, isDom: false },
  { code: '57', x: 358, y: 85, w: 38, h: 38, isDom: false },
  { code: '58', x: 318, y: 245, w: 38, h: 38, isDom: false },
  { code: '59', x: 278, y: 45, w: 38, h: 38, isDom: false },
  { code: '60', x: 238, y: 125, w: 38, h: 38, isDom: false },
  { code: '61', x: 158, y: 165, w: 38, h: 38, isDom: false },
  { code: '62', x: 238, y: 45, w: 38, h: 38, isDom: false },
  { code: '63', x: 198, y: 325, w: 38, h: 38, isDom: false },
  { code: '64', x: 78, y: 405, w: 38, h: 38, isDom: false },
  { code: '65', x: 78, y: 445, w: 38, h: 38, isDom: false },
  { code: '66', x: 238, y: 445, w: 38, h: 38, isDom: false },
  { code: '67', x: 398, y: 85, w: 38, h: 38, isDom: false },
  { code: '68', x: 398, y: 125, w: 38, h: 38, isDom: false },
  { code: '69', x: 278, y: 325, w: 38, h: 38, isDom: false },
  { code: '70', x: 438, y: 205, w: 38, h: 38, isDom: false },
  { code: '71', x: 318, y: 285, w: 38, h: 38, isDom: false },
  { code: '72', x: 198, y: 205, w: 38, h: 38, isDom: false },
  { code: '73', x: 358, y: 325, w: 38, h: 38, isDom: false },
  { code: '74', x: 398, y: 285, w: 38, h: 38, isDom: false },
  { code: '75', x: 238, y: 165, w: 38, h: 38, isDom: false },
  { code: '76', x: 158, y: 85, w: 38, h: 38, isDom: false },
  { code: '77', x: 278, y: 125, w: 38, h: 38, isDom: false },
  { code: '78', x: 198, y: 165, w: 38, h: 38, isDom: false },
  { code: '79', x: 118, y: 245, w: 38, h: 38, isDom: false },
  { code: '80', x: 198, y: 85, w: 38, h: 38, isDom: false },
  { code: '81', x: 198, y: 405, w: 38, h: 38, isDom: false },
  { code: '82', x: 158, y: 405, w: 38, h: 38, isDom: false },
  { code: '83', x: 358, y: 445, w: 38, h: 38, isDom: false },
  { code: '84', x: 358, y: 405, w: 38, h: 38, isDom: false },
  { code: '85', x: 78, y: 245, w: 38, h: 38, isDom: false },
  { code: '86', x: 158, y: 245, w: 38, h: 38, isDom: false },
  { code: '87', x: 158, y: 285, w: 38, h: 38, isDom: false },
  { code: '88', x: 398, y: 165, w: 38, h: 38, isDom: false },
  { code: '89', x: 398, y: 205, w: 38, h: 38, isDom: false },
  { code: '90', x: 478, y: 205, w: 38, h: 38, isDom: false },
  { code: '91', x: 278, y: 165, w: 38, h: 38, isDom: false },
  { code: '92', x: 278, y: 205, w: 38, h: 38, isDom: false },
  { code: '93', x: 198, y: 125, w: 38, h: 38, isDom: false },
  { code: '94', x: 318, y: 205, w: 38, h: 38, isDom: false },
  { code: '95', x: 158, y: 125, w: 38, h: 38, isDom: false },
  { code: '971', x: 38, y: 85, w: 38, h: 38, isDom: true },
  { code: '972', x: 38, y: 165, w: 38, h: 38, isDom: true },
  { code: '973', x: 38, y: 245, w: 38, h: 38, isDom: true },
  { code: '974', x: 38, y: 325, w: 38, h: 38, isDom: true },
  { code: '976', x: 38, y: 405, w: 38, h: 38, isDom: true },
];

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

const PROVINCES_IT = {
  "AG": "Agrigento", "AL": "Alessandria", "AN": "Ancona", "AO": "Valle d'Aosta/Vallée d'Aoste",
  "AP": "Ascoli Piceno", "AQ": "L'Aquila", "AR": "Arezzo", "AT": "Asti", "AV": "Avellino",
  "BA": "Bari", "BG": "Bergamo", "BI": "Biella", "BL": "Belluno", "BN": "Benevento",
  "BO": "Bologna", "BR": "Brindisi", "BS": "Brescia", "BT": "Barletta-Andria-Trani",
  "BZ": "Bolzano/Bozen", "CA": "Cagliari", "CB": "Campobasso", "CE": "Caserta",
  "CH": "Chieti", "CL": "Caltanissetta", "CN": "Cuneo", "CO": "Como", "CR": "Cremona",
  "CS": "Cosenza", "CT": "Catania", "CZ": "Catanzaro", "EN": "Enna", "FC": "Forlì-Cesena",
  "FE": "Ferrara", "FG": "Foggia", "FI": "Firenze", "FM": "Fermo", "FR": "Frosinone",
  "GE": "Genova", "GO": "Gorizia", "GR": "Grosseto", "IM": "Imperia", "IS": "Isernia",
  "KR": "Crotone", "LC": "Lecco", "LE": "Lecce", "LI": "Livorno", "LO": "Lodi",
  "LT": "Latina", "LU": "Lucca", "MB": "Monza e della Brianza", "MC": "Macerata",
  "ME": "Messina", "MI": "Milano", "MN": "Mantova", "MO": "Modena", "MS": "Massa-Carrara",
  "MT": "Matera", "NA": "Napoli", "NO": "Novara", "NU": "Nuoro", "OR": "Oristano",
  "PA": "Palermo", "PC": "Piacenza", "PD": "Padova", "PE": "Pescara", "PG": "Perugia",
  "PI": "Pisa", "PN": "Pordenone", "PO": "Prato", "PR": "Parma", "PT": "Pistoia",
  "PU": "Pesaro e Urbino", "PV": "Pavia", "PZ": "Potenza", "RA": "Ravenna",
  "RC": "Reggio di Calabria", "RE": "Reggio nell'Emilia", "RG": "Ragusa", "RI": "Rieti",
  "RM": "Roma", "RN": "Rimini", "RO": "Rovigo", "SA": "Salerno", "SI": "Siena",
  "SO": "Sondrio", "SP": "La Spezia", "SR": "Siracusa", "SS": "Sassari", "SU": "Sud Sardegna",
  "SV": "Savona", "TA": "Taranto", "TE": "Teramo", "TN": "Trento", "TO": "Torino",
  "TP": "Trapani", "TR": "Terni", "TS": "Trieste", "TV": "Treviso", "UD": "Udine",
  "VA": "Varese", "VB": "Verbano-Cusio-Ossola", "VC": "Vercelli", "VE": "Venezia",
  "VI": "Vicenza", "VR": "Verona", "VT": "Viterbo", "VV": "Vibo Valentia"
};

const STATES_US = {
  "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
  "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia", "FL": "Florida",
  "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana",
  "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine",
  "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
  "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire",
  "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota",
  "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island",
  "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
  "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin",
  "WY": "Wyoming"
};

const PROVINCES_CN = {
  "11": "Beijing", "12": "Tianjin", "13": "Hebei", "14": "Shanxi", "15": "Inner Mongolia",
  "21": "Liaoning", "22": "Jilin", "23": "Heilongjiang", "31": "Shanghai", "32": "Jiangsu",
  "33": "Zhejiang", "34": "Anhui", "35": "Fujian", "36": "Jiangxi", "37": "Shandong",
  "41": "Henan", "42": "Hubei", "43": "Hunan", "44": "Guangdong", "45": "Guangxi",
  "46": "Hainan", "50": "Chongqing", "51": "Sichuan", "52": "Guizhou", "53": "Yunnan",
  "54": "Tibet", "61": "Shaanxi", "62": "Gansu", "63": "Qinghai", "64": "Ningxia",
  "65": "Xinjiang", "81": "Hong Kong", "82": "Macau"
};

const PROVINCES_CN_LABELS = {
  "11": "BJ", "12": "TJ", "13": "HE", "14": "SX", "15": "IM",
  "21": "LN", "22": "JL", "23": "HL", "31": "SH", "32": "JS",
  "33": "ZJ", "34": "AH", "35": "FJ", "36": "JX", "37": "SD",
  "41": "HA", "42": "HB", "43": "HN", "44": "GD", "45": "GX",
  "46": "HI", "50": "CQ", "51": "SC", "52": "GZ", "53": "YN",
  "54": "XZ", "61": "SN", "62": "GS", "63": "QH", "64": "NX",
  "65": "XJ", "81": "HK", "82": "MC"
};

const PROVINCES_KR = {
  "1": "Busan", "2": "Chungcheongbuk-do", "3": "Chungcheongnam-do", "4": "Daegu", "5": "Daejeon",
  "6": "Gangwon-do", "7": "Gwangju", "8": "Gyeonggi-do", "9": "Gyeongsangbuk-do", "10": "Gyeongsangnam-do",
  "11": "Incheon", "12": "Jeju", "13": "Jeollabuk-do", "14": "Jeollanam-do", "15": "Seoul",
  "16": "Ulsan"
};

const PROVINCES_KR_LABELS = {
  "1": "BS", "2": "CB", "3": "CN", "4": "DG", "5": "DJ",
  "6": "GW", "7": "GJ", "8": "GG", "9": "GB", "10": "GN",
  "11": "IC", "12": "JJ", "13": "JB", "14": "JN", "15": "SU",
  "16": "US"
};

const STATES_AU = {
  "1": "New South Wales", "2": "Victoria", "3": "Queensland", "4": "South Australia",
  "5": "Western Australia", "6": "Tasmania", "7": "Northern Territory", "8": "Australian Capital Territory"
};

const STATES_AU_LABELS = {
  "1": "NSW", "2": "VIC", "3": "QLD", "4": "SA", "5": "WA", "6": "TAS", "7": "NT", "8": "ACT"
};

const STATES_IN = {
  "1": "Andaman and Nicobar", "2": "Andhra Pradesh", "3": "Arunachal Pradesh", "4": "Assam", "5": "Bihar",
  "6": "Chandigarh", "7": "Chhattisgarh", "8": "Dadra and Nagar Haveli", "9": "Daman and Diu", "10": "Delhi",
  "11": "Goa", "12": "Gujarat", "13": "Haryana", "14": "Himachal Pradesh", "15": "Jammu and Kashmir",
  "16": "Jharkhand", "17": "Karnataka", "18": "Kerala", "19": "Lakshadweep", "20": "Madhya Pradesh",
  "21": "Maharashtra", "22": "Manipur", "23": "Meghalaya", "24": "Mizoram", "25": "Nagaland",
  "26": "Orissa", "27": "Puducherry", "28": "Punjab", "29": "Rajasthan", "30": "Sikkim",
  "31": "Tamil Nadu", "32": "Tripura", "33": "Uttar Pradesh", "34": "Uttaranchal", "35": "West Bengal"
};

const STATES_IN_LABELS = {
  "1": "AN", "2": "AP", "3": "AR", "4": "AS", "5": "BR", "6": "CH", "7": "CT", "8": "DN", "9": "DD", "10": "DL",
  "11": "GA", "12": "GJ", "13": "HR", "14": "HP", "15": "JK", "16": "JH", "17": "KA", "18": "KL", "19": "LD", "20": "MP",
  "21": "MH", "22": "MN", "23": "ML", "24": "MZ", "25": "NL", "26": "OR", "27": "PY", "28": "PB", "29": "RJ", "30": "SK",
  "31": "TN", "32": "TR", "33": "UP", "34": "UT", "35": "WB"
};

const REGIONS_UK = {
  "UKC": "North East", "UKD": "North West", "UKE": "Yorkshire and the Humber", "UKF": "East Midlands",
  "UKG": "West Midlands", "UKH": "East of England", "UKI": "London", "UKJ": "South East",
  "UKK": "South West", "UKL": "Wales", "UKM": "Scotland", "UKN": "Northern Ireland"
};

const REGIONS_UK_LABELS = {
  "UKC": "NE", "UKD": "NW", "UKE": "YH", "UKF": "EM", "UKG": "WM", "UKH": "EE",
  "UKI": "LN", "UKJ": "SE", "UKK": "SW", "UKL": "WA", "UKM": "SC", "UKN": "NI"
};

const STATES_MX = {
  "1": "Aguascalientes", "2": "Baja California", "3": "Baja California Sur", "4": "Campeche",
  "5": "Coahuila", "6": "Colima", "7": "Chiapas", "8": "Chihuahua", "9": "Ciudad de México",
  "10": "Durango", "11": "Guanajuato", "12": "Guerrero", "13": "Hidalgo", "14": "Jalisco",
  "15": "México", "16": "Michoacán", "17": "Morelos", "18": "Nayarit", "19": "Nuevo León",
  "20": "Oaxaca", "21": "Puebla", "22": "Querétaro", "23": "Quintana Roo", "24": "San Luis Potosí",
  "25": "Sinaloa", "26": "Sonora", "27": "Tabasco", "28": "Tamaulipas", "29": "Tlaxcala",
  "30": "Veracruz", "31": "Yucatán", "32": "Zacatecas"
};

const STATES_MX_LABELS = {
  "1": "AGS", "2": "BC", "3": "BCS", "4": "CAMP", "5": "COAH", "6": "COL", "7": "CHIS", "8": "CHIH",
  "9": "CDMX", "10": "DGO", "11": "GTO", "12": "GRO", "13": "HGO", "14": "JAL", "15": "MEX", "16": "MICH",
  "17": "MOR", "18": "NAY", "19": "NL", "20": "OAX", "21": "PUE", "22": "QRO", "23": "QR", "24": "SLP",
  "25": "SIN", "26": "SON", "27": "TAB", "28": "TAMPS", "29": "TLAX", "30": "VER", "31": "YUC", "32": "ZAC"
};

const PROVINCES_TR = {
  "1": "Adana", "2": "Adıyaman", "3": "Afyonkarahisar", "4": "Ağrı", "5": "Amasya", "6": "Ankara",
  "7": "Antalya", "8": "Artvin", "9": "Aydın", "10": "Balıkesir", "11": "Bilecik", "12": "Bingöl",
  "13": "Bitlis", "14": "Bolu", "15": "Burdur", "16": "Bursa", "17": "Çanakkale", "18": "Çankırı",
  "19": "Çorum", "20": "Denizli", "21": "Diyarbakır", "22": "Edirne", "23": "Elazığ", "24": "Erzincan",
  "25": "Erzurum", "26": "Eskişehir", "27": "Gaziantep", "28": "Giresun", "29": "Gümüşhane", "30": "Hakkari",
  "31": "Hatay", "32": "Isparta", "33": "Mersin", "34": "İstanbul", "35": "İzmir", "36": "Kars",
  "37": "Kastamonu", "38": "Kayseri", "39": "Kırklareli", "40": "Kırşehir", "41": "Kocaeli", "42": "Konya",
  "43": "Kütahya", "44": "Malatya", "45": "Manisa", "46": "Kahramanmaraş", "47": "Mardin", "48": "Muğla",
  "49": "Muş", "50": "Nevşehir", "51": "Niğde", "52": "Ordu", "53": "Rize", "54": "Sakarya",
  "55": "Samsun", "56": "Siirt", "57": "Sinop", "58": "Sivas", "59": "Tekirdağ", "60": "Tokat",
  "61": "Trabzon", "62": "Tunceli", "63": "Şanlıurfa", "64": "Uşak", "65": "Van", "66": "Yozgat",
  "67": "Zonguldak", "68": "Aksaray", "69": "Bayburt", "70": "Karaman", "71": "Kırıkkale", "72": "Batman",
  "73": "Şırnak", "74": "Bartın", "75": "Ardahan", "76": "Iğdır", "77": "Yalova", "78": "Karabük",
  "79": "Kilis", "80": "Osmaniye", "81": "Düzce"
};

const PROVINCES_TR_LABELS = {
  "1": "ADA", "2": "ADY", "3": "AFY", "4": "AGR", "5": "AMA", "6": "ANK", "7": "ANT", "8": "ART",
  "9": "AYD", "10": "BAL", "11": "BIL", "12": "BIN", "13": "BIT", "14": "BOL", "15": "BUR", "16": "BSA",
  "17": "CAN", "18": "CKR", "19": "COR", "20": "DEN", "21": "DIY", "22": "EDI", "23": "ELA", "24": "ERC",
  "25": "ERZ", "26": "ESK", "27": "GAZ", "28": "GIR", "29": "GUM", "30": "HAK", "31": "HAT", "32": "ISP",
  "33": "MER", "34": "IST", "35": "IZM", "36": "KAS", "37": "KST", "38": "KAY", "39": "KLR", "40": "KIR",
  "41": "KOC", "42": "KON", "43": "KUT", "44": "MAL", "45": "MAN", "46": "MAR", "47": "MRD", "48": "MUG",
  "49": "MUS", "50": "NEV", "51": "NIG", "52": "ORD", "53": "RIZ", "54": "SAK", "55": "SAM", "56": "SII",
  "57": "SIN", "58": "SIV", "59": "TEK", "60": "TOK", "61": "TRA", "62": "TUN", "63": "URF", "64": "USA",
  "65": "VAN", "66": "YOZ", "67": "ZON", "68": "AKS", "69": "BAY", "70": "KRM", "71": "KRK", "72": "BAT",
  "73": "SIR", "74": "BAR", "75": "ARD", "76": "IGD", "77": "YAL", "78": "KRB", "79": "KIL", "80": "OSM",
  "81": "DUZ"
};


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



const COLORS = ["#f3f4f6", "#bfdbfe", "#a7f3d0", "#fef08a", "#fed7aa", "#fda4af"];

// State Variables
let state = {
  currentMap: "jp",
  username: "Votre nom",
  lang: "en",
  levels: {},
  jpLevels: {},
  worldLevels: {},
  frLevels: {},
  esLevels: {},
  itLevels: {},
  usLevels: {},
  cnLevels: {},
  krLevels: {},
  auLevels: {},
  inLevels: {},
  ukLevels: {},
  mxLevels: {},
  trLevels: {}
};
let activePrefCode = null;
let japanData = null;
let worldData = null; // Cache for parsed topojson data
let franceDepsData = null;
let franceDomTomData = null;
let spainProvincesData = null;
let italyProvincesData = null;
let usaStatesData = null;
let chinaProvincesData = null;
let koreaProvincesData = null;
let australiaStatesData = null;
let indiaStatesData = null;
let ukRegionsData = null;
let mexicoStatesData = null;
let turkeyProvincesData = null;

// Country Translation dictionary
const COUNTRY_NAMES = {
  "242": { en: "Fiji", fr: "Fidji", ja: "フィジー", es: "Fiyi", ko: "피지", zh: "斐济", hi: "Fiji" },
  "834": { en: "Tanzania", fr: "Tanzanie", ja: "タンザニア", es: "Tanzania", ko: "탄자니아", zh: "坦桑尼亚", hi: "Tanzania" },
  "732": { en: "Western Sahara", fr: "Sahara Occidental", ja: "西サハラ", es: "Sahara Occidental", ko: "서사하라", zh: "西撒哈拉", hi: "W. Sahara" },
  "124": { en: "Canada", fr: "Canada", ja: "カナダ", es: "Canadá", ko: "캐나다", zh: "加拿大", hi: "कनाडा" },
  "840": { en: "United States", fr: "États-Unis", ja: "アメリカ合衆国", es: "Estados Unidos", ko: "미국", zh: "美国", hi: "United States of America" },
  "398": { en: "Kazakhstan", fr: "Kazakhstan", ja: "カザフスタン", es: "Kazajistán", ko: "카자흐스탄", zh: "哈萨克斯坦", hi: "Kazakhstan" },
  "860": { en: "Uzbekistan", fr: "Ouzbékistan", ja: "ウズベキスタン", es: "Uzbekistán", ko: "우즈베키스탄", zh: "乌兹别克斯坦", hi: "Uzbekistan" },
  "598": { en: "Papua New Guinea", fr: "Papouasie-Nouvelle-Guinée", ja: "パプアニューギニア", es: "Papúa Nueva Guinea", ko: "파푸아뉴기니", zh: "巴布亚新几内亚", hi: "Papua New Guinea" },
  "360": { en: "Indonesia", fr: "Indonésie", ja: "インドネシア", es: "Indonesia", ko: "인도네시아", zh: "印度尼西亚", hi: "Indonesia" },
  "032": { en: "Argentina", fr: "Argentine", ja: "アルゼンチン", es: "Argentina", ko: "아르헨티나", zh: "阿根廷", hi: "Argentina" },
  "152": { en: "Chile", fr: "Chili", ja: "チリ", es: "Chile", ko: "칠레", zh: "智利", hi: "Chile" },
  "180": { en: "DR Congo", fr: "Congo (Rép. dém.)", ja: "コンゴ民主共和国", es: "Congo (Rep. Dem.)", ko: "콩고 민주 공화국", zh: "民主刚果", hi: "Dem. Rep. Congo" },
  "706": { en: "Somalia", fr: "Somalie", ja: "ソマリア", es: "Somalia", ko: "소말리아", zh: "索马里", hi: "Somalia" },
  "404": { en: "Kenya", fr: "Kenya", ja: "ケニア", es: "Kenia", ko: "케냐", zh: "肯尼亚", hi: "Kenya" },
  "729": { en: "Sudan", fr: "Soudan", ja: "スーダン", es: "Sudán", ko: "수단", zh: "苏丹", hi: "Sudan" },
  "148": { en: "Chad", fr: "Tchad", ja: "チャド", es: "Chad", ko: "차드", zh: "乍得", hi: "Chad" },
  "332": { en: "Haiti", fr: "Haïti", ja: "ハイチ", es: "Haití", ko: "아이티", zh: "海地", hi: "Haiti" },
  "214": { en: "Dominican Republic", fr: "République dominicaine", ja: "ドミニカ共和国", es: "República Dominicana", ko: "도미니카 공화국", zh: "多明尼加", hi: "Dominican Rep." },
  "643": { en: "Russia", fr: "Russie", ja: "ロシア連邦", es: "Rusia", ko: "러시아", zh: "俄罗斯", hi: "रूस" },
  "044": { en: "Bahamas", fr: "Bahamas", ja: "バハマ", es: "Bahamas", ko: "바하마", zh: "巴哈马", hi: "Bahamas" },
  "238": { en: "Falkland Islands", fr: "Îles Malouines", ja: "フォークランド（マルビナス）諸島", es: "Islas Malvinas", ko: "포클랜드 제도", zh: "福克兰群岛", hi: "Falkland Is." },
  "578": { en: "Norway", fr: "Norvège", ja: "ノルウェー", es: "Noruega", ko: "노르웨이", zh: "挪威", hi: "Norway" },
  "304": { en: "Greenland", fr: "Groenland", ja: "グリーンランド", es: "Groenlandia", ko: "그린란드", zh: "格陵兰", hi: "Greenland" },
  "260": { en: "French Southern and Antarctic Lands", fr: "Terres australes et antarctiques françaises", ja: "フランス領南方・南極地域", es: "Tierras Australes y Antárticas Francesas", ko: "프랑스령 남부와 남극 지역", zh: "法国南部和南极土地", hi: "Fr. S. Antarctic Lands" },
  "626": { en: "Timor-Leste", fr: "Timor oriental", ja: "東ティモール", es: "Timor Oriental", ko: "동티모르", zh: "东帝汶", hi: "Timor-Leste" },
  "710": { en: "South Africa", fr: "Afrique du Sud", ja: "南アフリカ", es: "Sudáfrica", ko: "남아프리카 공화국", zh: "南非", hi: "South Africa" },
  "426": { en: "Lesotho", fr: "Lesotho", ja: "レソト", es: "Lesotho", ko: "레소토", zh: "莱索托", hi: "Lesotho" },
  "484": { en: "Mexico", fr: "Mexique", ja: "メキシコ", es: "México", ko: "멕시코", zh: "墨西哥", hi: "Mexico" },
  "858": { en: "Uruguay", fr: "Uruguay", ja: "ウルグアイ", es: "Uruguay", ko: "우루과이", zh: "乌拉圭", hi: "Uruguay" },
  "076": { en: "Brazil", fr: "Brésil", ja: "ブラジル", es: "Brasil", ko: "브라질", zh: "巴西", hi: "Brazil" },
  "068": { en: "Bolivia", fr: "Bolivie", ja: "ボリビア多民族国", es: "Bolivia", ko: "볼리비아", zh: "玻利维亚", hi: "Bolivia" },
  "604": { en: "Peru", fr: "Pérou", ja: "ペルー", es: "Perú", ko: "페루", zh: "秘鲁", hi: "Peru" },
  "170": { en: "Colombia", fr: "Colombie", ja: "コロンビア", es: "Colombia", ko: "콜롬비아", zh: "哥伦比亚", hi: "Colombia" },
  "591": { en: "Panama", fr: "Panama", ja: "パナマ", es: "Panamá", ko: "파나마", zh: "巴拿马", hi: "Panama" },
  "188": { en: "Costa Rica", fr: "Costa Rica", ja: "コスタリカ", es: "Costa Rica", ko: "코스타리카", zh: "哥斯达黎加", hi: "Costa Rica" },
  "558": { en: "Nicaragua", fr: "Nicaragua", ja: "ニカラグア", es: "Nicaragua", ko: "니카라과", zh: "尼加拉瓜", hi: "Nicaragua" },
  "340": { en: "Honduras", fr: "Honduras", ja: "ホンジュラス", es: "Honduras", ko: "온두라스", zh: "洪都拉斯", hi: "Honduras" },
  "222": { en: "El Salvador", fr: "Salvador", ja: "エルサルバドル", es: "El Salvador", ko: "엘살바도르", zh: "萨尔瓦多", hi: "El Salvador" },
  "320": { en: "Guatemala", fr: "Guatemala", ja: "グアテマラ", es: "Guatemala", ko: "과테말라", zh: "危地马拉", hi: "Guatemala" },
  "084": { en: "Belize", fr: "Belize", ja: "ベリーズ", es: "Belice", ko: "벨리즈", zh: "伯利兹", hi: "Belize" },
  "862": { en: "Venezuela", fr: "Venezuela", ja: "ベネズエラ・ボリバル共和国", es: "Venezuela", ko: "베네수엘라", zh: "委内瑞拉", hi: "Venezuela" },
  "328": { en: "Guyana", fr: "Guyana", ja: "ガイアナ", es: "Guyana", ko: "가이아나", zh: "圭亚那", hi: "Guyana" },
  "740": { en: "Suriname", fr: "Surinam", ja: "スリナム", es: "Surinam", ko: "수리남", zh: "苏里南", hi: "Suriname" },
  "250": { en: "France", fr: "France", ja: "フランス", es: "Francia", ko: "프랑스", zh: "法国", hi: "फ़्रांस" },
  "218": { en: "Ecuador", fr: "Équateur", ja: "エクアドル", es: "Ecuador", ko: "에콰도르", zh: "厄瓜多尔", hi: "Ecuador" },
  "630": { en: "Puerto Rico", fr: "Porto Rico", ja: "プエルトリコ", es: "Puerto Rico", ko: "푸에르토리코", zh: "波多黎各", hi: "Puerto Rico" },
  "388": { en: "Jamaica", fr: "Jamaïque", ja: "ジャマイカ", es: "Jamaica", ko: "자메이카", zh: "牙买加", hi: "Jamaica" },
  "192": { en: "Cuba", fr: "Cuba", ja: "キューバ", es: "Cuba", ko: "쿠바", zh: "古巴", hi: "Cuba" },
  "716": { en: "Zimbabwe", fr: "Zimbabwe", ja: "ジンバブエ", es: "Zimbabue", ko: "짐바브웨", zh: "津巴布韦", hi: "Zimbabwe" },
  "072": { en: "Botswana", fr: "Botswana", ja: "ボツワナ", es: "Botswana", ko: "보츠와나", zh: "博茨瓦纳", hi: "Botswana" },
  "516": { en: "Namibia", fr: "Namibie", ja: "ナミビア", es: "Namibia", ko: "나미비아", zh: "纳米比亚", hi: "Namibia" },
  "686": { en: "Senegal", fr: "Sénégal", ja: "セネガル", es: "Senegal", ko: "세네갈", zh: "塞内加尔", hi: "Senegal" },
  "466": { en: "Mali", fr: "Mali", ja: "マリ", es: "Mali", ko: "말리", zh: "马里", hi: "Mali" },
  "478": { en: "Mauritania", fr: "Mauritanie", ja: "モーリタニア", es: "Mauritania", ko: "모리타니", zh: "毛里塔尼亚", hi: "Mauritania" },
  "204": { en: "Benin", fr: "Bénin", ja: "ベナン", es: "Benín", ko: "베냉", zh: "贝宁", hi: "Benin" },
  "562": { en: "Niger", fr: "Niger", ja: "ニジェール", es: "Níger", ko: "니제르", zh: "尼日尔", hi: "Niger" },
  "566": { en: "Nigeria", fr: "Nigéria", ja: "ナイジェリア", es: "Nigeria", ko: "나이지리아", zh: "尼日利亚", hi: "Nigeria" },
  "120": { en: "Cameroon", fr: "Cameroun", ja: "カメルーン", es: "Camerún", ko: "카메룬", zh: "喀麦隆", hi: "Cameroon" },
  "768": { en: "Togo", fr: "Togo", ja: "トーゴ", es: "Togo", ko: "토고", zh: "多哥", hi: "Togo" },
  "288": { en: "Ghana", fr: "Ghana", ja: "ガーナ", es: "Ghana", ko: "가나", zh: "加纳", hi: "Ghana" },
  "384": { en: "Ivory Coast", fr: "Côte d'Ivoire", ja: "コートジボワール", es: "Costa de Marfil", ko: "코트디부아르", zh: "科特迪瓦", hi: "Côte d'Ivoire" },
  "324": { en: "Guinea", fr: "Guinée", ja: "ギニア", es: "Guinea", ko: "기니", zh: "几内亚", hi: "Guinea" },
  "624": { en: "Guinea-Bissau", fr: "Guinée-Bissau", ja: "ギニアビサウ", es: "Guinea-Bisáu", ko: "기니비사우", zh: "几内亚比绍", hi: "Guinea-Bissau" },
  "430": { en: "Liberia", fr: "Liberia", ja: "リベリア", es: "Liberia", ko: "라이베리아", zh: "利比里亚", hi: "Liberia" },
  "694": { en: "Sierra Leone", fr: "Sierra Leone", ja: "シエラレオネ", es: "Sierra Leone", ko: "시에라리온", zh: "塞拉利昂", hi: "Sierra Leone" },
  "854": { en: "Burkina Faso", fr: "Burkina Faso", ja: "ブルキナファソ", es: "Burkina Faso", ko: "부르키나파소", zh: "布基纳法索", hi: "Burkina Faso" },
  "140": { en: "Central African Republic", fr: "République centrafricaine", ja: "中央アフリカ共和国", es: "República Centroafricana", ko: "중앙아프리카 공화국", zh: "中非共和国", hi: "Central African Rep." },
  "178": { en: "Republic of the Congo", fr: "Congo", ja: "コンゴ共和国", es: "Congo", ko: "콩고", zh: "刚果", hi: "Congo" },
  "266": { en: "Gabon", fr: "Gabon", ja: "ガボン", es: "Gabón", ko: "가봉", zh: "加蓬", hi: "Gabon" },
  "226": { en: "Equatorial Guinea", fr: "Guinée équatoriale", ja: "赤道ギニア", es: "Guinea Ecuatorial", ko: "적도 기니", zh: "赤道几内亚", hi: "Eq. Guinea" },
  "894": { en: "Zambia", fr: "Zambie", ja: "ザンビア", es: "Zambia", ko: "잠비아", zh: "赞比亚", hi: "Zambia" },
  "454": { en: "Malawi", fr: "Malawi", ja: "マラウイ", es: "Malawi", ko: "말라위", zh: "马拉维", hi: "Malawi" },
  "508": { en: "Mozambique", fr: "Mozambique", ja: "モザンビーク", es: "Mozambique", ko: "모잠비크", zh: "莫桑比克", hi: "Mozambique" },
  "748": { en: "Eswatini", fr: "Swaziland", ja: "スワジランド", es: "Suazilandia", ko: "에스와티니", zh: "斯威士兰", hi: "eSwatini" },
  "024": { en: "Angola", fr: "Angola", ja: "アンゴラ", es: "Angola", ko: "앙골라", zh: "安哥拉", hi: "Angola" },
  "108": { en: "Burundi", fr: "Burundi", ja: "ブルンジ", es: "Burundi", ko: "부룬디", zh: "布隆迪", hi: "Burundi" },
  "376": { en: "Israel", fr: "Israël", ja: "イスラエル", es: "Israel", ko: "이스라엘", zh: "以色列", hi: "Israel" },
  "422": { en: "Lebanon", fr: "Liban", ja: "レバノン", es: "Líbano", ko: "레바논", zh: "黎巴嫩", hi: "Lebanon" },
  "450": { en: "Madagascar", fr: "Madagascar", ja: "マダガスカル", es: "Madagascar", ko: "마다가스카르", zh: "马达加斯加", hi: "Madagascar" },
  "275": { en: "Palestine", fr: "Palestine", ja: "パレスチナ", es: "Palestina", ko: "팔레스타인", zh: "巴勒斯坦", hi: "Palestine" },
  "270": { en: "Gambia", fr: "Gambie", ja: "ガンビア", es: "Gambia", ko: "감비아", zh: "冈比亚", hi: "Gambia" },
  "788": { en: "Tunisia", fr: "Tunisie", ja: "チュニジア", es: "Túnez", ko: "튀니지", zh: "突尼斯", hi: "Tunisia" },
  "012": { en: "Algeria", fr: "Algérie", ja: "アルジェリア", es: "Argelia", ko: "알제리", zh: "阿尔及利亚", hi: "Algeria" },
  "400": { en: "Jordan", fr: "Jordanie", ja: "ヨルダン", es: "Jordania", ko: "요르단", zh: "约旦", hi: "Jordan" },
  "784": { en: "United Arab Emirates", fr: "Émirats arabes unis", ja: "アラブ首長国連邦", es: "Emiratos Árabes Unidos", ko: "아랍에미리트", zh: "阿拉伯联合酋长国", hi: "United Arab Emirates" },
  "634": { en: "Qatar", fr: "Qatar", ja: "カタール", es: "Catar", ko: "카타르", zh: "卡塔尔", hi: "Qatar" },
  "414": { en: "Kuwait", fr: "Koweït", ja: "クウェート", es: "Kuwait", ko: "쿠웨이트", zh: "科威特", hi: "Kuwait" },
  "368": { en: "Iraq", fr: "Irak", ja: "イラク", es: "Irak", ko: "이라크", zh: "伊拉克", hi: "Iraq" },
  "512": { en: "Oman", fr: "Oman", ja: "オマーン", es: "Omán", ko: "오만", zh: "阿曼", hi: "Oman" },
  "548": { en: "Vanuatu", fr: "Vanuatu", ja: "バヌアツ", es: "Vanuatu", ko: "바누아투", zh: "瓦努阿图", hi: "Vanuatu" },
  "116": { en: "Cambodia", fr: "Cambodge", ja: "カンボジア", es: "Camboya", ko: "캄보디아", zh: "柬埔寨", hi: "Cambodia" },
  "764": { en: "Thailand", fr: "Thaïlande", ja: "タイ", es: "Tailandia", ko: "태국", zh: "泰国", hi: "Thailand" },
  "418": { en: "Laos", fr: "Laos", ja: "ラオス人民民主共和国", es: "Laos", ko: "라오스", zh: "老挝", hi: "Laos" },
  "104": { en: "Myanmar", fr: "Birmanie", ja: "ミャンマー", es: "Myanmar", ko: "미얀마", zh: "缅甸", hi: "Myanmar" },
  "704": { en: "Vietnam", fr: "Viêt Nam", ja: "ベトナム", es: "Vietnam", ko: "베트남", zh: "越南", hi: "Vietnam" },
  "408": { en: "North Korea", fr: "Corée du Nord", ja: "朝鮮民主主義人民共和国", es: "Corea del Norte", ko: "조선", zh: "朝鲜", hi: "North Korea" },
  "410": { en: "South Korea", fr: "Corée du Sud", ja: "韓国", es: "Corea del Sur", ko: "한국", zh: "韩国", hi: "दक्षिण कोरिया" },
  "496": { en: "Mongolia", fr: "Mongolie", ja: "モンゴル", es: "Mongolia", ko: "몽골", zh: "蒙古", hi: "Mongolia" },
  "356": { en: "India", fr: "Inde", ja: "インド", es: "India", ko: "인도", zh: "印度", hi: "भारत" },
  "050": { en: "Bangladesh", fr: "Bangladesh", ja: "バングラデシュ", es: "Bangladesh", ko: "방글라데시", zh: "孟加拉国", hi: "Bangladesh" },
  "064": { en: "Bhutan", fr: "Bhoutan", ja: "ブータン", es: "Bután", ko: "부탄", zh: "不丹", hi: "Bhutan" },
  "524": { en: "Nepal", fr: "Népal", ja: "ネパール", es: "Nepal", ko: "네팔", zh: "尼泊尔", hi: "Nepal" },
  "586": { en: "Pakistan", fr: "Pakistan", ja: "パキスタン", es: "Pakistán", ko: "파키스탄", zh: "巴基斯坦", hi: "Pakistan" },
  "004": { en: "Afghanistan", fr: "Afghanistan", ja: "アフガニスタン", es: "Afganistán", ko: "아프가니스탄", zh: "阿富汗", hi: "Afghanistan" },
  "762": { en: "Tajikistan", fr: "Tadjikistan", ja: "タジキスタン", es: "Tayikistán", ko: "타지키스탄", zh: "塔吉克斯坦", hi: "Tajikistan" },
  "417": { en: "Kyrgyzstan", fr: "Kirghizistan", ja: "キルギス", es: "Kirguizistán", ko: "키르기스스탄", zh: "吉尔吉斯斯坦", hi: "Kyrgyzstan" },
  "795": { en: "Turkmenistan", fr: "Turkménistan", ja: "トルクメニスタン", es: "Turkmenistán", ko: "투르크메니스탄", zh: "土库曼斯坦", hi: "Turkmenistan" },
  "364": { en: "Iran", fr: "Iran", ja: "イラン・イスラム共和国", es: "Iran", ko: "이란", zh: "伊朗", hi: "Iran" },
  "760": { en: "Syria", fr: "Syrie", ja: "シリア・アラブ共和国", es: "Siria", ko: "시리아", zh: "叙利亚", hi: "Syria" },
  "051": { en: "Armenia", fr: "Arménie", ja: "アルメニア", es: "Armenia", ko: "아르메니아", zh: "亚美尼亚", hi: "Armenia" },
  "752": { en: "Sweden", fr: "Suède", ja: "スウェーデン", es: "Suecia", ko: "스웨덴", zh: "瑞典", hi: "Sweden" },
  "112": { en: "Belarus", fr: "Biélorussie", ja: "ベラルーシ", es: "Bielorrusia", ko: "벨라루스", zh: "白俄罗斯", hi: "Belarus" },
  "804": { en: "Ukraine", fr: "Ukraine", ja: "ウクライナ", es: "Ucrania", ko: "우크라이나", zh: "乌克兰", hi: "Ukraine" },
  "616": { en: "Poland", fr: "Pologne", ja: "ポーランド", es: "Polonia", ko: "폴란드", zh: "波兰", hi: "Poland" },
  "040": { en: "Austria", fr: "Autriche", ja: "オーストリア", es: "Austria", ko: "오스트리아", zh: "奥地利", hi: "Austria" },
  "348": { en: "Hungary", fr: "Hongrie", ja: "ハンガリー", es: "Hungría", ko: "헝가리", zh: "匈牙利", hi: "Hungary" },
  "498": { en: "Moldova", fr: "Moldavie", ja: "モルドバ共和国", es: "Moldavia", ko: "몰도바", zh: "摩尔多瓦", hi: "Moldova" },
  "642": { en: "Romania", fr: "Roumanie", ja: "ルーマニア", es: "Rumania", ko: "루마니아", zh: "罗马尼亚", hi: "Romania" },
  "440": { en: "Lithuania", fr: "Lituanie", ja: "リトアニア", es: "Lituania", ko: "리투아니아", zh: "立陶宛", hi: "Lithuania" },
  "428": { en: "Latvia", fr: "Lettonie", ja: "ラトビア", es: "Letonia", ko: "라트비아", zh: "拉脱维亚", hi: "Latvia" },
  "233": { en: "Estonia", fr: "Estonie", ja: "エストニア", es: "Estonia", ko: "에스토니아", zh: "爱沙尼亚", hi: "Estonia" },
  "276": { en: "Germany", fr: "Allemagne", ja: "ドイツ", es: "Alemania", ko: "독일", zh: "德国", hi: "जर्मनी" },
  "100": { en: "Bulgaria", fr: "Bulgarie", ja: "ブルガリア", es: "Bulgaria", ko: "불가리아", zh: "保加利亚", hi: "Bulgaria" },
  "300": { en: "Greece", fr: "Grèce", ja: "ギリシャ", es: "Grecia", ko: "그리스", zh: "希腊", hi: "Greece" },
  "792": { en: "Turkey", fr: "Turquie", ja: "トルコ", es: "Turquía", ko: "터키", zh: "土耳其", hi: "Turkey" },
  "008": { en: "Albania", fr: "Albanie", ja: "アルバニア", es: "Albania", ko: "알바니아", zh: "阿尔巴尼亚", hi: "Albania" },
  "191": { en: "Croatia", fr: "Croatie", ja: "クロアチア", es: "Croacia", ko: "크로아티아", zh: "克罗地亚", hi: "Croatia" },
  "756": { en: "Switzerland", fr: "Suisse", ja: "スイス", es: "Suiza", ko: "스위스", zh: "瑞士", hi: "Switzerland" },
  "442": { en: "Luxembourg", fr: "Luxembourg", ja: "ルクセンブルク", es: "Luxemburgo", ko: "룩셈부르크", zh: "卢森堡", hi: "Luxembourg" },
  "056": { en: "Belgium", fr: "Belgique", ja: "ベルギー", es: "Bélgica", ko: "벨기에", zh: "比利时", hi: "Belgium" },
  "528": { en: "Netherlands", fr: "Pays-Bas", ja: "オランダ", es: "Países Bajos", ko: "네덜란드", zh: "荷兰", hi: "Netherlands" },
  "620": { en: "Portugal", fr: "Portugal", ja: "ポルトガル", es: "Portugal", ko: "포르투갈", zh: "葡萄牙", hi: "Portugal" },
  "724": { en: "Spain", fr: "Espagne", ja: "スペイン", es: "España", ko: "스페인", zh: "西班牙", hi: "स्पेन" },
  "372": { en: "Ireland", fr: "Irlande", ja: "アイルランド", es: "Irlanda", ko: "아일랜드", zh: "爱尔兰", hi: "Ireland" },
  "540": { en: "New Caledonia", fr: "Nouvelle-Calédonie", ja: "ニューカレドニア", es: "Nueva Caledonia", ko: "누벨칼레도니", zh: "新喀里多尼亚", hi: "New Caledonia" },
  "090": { en: "Solomon Islands", fr: "Îles Salomon", ja: "ソロモン諸島", es: "Islas Salomón", ko: "솔로몬 제도", zh: "所罗门群岛", hi: "Solomon Is." },
  "554": { en: "New Zealand", fr: "Nouvelle-Zélande", ja: "ニュージーランド", es: "Nueva Zelanda", ko: "뉴질랜드", zh: "新西兰", hi: "New Zealand" },
  "036": { en: "Australia", fr: "Australie", ja: "オーストラリア", es: "Australia", ko: "호주", zh: "澳大利亚", hi: "Australia" },
    "144": { en: "Sri Lanka", fr: "Sri Lanka", ja: "スリランカ", es: "Sri Lanka", ko: "스리랑카", zh: "斯里兰卡", hi: "Sri Lanka" },
  "156": { en: "China", fr: "Chine", ja: "中国", es: "China", ko: "중국", zh: "中国", hi: "चीन" },
  "410": { en: "South Korea", fr: "Corée du Sud", ja: "韓国", es: "Corea del Sur", ko: "한국", zh: "韩国", hi: "दक्षिण कोरिया" },
  "036": { en: "Australia", fr: "Australie", ja: "オーストラリア", es: "Australia", ko: "호주", zh: "澳大利亚", hi: "ऑस्ट्रेलिया" },
  "356": { en: "India", fr: "Inde", ja: "インド", es: "India", ko: "인도", zh: "भारत", hi: "भारत" },
  "826": { en: "United Kingdom", fr: "Royaume-Uni", ja: "イギリス", es: "Reino Unido", ko: "영국", zh: "英国", hi: "यूनाइटेड किंगडम" }
};

// ── UI Translations ─────────────────────────────────────────
const UI_TRANSLATIONS = {
  en: {
    subtitle: "How much of Japan have you explored?",
    subtitleWorld: "How much of the World have you explored?",
    subtitleFrance: "How much of France have you explored?",
    subtitleSpain: "How much of Spain have you explored?",
    subtitleItaly: "How much of Italy have you explored?",
    subtitleUS: "How much of USA have you explored?",
    subtitleChina: "How much of China have you explored?",
    subtitleKorea: "How much of South Korea have you explored?",
    subtitleAustralia: "How much of Australia have you explored?",
    subtitleIndia: "How much of India have you explored?",
    subtitleUK: "How much of United Kingdom have you explored?",
    subtitleMexico: "How much of Mexico have you explored?",
    subtitleTurkey: "How much of Turkey have you explored?",
    exportBtn: '<i class="fa fa-download"></i> Export',
    legend: ["Lived", "Stayed", "Visited", "Alighted", "Passed", "Never"],
    insetLabel: "INSET",
    explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} regions</strong></span></div>`,
    exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} countries</strong></span></div>`,
    exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} departments</strong></span></div>`,
    exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
    exploredItaly: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
    exploredUS: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} states</strong></span></div>`,
    exploredChina: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
    exploredKorea: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
    exploredAustralia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} states</strong></span></div>`,
    exploredIndia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} states</strong></span></div>`,
    exploredUK: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} regions</strong></span></div>`,
    exploredMexico: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} states</strong></span></div>`,
    exploredTurkey: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">has explored </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
    modal: {
      title: "Export Your Map!",
      desc: "This application is <strong>100% free</strong>!<br>A simple follow on Instagram helps me<br>tremendously to continue this adventure.<br>🏍️🇯🇵 <strong>Thank you for your support!</strong>",
      follow: `<i class="fa-brands fa-instagram"></i> Follow @french_rider_in_japan`,
      dlAnyway: "Download anyway",
      dlShared: "I followed! Download in HD 🎉"
    },
    levelModal: {
      subtitle: "What is your exploration level?",
      l5: { main: "Lived there", sub: "I lived there (+5 pts)" },
      l4: { main: "Stayed there", sub: "Stayed ≥ 1 night (+4 pts)" },
      l3: { main: "Visited there", sub: "Day trip (+3 pts)" },
      l2: { main: "Alighted there", sub: "Stopover / Transit (+2 pts)" },
      l1: { main: "Passed there", sub: "Just passing through (+1 pt)" },
      l0: { main: "Never been", sub: "Never been (0 pt)" }
    },
    countryModal: {
      title: "Choose a country",
      world: "🌍 World", fr: "🇫🇷 France", it: "🇮🇹 Italy", es: "🇪🇸 Spain", jp: "🇯🇵 Japan", us: "🇺🇸 USA",
      cn: "🇨🇳 China", kr: "🇰🇷 South Korea", au: "🇦🇺 Australia", in: "🇮🇳 India", uk: "🇬🇧 United Kingdom", mx: "🇲🇽 Mexico", tr: "🇹🇷 Turkey",
      avail: "Available", soon: "Coming soon"
    },
    langModalTitle: "Choose language",
    tapName: "👉 Tap your name",
    bgWatermark: "JAPAN",
    bgWatermarkWorld: "WORLD",
    bgWatermarkFrance: "FRANCE",
    bgWatermarkSpain: "SPAIN",
    bgWatermarkItaly: "ITALY",
    bgWatermarkUS: "USA",
    bgWatermarkChina: "CHINA",
    bgWatermarkKorea: "KOREA",
    bgWatermarkAustralia: "AUSTRALIA",
    bgWatermarkIndia: "INDIA",
    bgWatermarkUK: "UK",
    bgWatermarkMexico: "MEXICO",
    bgWatermarkTurkey: "TURKEY",
    tutorial: {
      title: "Welcome! 🌍",
      subtitle: "How to use the app",
      step1Title: "Zoom & Pan",
      step1Desc: "Pinch with 2 fingers or use mouse scroll to navigate the map.",
      step2Title: "Select Status",
      step2Desc: "Click on a region or department to record your exploration level.",
      step3Title: "Export & Share",
      step3Desc: "Click the export button to download a beautiful map ready for social networks!",
      closeBtn: "Let's go!"
    }
  },
  ja: {
    subtitle: "日本のどこを旅しましたか？",
    subtitleWorld: "世界のどこを旅しましたか？",
    subtitleFrance: "フランスのどこを旅しましたか？",
    subtitleSpain: "スペインのどこを旅しましたか？",
    subtitleItaly: "イタリアのどこを旅しましたか？",
    subtitleUS: "アメリカのどこを旅しましたか？",
    subtitleChina: "中国のどこを旅しましたか？",
    subtitleKorea: "韓国 of どこを旅しましたか？",
    subtitleAustralia: "オーストラリアのどこを旅しましたか？",
    subtitleIndia: "インド of どこを旅しましたか？",
    subtitleUK: "イギリスのどこを旅しましたか？",
    subtitleMexico: "メキシコをどれだけ探索しましたか？",
    subtitleTurkey: "トルコをどれだけ探索しましたか？",
    exportBtn: '<i class="fa fa-download"></i> 書き出し',
    legend: ["住んだ", "泊まった", "訪れた", "立ち寄り", "通過", "未踏"],
    insetLabel: "拡大図",
    explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 地域</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} ヶ国</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredItaly: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredUS: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 州</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredChina: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 省</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredKorea: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 道</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredAustralia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 州</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredIndia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 州</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredUK: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 地域</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredMexico: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 州</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    exploredTurkey: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">は </span><strong style="color:#ffffff;">${count} 県</strong><span style="opacity:0.7; font-weight:400;">を探索しました</span></span></div>`,
    modal: {
      title: "マップを書き出す！",
      desc: "このアプリは<strong>100%無料</strong>です！<br>Instagramをフォローして応援していただけると<br>旅の励みになります。よろしくお願いします！🏍️🇯🇵",
      follow: `<i class="fa-brands fa-instagram"></i> @french_rider_in_japan をフォロー`,
      dlAnyway: "そのままダウンロードする",
      dlShared: "フォローしました！HD版を保存 🎉"
    },
    levelModal: {
      subtitle: "訪問レベルを選択してください",
      l5: { main: "住んだ", sub: "住んだことがある (+5 pts)" },
      l4: { main: "泊まった", sub: "1泊以上した (+4 pts)" },
      l3: { main: "訪れた", sub: "日帰り旅行 (+3 pts)" },
      l2: { main: "立ち寄り", sub: "乗り換え / 立ち寄り (+2 pts)" },
      l1: { main: "通過", sub: "通過しただけ (+1 pt)" },
      l0: { main: "未踏", sub: "行ったことがない (0 pt)" }
    },
    countryModal: {
      title: "国を選択",
      world: "🌍 世界", fr: "🇫🇷 フランス", it: "🇮🇹 イタリア", es: "🇪🇸 スペイン", jp: "🇯🇵 日本", us: "🇺🇸 アメリカ",
      cn: "🇨🇳 中国", kr: "🇰🇷 韓国", au: "🇦🇺 オーストラリア", in: "🇮🇳 インド", uk: "🇬🇧 イギリス", mx: "🇲🇽 メキシコ", tr: "🇹🇷 トルコ",
      avail: "利用可能", soon: "近日公開"
    },
    langModalTitle: "言語を選択",
    tapName: "👉 名前を入力",
    bgWatermark: "日本",
    bgWatermarkWorld: "世界",
    bgWatermarkFrance: "フランス",
    bgWatermarkSpain: "スペイン",
    bgWatermarkItaly: "イタリア",
    bgWatermarkUS: "USA",
    bgWatermarkChina: "中国",
    bgWatermarkKorea: "韓国",
    bgWatermarkAustralia: "オーストラリア",
    bgWatermarkIndia: "インド",
    bgWatermarkUK: "英国",
    bgWatermarkMexico: "メキシコ",
    bgWatermarkTurkey: "トルコ",
    tutorial: {
      title: "ようこそ！ 🌍",
      subtitle: "アプリの使い方",
      step1Title: "ズーム＆移動",
      step1Desc: "2本の指でピンチするか、マウスホイールを使用してマップをナビゲートします。",
      step2Title: "訪問レベルの選択",
      step2Desc: "地域や県をクリックして、訪問レベルを記録します。",
      step3Title: "書き出し＆シェア",
      step3Desc: "書き出しボタンをクリックして、SNS to 最適な美しいマップをダウンロードしましょう！",
      closeBtn: "スタート！"
    }
  },
  fr: {
    subtitle: "À quel point as-tu exploré <span style='display: inline-block;'>le Japon ?</span>",
    subtitleWorld: "À quel point as-tu exploré <span style='display: inline-block;'>le Monde ?</span>",
    subtitleFrance: "Combien de départements <span style='display: inline-block;'>de France as-tu exploré ?</span>",
    subtitleSpain: "Combien de provinces <span style='display: inline-block;'>d'Espagne as-tu exploré ?</span>",
    subtitleItaly: "À quel point as-tu exploré <span style='display: inline-block;'>l'Italie ?</span>",
    subtitleUS: "À quel point as-tu exploré <span style='display: inline-block;'>les USA ?</span>",
    subtitleChina: "Combien de provinces de<br><span style='display: inline-block;'>la Chine as-tu exploré ?</span>",
    subtitleKorea: "À quel point as-tu exploré<br><span style='display: inline-block;'>la Corée du Sud ?</span>",
    subtitleAustralia: "À quel point as-tu exploré<br><span style='display: inline-block;'>l'Australie ?</span>",
    subtitleIndia: "À quel point as-tu exploré<br><span style='display: inline-block;'>l'Inde ?</span>",
    subtitleUK: "À quel point as-tu exploré<br><span style='display: inline-block;'>le Royaume-Uni ?</span>",
    exportBtn: '<i class="fa fa-download"></i> Exporter',
    legend: ["Habité", "Séjourné", "Visité", "Escale", "Passé", "Jamais"],
    insetLabel: "ENCART",
    explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} régions</strong></span></div>`,
    exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} pays</strong></span></div>`,
    exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} départements</strong></span></div>`,
    exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
    exploredItaly: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
    exploredUS: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} états</strong></span></div>`,
    exploredChina: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
    exploredKorea: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
    exploredAustralia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} états</strong></span></div>`,
    exploredIndia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} états</strong></span></div>`,
    exploredUK: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} régions</strong></span></div>`,
    exploredMexico: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} États</strong></span></div>`,
    exploredTurkey: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">a exploré </span><strong style="color:#ffffff;">${count} provinces</strong></span></div>`,
    modal: {
      title: "Exporter ta carte !",
      desc: "Cette application est <strong>100% gratuite</strong> !<br>Un simple abonnement sur Instagram m'aide<br>énormément à continuer cette aventure.<br>🏍️🇯🇵 <strong>Merci pour ton soutien !</strong>",
      follow: `<i class="fa-brands fa-instagram"></i> Suivre @french_rider_in_japan`,
      dlAnyway: "Télécharger quand même",
      dlShared: "Je me suis abonné ! HD 🎉"
    },
    levelModal: {
      subtitle: "Quel est votre niveau de visite ?",
      l5: { main: "Habité", sub: "J'y ai habité (+5 pts)" },
      l4: { main: "Séjourné", sub: "Séjour ≥ 1 nuit (+4 pts)" },
      l3: { main: "Visité", sub: "Visite de journée (+3 pts)" },
      l2: { main: "Escale", sub: "Arrêt / Escale (+2 pts)" },
      l1: { main: "Passé", sub: "Simple passage (+1 pt)" },
      l0: { main: "Jamais", sub: "Jamais allé (0 pt)" }
    },
    countryModal: {
      title: "Choisis ton pays",
      world: "🌍 Monde", fr: "🇫🇷 France", it: "🇮🇹 Italie", es: "🇪🇸 Espagne", jp: "🇯🇵 Japon", us: "🇺🇸 USA",
      cn: "🇨🇳 Chine", kr: "🇰🇷 Corée du Sud", au: "🇦🇺 Australie", in: "🇮🇳 Inde", uk: "🇬🇧 Royaume-Uni", mx: "🇲🇽 Mexique", tr: "🇹🇷 Turquie",
      avail: "Disponible", soon: "Bientôt"
    },
    langModalTitle: "Choisis ta langue",
    tapName: "👉 Entre ton nom",
    bgWatermark: "JAPON",
    bgWatermarkWorld: "MONDE",
    bgWatermarkFrance: "FRANCE",
    bgWatermarkSpain: "ESPAGNE",
    bgWatermarkItaly: "ITALIE",
    bgWatermarkUS: "USA",
    bgWatermarkChina: "CHINE",
    bgWatermarkKorea: "CORÉE",
    bgWatermarkAustralia: "AUSTRALIE",
    bgWatermarkIndia: "INDE",
    bgWatermarkUK: "ROYAUME-UNI",
    bgWatermarkMexico: "MEXIQUE",
    bgWatermarkTurkey: "TURQUIE",
    tutorial: {
      title: "Bienvenue ! 🌍",
      subtitle: "Comment utiliser l'application",
      step1Title: "Zoomer & Déplacer",
      step1Desc: "Pincez avec 2 doigts ou utilisez la molette de la souris pour naviguer sur la carte.",
      step2Title: "Sélectionner un Statut",
      step2Desc: "Cliquez sur une région ou un département pour enregistrer votre niveau d'exploration.",
      step3Title: "Exporter & Partager",
      step3Desc: "Cliquez sur le bouton d'export pour télécharger une superbe carte prête pour vos réseaux sociaux !",
      closeBtn: "C'est parti !"
    }
  },
  es: {
    subtitle: "¿Cuánto de Japón has explorado?",
    subtitleWorld: "¿Cuánto del Mundo has explorado?",
    subtitleFrance: "¿Cuánto de Francia has explorado?",
    subtitleSpain: "¿Cuánto de España has explorado?",
    subtitleItaly: "¿Cuánto de Italia has explorado?",
    subtitleUS: "¿Cuánto de USA has explorado?",
    subtitleChina: "¿Cuánto de China has explorado?",
    subtitleKorea: "¿Cuánto de Corea del Sur has explorado?",
    subtitleAustralia: "¿Cuánto de Australia has explorado?",
    subtitleIndia: "¿Cuánto de India has explorado?",
    subtitleUK: "¿Cuánto del Reino Unido has explorado?",
    exportBtn: '<i class="fa fa-download"></i> Exportar',
    legend: ["Vivido", "Alojado", "Visitado", "Escala", "Pasado", "Nunca"],
    insetLabel: "RECUADRO",
    explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} regiones</strong></span></div>`,
    exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} países</strong></span></div>`,
    exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} departamentos</strong></span></div>`,
    exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} provincias</strong></span></div>`,
    exploredItaly: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} provincias</strong></span></div>`,
    exploredUS: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} estados</strong></span></div>`,
    exploredChina: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} provincias</strong></span></div>`,
    exploredKorea: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} provincias</strong></span></div>`,
    exploredAustralia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} estados</strong></span></div>`,
    exploredIndia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} estados</strong></span></div>`,
    exploredUK: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} regiones</strong></span></div>`,
    exploredMexico: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} estados</strong></span></div>`,
    exploredTurkey: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">ha explorado </span><strong style="color:#ffffff;">${count} provincias</strong></span></div>`,
    modal: {
      title: "¡Exporta tu mapa!",
      desc: "Esta aplicación es <strong>100% gratuita</strong>.<br>Un simple seguimiento en Instagram me ayuda<br>muchísimo a continuar esta aventura.<br>🏍️🇯🇵 <strong>¡Gracias por tu apoyo!</strong>",
      follow: `<i class="fa-brands fa-instagram"></i> Seguir @french_rider_in_japan`,
      dlAnyway: "Descargar de todos modos",
      dlShared: "¡Ya te sigo! Descargar en HD 🎉"
    },
    levelModal: {
      subtitle: "¿Cuál es tu nivel de exploración?",
      l5: { main: "Vivido", sub: "He vivido ahí (+5 pts)" },
      l4: { main: "Alojado", sub: "Estancia ≥ 1 noche (+4 pts)" },
      l3: { main: "Visitado", sub: "Visita de un día (+3 pts)" },
      l2: { main: "Escala", sub: "Parada / Escala (+2 pts)" },
      l1: { main: "Pasado", sub: "Solo de paso (+1 pt)" },
      l0: { main: "Nunca", sub: "Nunca he ido (0 pt)" }
    },
    countryModal: {
      title: "Elige un país",
      world: "🌍 Mundo", fr: "🇫🇷 Francia", it: "🇮🇹 Italia", es: "🇪🇸 España", jp: "🇯🇵 Japón", us: "🇺🇸 EE.UU.",
      cn: "🇨🇳 China", kr: "🇰🇷 Corea del Sur", au: "🇦🇺 Australia", in: "🇮🇳 India", uk: "🇬🇧 Reino Unido", mx: "🇲🇽 México", tr: "🇹🇷 Turquía",
      avail: "Disponible", soon: "Próximamente"
    },
    langModalTitle: "Elige tu idioma",
    tapName: "👉 Escribe tu nombre",
    bgWatermark: "JAPÓN",
    bgWatermarkWorld: "MUNDO",
    bgWatermarkFrance: "FRANCIA",
    bgWatermarkSpain: "ESPAÑA",
    bgWatermarkItaly: "ITALIA",
    bgWatermarkUS: "USA",
    bgWatermarkChina: "CHINA",
    bgWatermarkKorea: "COREA",
    bgWatermarkAustralia: "AUSTRALIA",
    bgWatermarkIndia: "INDIA",
    bgWatermarkUK: "REINO UNIDO",
    tutorial: {
      title: "¡Bienvenido! 🌍",
      subtitle: "Cómo usar la aplicación",
      step1Title: "Zoom y Mover",
      step1Desc: "Pellizca con 2 dedos o usa la rueda del ratón para navegar por el mapa.",
      step2Title: "Seleccionar Nivel",
      step2Desc: "Pulsa una región o departamento para registrar tu nivel de exploración.",
      step3Title: "Exportar y Compartir",
      step3Desc: "Pulsa el botón de exportar para descargar un mapa hermoso listo para tus redes sociales.",
      closeBtn: "¡Vamos!"
    }
  },
  ko: {
    subtitle: "일본을 얼마나 탐험했나요?",
    subtitleWorld: "세계의 얼마나 탐험했나요?",
    subtitleFrance: "프랑스의 어디를 여행하셨나요?",
    subtitleSpain: "스페인의 어디를 여행하셨나요?",
    subtitleItaly: "이탈리아의 어디를 여행하셨나요?",
    subtitleUS: "미국의 어디를 여행하셨나요?",
    subtitleChina: "중국의 어디를 여행하셨나요?",
    subtitleKorea: "한국의 어디를 여행하셨나요?",
    subtitleAustralia: "호주의 어디를 여행하셨나요?",
    subtitleIndia: "인도의 어디를 여행하셨나요?",
    subtitleUK: "영국의 어디를 여행하셨나요?",
    exportBtn: '<i class="fa fa-download"></i> 내보내기',
    legend: ["거주", "숙박", "방문", "경유", "통과", "미방문"],
    insetLabel: "확대도",
    explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 지역</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개국</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 부서</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 주</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredItaly: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 주</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredUS: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 주</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredChina: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 성</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredKorea: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 도</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredAustralia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 주</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredIndia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 주</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredUK: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 지역</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredMexico: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 주</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    exploredTurkey: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count}개 성</strong><span style="opacity:0.7; font-weight:400;"> 탐험</span></span></div>`,
    modal: {
      title: "지도 내보내기!",
      desc: "이 앱은 <strong>100% 무료</strong>입니다!<br>인스타그램 팔로우 하나로<br>이 모험을 이어갈 수 있습니다.<br>🏍️🇯🇵 <strong>응원 감사합니다!</strong>",
      follow: `<i class="fa-brands fa-instagram"></i> @french_rider_in_japan 팔로우`,
      dlAnyway: "그냥 다운로드",
      dlShared: "팔로우했어요! HD 다운로드 🎉"
    },
    levelModal: {
      subtitle: "탐험 레벨을 선택하세요",
      l5: { main: "거주", sub: "거주한 적 있음 (+5 pts)" },
      l4: { main: "숙박", sub: "1박 이상 숙박 (+4 pts)" },
      l3: { main: "방문", sub: "당일 방문 (+3 pts)" },
      l2: { main: "경유", sub: "경유 / 환승 (+2 pts)" },
      l1: { main: "통과", sub: "지나간 적 있음 (+1 pt)" },
      l0: { main: "미방문", sub: "가본 적 없음 (0 pt)" }
    },
    countryModal: {
      title: "국가 선택",
      world: "🌍 세계", fr: "🇫🇷 프랑스", it: "🇮🇹 이탈리아", es: "🇪🇸 스페인", jp: "🇯🇵 일본", us: "🇺🇸 미국",
      cn: "🇨🇳 중국", kr: "🇰🇷 한국", au: "🇦🇺 호주", in: "🇮🇳 인도", uk: "🇬🇧 영국",
      avail: "사용 가능", soon: "곧 출시"
    },
    langModalTitle: "언어 선택",
    tapName: "👉 이름을 입력하세요",
    bgWatermark: "일본",
    bgWatermarkWorld: "세계",
    bgWatermarkFrance: "프랑스",
    bgWatermarkSpain: "스페인",
    bgWatermarkItaly: "이탈리아",
    bgWatermarkUS: "미국",
    bgWatermarkChina: "중국",
    bgWatermarkKorea: "한국",
    bgWatermarkAustralia: "호주",
    bgWatermarkIndia: "인도",
    bgWatermarkUK: "영국",
    bgWatermarkMexico: "멕시코",
    bgWatermarkTurkey: "터키",
    tutorial: {
      title: "환영합니다! 🌍",
      subtitle: "앱 사용 방법",
      step1Title: "확대 및 이동",
      step1Desc: "두 손가락으로 핀치하거나 마우스 휠을 사용하여 지도를 탐색하세요.",
      step2Title: "탐험 레벨 선택",
      step2Desc: "지역이나 도를 클릭하여 탐험 레벨을 기록하세요.",
      step3Title: "내보내기 및 공유",
      step3Desc: "내보내기 버튼을 클릭하여 SNS에 공유할 멋진 지도를 다운로드하세요!",
      closeBtn: "시작!"
    }
  },
  zh: {
    subtitle: "你探索了多少日本？",
    subtitleWorld: "你探索了多少世界？",
    subtitleFrance: "你探索了多少法国？",
    subtitleSpain: "你探索了多少西班牙？",
    subtitleItaly: "你探索了多少意大利？",
    subtitleUS: "你探索了多少美国？",
    subtitleChina: "你探索了多少中国？",
    subtitleKorea: "你探索了多少韩国？",
    subtitleAustralia: "你探索了多少澳大利亚？",
    subtitleIndia: "你探索了多少印度？",
    subtitleUK: "你探索了多少英国？",
    exportBtn: '<i class="fa fa-download"></i> 导出',
    legend: ["居住", "住宿", "游览", "经停", "路过", "未去"],
    insetLabel: "放大图",
    explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个地区</strong></span></div>`,
    exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个国家</strong></span></div>`,
    exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个省份</strong></span></div>`,
    exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个省份</strong></span></div>`,
    exploredItaly: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个省份</strong></span></div>`,
    exploredUS: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个州</strong></span></div>`,
    exploredChina: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个省份</strong></span></div>`,
    exploredKorea: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个道</strong></span></div>`,
    exploredAustralia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个州</strong></span></div>`,
    exploredIndia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个州</strong></span></div>`,
    exploredUK: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个地区</strong></span></div>`,
    exploredMexico: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个州</strong></span></div>`,
    exploredTurkey: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><span style="opacity:0.7; font-weight:400;">已探索 </span><strong style="color:#ffffff;">${count} 个省</strong></span></div>`,
    modal: {
      title: "导出你的地图！",
      desc: "这个应用是<strong>100%免费</strong>的！<br>在Instagram上关注我<br>将极大地帮助我继续这段冒险。<br>🏍️🇯🇵 <strong>感谢你的支持！</strong>",
      follow: `<i class="fa-brands fa-instagram"></i> 关注 @french_rider_in_japan`,
      dlAnyway: "直接下载",
      dlShared: "已关注！下载高清版 🎉"
    },
    levelModal: {
      subtitle: "选择你的探索等级",
      l5: { main: "居住", sub: "曾经居住 (+5 pts)" },
      l4: { main: "住宿", sub: "住宿 ≥ 1 晚 (+4 pts)" },
      l3: { main: "游览", sub: "一日游 (+3 pts)" },
      l2: { main: "经停", sub: "中转 / 经停 (+2 pts)" },
      l1: { main: "路过", sub: "路过 (+1 pt)" },
      l0: { main: "未去", sub: "从未去过 (0 pt)" }
    },
    countryModal: {
      title: "选择国家",
      world: "🌍 世界", fr: "🇫🇷 法国", it: "🇮🇹 意大利", es: "🇪🇸 西班牙", jp: "🇯🇵 日本", us: "🇺🇸 美国",
      cn: "🇨🇳 中国", kr: "🇰🇷 韩国", au: "🇦🇺 澳大利亚", in: "🇮🇳 印度", uk: "🇬🇧 英国", mx: "🇲🇽 墨西哥", tr: "🇹🇷 土耳其",
      avail: "可用", soon: "即将推出"
    },
    langModalTitle: "选择语言",
    tapName: "👉 输入你的名字",
    bgWatermark: "日本",
    bgWatermarkWorld: "世界",
    bgWatermarkFrance: "法国",
    bgWatermarkSpain: "西班牙",
    bgWatermarkItaly: "意大利",
    bgWatermarkUS: "USA",
    bgWatermarkChina: "中国",
    bgWatermarkKorea: "韩国",
    bgWatermarkAustralia: "澳大利亚",
    bgWatermarkIndia: "印度",
    bgWatermarkUK: "英国",
    bgWatermarkMexico: "メキシコ",
    bgWatermarkTurkey: "トルコ",
    tutorial: {
      title: "欢迎！ 🌍",
      subtitle: "如何使用此应用",
      step1Title: "缩放与移动",
      step1Desc: "用两根手指捏合或使用鼠标滚轮在地图上导航。",
      step2Title: "选择探索等级",
      step2Desc: "点击地区或省份以记录您的探索等级。",
      step3Title: "导出与分享",
      step3Desc: "点击导出按钮，下载一张适合社交媒体的精美地图！",
      closeBtn: "出发！"
    }
  },
  hi: {
    subtitle: "आपने जापान का कितना हिस्सा खोजा है?",
    subtitleWorld: "आपने दुनिया का कितना हिस्सा खोजा है?",
    subtitleFrance: "आपने फ्रांस का कितना हिस्सा खोजा है?",
    subtitleSpain: "आपने स्पेन का कितना हिस्सा खोजा है?",
    subtitleItaly: "आपने इटली का कितना हिस्सा खोजा है?",
    subtitleUS: "आपने अमेरिका का कितना हिस्सा खोजा है?",
    subtitleChina: "आपने चीन का कितना हिस्सा खोजा है?",
    subtitleKorea: "आपने दक्षिण कोरिया का कितना हिस्सा खोजा है?",
    subtitleAustralia: "आपने ऑस्ट्रेलिया का कितना हिस्सा खोजा है?",
    subtitleIndia: "आपने भारत का कितना हिस्सा खोजा है?",
    subtitleUK: "आपने यूनाइटेड किंगडम का कितना हिस्सा खोजा है?",
    subtitleMexico: "आपने मेक्सिको का कितना हिस्सा खोजा है?",
    subtitleTurkey: "आपने तुर्की का कितना हिस्सा खोजा है?",
    exportBtn: '<i class="fa fa-download"></i> निर्यात',
    legend: ["रहे", "ठहरे", "देखा", "रुके", "गुज़रे", "कभी नहीं"],
    insetLabel: "इनसेट",
    explored: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} क्षेत्र</strong><span style="opacity:0.7; font-weight:400;"> खोजे</span></span></div>`,
    exploredWorld: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} देश</strong><span style="opacity:0.7; font-weight:400;"> खोजे</span></span></div>`,
    exploredFrance: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} विभागों</strong><span style="opacity:0.7; font-weight:400;"> का दौरा किया है</span></span></div>`,
    exploredSpain: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} प्रांतों</strong><span style="opacity:0.7; font-weight:400;"> का दौरा किया है</span></span></div>`,
    exploredItaly: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} प्रांतों</strong><span style="opacity:0.7; font-weight:400;"> का दौरा किया है</span></span></div>`,
    exploredUS: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} राज्यों</strong><span style="opacity:0.7; font-weight:400;"> का दौरा किया है</span></span></div>`,
    exploredChina: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} प्रांतों</strong><span style="opacity:0.7; font-weight:400;"> का दौरा किया है</span></span></div>`,
    exploredKorea: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} प्रांतों</strong><span style="opacity:0.7; font-weight:400;"> का दौरा किया है</span></span></div>`,
    exploredAustralia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} राज्यों</strong><span style="opacity:0.7; font-weight:400;"> का दौरा किया है</span></span></div>`,
    exploredIndia: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} राज्यों</strong><span style="opacity:0.7; font-weight:400;"> का दौरा किया है</span></span></div>`,
    exploredUK: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} क्षेत्रों</strong><span style="opacity:0.7; font-weight:400;"> की यात्रा की है</span></span></div>`,
    exploredMexico: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} राज्यों</strong><span style="opacity:0.7; font-weight:400;"> की यात्रा की है</span></span></div>`,
    exploredTurkey: (nameHtml, count) => `<div style="display:flex; flex-direction:column; align-items:center; line-height:1.2;"><span>${nameHtml}</span><span style="font-size:0.75em; text-transform:none; margin-top:3px; letter-spacing:0.2px;"><strong style="color:#ffffff;">${count} प्रांतों</strong><span style="opacity:0.7; font-weight:400;"> की यात्रा की है</span></span></div>`,
    modal: {
      title: "अपना मानचित्र निर्यात करें!",
      desc: "यह ऐप <strong>100% मुफ़्त</strong> है!<br>Instagram पर फ़ॉलो करना<br>इस यात्रा को जारी रखने में बहुत मदद करता है।<br>🏍️🇯🇵 <strong>आपके समर्थन का धन्यवाद!</strong>",
      follow: `<i class="fa-brands fa-instagram"></i> @french_rider_in_japan फ़ॉलो करें`,
      dlAnyway: "वैसे भी डाउनलोड करें",
      dlShared: "मैंने फ़ॉलो किया! HD डाउनलोड 🎉"
    },
    levelModal: {
      subtitle: "अपना अन्वेषण स्तर चुनें",
      l5: { main: "रहे", sub: "वहाँ रहा (+5 pts)" },
      l4: { main: "ठहरे", sub: "1 रात ≥ ठहरा (+4 pts)" },
      l3: { main: "देखा", sub: "दिन की यात्रा (+3 pts)" },
      l2: { main: "रुके", sub: "पड़ाव / रुकावट (+2 pts)" },
      l1: { main: "गुज़रे", sub: "बस गुज़रा (+1 pt)" },
      l0: { main: "कभी नहीं", sub: "कभी नहीं गया (0 pt)" }
    },
    countryModal: {
      title: "देश चुनें",
      world: "🌍 विश्व", fr: "🇫🇷 फ़्रांस", it: "🇮🇹 इटली", es: "🇪🇸 स्पेन", jp: "🇯🇵 जापान", us: "🇺🇸 अमेरिका",
      cn: "🇨🇳 चीन", kr: "🇰🇷 दक्षिण कोरिया", au: "🇦🇺 ऑस्ट्रेलिया", in: "🇮🇳 भारत", uk: "🇬🇧 यूनाइटेड किंगडम", mx: "🇲🇽 मेक्सिको", tr: "🇹🇷 तुर्की",
      avail: "उपलब्ध", soon: "जल्द आ रहा है"
    },
    langModalTitle: "भाषा चुनें",
    tapName: "👉 अपना नाम लिखें",
    bgWatermark: "जापान",
    bgWatermarkWorld: "दुनिया",
    bgWatermarkFrance: "फ्रांस",
    bgWatermarkSpain: "स्पेन",
    bgWatermarkItaly: "इटली",
    bgWatermarkUS: "USA",
    bgWatermarkChina: "चीन",
    bgWatermarkKorea: "कोरिया",
    bgWatermarkAustralia: "ऑस्ट्रेलिया",
    bgWatermarkIndia: "भारत",
    bgWatermarkUK: "UK",
    bgWatermarkMexico: "MEXICO",
    bgWatermarkTurkey: "TURKEY",
    tutorial: {
      title: "स्वागत है! 🌍",
      subtitle: "एप कैसे उपयोग करें",
      step1Title: "ज़ूम और नेविगेट",
      step1Desc: "मानचित्र पर नेविगेट करने के लिए 2 उंगलियों से पिंच करें या माउस स्क्रॉल का उपयोग करें।",
      step2Title: "स्तर चुनें",
      step2Desc: "अपना अन्वेषण स्तर दर्ज करने के लिए किसी क्षेत्र पर क्लिक करें।",
      step3Title: "निर्यात और साझा करें",
      step3Desc: "सोशल मीडिया के लिए तैयार एक सुंदर मानचित्र डाउनलोड करने के लिए निर्यात बटन पर क्लिक करें!",
      closeBtn: "चलिए शुरू करें!"
    }
  }
};

function updateUITranslations() {
  const lang = state.lang || "en";
  const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];
  
  // Subtitle
  const subtitle = document.getElementById("card-subtitle-phrase");
  if (subtitle) {
    if (state.currentMap === "jp") {
      subtitle.innerHTML = t.subtitle;
    } else if (state.currentMap === "fr") {
      subtitle.innerHTML = t.subtitleFrance;
    } else if (state.currentMap === "es") {
      subtitle.innerHTML = t.subtitleSpain;
    } else if (state.currentMap === "it") {
      subtitle.innerHTML = t.subtitleItaly;
    } else if (state.currentMap === "us") {
      subtitle.innerHTML = t.subtitleUS;
    } else if (state.currentMap === "cn") {
      subtitle.innerHTML = t.subtitleChina;
    } else if (state.currentMap === "kr") {
      subtitle.innerHTML = t.subtitleKorea;
    } else if (state.currentMap === "au") {
      subtitle.innerHTML = t.subtitleAustralia;
    } else if (state.currentMap === "in") {
      subtitle.innerHTML = t.subtitleIndia;
    } else if (state.currentMap === "uk") {
      subtitle.innerHTML = t.subtitleUK;
    } else {
      subtitle.innerHTML = t.subtitleWorld;
    }
  }
  
  // Flag
  const cardFlag = document.getElementById("card-flag");
  if (cardFlag) {
    if (state.currentMap === "jp") cardFlag.textContent = "🇯🇵";
    else if (state.currentMap === "fr") cardFlag.textContent = "🇫🇷";
    else if (state.currentMap === "es") cardFlag.textContent = "🇪🇸";
    else if (state.currentMap === "it") cardFlag.textContent = "🇮🇹";
    else if (state.currentMap === "us") cardFlag.textContent = "🇺🇸";
    else if (state.currentMap === "cn") cardFlag.textContent = "🇨🇳";
    else if (state.currentMap === "kr") cardFlag.textContent = "🇰🇷";
    else if (state.currentMap === "au") cardFlag.textContent = "🇦🇺";
    else if (state.currentMap === "in") cardFlag.textContent = "🇮🇳";
    else if (state.currentMap === "uk") cardFlag.textContent = "🇬🇧";
    else cardFlag.textContent = "🌍";
  }

  // Export button
  const exportBtn = document.getElementById("btn-export");
  if (exportBtn) exportBtn.innerHTML = t.exportBtn;
  
  // Inset Label
  const insetLabel = document.getElementById("inset-label");
  if (insetLabel) {
    insetLabel.textContent = t.insetLabel;
    // Show only for Japan map
    insetLabel.style.display = state.currentMap === "jp" ? "block" : "none";
  }
  
  // Legend
  const legItems = document.querySelectorAll("#card-legend .leg-item");
  if (legItems.length === 6) {
    legItems[0].innerHTML = `<span class="leg-dot" data-l="5"></span>${t.legend[0]}`;
    legItems[1].innerHTML = `<span class="leg-dot" data-l="4"></span>${t.legend[1]}`;
    legItems[2].innerHTML = `<span class="leg-dot" data-l="3"></span>${t.legend[2]}`;
    legItems[3].innerHTML = `<span class="leg-dot" data-l="2"></span>${t.legend[3]}`;
    legItems[4].innerHTML = `<span class="leg-dot" data-l="1"></span>${t.legend[4]}`;
    legItems[5].innerHTML = `<span class="leg-dot" data-l="0"></span>${t.legend[5]}`;
  }
  
  // Export Modal
  const m = t.modal;
  const title = document.getElementById("export-title");
  const desc = document.getElementById("export-desc");
  const btnFollow = document.getElementById("btn-follow");
  const btnAnyway = document.getElementById("btn-dl-anyway");
  const btnShared = document.getElementById("btn-dl-shared");
  
  if (title) title.textContent = m.title;
  if (desc) desc.innerHTML = m.desc;
  if (btnFollow) btnFollow.innerHTML = m.follow;
  if (btnAnyway) btnAnyway.textContent = m.dlAnyway;
  if (btnShared) btnShared.textContent = m.dlShared;
  
  // Level Modal
  const modSub = document.getElementById("modal-sub");
  if (modSub) modSub.textContent = t.levelModal.subtitle;
  
  [5,4,3,2,1,0].forEach(lvl => {
    const btn = document.querySelector(`#modal-opts .opt-btn[data-level="${lvl}"]`);
    if (btn) {
      const div = btn.querySelector("div");
      if (div) {
        div.innerHTML = `<strong>${t.levelModal['l'+lvl].main}</strong><small>${t.levelModal['l'+lvl].sub}</small>`;
      }
    }
  });

  // Country Modal
  const countryTitle = document.querySelector("#country-modal .modal-header h3");
  if (countryTitle) countryTitle.textContent = t.countryModal.title;
  
  document.querySelectorAll("#country-modal .opt-btn").forEach(btn => {
    const key = btn.dataset.val;
    if (key) {
      let label = t.countryModal[key] || key;
      const smallText = t.countryModal.avail;
      const div = btn.querySelector("div");
      if (div) {
        div.innerHTML = `<strong>${label}</strong><small>${smallText}</small>`;
      }
      btn.removeAttribute("disabled");
      btn.removeAttribute("style");
    }
  });

  // Country selector button text
  const btnCountry = document.getElementById("btn-country-select");
  if (btnCountry) {
    const label = t.countryModal[state.currentMap] || state.currentMap;
    btnCountry.innerHTML = `${label} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
  }
  
  // Background text watermark
  const bgWatermark = document.getElementById("bg-watermark");
  if (bgWatermark) {
    let text = "JAPAN";
    if (state.currentMap === "jp") text = t.bgWatermark || "JAPAN";
    else if (state.currentMap === "fr") text = t.bgWatermarkFrance || "FRANCE";
    else if (state.currentMap === "es") text = t.bgWatermarkSpain || "SPAIN";
    else if (state.currentMap === "it") text = t.bgWatermarkItaly || "ITALY";
    else if (state.currentMap === "us") text = t.bgWatermarkUS || "USA";
    else if (state.currentMap === "cn") text = t.bgWatermarkChina || "CHINA";
    else if (state.currentMap === "kr") text = t.bgWatermarkKorea || "KOREA";
    else if (state.currentMap === "au") text = t.bgWatermarkAustralia || "AUSTRALIA";
    else if (state.currentMap === "in") text = t.bgWatermarkIndia || "INDIA";
    else if (state.currentMap === "uk") text = t.bgWatermarkUK || "UK";
    else text = t.bgWatermarkWorld || "WORLD";
    bgWatermark.innerHTML = Array(5).fill(`<div>${text}</div>`).join("");
  }
  
  // Tutorial Modal translation
  const tuto = t.tutorial || UI_TRANSLATIONS["en"].tutorial;
  if (tuto) {
    const tutoTitle = document.getElementById("tuto-title");
    if (tutoTitle) tutoTitle.textContent = tuto.title;
    const tutoSub = document.getElementById("tuto-subtitle");
    if (tutoSub) tutoSub.textContent = tuto.subtitle || UI_TRANSLATIONS["en"].tutorial.subtitle;
    const tutoStep1T = document.getElementById("tuto-step1-title");
    if (tutoStep1T) tutoStep1T.textContent = tuto.step1Title;
    const tutoStep1D = document.getElementById("tuto-step1-desc");
    if (tutoStep1D) tutoStep1D.textContent = tuto.step1Desc;
    const tutoStep2T = document.getElementById("tuto-step2-title");
    if (tutoStep2T) tutoStep2T.textContent = tuto.step2Title;
    const tutoStep2D = document.getElementById("tuto-step2-desc");
    if (tutoStep2D) tutoStep2D.textContent = tuto.step2Desc;
    const tutoStep3T = document.getElementById("tuto-step3-title");
    if (tutoStep3T) tutoStep3T.textContent = tuto.step3Title;
    const tutoStep3D = document.getElementById("tuto-step3-desc");
    if (tutoStep3D) tutoStep3D.textContent = tuto.step3Desc;
    const tutoClose = document.getElementById("btn-tuto-close");
    if (tutoClose) tutoClose.textContent = tuto.closeBtn;
  }
  
  updateHeader();
}

// ── State Management ─────────────────────────────────────────
function loadState() {
  try {
    const s = JSON.parse(localStorage.getItem("maplevel_jp_v5") || "{}");
    if (s.username) state.username = s.username;
    if (s.lang) state.lang = s.lang;
    state.currentMap = s.currentMap || "jp";
    if (state.currentMap === "world") state.currentMap = "jp";
    state.jpLevels = s.jpLevels || s.levels || {};
    state.worldLevels = s.worldLevels || {};
    state.frLevels = s.frLevels || {};
    state.esLevels = s.esLevels || {};
    state.itLevels = s.itLevels || {};
    state.usLevels = s.usLevels || {};
    state.cnLevels = s.cnLevels || {};
    state.krLevels = s.krLevels || {};
    state.auLevels = s.auLevels || {};
    state.inLevels = s.inLevels || {};
    state.ukLevels = s.ukLevels || {};
    state.mxLevels = s.mxLevels || {};
    state.trLevels = s.trLevels || {};
    
    if (state.currentMap === "jp") state.levels = state.jpLevels;
    else if (state.currentMap === "fr") state.levels = state.frLevels;
    else if (state.currentMap === "es") state.levels = state.esLevels;
    else if (state.currentMap === "it") state.levels = state.itLevels;
    else if (state.currentMap === "us") state.levels = state.usLevels;
    else if (state.currentMap === "cn") state.levels = state.cnLevels;
    else if (state.currentMap === "kr") state.levels = state.krLevels;
    else if (state.currentMap === "au") state.levels = state.auLevels;
    else if (state.currentMap === "in") state.levels = state.inLevels;
    else if (state.currentMap === "uk") state.levels = state.ukLevels;
    else if (state.currentMap === "mx") state.levels = state.mxLevels;
    else if (state.currentMap === "tr") state.levels = state.trLevels;
    else state.levels = state.worldLevels;
  } catch(e) {}
  
  if (state.currentMap === "jp") {
    Object.keys(NAMES_EN).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "fr") {
    Object.keys(DEPARTEMENTS_FR).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "es") {
    Object.keys(PROVINCES_ES).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "it") {
    Object.keys(PROVINCES_IT).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "us") {
    Object.keys(STATES_US).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "cn") {
    Object.keys(PROVINCES_CN).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "kr") {
    Object.keys(PROVINCES_KR).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "au") {
    Object.keys(STATES_AU).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "in") {
    Object.keys(STATES_IN).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "uk") {
    Object.keys(REGIONS_UK).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "mx") {
    Object.keys(STATES_MX).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  } else if (state.currentMap === "tr") {
    Object.keys(PROVINCES_TR).forEach(c => {
      if (state.levels[c] == null) state.levels[c] = 0;
    });
  }

  // Select active country button
  document.querySelectorAll(".country-btn").forEach(btn => {
    if (btn.dataset.val === state.currentMap) {
      btn.classList.add("selected");
    } else {
      btn.classList.remove("selected");
    }
  });
  
  const val = state.lang;
  let txt = "🇬🇧 English";
  if(val === "es") txt = "🇪🇸 Español";
  if(val === "fr") txt = "🇫🇷 Français";
  if(val === "hi") txt = "🇮🇳 हिन्दी";
  if(val === "ja") txt = "🇯🇵 日本語";
  if(val === "ko") txt = "🇰🇷 한국어";
  if(val === "zh") txt = "🇨🇳 中文";
  
  const btnLang = document.getElementById("btn-lang-select");
  if (btnLang) btnLang.innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
  
  document.querySelectorAll(".lang-btn").forEach(b => {
    if(b.dataset.val === val) b.classList.add("selected");
    else b.classList.remove("selected");
  });

  updateUITranslations();
}

function saveState() {
  if (state.currentMap === "jp") {
    state.jpLevels = state.levels;
  } else if (state.currentMap === "fr") {
    state.frLevels = state.levels;
  } else if (state.currentMap === "es") {
    state.esLevels = state.levels;
  } else if (state.currentMap === "it") {
    state.itLevels = state.levels;
  } else if (state.currentMap === "us") {
    state.usLevels = state.levels;
  } else if (state.currentMap === "cn") {
    state.cnLevels = state.levels;
  } else if (state.currentMap === "kr") {
    state.krLevels = state.levels;
  } else if (state.currentMap === "au") {
    state.auLevels = state.levels;
  } else if (state.currentMap === "in") {
    state.inLevels = state.levels;
  } else if (state.currentMap === "uk") {
    state.ukLevels = state.levels;
  } else if (state.currentMap === "mx") {
    state.mxLevels = state.levels;
  } else if (state.currentMap === "tr") {
    state.trLevels = state.levels;
  } else {
    state.worldLevels = state.levels;
  }
  localStorage.setItem("maplevel_jp_v5", JSON.stringify(state));
}

// ── UI / Header ──────────────────────────────────────────────
function updateHeader() {
  const total = Object.values(state.levels).reduce((a, b) => a + b, 0);
  document.getElementById("card-level").textContent = "Ride the world";
  document.getElementById("card-score").textContent = total;

  let maxPoints = 235; // Japan
  if (state.currentMap === "fr") {
    maxPoints = 505; // France (101 departments * 5)
  } else if (state.currentMap === "es") {
    maxPoints = 260; // Spain (52 provinces * 5)
  } else if (state.currentMap === "it") {
    maxPoints = 535; // Italy (107 provinces * 5)
  } else if (state.currentMap === "us") {
    maxPoints = 255; // US (51 states/territories * 5)
  } else if (state.currentMap === "cn") {
    maxPoints = 165; // China (33 provinces * 5)
  } else if (state.currentMap === "kr") {
    maxPoints = 80; // South Korea (16 provinces * 5)
  } else if (state.currentMap === "au") {
    maxPoints = 40; // Australia (8 states/territories * 5)
  } else if (state.currentMap === "in") {
    maxPoints = 175; // India (35 states/territories * 5)
  } else if (state.currentMap === "uk") {
    maxPoints = 60; // UK (12 regions * 5)
  } else if (state.currentMap === "mx") {
    maxPoints = 160; // Mexico (32 states * 5)
  } else if (state.currentMap === "tr") {
    maxPoints = 405; // Turkey (81 provinces * 5)
  } else if (state.currentMap === "world") {
    if (worldData) {
      const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
      const countries = countriesGeoJson.features.filter(d => d.id !== "010");
      maxPoints = countries.length * 5;
    } else {
      maxPoints = 885; // estimate
    }
  }
  document.getElementById("card-max-score").textContent = `/ ${maxPoints} pts`;

  const lang = state.lang || "en";
  const t = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS["en"];

  // Update traveler watermark dynamically
  const userWatermark = document.getElementById("card-user-watermark");
  if (userWatermark) {
    userWatermark.innerHTML = `<i class="fa-solid fa-user"></i> ${state.username !== "Votre nom" ? state.username : "French Rider"}`;
  }

  // Update floating profile button text dynamically
  const floatingName = document.getElementById("lbl-floating-name");
  if (floatingName) {
    let displayName = state.username;
    let isDefault = false;
    
    if (!displayName || displayName === "Votre nom" || displayName === "French Rider") {
       displayName = t.tapName;
       isDefault = true;
    }
    
    const exploredCount = Object.values(state.levels).filter(l => l >= 3).length;
    const nameHtml = `<span style="${isDefault ? 'border-bottom: 1px dashed rgba(255,255,255,0.7); opacity: 0.9;' : 'font-weight: 800; border-bottom: 1px solid rgba(255,255,255,0.5);'}">${displayName} <i class="fa-solid fa-pen" style="font-size: 0.7em;"></i></span>`;
    
    if (state.currentMap === "jp") {
      floatingName.innerHTML = t.explored(nameHtml, exploredCount);
    } else if (state.currentMap === "fr") {
      floatingName.innerHTML = t.exploredFrance(nameHtml, exploredCount);
    } else if (state.currentMap === "es") {
      floatingName.innerHTML = t.exploredSpain(nameHtml, exploredCount);
    } else if (state.currentMap === "it") {
      floatingName.innerHTML = t.exploredItaly(nameHtml, exploredCount);
    } else if (state.currentMap === "us") {
      floatingName.innerHTML = t.exploredUS(nameHtml, exploredCount);
    } else if (state.currentMap === "cn") {
      floatingName.innerHTML = t.exploredChina(nameHtml, exploredCount);
    } else if (state.currentMap === "kr") {
      floatingName.innerHTML = t.exploredKorea(nameHtml, exploredCount);
    } else if (state.currentMap === "au") {
      floatingName.innerHTML = t.exploredAustralia(nameHtml, exploredCount);
    } else if (state.currentMap === "in") {
      floatingName.innerHTML = t.exploredIndia(nameHtml, exploredCount);
    } else if (state.currentMap === "uk") {
      floatingName.innerHTML = t.exploredUK(nameHtml, exploredCount);
    } else {
      floatingName.innerHTML = t.exploredWorld(nameHtml, exploredCount);
    }
  }
}

function toast(msg) {
  const el = document.getElementById("toast");
  el.textContent = msg;
  el.classList.add("show");
  clearTimeout(el._t);
  el._t = setTimeout(() => el.classList.remove("show"), 2500);
}

// ── Build SVG Proportional Cartogram Map ────────────────────
function buildMap() {
  const svg = d3.select("#map-svg");
  svg.selectAll("*").remove();

  if (state.currentMap === "jp") {
    if (japanData) {
      drawJapanMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("japan.json")
        .then(res => res.json())
        .then(data => {
          japanData = data;
          drawJapanMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading Japan map data:", err);
          toast("Erreur de chargement de la carte du Japon.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else if (state.currentMap === "fr") {
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
  } else if (state.currentMap === "it") {
    if (italyProvincesData) {
      drawItalyMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("italy_provinces.geojson")
        .then(res => res.json())
        .then(data => {
          italyProvincesData = data;
          drawItalyMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading Italy map data:", err);
          toast("Erreur de chargement de la carte d'Italie.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else if (state.currentMap === "us") {
    if (usaStatesData) {
      drawUSAMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("usa_states.geojson")
        .then(res => res.json())
        .then(data => {
          usaStatesData = data;
          drawUSAMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading USA map data:", err);
          toast("Erreur de chargement de la carte des USA.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else if (state.currentMap === "cn") {
    if (chinaProvincesData) {
      drawChinaMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("china_provinces.geojson")
        .then(res => res.json())
        .then(data => {
          chinaProvincesData = data;
          if (chinaProvincesData && chinaProvincesData.features) {
            chinaProvincesData.features = chinaProvincesData.features.filter(f => f.properties.id !== "71");
          }
          drawChinaMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading China map:", err);
          toast("Erreur de chargement de la carte de Chine.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else if (state.currentMap === "kr") {
    if (koreaProvincesData) {
      drawKoreaMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("korea_provinces.geojson")
        .then(res => res.json())
        .then(data => {
          koreaProvincesData = data;
          drawKoreaMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading Korea map:", err);
          toast("Erreur de chargement de la carte de Corée.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else if (state.currentMap === "au") {
    if (australiaStatesData) {
      drawAustraliaMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("australia_states.geojson")
        .then(res => res.json())
        .then(data => {
          australiaStatesData = data;
          drawAustraliaMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading Australia map:", err);
          toast("Erreur de chargement de la carte d'Australie.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else if (state.currentMap === "in") {
    if (indiaStatesData) {
      drawIndiaMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("india_states.geojson")
        .then(res => res.json())
        .then(data => {
          indiaStatesData = data;
          drawIndiaMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading India map:", err);
          toast("Erreur de chargement de la carte de l'Inde.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else if (state.currentMap === "uk") {
    if (ukRegionsData) {
      drawUKMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("uk_regions.json")
        .then(res => res.json())
        .then(data => {
          ukRegionsData = data;
          drawUKMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading UK map:", err);
          toast("Erreur de chargement de la carte du Royaume-Uni.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else if (state.currentMap === "mx") {
    if (mexicoStatesData) {
      drawMexicoMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("mexico_states.geojson")
        .then(res => res.json())
        .then(data => {
          mexicoStatesData = data;
          drawMexicoMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading Mexico map:", err);
          toast("Erreur de chargement de la carte du Mexique.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else if (state.currentMap === "tr") {
    if (turkeyProvincesData) {
      drawTurkeyMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("turkey_provinces.geojson")
        .then(res => res.json())
        .then(data => {
          turkeyProvincesData = data;
          drawTurkeyMap();
          updateHeader();
        })
        .catch(err => {
          console.error("Error loading Turkey map:", err);
          toast("Erreur de chargement de la carte de la Turquie.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  } else {
    if (worldData) {
      drawWorldMap();
    } else {
      document.getElementById("map-loading").style.display = "flex";
      fetch("world.json")
        .then(res => res.json())
        .then(data => {
          worldData = data;
          drawWorldMap();
          updateHeader(); // Recalculate accurate max score with actual country count
        })
        .catch(err => {
          console.error("Error loading world map data:", err);
          toast("Error loading map data.");
          document.getElementById("map-loading").style.display = "none";
        });
    }
  }
}

function drawChinaMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  Object.keys(PROVINCES_CN).forEach(code => {
    if (state.levels[code] == null) state.levels[code] = 0;
  });

  const mapG = svg.append("g").attr("id", "china-group");

  const projection = d3.geoMercator()
    .center([105, 36])
    .fitExtent([[30, 20], [530, 510]], chinaProvincesData);

  const pathGenerator = d3.geoPath().projection(projection);

  // Render provinces
  mapG.selectAll(".china-path")
    .data(chinaProvincesData.features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path china-path")
    .attr("data-code", d => d.properties.id)
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[d.properties.id] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return;
      openModal(d.properties.id);
    });

  // Render labels (using d.properties.cp if present)
  mapG.selectAll(".china-label")
    .data(chinaProvincesData.features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => d.properties.id)
    .attr("x", d => {
      if (d.properties.cp && d.properties.cp.length === 2) {
        return projection(d.properties.cp)[0];
      }
      const centroid = pathGenerator.centroid(d);
      return centroid ? centroid[0] : 0;
    })
    .attr("y", d => {
      if (d.properties.cp && d.properties.cp.length === 2) {
        return projection(d.properties.cp)[1];
      }
      const centroid = pathGenerator.centroid(d);
      return centroid ? centroid[1] : 0;
    })
    .attr("text-anchor", "middle")
    .attr("dominant-baseline", "middle")
    .attr("font-family", "'Outfit', sans-serif")
    .attr("font-size", "4px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => {
      if (d.properties.id === "81" || d.properties.id === "82") return ""; // Hide HK & Macau labels at repos
      return PROVINCES_CN_LABELS[d.properties.id] || d.properties.id;
    });

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
  document.getElementById("map-loading").style.display = "none";
}

function drawKoreaMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  Object.keys(PROVINCES_KR).forEach(code => {
    if (state.levels[code] == null) state.levels[code] = 0;
  });

  const mapG = svg.append("g").attr("id", "korea-group");

  const projection = d3.geoMercator()
    .center([127.5, 36])
    .fitExtent([[60, 30], [500, 520]], koreaProvincesData);

  const pathGenerator = d3.geoPath().projection(projection);

  mapG.selectAll(".korea-path")
    .data(koreaProvincesData.features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path korea-path")
    .attr("data-code", d => d.properties.ID_1)
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[d.properties.ID_1] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return;
      openModal(d.properties.ID_1);
    });

  mapG.selectAll(".korea-label")
    .data(koreaProvincesData.features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => d.properties.ID_1)
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
      if (d.properties.ID_1 === 15) return ""; // Hide Seoul (SU) label at repos to avoid collision
      return PROVINCES_KR_LABELS[d.properties.ID_1] || d.properties.ID_1;
    });

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
  document.getElementById("map-loading").style.display = "none";
}

function drawAustraliaMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  Object.keys(STATES_AU).forEach(code => {
    if (state.levels[code] == null) state.levels[code] = 0;
  });

  const mapG = svg.append("g").attr("id", "australia-group");

  const projection = d3.geoMercator()
    .center([133, -25])
    .fitExtent([[40, 40], [520, 500]], australiaStatesData);

  const pathGenerator = d3.geoPath().projection(projection);

  mapG.selectAll(".australia-path")
    .data(australiaStatesData.features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path australia-path")
    .attr("data-code", d => d.properties.STATE_CODE)
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[d.properties.STATE_CODE] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return;
      openModal(d.properties.STATE_CODE);
    });

  mapG.selectAll(".australia-label")
    .data(australiaStatesData.features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => d.properties.STATE_CODE)
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
    .attr("font-size", "5px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => STATES_AU_LABELS[d.properties.STATE_CODE] || d.properties.STATE_CODE);

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
  document.getElementById("map-loading").style.display = "none";
}

function drawIndiaMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  Object.keys(STATES_IN).forEach(code => {
    if (state.levels[code] == null) state.levels[code] = 0;
  });

  const mapG = svg.append("g").attr("id", "india-group");

  const projection = d3.geoMercator()
    .center([78, 22])
    .fitExtent([[40, 20], [520, 530]], indiaStatesData);

  const pathGenerator = d3.geoPath().projection(projection);

  mapG.selectAll(".india-path")
    .data(indiaStatesData.features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path india-path")
    .attr("data-code", d => d.properties.ID_1)
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[d.properties.ID_1] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return;
      openModal(d.properties.ID_1);
    });

  mapG.selectAll(".india-label")
    .data(indiaStatesData.features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => d.properties.ID_1)
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
    .attr("font-size", "4px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => {
      const code = d.properties.ID_1;
      if ([6, 8, 9, 10, 19, 27].includes(code)) return ""; // Hide small union territory labels at repos to avoid overlaps
      return STATES_IN_LABELS[code] || code;
    });

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
  document.getElementById("map-loading").style.display = "none";
}


function drawUKMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  Object.keys(REGIONS_UK).forEach(code => {
    if (state.levels[code] == null) state.levels[code] = 0;
  });

  const mapG = svg.append("g").attr("id", "uk-group");

  // Extract TopoJSON features
  const ukGeoJSON = topojson.feature(ukRegionsData, ukRegionsData.objects.poly);

  const projection = d3.geoMercator()
    .fitExtent([[30, 20], [530, 510]], ukGeoJSON);

  const pathGenerator = d3.geoPath().projection(projection);

  // Render regions
  mapG.selectAll(".uk-path")
    .data(ukGeoJSON.features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path uk-path")
    .attr("data-code", d => d.properties.ID)
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[d.properties.ID] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return;
      openModal(d.properties.ID);
    });

  // Render labels
  mapG.selectAll(".uk-label")
    .data(ukGeoJSON.features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => d.properties.ID)
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
    .attr("font-size", "7px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => REGIONS_UK_LABELS[d.properties.ID] || d.properties.ID);

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
  document.getElementById("map-loading").style.display = "none";
}


function drawMexicoMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  Object.keys(STATES_MX).forEach(code => {
    if (state.levels[code] == null) state.levels[code] = 0;
  });

  const mapG = svg.append("g").attr("id", "mexico-group");

  const projection = d3.geoMercator()
    .fitExtent([[30, 30], [530, 500]], mexicoStatesData);

  const pathGenerator = d3.geoPath().projection(projection);

  // Render states
  mapG.selectAll(".mexico-path")
    .data(mexicoStatesData.features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path mexico-path")
    .attr("data-code", d => String(d.properties.state_code))
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[String(d.properties.state_code)] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return;
      openModal(String(d.properties.state_code));
    });

  // Render labels
  mapG.selectAll(".mexico-label")
    .data(mexicoStatesData.features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => String(d.properties.state_code))
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
    .attr("font-size", "7px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => STATES_MX_LABELS[String(d.properties.state_code)] || d.properties.state_name);

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
  document.getElementById("map-loading").style.display = "none";
}

function drawTurkeyMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  Object.keys(PROVINCES_TR).forEach(code => {
    if (state.levels[code] == null) state.levels[code] = 0;
  });

  const mapG = svg.append("g").attr("id", "turkey-group");

  const projection = d3.geoMercator()
    .fitExtent([[30, 30], [530, 500]], turkeyProvincesData);

  const pathGenerator = d3.geoPath().projection(projection);

  // Render provinces
  mapG.selectAll(".turkey-path")
    .data(turkeyProvincesData.features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path turkey-path")
    .attr("data-code", d => String(d.properties.number))
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[String(d.properties.number)] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return;
      openModal(String(d.properties.number));
    });

  // Render labels
  mapG.selectAll(".turkey-label")
    .data(turkeyProvincesData.features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => String(d.properties.number))
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
    .attr("font-size", "5.5px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => PROVINCES_TR_LABELS[String(d.properties.number)] || d.properties.name);

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
  document.getElementById("map-loading").style.display = "none";
}


function drawJapanMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  // Initialize missing levels for Japan prefectures
  for (let i = 1; i <= 47; i++) {
    const code = String(i).padStart(2, '0');
    if (state.levels[code] == null) {
      state.levels[code] = 0;
    }
  }

  // Convert TopoJSON to GeoJSON
  const prefecturesGeoJSON = topojson.feature(japanData, japanData.objects.prefectures);
  const honshuGeoJSON = {
    type: "FeatureCollection",
    features: prefecturesGeoJSON.features.filter(f => f.id !== "47")
  };
  const okinawaFeature = prefecturesGeoJSON.features.find(f => f.id === "47");

  // 1. Draw Metropolitan / Main Japan inside a zoomable group
  const mapG = svg.append("g")
    .attr("id", "japan-group");

  const projection = d3.geoIdentity()
    .fitExtent([[110, 25], [550, 545]], honshuGeoJSON);

  const pathGenerator = d3.geoPath().projection(projection);

  // Render main prefectures
  mapG.selectAll(".pref-path")
    .data(honshuGeoJSON.features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path pref-path")
    .attr("data-code", d => d.id)
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[d.id] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      // Prevent modal opening if dragging
      if (event.defaultPrevented) return;
      openModal(d.id);
    });

  // Draw prefecture label names inside centroids for Honshu/Hokkaido
  mapG.selectAll(".pref-label")
    .data(honshuGeoJSON.features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => d.id)
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
    .attr("font-size", "3.8px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => state.lang === "ja" ? NAMES_JA[d.id] : NAMES_EN[d.id]);

  // 2. Setup D3 Zoom & Pinch support for Honshu/Hokkaido
  const zoomBehavior = d3.zoom()
    .scaleExtent([1, 8])
    .filter((event) => {
      // Exclude zoom gestures starting on the left side of the map (x < 110) where Okinawa inset is located
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
      
      // Keep D3 default filters: no ctrlKey, left click only for mouse events
      return !event.ctrlKey && (!event.type.startsWith("mouse") || event.button === 0) && xInSvg >= 110;
    })
    .on("zoom", (event) => {
      mapG.attr("transform", event.transform);
    });

  svg.call(zoomBehavior);

  // 3. Render Okinawa Inset Box in top-left (outside mapG so it stays fixed!)
  const OX = 12, OY = 12, OW = 90, OH = 82;

  svg.append("rect")
    .attr("x", OX).attr("y", OY).attr("width", OW).attr("height", OH)
    .attr("fill", "rgba(255, 255, 255, 0.05)")
    .attr("stroke", "rgba(255, 255, 255, 0.35)")
    .attr("stroke-width", 1.2)
    .attr("rx", 4);

  svg.append("text")
    .attr("id", "inset-label")
    .attr("x", OX + OW / 2)
    .attr("y", OY + OH - 7)
    .attr("text-anchor", "middle")
    .attr("font-family", "'Outfit', sans-serif")
    .attr("font-size", "8.5px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(255, 255, 255, 0.8)")
    .text(`47 - ${state.lang === "ja" ? "沖縄" : "Okinawa"}`);

  if (okinawaFeature) {
    const gOk = svg.append("g")
      .attr("class", "cell-group")
      .attr("data-code", "47")
      .style("cursor", "pointer")
      .on("click", (event) => {
        if (event.defaultPrevented) return;
        openModal("47");
      });

    const localProjection = d3.geoIdentity()
      .fitExtent([[OX + 6, OY + 6], [OX + OW - 6, OY + OH - 20]], okinawaFeature);

    const localPath = d3.geoPath().projection(localProjection);

    gOk.append("path")
      .attr("class", "cell-path")
      .attr("data-code", "47")
      .attr("d", localPath(okinawaFeature))
      .attr("fill", COLORS[state.levels["47"] || 0])
      .attr("stroke", "#ffffff")
      .attr("stroke-width", 0.7);

    // Transparent click helper covering the entire inset box for easy tapping, placed last to be on top!
    gOk.append("rect")
      .attr("x", OX)
      .attr("y", OY)
      .attr("width", OW)
      .attr("height", OH)
      .attr("fill", "rgba(0,0,0,0)")
      .attr("pointer-events", "all")
      .style("cursor", "pointer");
  }

  document.getElementById("map-loading").style.display = "none";
}

function drawFranceMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  // Initialize missing levels for departments in France
  Object.keys(DEPARTEMENTS_FR).forEach(code => {
    if (state.levels[code] == null) {
      state.levels[code] = 0;
    }
  });

  // 1. Draw Metropolitan France Departments inside a zoomable group
  const mapG = svg.append("g")
    .attr("id", "metro-group");

  const projection = d3.geoConicConformal()
    .center([2.454071, 46.275418])
    .fitExtent([[110, 25], [550, 545]], franceDepsData);

  const pathGenerator = d3.geoPath().projection(projection);

  // Render metropolitan departments
  mapG.selectAll(".metro-path")
    .data(franceDepsData.features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path metro-path")
    .attr("data-code", d => d.properties.code)
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[d.properties.code] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      // Prevent modal opening if dragging
      if (event.defaultPrevented) return;
      openModal(d.properties.code);
    });

  // Draw department label numbers inside centroids for metropolitan departments
  mapG.selectAll(".dep-label")
    .data(franceDepsData.features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => d.properties.code)
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
    .attr("font-size", "3.8px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => d.properties.code);

  // 2. Setup D3 Zoom & Pinch support for Metropolitan France
  const zoomBehavior = d3.zoom()
    .scaleExtent([1, 8]) // zoom levels from 1x to 8x
    .filter((event) => {
      // Exclude zoom gestures starting on the left side of the map (x < 92) where DOM-TOMs are located
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
      
      // Keep D3 default filters: no ctrlKey, left click only for mouse events
      return !event.ctrlKey && (!event.type.startsWith("mouse") || event.button === 0) && xInSvg >= 92;
    })
    .on("zoom", (event) => {
      mapG.attr("transform", event.transform);
    });

  svg.call(zoomBehavior);

  // 3. Draw 5 Overseas Insets (Okinawa-style) stacked vertically on the left side (outside mapG so they stay fixed!)
  const domtoms = [
    { code: "971", name: "Guadeloupe", nameJa: "グアドループ", y: 35 },
    { code: "972", name: "Martinique", nameJa: "マルティニーク", y: 132 },
    { code: "973", name: "Guyane", nameJa: "ギアナ", y: 229 },
    { code: "974", name: "La Réunion", nameJa: "レユニオン", y: 326 },
    { code: "976", name: "Mayotte", nameJa: "マヨット", y: 423 }
  ];

  domtoms.forEach(dt => {
    const OX = 12, OY = dt.y, OW = 90, OH = 82;

    // Draw Inset Box Border
    svg.append("rect")
      .attr("x", OX).attr("y", OY).attr("width", OW).attr("height", OH)
      .attr("fill", "rgba(255, 255, 255, 0.05)")
      .attr("stroke", "rgba(255, 255, 255, 0.35)")
      .attr("stroke-width", 1.2)
      .attr("rx", 4);

    // Draw Inset Label Box
    svg.append("text")
      .attr("x", OX + OW / 2)
      .attr("y", OY + OH - 7)
      .attr("text-anchor", "middle")
      .attr("font-family", "'Outfit', sans-serif")
      .attr("font-size", "8.5px")
      .attr("font-weight", "800")
      .attr("fill", "rgba(255, 255, 255, 0.8)")
      .text(`${dt.code} - ${state.lang === "ja" ? dt.nameJa : dt.name}`);

    // Get GeoJSON Feature for this DOM-TOM
    const feature = franceDomTomData.features.find(f => f.properties.code === dt.code);
    if (feature) {
      const gInset = svg.append("g")
        .attr("class", "cell-group")
        .attr("data-code", dt.code)
        .style("cursor", "pointer")
        .on("click", (event) => {
          openModal(dt.code);
        });

      // Setup small local projection for the inset box
      const localProjection = d3.geoMercator()
        .fitExtent([[OX + 6, OY + 6], [OX + OW - 6, OY + OH - 20]], feature);

      const localPath = d3.geoPath().projection(localProjection);

      gInset.append("path")
        .attr("class", "cell-path")
        .attr("data-code", dt.code)
        .attr("d", localPath(feature))
        .attr("fill", COLORS[state.levels[dt.code] || 0])
        .attr("stroke", "#ffffff")
        .attr("stroke-width", 0.7);

      // Transparent click helper covering the entire inset box for easy tapping, placed last to be on top!
      gInset.append("rect")
        .attr("x", OX)
        .attr("y", OY)
        .attr("width", OW)
        .attr("height", OH)
        .attr("fill", "rgba(0,0,0,0)")
        .attr("pointer-events", "all")
        .style("cursor", "pointer");
    }
  });

  document.getElementById("map-loading").style.display = "none";
}


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


function drawItalyMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  // Initialize missing levels for Italy provinces
  Object.keys(PROVINCES_IT).forEach(code => {
    if (state.levels[code] == null) {
      state.levels[code] = 0;
    }
  });

  // Create zoomable group
  const mapG = svg.append("g")
    .attr("id", "italy-group");

  // Project and fit extent (covers mainland, Sicily, and Sardinia)
  // Using d3.geoMercator() centered around Rome, fits perfectly
  const projection = d3.geoMercator()
    .center([12.5, 41.9])
    .fitExtent([[60, 30], [500, 520]], italyProvincesData);

  const pathGenerator = d3.geoPath().projection(projection);

  // Render provinces
  mapG.selectAll(".italy-path")
    .data(italyProvincesData.features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path italy-path")
    .attr("data-code", d => d.properties.prov_acr)
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[d.properties.prov_acr] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return;
      openModal(d.properties.prov_acr);
    });

  // Render province labels
  mapG.selectAll(".italy-label")
    .data(italyProvincesData.features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => d.properties.prov_acr)
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
    .attr("font-size", "4px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => d.properties.prov_acr);

  // Setup D3 Zoom & Pinch
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

  document.getElementById("map-loading").style.display = "none";
}


function drawUSAMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  const FIPS_TO_US_CODE = {
    "01": "AL", "02": "AK", "04": "AZ", "05": "AR", "06": "CA", "08": "CO", "09": "CT", "10": "DE",
    "11": "DC", "12": "FL", "13": "GA", "15": "HI", "16": "ID", "17": "IL", "18": "IN", "19": "IA",
    "20": "KS", "21": "KY", "22": "LA", "23": "ME", "24": "MD", "25": "MA", "26": "MI", "27": "MN",
    "28": "MS", "29": "MO", "30": "MT", "31": "NE", "32": "NV", "33": "NH", "34": "NJ", "35": "NM",
    "36": "NY", "37": "NC", "38": "ND", "39": "OH", "40": "OK", "41": "OR", "42": "PA", "44": "RI",
    "45": "SC", "46": "SD", "47": "TN", "48": "TX", "49": "UT", "50": "VT", "51": "VA", "53": "WA",
    "54": "WV", "55": "WI", "56": "WY", "72": "PR"
  };

  // Filter features to exclude Puerto Rico (72) which pushes map boundaries too far south
  const features = usaStatesData.features.filter(d => d.properties.STATE !== "72");

  // Initialize missing levels for US states
  features.forEach(d => {
    const code = FIPS_TO_US_CODE[d.properties.STATE];
    if (code && state.levels[code] == null) {
      state.levels[code] = 0;
    }
  });

  // Create zoomable group
  const mapG = svg.append("g")
    .attr("id", "usa-group");

  // Project and fit extent using geoAlbersUsa (native Alaska & Hawaii insets)
  const projection = d3.geoAlbersUsa()
    .fitExtent([[15, 20], [545, 510]], { type: "FeatureCollection", features: features });

  const pathGenerator = d3.geoPath().projection(projection);

  // Render US states
  mapG.selectAll(".usa-path")
    .data(features)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path usa-path")
    .attr("data-code", d => FIPS_TO_US_CODE[d.properties.STATE] || "")
    .attr("d", pathGenerator)
    .attr("fill", d => {
      const code = FIPS_TO_US_CODE[d.properties.STATE];
      return COLORS[state.levels[code] || 0];
    })
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.7)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return;
      const code = FIPS_TO_US_CODE[d.properties.STATE];
      if (code) openModal(code);
    });

  // Render US states labels
  mapG.selectAll(".usa-label")
    .data(features)
    .enter()
    .append("text")
    .attr("class", "cell-label")
    .attr("data-code", d => FIPS_TO_US_CODE[d.properties.STATE] || "")
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
    .attr("font-size", "6px")
    .attr("font-weight", "800")
    .attr("fill", "rgba(26,37,51,0.85)")
    .attr("pointer-events", "none")
    .text(d => {
      const code = FIPS_TO_US_CODE[d.properties.STATE];
      // Hide label for DC on general view to avoid overlapping with MD/VA
      return code === "DC" ? "" : code;
    });

  // Setup D3 Zoom & Pinch
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

  document.getElementById("map-loading").style.display = "none";
}


function drawWorldMap() {
  const svg = d3.select("#map-svg");
  const W = 560, H = 570;
  svg.attr("viewBox", `0 0 ${W} ${H}`);

  const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
  const countries = countriesGeoJson.features.filter(d => d.id !== "010"); // Exclude Antarctica

  // Project and fit extent
  const projection = d3.geoMercator()
    .fitExtent([[10, 50], [550, 530]], countriesGeoJson);

  const pathGenerator = d3.geoPath().projection(projection);

  const mapG = svg.append("g");

  // Initialize missing levels
  countries.forEach(d => {
    if (state.levels[d.id] == null) {
      state.levels[d.id] = 0;
    }
  });

  // Render countries
  mapG.selectAll("path")
    .data(countries)
    .enter()
    .append("path")
    .attr("class", "cell-group cell-path")
    .attr("data-code", d => d.id)
    .attr("d", pathGenerator)
    .attr("fill", d => COLORS[state.levels[d.id] || 0])
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 0.5)
    .style("cursor", "pointer")
    .on("click", (event, d) => {
      if (event.defaultPrevented) return; // Ignore drag clicks
      openModal(d.id);
    });

  // Manual centroid overrides for countries where the auto-centroid is misleading
  // (due to overseas territories, large landmasses like Alaska, etc.)
  const CENTROID_OVERRIDES = {
    "840": [-97, 38],     // USA → center of contiguous US
    "250": [2.5, 46.5],   // France → metropolitan France
    "643": [55, 60],      // Russia → shifted west for readability
    "578": [10, 62],      // Norway → mainland Norway
    "124": [-100, 57],    // Canada → center of mainland
    "036": [134, -25],    // Australia → center of mainland
    "360": [118, -2],     // Indonesia → center of archipelago
    "554": [173, -41],    // New Zealand → center of islands
    "458": [109, 3],      // Malaysia → Peninsular Malaysia
    "156": [104, 35],     // China → center of mainland
    "076": [-53, -14],    // Brazil → center
    "304": [-42, 72],     // Greenland → center
    "540": [165, -21.5],  // New Caledonia
  };

  // Add labels for all countries
  countries.forEach(d => {
    const area = pathGenerator.area(d);
    let labelPos;
    
    if (CENTROID_OVERRIDES[d.id]) {
      const coords = CENTROID_OVERRIDES[d.id];
      labelPos = projection(coords);
    } else {
      labelPos = pathGenerator.centroid(d);
    }
    
    if (labelPos && !isNaN(labelPos[0]) && !isNaN(labelPos[1])) {
      const name = getCountryName(d.id, d.properties.name);
      const baseFs = Math.max(2.5, Math.min(8.5, Math.sqrt(area) * 0.15));
      
      mapG.append("text")
        .attr("class", "cell-label-world")
        .attr("data-area", area)
        .attr("data-fs", baseFs)
        .attr("x", labelPos[0])
        .attr("y", labelPos[1])
        .attr("text-anchor", "middle")
        .attr("dominant-baseline", "middle")
        .attr("font-family", "'Outfit', sans-serif")
        .attr("font-size", baseFs + "px")
        .attr("font-weight", "800")
        .attr("fill", "rgba(26,37,51,0.85)")
        .attr("pointer-events", "none")
        .style("opacity", area > 300 ? 1 : 0)
        .text(name);
    }
  });

  // Setup D3 Zoom & Pinch for World
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
      
      return !event.ctrlKey && (!event.type.startsWith("mouse") || event.button === 0) && xInSvg >= 0;
    })
    .on("zoom", (event) => {
      mapG.attr("transform", event.transform);
      const k = event.transform.k;
      
      mapG.selectAll(".cell-label-world").each(function() {
        const txt = d3.select(this);
        const area = parseFloat(txt.attr("data-area"));
        const baseFs = parseFloat(txt.attr("data-fs"));
        
        if (area * k * k > 150) {
          txt.style("opacity", 1);
          txt.attr("font-size", (baseFs / Math.pow(k, 0.4)) + "px");
        } else {
          txt.style("opacity", 0);
        }
      });
    });

  svg.call(zoomBehavior);

  document.getElementById("map-loading").style.display = "none";
}

function getCountryDisplayName(code) {
  if (state.currentMap === "jp") {
    return state.lang === "ja" ? NAMES_JA[code] : NAMES_EN[code];
  } else if (state.currentMap === "fr") {
    return `${code} - ${DEPARTEMENTS_FR[code] || code}`;
  } else if (state.currentMap === "es") {
    return PROVINCES_ES[code] || code;
  } else if (state.currentMap === "it") {
    return `${code} - ${PROVINCES_IT[code] || code}`;
  } else if (state.currentMap === "us") {
    return STATES_US[code] || code;
  } else if (state.currentMap === "cn") {
    return PROVINCES_CN[code] || code;
  } else if (state.currentMap === "kr") {
    return PROVINCES_KR[code] || code;
  } else if (state.currentMap === "au") {
    return STATES_AU[code] || code;
  } else if (state.currentMap === "in") {
    return STATES_IN[code] || code;
  } else if (state.currentMap === "uk") {
    return REGIONS_UK[code] || code;
  } else if (state.currentMap === "mx") {
    return STATES_MX[code] || code;
  } else if (state.currentMap === "tr") {
    return PROVINCES_TR[code] || code;
  } else {
    if (worldData) {
      const countriesGeoJson = topojson.feature(worldData, worldData.objects.countries);
      const feature = countriesGeoJson.features.find(f => f.id === code);
      if (feature) {
        return getCountryName(code, feature.properties.name);
      }
    }
    return code;
  }
}

// ── Modal level selection ────────────────────────────────────
function openModal(code) {
  activePrefCode = code;
  const name = getCountryDisplayName(code);
  document.getElementById("modal-title").textContent = `@ ${name}`;
  const cur = state.levels[code] || 0;
  document.querySelectorAll(".opt-btn").forEach(btn => {
    btn.classList.toggle("selected", +btn.dataset.level === cur);
  });
  document.getElementById("modal-overlay").classList.remove("hidden");
}

function closeModal() {
  document.getElementById("modal-overlay").classList.add("hidden");
  activePrefCode = null;
}

// ── Event Setup ──────────────────────────────────────────────
function setupEvents() {
  document.getElementById("modal-close").addEventListener("click", closeModal);
  document.getElementById("modal-overlay").addEventListener("click", e => {
    if (e.target.id === "modal-overlay") closeModal();
  });

  document.querySelectorAll(".opt-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      if (!activePrefCode) return;
      const lvl = +btn.dataset.level;
      state.levels[activePrefCode] = lvl;
      saveState();
      
      // Update cell rect/path color dynamically
      const g = document.querySelector(`.cell-group[data-code="${activePrefCode}"]`);
      if (g) {
        if (g.tagName === "path" || g.tagName === "rect") {
          g.setAttribute("fill", COLORS[lvl]);
        } else {
          const targetElement = g.querySelector(".cell-rect, .cell-path");
          if (targetElement) targetElement.setAttribute("fill", COLORS[lvl]);
        }
      } else {
        // Also support selection via path selector direct mapping (World Map fallback)
        const cellPath = document.querySelector(`path.cell-path[data-code="${activePrefCode}"]`);
        if (cellPath) cellPath.setAttribute("fill", COLORS[lvl]);
      }
      
      updateHeader();
      closeModal();

      const name = getCountryDisplayName(activePrefCode);
      const lbls = ["Jamais", "Passé", "Escale", "Visité", "Séjourné", "Habité"];
      toast(`${name} → ${lbls[lvl]}`);
    });
  });

  // Country Modal
  const countryOverlay = document.getElementById("country-overlay");
  document.getElementById("btn-country-select").addEventListener("click", () => {
    countryOverlay.classList.remove("hidden");
  });
  document.getElementById("country-close").addEventListener("click", () => {
    countryOverlay.classList.add("hidden");
  });
  countryOverlay.addEventListener("click", e => {
    if (e.target.id === "country-overlay") countryOverlay.classList.add("hidden");
  });

  document.querySelectorAll(".country-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      if (btn.hasAttribute("disabled")) return;
      document.querySelectorAll(".country-btn").forEach(b => b.classList.remove("selected"));
      btn.classList.add("selected");
      
      const newMap = btn.dataset.val;
      if (newMap !== state.currentMap) {
        if (state.currentMap === "jp") state.jpLevels = state.levels;
        else if (state.currentMap === "fr") state.frLevels = state.levels;
        else if (state.currentMap === "es") state.esLevels = state.levels;
        else if (state.currentMap === "it") state.itLevels = state.levels;
        else if (state.currentMap === "us") state.usLevels = state.levels;
        else if (state.currentMap === "cn") state.cnLevels = state.levels;
        else if (state.currentMap === "kr") state.krLevels = state.levels;
        else if (state.currentMap === "au") state.auLevels = state.levels;
        else if (state.currentMap === "in") state.inLevels = state.levels;
        else if (state.currentMap === "uk") state.ukLevels = state.levels;
        else if (state.currentMap === "mx") state.mxLevels = state.levels;
        else if (state.currentMap === "tr") state.trLevels = state.levels;
        else state.worldLevels = state.levels;
        
        state.currentMap = newMap;
        
        if (newMap === "jp") state.levels = state.jpLevels;
        else if (newMap === "fr") state.levels = state.frLevels;
        else if (newMap === "es") state.levels = state.esLevels;
        else if (newMap === "it") state.levels = state.itLevels;
        else if (newMap === "us") state.levels = state.usLevels;
        else if (newMap === "cn") state.levels = state.cnLevels;
        else if (newMap === "kr") state.levels = state.krLevels;
        else if (newMap === "au") state.levels = state.auLevels;
        else if (newMap === "in") state.levels = state.inLevels;
        else if (newMap === "uk") state.levels = state.ukLevels;
        else if (newMap === "mx") state.levels = state.mxLevels;
        else if (newMap === "tr") state.levels = state.trLevels;
        else state.levels = state.worldLevels;
        saveState();
        
        updateUITranslations();
        buildMap();
      }
      
      countryOverlay.classList.add("hidden");
    });
  });

  // Language Modal
  const langOverlay = document.getElementById("lang-overlay");
  document.getElementById("btn-lang-select").addEventListener("click", () => {
    langOverlay.classList.remove("hidden");
  });
  document.getElementById("lang-close").addEventListener("click", () => {
    langOverlay.classList.add("hidden");
  });
  langOverlay.addEventListener("click", e => {
    if (e.target.id === "lang-overlay") langOverlay.classList.add("hidden");
  });

  document.querySelectorAll(".lang-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".lang-btn").forEach(b => b.classList.remove("selected"));
      btn.classList.add("selected");
      
      const val = btn.dataset.val;
      state.lang = val;
      saveState();
      
      let txt = "🇬🇧 English";
      if(val === "es") txt = "🇪🇸 Español";
      if(val === "fr") txt = "🇫🇷 Français";
      if(val === "hi") txt = "🇮🇳 हिन्दी";
      if(val === "ja") txt = "🇯🇵 日本語";
      if(val === "ko") txt = "🇰🇷 한국어";
      if(val === "zh") txt = "🇨🇳 中文";
      document.getElementById("btn-lang-select").innerHTML = `${txt} <i class="fa-solid fa-chevron-down" style="font-size:0.7em;margin-left:4px;"></i>`;
      
      buildMap();
      updateUITranslations();
      langOverlay.classList.add("hidden");
    });
  });

  // Edit Name
  const btnFloatingProfile = document.getElementById("btn-floating-profile");
  if (btnFloatingProfile) {
    btnFloatingProfile.addEventListener("click", () => {
      const n = prompt("Votre prénom/pseudo :", state.username === "Votre nom" ? "" : state.username);
      if (n !== null) {
        state.username = n.trim() || "Votre nom";
        saveState();
        updateHeader();
        toast("Nom mis à jour !");
      }
    });
  }

  // Export overlay
  document.getElementById("btn-export").addEventListener("click", () => {
    document.getElementById("export-overlay").classList.remove("hidden");
  });
  
  document.getElementById("export-overlay").addEventListener("click", e => {
    if (e.target.id === "export-overlay") {
      document.getElementById("export-overlay").classList.add("hidden");
    }
  });

  const doExport = () => {
    document.getElementById("export-overlay").classList.add("hidden");
    const card = document.getElementById("export-card");
    const mapSvg = document.getElementById("map-svg");
    const floatingBtn = document.getElementById("btn-floating-profile");
    const header = document.getElementById("card-header");
    const legend = document.getElementById("card-legend");
    
    const domainWatermark = document.getElementById("card-domain-watermark");
    
    // Save current styles
    const savedCardWidth = card.style.width;
    const savedSvgTransform = mapSvg.style.transform;
    const savedBtnBottom = floatingBtn ? floatingBtn.style.bottom : null;
    const savedBtnTransform = floatingBtn ? floatingBtn.style.transform : null;
    const savedDomainBottom = domainWatermark ? domainWatermark.style.bottom : null;
    const savedDomainTransform = domainWatermark ? domainWatermark.style.transform : null;
    const savedHeaderPaddingTop = header ? header.style.paddingTop : null;
    const savedLegendPaddingBottom = legend ? legend.style.paddingBottom : null;
    
    // Temporarily adjust for clean export (no cropping)
    card.style.width = "560px";
    if (state.currentMap === "jp") {
      mapSvg.style.transform = "translateY(-35px)";
    } else {
      mapSvg.style.transform = "none";
    }
    if (floatingBtn) {
      floatingBtn.style.bottom = "77px";
      floatingBtn.style.transform = "translateX(-50%) scale(1.5)";
    }
    if (domainWatermark) {
      domainWatermark.style.bottom = "128px";
      domainWatermark.style.transform = "scale(1.5)";
    }
    if (header) {
      header.style.paddingTop = "75px";
    }
    if (legend) {
      legend.style.paddingBottom = "51px";
    }

    html2canvas(card, {
      scale: 3,
      useCORS: true,
      logging: false,
      backgroundColor: "#ffffff"
    }).then(canvas => {
      // Restore original styles
      card.style.width = savedCardWidth;
      mapSvg.style.transform = savedSvgTransform;
      if (floatingBtn) {
        floatingBtn.style.bottom = savedBtnBottom;
        floatingBtn.style.transform = savedBtnTransform;
      }
      if (domainWatermark) {
        domainWatermark.style.bottom = savedDomainBottom;
        domainWatermark.style.transform = savedDomainTransform;
      }
      if (header) {
        header.style.paddingTop = savedHeaderPaddingTop;
      }
      if (legend) {
        legend.style.paddingBottom = savedLegendPaddingBottom;
      }
      
      const a = document.createElement("a");
      const mapName = state.currentMap === "jp" ? "japan" : (state.currentMap === "fr" ? "france" : "world");
      a.download = `maplevel_${mapName}_${state.username.replace(/\W/g, "_")}.png`;
      a.href = canvas.toDataURL("image/png");
      a.click();
      toast("🎉 Image enregistrée !");
    }).catch((err) => {
      console.error(err);
      // Restore original styles on error too
      card.style.width = savedCardWidth;
      mapSvg.style.transform = savedSvgTransform;
      if (floatingBtn) {
        floatingBtn.style.bottom = savedBtnBottom;
        floatingBtn.style.transform = savedBtnTransform;
      }
      if (header) {
        header.style.paddingTop = savedHeaderPaddingTop;
      }
      if (legend) {
        legend.style.paddingBottom = savedLegendPaddingBottom;
      }
      toast("Erreur d'export.");
    });
  };

  document.getElementById("btn-dl-anyway").addEventListener("click", doExport);
  document.getElementById("btn-dl-shared").addEventListener("click", () => {
    toast("🙏 Merci !");
    doExport();
  });

  // Reset
  document.getElementById("btn-reset").addEventListener("click", () => {
    if (!confirm("Réinitialiser toute la carte ?")) return;
    Object.keys(state.levels).forEach(c => state.levels[c] = 0);
    saveState();
    
    // Clear all rects and paths
    document.querySelectorAll(".cell-rect, .cell-path").forEach(r => r.setAttribute("fill", COLORS[0]));
    updateHeader();
    toast("Carte réinitialisée !");
  });
}

// ── INIT ─────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  loadState();
  updateHeader();
  setupEvents();
  buildMap();
  
  // Show tutorial modal on load
  const tutoOverlay = document.getElementById("tutorial-overlay");
  if (tutoOverlay) {
    tutoOverlay.classList.remove("hidden");
    
    const closeTuto = () => {
      tutoOverlay.classList.add("hidden");
    };
    
    const closeBtn = document.getElementById("btn-tuto-close");
    if (closeBtn) closeBtn.addEventListener("click", closeTuto);
    
    const headerCloseBtn = document.getElementById("btn-tuto-header-close");
    if (headerCloseBtn) headerCloseBtn.addEventListener("click", closeTuto);
  }
});
