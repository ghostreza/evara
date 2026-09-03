SITE = {
    "name": "Evara",
    "tagline": "Charter perahu untuk memancing, snorkeling, diving & island hopping",
    "slogan": "Blessings of the sea, Timeless memories",
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

STORY_SIGN = "— Joanita & Donald · Keluarga Evara"

STORY_MEDIA = [
    ("jo-trip.jpeg", "Evara menanti perjalanan baru", "Setiap trip dimulai dari semangat yang sama: kelautan, rasa aman, dan cerita yang hangat."),
    ("jo-snorkeling.jpeg", "Snorkeling bersama Evara", "Air jernih, terumbu hidup, dan momen santai di laut yang menenangkan."),
    ("Jo-fishing.jpeg", "Fishing trip di laut Tidung", "Dari pagi sampai siang, kami menyesuaikan jalur menangkap ikan dengan kondisi laut."),
    ("jo-diving.jpeg", "Diving akan dimulai 2027", "Layanan diving resmi akan mulai pada 2027, dengan jadwal dan harga akan diumumkan kemudian."),
    ("fish.jpeg", "Evara siap mengantar petualangan", "Perahu dan kru kami siap membawa Anda menjelajahi laut dengan aman dan nyaman."),
]

BOAT_INFO = {
    "nama": "KM Evara",
    "panjang": "12 m",
    "kapasitas": "6 penumpang",
    "fasilitas": [
        "Alat pancing & fighting chair",
        "Set snorkeling",
        "Cabin teduh & sun deck",
        "Cool box & air minum",
        "Life jacket & perlengkapan keselamatan lengkap",
    ],
}

SERVICES = [
    {
        "nama": "Pulau Air",
        "durasi": "Trip pulang pergi",
        "harga": 600000,
        "kategori": "Island Hopping",
        "harga_tiers": [{"harga": 600000, "unit": "/ trip", "label": "pulang pergi", "min": 1, "max": 6}],
        "desk": "Island hopping ke Pulau Air dengan trip pulang pergi."
    },
    {
        "nama": "Pulau Pramuka",
        "durasi": "Trip pulang pergi",
        "harga": 700000,
        "kategori": "Island Hopping",
        "harga_tiers": [{"harga": 700000, "unit": "/ trip", "label": "pulang pergi", "min": 1, "max": 6}],
        "desk": "Island hopping ke Pulau Pramuka dengan trip pulang pergi."
    },
    {
        "nama": "Pulau Payung",
        "durasi": "Trip pulang pergi",
        "harga": 350000,
        "kategori": "Island Hopping",
        "harga_tiers": [{"harga": 350000, "unit": "/ trip", "label": "pulang pergi", "min": 1, "max": 6}],
        "desk": "Island hopping ke Pulau Payung dengan trip pulang pergi."
    },
    {
        "nama": "Pulau Pari",
        "durasi": "Trip pulang pergi",
        "harga": 700000,
        "kategori": "Island Hopping",
        "harga_tiers": [{"harga": 700000, "unit": "/ trip", "label": "pulang pergi", "min": 1, "max": 6}],
        "desk": "Island hopping ke Pulau Pari dengan trip pulang pergi."
    },
    {
        "nama": "Pulau Gosong Patrick",
        "durasi": "Trip pulang pergi",
        "harga": 600000,
        "kategori": "Island Hopping",
        "harga_tiers": [{"harga": 600000, "unit": "/ trip", "label": "pulang pergi", "min": 1, "max": 6}],
        "desk": "Island hopping ke Pulau Gosong Patrick dengan trip pulang pergi."
    },
    {"nama": "Snorkeling 1,5 Jam (Spot)", "durasi": "Maks. 1,5 jam di satu spot", "harga": 250000, "kategori": "Snorkeling",
    "harga_tiers": [{"harga": 250000, "unit": "/ orang", "label": "min 3 — maks 6 orang", "min": 3, "max": 6}],
     "desk": "Minimal 3 orang dan maksimal 6 orang. Tambahan tour guide + Photo & Video: Rp200.000 per trip."},
    {"nama": "Fishing Trip", "durasi": "Full day (8 jam)", "harga": 250000, "kategori": "Fishing",
    "harga_tiers": [{"harga": 250000, "unit": "/ orang", "label": "5–6 orang", "min": 5, "max": 6}, {"harga": 300000, "unit": "/ orang", "label": "3–4 orang", "min": 3, "max": 4}, {"harga": 500000, "unit": "/ orang", "label": "1–2 orang", "min": 1, "max": 2}],
     "desk": "Trip memancing di spot pilihan kru, cocok untuk pemula hingga pemancing serius."},
    {"nama": "Diving Trip", "durasi": "Mulai 2027", "harga": None, "kategori": "Diving",
    "harga_tiers": [],
     "desk": "Layanan diving akan mulai pada 2027. Harga dan jadwal akan diinformasikan saat layanan resmi dibuka."},
    {"nama": "Property Recovery", "durasi": "Sesuai kebutuhan", "harga": None, "kategori": "Other",
     "desk": "Layanan pencarian dan pengambilan barang yang hilang di laut hingga kedalaman 100 meter, subject to weather and sea conditions."},
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
     "lat": -5.8032, "lng": 106.5238, "image": "Pulau_Tidung_Kecil_1.jpg",
     "images": ["Pulau_Tidung_Kecil_1.jpg", "Pulau_Tidung_Kecil_2.png", "tidung-kecil-1.jpg"]},
    {"nama": "Area Jembatan Cinta", "ring": 1, "kategori": "Snorkeling", "jarak": "0–3 km",
     "desk": "Menghubungkan Tidung Besar dan Tidung Kecil; transisi air dangkal–sedang. Populer untuk anemon laut dan clownfish.",
     "lat": -5.7984, "lng": 106.5192, "image": "jembatan-cinta-1.jpg",
     "images": ["jembatan-cinta-1.jpg", "Jembatan-Cinta-2.jpg", "dermaga-tidung-1.jpg"]},
    {"nama": "Tepi Karang Tidung Kecil", "ring": 1, "kategori": "Diving", "jarak": "0–3 km",
     "desk": "Drop-off terumbu kedalaman 10–18 m; cocok untuk fun dive dan pemula Open Water.",
     "lat": -5.8060, "lng": 106.5300, "image": "293516c9-66bb-40df-8ea1-08a505bb1a4e.jpeg",
     "images": ["293516c9-66bb-40df-8ea1-08a505bb1a4e.jpeg", "IMG-20250405-WA0001.jpg", "evara-boat-beach.jpeg"]},
    {"nama": "Dermaga / Jembatan Cinta", "ring": 1, "kategori": "Fishing", "jarak": "0–3 km",
     "desk": "Dasaran santai dari struktur jembatan/dermaga. Target: ikan karang kecil, kerong-kerong, dan cumi di malam hari.",
     "lat": -5.7994, "lng": 106.5178, "image": "dermaga-tidung-1.jpg",
     "images": ["dermaga-tidung-1.jpg", "dermaga-tidung-2.jpeg", "WhatsApp Image 2026-08-13 at 11.37.28.jpeg"]},
    {"nama": "Pulau Air", "ring": 2, "kategori": "Island Hopping", "jarak": "± 3–6 km Utara",
     "desk": "Pulau indah dengan air tenang dan rataan karang cantik; pilihan favorit untuk island hopping pagi hari.",
     "lat": -5.7628, "lng": 106.5925, "image": "Pulau-Air-1.jpg",
     "images": ["Pulau-Air-1.jpg", "Pulau-Air-2.jpg"]},
    {"nama": "Pulau Pramuka", "ring": 2, "kategori": "Island Hopping", "jarak": "± 4–7 km Timur Laut",
     "desk": "Pulau dengan panorama pantai dan aktivitas santai, cocok untuk family trip dan sunset time.",
     "lat": -5.7447, "lng": 106.6150, "image": "pulau-pramuka.jpg",
     "images": ["pulau-pramuka.jpg", "prmauka-1.jpeg", "pramuka-2.jpeg"]},
    {"nama": "Pulau Payung (Payung Besar)", "ring": 2, "kategori": "Island Hopping", "jarak": "± 3–6 km Tenggara",
     "desk": "Rataan karang dangkal jernih, terlindung dari arus kencang, dengan banyak ikan sersan mayor.",
     "lat": -5.8236, "lng": 106.5544, "image": "pulau-payung-besar-1.jpg",
     "images": ["pulau-payung-besar-1.jpg", "pulau-payung-1.jpeg"]},
    {"nama": "Pulau Pari", "ring": 2, "kategori": "Island Hopping", "jarak": "± 10–12 km Timur",
     "desk": "Pulau dengan pesisir berpasir dan jalur berlayar yang nyaman untuk quick island hopping.",
     "lat": -5.8596, "lng": 106.6167, "image": "pulau-pari-1.jpg",
     "images": ["pulau-pari-1.jpg", "pulau-pari-2.jpg"]},
    {"nama": "Pulau Gosong Patrick", "ring": 2, "kategori": "Island Hopping", "jarak": "± 4–7 km Timur Laut",
     "desk": "Pulau gosong dengan warna air jernih dan spot snorkeling terkesan eksotis serta santai.",
     "lat": -5.7958, "lng": 106.6025, "image": "pulau-gosong-patrick-1.jpg",
     "images": ["pulau-gosong-patrick-1.jpg", "Pulau-gosong-2.jpg"]},
    {"nama": "Pulau Payung", "ring": 2, "kategori": "Snorkeling", "jarak": "± 3–6 km Tenggara",
     "desk": "Rataan karang dangkal jernih (acropora), terlindung dari arus kencang. Banyak ikan sersan mayor.",
     "lat": -5.8190, "lng": 106.5500, "image": "pulau-payung-besar-1.jpg",
     "images": ["pulau-payung-besar-1.jpg", "pulau-payung-1.jpeg"]},
    {"nama": "Gusong Karang Beras", "ring": 2, "kategori": "Snorkeling", "jarak": "± 7–9 km Timur",
     "desk": "Gosong karang di tengah laut dengan visibilitas sangat jernih; dominan karang lunak.",
     "lat": -5.7712, "lng": 106.5700, "image": "karang-beras.jpeg",
     "images": ["karang-beras.jpeg", "karang-beras-2.jpg", "karang-beras-deep.jpg"]},
    {"nama": "Pulau Tikus", "ring": 2, "kategori": "Snorkeling", "jarak": "± 10–12 km Timur",
     "desk": "Pulau tak berpenghuni dengan pantai dangkal dan rataan karang yang sangat tenang.",
     "lat": -5.8563, "lng": 106.5866, "image": "pulau-tikus-1.jpg",
     "images": ["pulau-tikus-1.jpg", "pulau-tikus-2.jpg"]},
    {"nama": "Diving Wall Pulau Payung", "ring": 2, "kategori": "Diving", "jarak": "± 5–7 km Tenggara",
     "desk": "Wall dive 18–25 m; arus sedang–kencang. Kipas laut besar, penyu, dan ikan pelagis.",
     "lat": -5.8220, "lng": 106.5550, "image": "diving-wall-1.jpg",
     "images": ["diving-wall-1.jpg", "diving-wall-2.jpg"]},
    {"nama": "Gusong Karang Beras Deep", "ring": 2, "kategori": "Diving", "jarak": "± 8–10 km Timur",
     "desk": "Kedalaman 12–20 m dengan karang keras padat; jalur kuwe (GT) dan barakuda.",
     "lat": -5.7700, "lng": 106.5800, "image": "karang-beras-deep.jpg",
     "images": ["karang-beras-deep.jpg", "karang-beras-2.jpg"]},
    {"nama": "Karang Badongan & Karang Puret", "ring": 2, "kategori": "Fishing", "jarak": "± 5–8 km Barat/BD",
     "desk": "Karang dalam dan rumpon tengah laut. Favorit bottom fishing & jigging: kerapu, kakap merah, lencam.",
     "lat": -5.8150, "lng": 106.4500, "image": "karang-bedongan.jpg",
     "images": ["karang-bedongan.jpg", "karang-puret.jpg"]},
    {"nama": "Koridor Laut Pulau Pari", "ring": 2, "kategori": "Fishing", "jarak": "± 10–12 km Timur",
     "desk": "Perairan dalam jalur pelagis untuk trolling. Target: tenggiri, tongkol, cakalang.",
     "lat": -5.8572, "lng": 106.6197, "image": "koridor-pulau-pari-1.jpg",
     "images": ["koridor-pulau-pari-1.jpg", "koridor-pulau-pari-2.jpg"]},
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
        "judul": "Via Pelabuhan Sunda Kelapa",
        "label": "Opsi cepat & nyaman",
        "desk": "Cocok untuk keluarga, anak kecil, dan perjalanan yang mengutamakan kenyamanan.",
        "pilihan": [{"nama": "Speedboat Fiber ber-AC", "titik": "Pelabuhan Sunda Kelapa, Jakarta Utara", "harga": "Mulai dari Rp175.000 / orang sekali jalan", "durasi": "Sekitar 2 jam", "jadwal": "Ke Tidung 07.30–08.00 WIB. Kembali 14.30–15.00 WIB.", "langkah": ["Pesan jauh-jauh hari melalui agen travel atau operator speedboat.", "Tiba di Pelabuhan Sunda Kelapa paling lambat pukul 07.00 WIB.", "Konfirmasi manifes dan ambil tiket sebelum boarding.", "Ikuti briefing lalu berlayar menuju Pulau Tidung."]}],
    },
    {
        "judul": "Via Pelabuhan Cituis, Tangerang",
        "label": "Alternatif Banten & Tangerang",
        "desk": "Pilihan praktis bagi Anda yang tinggal di Tangerang, Banten, atau sekitar Bandara Soekarno-Hatta.",
        "pilihan": [{"nama": "Kapal Motor Kayu / Speedboat Nelayan Lokal", "titik": "Pelabuhan Cituis, Kabupaten Tangerang", "harga": "± Rp50.000–Rp70.000 / orang sekali jalan", "durasi": "1,5–2 jam", "jadwal": "07.30–08.30 WIB.", "langkah": ["Menuju Dermaga Cituis di Pakuhaji dengan kendaraan pribadi atau transportasi online.", "Beli tiket penyeberangan langsung di tempat.", "Boarding ke kapal motor nelayan menuju pelabuhan rakyat Pulau Tidung."]}],
    },
]

ACCESS_COMPARISON = [
    ("Kali Adem", "Kapal Kayu", "Rp85.000–Rp100.000", "2,5–3 jam", "Paling murah, pengalaman tradisional"),
    ("Kali Adem", "Kapal Dishub", "Rp54.000–Rp75.000", "1,5–2 jam", "Ekonomis, ber-AC, jadwal teratur"),
    ("Sunda Kelapa", "Speedboat AC", "Mulai dari Rp175.000", "Sekitar 2 jam", "Cepat, nyaman, ber-AC"),
    ("Cituis", "Kapal Kayu / Motor", "Rp50.000–Rp70.000", "1,5–2 jam", "Akses praktis dari Tangerang/Banten"),
]

ACCESS_TIPS = [
    "Tiba di pelabuhan minimal 1 jam sebelum jadwal keberangkatan.",
    "Parkir inap tersedia di Kali Adem dan Pelabuhan Sunda Kelapa; tarif mengikuti ketentuan lokasi.",
]


def localized_content(lang):
    """Return the content dataset for the requested language."""
    if lang != "en":
        return {
            "site": SITE, "story": STORY, "story_sign": STORY_SIGN, "story_media": STORY_MEDIA,
            "boat": BOAT_INFO, "services": SERVICES, "destinations": DESTINATIONS,
            "home_port": HOME_PORT, "rings": RINGS, "spots": SPOTS, "access_steps": ACCESS_STEPS,
            "access_options": ACCESS_OPTIONS, "access_comparison": ACCESS_COMPARISON, "access_tips": ACCESS_TIPS,
        }

    boat = {**BOAT_INFO, "kapasitas": "6 passengers", "fasilitas": [
        "Fishing gear & fighting chair", "Snorkeling set", "Diving cylinder for certified divers",
        "Shaded cabin & sun deck", "Cool box & drinking water", "Life jackets & complete safety equipment",
    ]}
    story = [
        "Evara was not born in a shipyard - She was born from a promise. Donald and Joanita, a married couple bound not only by their wedding vows but also by a deep love for the sea: diving among reefs, casting lines at dawn, and reading the stars for navigation. To them, the sea was not a destination - it was home.",
        "As the highest expression of his love and appreciation, Donald gave Joanita a recreational fishing boat. Not merely a gift, but a reflection of the woman who is his life's companion. She named the boat Evara.",
        "Evara means 'Gift Of God' - just as Joanita was in Donald's eyes. From that day on, every dawn breaking over the waves, every line cast, and every dive into the blue sea became gratitude that could never be fully spoken.",
        "Today, that love is open to you. With Evara, we invite you to feel the same joy that brought this boat to life: the thrill of a strike at the end of the line, the silence among living reefs, and golden sunlight from the deck. A story that began with gratitude deserves to be shared.",
    ]
    story_media = [(image, title, caption) for image, title, caption in [
        ("jo-trip.jpeg", "Evara welcomes a new journey", "Every trip begins with the same spirit: the sea, comfort, and a warm story."),
        ("jo-snorkeling.jpeg", "Snorkeling with Evara", "Clear water, living reefs, and calm moments in the ocean."),
        ("Jo-fishing.jpeg", "Fishing trip in Tidung waters", "From dawn to noon, we tailor the route to the sea and fishing conditions."),
        ("jo-diving.jpeg", "Diving starts in 2027", "Diving operations will begin in 2027, with schedule and pricing announced later."),
        ("fish.jpeg", "Evara ready for adventure", "Our boat and crew are ready to take you safely across the sea."),
    ]]
    services = []
    for item in SERVICES:
        entry = {**item}
        if item["kategori"] == "Island Hopping":
            entry["durasi"] = "Round trip"
            entry["desk"] = f"Island hopping to {item['nama']} with round-trip service."
        elif item["kategori"] == "Snorkeling":
            entry["nama"] = "Snorkeling 1.5 Hours (Spot)"
            entry["durasi"] = "Max. 1.5 hours at one spot"
            entry["harga_tiers"] = [{"harga": 250000, "unit": "/ person", "label": "min 3 - max 6 people", "min": 3, "max": 6}]
            entry["desk"] = "Minimum 3 people and maximum 6 people. Add tour guide + Photo & Video: Rp200,000 per trip."
        elif item["kategori"] == "Fishing":
            entry["nama"] = "Fishing Trip"
            entry["durasi"] = "Full day (8 hours)"
            entry["harga_tiers"] = [{"harga": 250000, "unit": "/ person", "label": "5-6 guests", "min": 5, "max": 6}, {"harga": 300000, "unit": "/ person", "label": "3-4 guests", "min": 3, "max": 4}, {"harga": 500000, "unit": "/ person", "label": "1-2 guests", "min": 1, "max": 2}]
            entry["desk"] = "Fishing at the crew's selected spots, suitable for beginners and serious anglers."
        elif item["kategori"] == "Diving":
            entry["nama"] = "Diving Trip"
            entry["durasi"] = "Starts in 2027"
            entry["harga"] = None
            entry["harga_tiers"] = []
            entry["desk"] = "Diving service will begin in 2027. Pricing and schedule will be announced when operations officially start."
        elif item["kategori"] == "Other":
            entry["nama"] = "Property Recovery"
            entry["durasi"] = "As needed"
            entry["desk"] = "Search and recovery of items lost at sea, down to 100 meters, subject to weather and sea conditions."
        services.append(entry)

    destinations = [{**item, "desk": desk} for item, desk in zip(DESTINATIONS, [
        "A shallow reef chain with clear water, ideal for morning snorkeling.",
        "A favorite casting spot; sand emerges at low tide and is beautiful for photos.",
        "A wall dive with visibility up to 20 m, where turtles are often seen.",
        "A beginner-friendly reef dive and productive bottom-fishing spot.",
        "A shaded mangrove trail for families, ending with sunset on Evara's deck.",
    ])]
    spots = [{**item, "desk": desk} for item, desk in zip(SPOTS, [
        "Calm shallow waters rich in mangrove vegetation and edge reefs. Ideal for beginners and families.",
        "Connecting Big Tidung and Small Tidung; a shallow-to-medium water transition popular for sea anemones and clownfish.",
        "A 10-18 m reef drop-off, suitable for fun dives and Open Water beginners.",
        "An easy bottom-fishing area around the bridge and pier. Targets include small reef fish, sweetlips, and squid at night.",
        "Clear shallow acropora reef flats sheltered from strong currents, with many sergeant major fish.",
        "A mid-sea reef shoal with exceptionally clear visibility and mostly soft coral.",
        "An uninhabited island with shallow beaches and very calm reef flats.",
        "An 18-25 m wall dive with moderate to strong currents, sea fans, turtles, and pelagic fish.",
        "A 12-20 m site with dense hard coral, frequented by giant trevally and barracuda.",
        "Deep reefs and offshore fish aggregating devices, favored for bottom fishing and jigging.",
        "Deep pelagic waters for trolling, targeting Spanish mackerel, tuna, and skipjack.",
        "An uninhabited island with shallow beaches and calm reef flats, ideal for a relaxed snorkeling trip.",
        "An 18-25 m wall dive around Payung Island with moderate to strong currents, sea fans, turtles, and pelagic fish.",
        "A 12-20 m deep site with dense hard coral, where giant trevally and barracuda are often found.",
        "Deep reefs and offshore fish aggregating devices, favored for bottom fishing and jigging for grouper, snapper, and emperor fish.",
        "Deep waters along the Pulau Pari route for trolling, targeting Spanish mackerel, tuna, and skipjack.",
    ])]
    options = [
        {"judul": "Via Kali Adem / Muara Angke Port", "label": "Budget option", "desk": "A popular route for backpackers and budget groups.", "pilihan": [
            {"nama": "Traditional Wooden Boat / Motor Boat", "titik": "Kali Adem Pier, Muara Angke (North Jakarta)", "harga": "Approx. Rp85,000-Rp100,000 / person one way", "durasi": "2.5-3 hours", "jadwal": "To Tidung 07:00-07:30 WIB daily. Return 07:00-08:00 WIB (Mon-Sat), or 10:00 / 13:00 WIB (Sun/holidays).", "langkah": ["Arrive by 06:00 WIB; KRL to Jakarta Kota Station then Grab/Gojek to the port is recommended.", "Buy a ticket at the wooden boat counter or report to the travel coordinator for a package.", "Board at 07:00 WIB and choose a seat on the upper deck or in the cabin.", "The boat sails directly to Tidung Island Pier."]},
            {"nama": "Dishub Express Boat / JaketBoat", "titik": "Kali Adem Pier, Muara Angke", "harga": "Approx. Rp54,000-Rp75,000 / person one way", "durasi": "1.5-2 hours", "jadwal": "07:30-08:00 WIB.", "langkah": ["Book through the official JaketBoat app or official counter if seats are available.", "Arrive at 06:30 WIB for verification or e-ticket printing.", "Wait in the air-conditioned room and board when your number is called."]},
        ]},
        {"judul": "Via Sunda Kelapa Port", "label": "Fast & comfortable option", "desk": "Ideal for families, young children, and journeys prioritizing comfort.", "pilihan": [{"nama": "Air-conditioned Fiber Speedboat", "titik": "Sunda Kelapa Port, North Jakarta", "harga": "Starting from Rp175,000 / person one way", "durasi": "Around 2 hours", "jadwal": "To Tidung 07:30-08:00 WIB. Return 14:30-15:00 WIB.", "langkah": ["Book well in advance through a travel agent or speedboat operator.", "Arrive at Sunda Kelapa Port by 07:00 WIB.", "Confirm the manifest and collect your ticket before boarding.", "Follow the briefing and sail to Tidung Island."]}]},
        {"judul": "Via Cituis Port, Tangerang", "label": "Banten & Tangerang alternative", "desk": "A practical choice for guests living in Tangerang, Banten, or near Soekarno-Hatta Airport.", "pilihan": [{"nama": "Local Wooden Motor Boat / Fisherman's Speedboat", "titik": "Cituis Port, Tangerang Regency", "harga": "Approx. Rp50,000-Rp70,000 / person one way", "durasi": "1.5-2 hours", "jadwal": "07:30-08:30 WIB.", "langkah": ["Travel to Cituis Pier in Pakuhaji by private or online transport.", "Buy the crossing ticket directly at the port.", "Board the fishing boat to the public port at Tidung Island."]}]},
    ]
    return {"site": {**SITE, "tagline": "Boat charter for fishing, snorkeling, diving & island hopping"}, "story": story, "story_sign": "- Joanita & Donald · Evara Family", "story_media": story_media, "boat": boat, "services": services, "destinations": destinations, "home_port": {**HOME_PORT, "nama": "Tidung Island Pier"}, "rings": RINGS, "spots": spots, "access_steps": [("Fill in the booking form", "Send the form - your message will be neatly prepared for our WhatsApp/email."), ("Confirm & pay deposit", "We reply with schedule availability and total cost within 24 hours."), ("Meet at the pier", "Meeting point: Main Pier, 30 minutes before departure."), ("Briefing & set sail", "Safety briefing, equipment allocation, then Evara departs!")], "access_options": options, "access_comparison": [("Kali Adem", "Wooden Boat", "Rp85,000-Rp100,000", "2.5-3 hours", "Lowest cost, traditional experience"), ("Kali Adem", "Dishub Boat", "Rp54,000-Rp75,000", "1.5-2 hours", "Budget-friendly, air-conditioned, regular schedule"), ("Sunda Kelapa", "AC Speedboat", "Starting from Rp175,000", "Around 2 hours", "Fast, comfortable, air-conditioned"), ("Cituis", "Wooden / Motor Boat", "Rp50,000-Rp70,000", "1.5-2 hours", "Convenient access from Tangerang/Banten")], "access_tips": ["Arrive at the port at least 1 hour before departure.", "Overnight parking is available at Kali Adem and Sunda Kelapa; rates follow the port's regulations."]}