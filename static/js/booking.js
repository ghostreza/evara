// booking.js — estimasi biaya + susun pesan → wa.me / mailto
const form = document.getElementById("bookingForm");
const isEnglish = form.dataset.lang === "en";
const fmtIDR = new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", maximumFractionDigits: 0 });

// batas tanggal minimal = hari ini
const tgl = document.getElementById("tanggal");
tgl.min = new Date().toISOString().split("T")[0];

// estimasi live
function hitungEstimasi() {
  const opt = form.paket.selectedOptions[0];
  if (opt.dataset.byRequest === "true") {
    document.getElementById("estimate").textContent = isEnglish ? "Contact crew" : "Hubungi kru";
    return 0;
  }
  const total = (+opt.dataset.harga || 0) * (+form.pax.value || 0);
  document.getElementById("estimate").textContent = fmtIDR.format(total);
  return total;
}
form.paket.addEventListener("change", hitungEstimasi);
form.pax.addEventListener("input", hitungEstimasi);
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
  const pesan =
`Halo Evara! 👋 Saya ingin memesan:

Nama    : ${form.nama.value}
Tanggal : ${tanggalIndo(form.tanggal.value)}
Paket   : ${form.paket.value} (${form.pax.value} orang)
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