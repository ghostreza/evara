// booking.js — estimasi biaya + susun pesan → wa.me / mailto
const form = document.getElementById("bookingForm");
const isEnglish = form.dataset.lang === "en";
const fmtIDR = new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", maximumFractionDigits: 0 });

// batas tanggal minimal = hari ini
const tgl = document.getElementById("tanggal");
tgl.min = new Date().toISOString().split("T")[0];

function updateSnorkelingAddon() {
  const selectedPackage = form.paket.value || "";
  const isSnorkeling = selectedPackage.toLowerCase().includes("snorkeling");
  const addonGroup = document.getElementById("addonGroup");
  const tourGuide = document.getElementById("tourGuide");

  addonGroup.hidden = !isSnorkeling;
  if (!isSnorkeling) {
    tourGuide.checked = false;
  }

  const paxInput = document.getElementById("pax");
  if (isSnorkeling) {
    paxInput.min = 3;
    paxInput.max = 6;
    if ((+paxInput.value || 0) < 3) paxInput.value = 3;
    if ((+paxInput.value || 0) > 6) paxInput.value = 6;
  } else {
    paxInput.min = 1;
    paxInput.max = 12;
  }
}

// estimasi live
function hitungEstimasi() {
  const opt = form.paket.selectedOptions[0];
  if (opt.dataset.byRequest === "true") {
    document.getElementById("estimate").textContent = isEnglish ? "Contact crew" : "Hubungi kru";
    return 0;
  }

  const pax = +form.pax.value || 0;
  const tiers = JSON.parse(opt.dataset.priceTiers || "[]");
  const tier = tiers.find((item) => pax >= item.min && pax <= item.max);
  const unitPrice = tier?.harga || +opt.dataset.harga || 0;
  let total = tier?.unit === "/ trip" ? unitPrice : unitPrice * pax;

  if (form.paket.value.toLowerCase().includes("snorkeling") && document.getElementById("tourGuide").checked) {
    total += 100000;
  }

  document.getElementById("estimate").textContent = fmtIDR.format(total);
  return total;
}
form.paket.addEventListener("change", () => {
  updateSnorkelingAddon();
  hitungEstimasi();
});
form.pax.addEventListener("input", () => {
  updateSnorkelingAddon();
  hitungEstimasi();
});
document.getElementById("tourGuide").addEventListener("change", hitungEstimasi);
updateSnorkelingAddon();
hitungEstimasi();

// label tombol mengikuti kanal
form.querySelectorAll("[name=kanal]").forEach((r) =>
  r.addEventListener("change", () => {
    document.getElementById("submitBtn").textContent =
      form.kanal.value === "whatsapp"
        ? (isEnglish ? "Send via WhatsApp" : "Kirim via WhatsApp")
        : (isEnglish ? "Send via Email" : "Kirim via Email");
  })
);

function tanggalIndo(iso) {
  return new Date(iso + "T00:00:00").toLocaleDateString("id-ID",
    { weekday: "long", day: "numeric", month: "long", year: "numeric" });
}

form.addEventListener("submit", (e) => {
  e.preventDefault(); // submit event hanya fires jika valid (HTML5 validation)
  const total = hitungEstimasi();
  const extraText = form.paket.value.toLowerCase().includes("snorkeling") && document.getElementById("tourGuide").checked
    ? " + tour guide + camera man"
    : "";
  const pesan =
`Halo Evara! 👋 Saya ingin memesan:

Nama    : ${form.nama.value}
Tanggal : ${tanggalIndo(form.tanggal.value)}
Paket   : ${form.paket.value} (${form.pax.value} orang)${extraText}
Estimasi: ${fmtIDR.format(total)}
Catatan : ${form.catatan.value || "-"}

Mohon info ketersediaan jadwal. Terima kasih!`;

  const enc = encodeURIComponent(pesan);
  if (form.kanal.value === "whatsapp") {
    window.open(`https://wa.me/${form.dataset.wa}?text=${enc}`, "_blank", "noopener");
  } else {
    const subjek = encodeURIComponent(`Pemesanan Evara — ${form.nama.value} — ${tanggalIndo(form.tanggal.value)}`);
    location.href = `mailto:${form.dataset.email}?subject=${subjek}&body=${enc}`;
  }
});