SITE = {
    "name": "Evara",
    "tagline": "Charter perahu untuk memancing, snorkeling, diving & island hopping",
    "wa_number": "6287775382824",
    "email": "jd.associates800@gmail.com",
    # baru: quote untuk section full-image di halaman utama
    "quote": "Laut, sekali ia menebar pesonanya, akan memegangmu dalam jaring kekaguman — selamanya.",
    "quote_author": "Jacques-Yves Cousteau",
}

STORY = [
    "Evara tidak lahir di galangan kapal — ia lahir dari sebuah janji. Donald dan Joan, sepasang suami istri yang diikat bukan hanya oleh janji pernikahan, tetapi juga oleh cinta yang dalam pada laut: menyelam di terumbu, melempar pancing saat fajar, dan membaca bintang dalam navigasi. Bagi mereka, laut bukan tujuan — laut adalah rumah.",
    "Sebagai bentuk cinta dan apresiasi tertinggi, Donald mempersembahkan sebuah perahu nelayan rekreasi untuk Joan. Bukan sekadar hadiah, melainkan perwujudan dari perempuan yang menjadi teman seperjalanan hidupnya. Perahu itu ia namai Evara.",
    "Evara berarti “hadiah terindah dari Tuhan” — sebagaimana Joan di mata Donald. Sejak hari itu, setiap fajar yang dibelah di atas ombak, setiap tali pancing yang diulur, dan setiap penyelaman ke birunya laut adalah rasa syukur yang tak pernah selesai diucapkan.",
    "Kini, cinta itu terbuka untuk Anda. Bersama Evara, kami mengundang Anda merasakan kegembiraan yang sama yang melahirkan perahu ini: sensasi strike di ujung pancing, keheningan di antara terumbu yang hidup, dan matahari keemasan dari atas dek. Karena kisah yang dimulai dengan rasa syukur, layak dibagikan kepada banyak orang.",
]

STORY_SIGN = "— Donald & Joan · Keluarga Evara"

STORY_MEDIA = [
    ("293516c9-66bb-40df-8ea1-08a505bb1a4e.jpeg", "Evara di atas jalur galangan", "Merawat kapal adalah bagian dari menjaga cerita."),
    ("IMG-20250405-WA0001.jpg", "Evara siap kembali berlayar", "Setiap detail kapal disiapkan untuk perjalanan yang aman."),
    ("WhatsApp Image 2026-08-13 at 11.37.28.jpeg", "Suasana dermaga Pulau Tidung", "Dari dermaga inilah banyak perjalanan laut dimulai."),
    ("evara-boat-beach.jpeg", "Evara menyambut perjalanan", "Rumah kecil di atas laut, siap membawa cerita baru."),
]

BOAT_INFO = {
    "nama": "KM Evara",
    "panjang": "12 m",
    "kapasitas": "12 penumpang",
    "fasilitas": [
        "Alat pancing & fighting chair",
        "Set snorkeling & diving",
        "Cabin teduh & sun deck",
        "Cool box, air minum & makan siang",
        "Life jacket & peralatan keselamatan lengkap",
    ],
}

SERVICES = [
    {"nama": "Fishing Trip",   "durasi": "Full day (8 jam)",  "harga": 650000,
     "desk": "Trip memancing di spot pilihan kru, cocok untuk pemula hingga pemancing serius."},
    {"nama": "Snorkeling Trip","durasi": "Half day (4 jam)",  "harga": 450000,
     "desk": "Kunjungi 2–3 spot terumbu dangkal dengan pemandu dan alat lengkap."},
    {"nama": "Diving Trip",    "durasi": "Full day (2 dive)", "harga": 850000,
     "desk": "Dive tersembunyi di spot wall & reef, didampingi dive master berlisensi."},
    {"nama": "Island Hopping", "durasi": "Full day",          "harga": 500000,
     "desk": "Keliling pulau, beach time, dan sunset point sesuai permintaan Anda."},
    {"nama": "Property Recovery", "durasi": "Sesuai kebutuhan", "harga": None,
     "desk": "Layanan pencarian dan pengambilan barang yang hilang di laut hingga kedalaman 100 meter."},
]

DESTINATIONS = [
    {"nama": "Pulau Karang Putih",  "waktu": "± 45 menit", "aktivitas": ["Snorkeling", "Beach"],
     "desk": "Gugusan terumbu dangkal dengan air jernih, ideal untuk snorkeling pagi hari."},
    {"nama": "Gosong Pasir Timur",  "waktu": "± 30 menit", "aktivitas": ["Fishing", "Snorkeling"],
     "desk": "Spot casting favorit; pasir timbul saat surut, cantik untuk foto."},
    {"nama": "Tanjung Bima",        "waktu": "± 1,5 jam",  "aktivitas": ["Diving"],
     "desk": "Wall dive dengan visibilitas hingga 20 m, sering terlihat penyu."},
    {"nama": "Spot Karang Lima",    "waktu": "± 1 jam",    "aktivitas": ["Diving", "Fishing"],
     "desk": "Reef dive ramah pemula sekaligus spot bottom fishing yang produktif."},
    {"nama": "Pulau Mangrove",      "waktu": "± 1 jam",    "aktivitas": ["Traveling", "Beach"],
     "desk": "Jalur mangrove teduh untuk keluarga, ditutup sunset di dek Evara."},
]

HOME_PORT = {"nama": "Dermaga Pulau Tidung", "lat": -5.7989, "lng": 106.5185}

RINGS = [
    {"nama": "Ring 1", "label": "0–3 km", "radius": 3000},
    {"nama": "Ring 2", "label": "3–12 km", "radius": 12000},
]

SPOTS = [
    {"nama": "Perairan Pulau Tidung Kecil", "ring": 1, "kategori": "Snorkeling", "jarak": "0–3 km",
     "desk": "Perairan dangkal yang tenang, kaya vegetasi mangrove dan karang tepi. Ideal untuk pemula dan keluarga.",
     "lat": -5.8032, "lng": 106.5238},
    {"nama": "Area Jembatan Cinta", "ring": 1, "kategori": "Snorkeling", "jarak": "0–3 km",
     "desk": "Menghubungkan Tidung Besar dan Tidung Kecil; transisi air dangkal–sedang. Populer untuk anemon laut dan clownfish.",
     "lat": -5.7984, "lng": 106.5192},
    {"nama": "Tepi Karang Tidung Kecil", "ring": 1, "kategori": "Diving", "jarak": "0–3 km",
     "desk": "Drop-off terumbu kedalaman 10–18 m; cocok untuk fun dive dan pemula Open Water.",
     "lat": -5.8060, "lng": 106.5300},
    {"nama": "Dermaga / Jembatan Cinta", "ring": 1, "kategori": "Fishing", "jarak": "0–3 km",
     "desk": "Dasaran santai dari struktur jembatan/dermaga. Target: ikan karang kecil, kerong-kerong, dan cumi di malam hari.",
     "lat": -5.7994, "lng": 106.5178},
    {"nama": "Pulau Payung", "ring": 2, "kategori": "Snorkeling", "jarak": "± 3–6 km Tenggara",
     "desk": "Rataan karang dangkal jernih (acropora), terlindung dari arus kencang. Banyak ikan sersan mayor.",
     "lat": -5.8190, "lng": 106.5500},
    {"nama": "Gusong Karang Beras", "ring": 2, "kategori": "Snorkeling", "jarak": "± 7–9 km Timur",
     "desk": "Gosong karang di tengah laut dengan visibilitas sangat jernih; dominan karang lunak.",
     "lat": -5.7712, "lng": 106.5700},
    {"nama": "Pulau Tikus", "ring": 2, "kategori": "Snorkeling", "jarak": "± 10–12 km Timur",
     "desk": "Pulau tak berpenghuni dengan pantai dangkal dan rataan karang yang sangat tenang.",
     "lat": -5.8563, "lng": 106.5866},
    {"nama": "Diving Wall Pulau Payung", "ring": 2, "kategori": "Diving", "jarak": "± 5–7 km Tenggara",
     "desk": "Wall dive 18–25 m; arus sedang–kencang. Kipas laut besar, penyu, dan ikan pelagis.",
     "lat": -5.8220, "lng": 106.5550},
    {"nama": "Gusong Karang Beras Deep", "ring": 2, "kategori": "Diving", "jarak": "± 8–10 km Timur",
     "desk": "Kedalaman 12–20 m dengan karang keras padat; jalur kuwe (GT) dan barakuda.",
     "lat": -5.7700, "lng": 106.5800},
    {"nama": "Karang Badongan & Karang Puret", "ring": 2, "kategori": "Fishing", "jarak": "± 5–8 km Barat/BD",
     "desk": "Karang dalam dan rumpon tengah laut. Favorit bottom fishing & jigging: kerapu, kakap merah, lencam.",
     "lat": -5.8150, "lng": 106.4500},
    {"nama": "Koridor Laut Pulau Pari", "ring": 2, "kategori": "Fishing", "jarak": "± 10–12 km Timur",
     "desk": "Perairan dalam jalur pelagis untuk trolling. Target: tenggiri, tongkol, cakalang.",
     "lat": -5.8572, "lng": 106.6197},
]

ACCESS_STEPS = [
    ("Isi form booking", "Kirim form — pesan otomatis tersusun rapi ke WhatsApp/email kami."),
    ("Konfirmasi & DP", "Kami balas ketersediaan jadwal & total biaya maksimal 1×24 jam."),
    ("Bertemu di dermaga", "Meeting point Dermaga Utama, 30 menit sebelum keberangkatan."),
    ("Briefing & berlayar", "Briefing keselamatan, pembagian alat, lalu Evara berangkat!"),
]

ACCESS_OPTIONS = [
    {
        "judul": "Via Pelabuhan Kali Adem / Muara Angke",
        "label": "Opsi ekonomis",
        "desk": "Jalur populer untuk backpacker dan rombongan hemat.",
        "pilihan": [
            {"nama": "Kapal Tradisional Kayu / Kayu Motor", "titik": "Dermaga Kali Adem, Muara Angke (Jakarta Utara)", "harga": "± Rp85.000–Rp100.000 / orang sekali jalan", "durasi": "2,5–3 jam", "jadwal": "Ke Tidung 07.00–07.30 WIB setiap hari. Kembali 07.00–08.00 WIB (Senin–Sabtu), atau 10.00 / 13.00 WIB (Minggu/libur).", "langkah": ["Tiba maksimal pukul 06.00 WIB; disarankan KRL ke Stasiun Jakarta Kota lalu Grab/Gojek ke pelabuhan.", "Beli tiket di loket kapal kayu atau lapor ke koordinator travel jika mengambil paket.", "Boarding pukul 07.00 WIB dan pilih tempat duduk di dek atas atau kabin.", "Kapal berlayar langsung menuju Dermaga Pulau Tidung."]},
            {"nama": "Kapal Express Dishub / JaketBoat", "titik": "Dermaga Kali Adem, Muara Angke", "harga": "± Rp54.000–Rp75.000 / orang sekali jalan", "durasi": "1,5–2 jam", "jadwal": "07.30–08.00 WIB.", "langkah": ["Pesan melalui aplikasi resmi JaketBoat atau loket resmi jika kuota tersedia.", "Tiba pukul 06.30 WIB untuk verifikasi atau cetak e-ticket.", "Tunggu di ruang tunggu ber-AC dan boarding sesuai nomor panggil."]},
        ],
    },
    {
        "judul": "Via Marina Ancol",
        "label": "Opsi premium & cepat",
        "desk": "Cocok untuk keluarga, anak kecil, dan perjalanan yang mengutamakan kenyamanan.",
        "pilihan": [{"nama": "Speedboat Fiber ber-AC", "titik": "Dermaga 16 / 17, Marina Ancol (Jakarta Utara)", "harga": "± Rp215.000 / orang sekali jalan + tiket masuk Ancol ± Rp30.000–Rp35.000", "durasi": "1–1,5 jam", "jadwal": "Ke Tidung 07.30–08.00 WIB. Kembali 14.30–15.00 WIB.", "langkah": ["Pesan jauh-jauh hari melalui agen travel atau operator speedboat online.", "Masuk melalui Pintu Gerbang Utama Ancol.", "Tiba di Dermaga 16/17 paling lambat pukul 07.00 WIB untuk konfirmasi manifes dan mengambil tiket fisik.", "Boarding pukul 07.30 WIB menuju Pulau Tidung."]}],
    },
    {
        "judul": "Via Pelabuhan Rawasaban, Tangerang",
        "label": "Alternatif Banten & Tangerang",
        "desk": "Pilihan praktis bagi Anda yang tinggal di Tangerang, Banten, atau sekitar Bandara Soekarno-Hatta.",
        "pilihan": [{"nama": "Kapal Motor Kayu / Speedboat Nelayan Lokal", "titik": "Pelabuhan Rawasaban, Cituis, Kabupaten Tangerang", "harga": "± Rp50.000–Rp70.000 / orang sekali jalan", "durasi": "1,5–2 jam", "jadwal": "07.30–08.30 WIB.", "langkah": ["Menuju Dermaga Cituis / Rawasaban di Pakuhaji dengan kendaraan pribadi atau transportasi online.", "Beli tiket penyeberangan langsung di tempat.", "Boarding ke kapal motor nelayan menuju pelabuhan rakyat Pulau Tidung."]}],
    },
]

ACCESS_COMPARISON = [
    ("Kali Adem", "Kapal Kayu", "Rp85.000–Rp100.000", "2,5–3 jam", "Paling murah, pengalaman tradisional"),
    ("Kali Adem", "Kapal Dishub", "Rp54.000–Rp75.000", "1,5–2 jam", "Ekonomis, ber-AC, jadwal teratur"),
    ("Marina Ancol", "Speedboat AC", "± Rp215.000", "1–1,5 jam", "Cepat, nyaman, ber-AC"),
    ("Rawasaban", "Kapal Kayu / Motor", "Rp50.000–Rp70.000", "1,5–2 jam", "Akses praktis dari Tangerang/Banten"),
]

ACCESS_TIPS = [
    "Tiba di pelabuhan minimal 1 jam sebelum jadwal keberangkatan.",
    "Parkir inap tersedia di Kali Adem dan Marina Ancol, sekitar Rp25.000/hari untuk motor dan Rp45.000/hari untuk mobil.",
]