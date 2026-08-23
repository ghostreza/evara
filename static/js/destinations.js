const mapData = window.evaraMapData;
const map = L.map("destinationMap", { scrollWheelZoom: false }).setView(
  [mapData.home_port.lat, mapData.home_port.lng], 12
);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

const markers = [];
const markerLayer = L.layerGroup().addTo(map);
const spotCards = [...document.querySelectorAll(".spot-card")];
const spotCount = document.getElementById("spotCount");

const portIcon = L.divIcon({ className: "port-marker", html: "<span>⌂</span>", iconSize: [30, 30], iconAnchor: [15, 15] });
L.marker([mapData.home_port.lat, mapData.home_port.lng], { icon: portIcon })
  .addTo(map).bindPopup(`<strong>${mapData.home_port.nama}</strong><br>Titik keberangkatan Evara`);

mapData.rings.forEach((ring) => {
  L.circle([mapData.home_port.lat, mapData.home_port.lng], {
    radius: ring.radius, color: ring.nama === "Ring 1" ? "#C9A227" : "#1F4E79",
    fillColor: ring.nama === "Ring 1" ? "#C9A227" : "#1F4E79", fillOpacity: .035, weight: 1, dashArray: "5 7"
  }).addTo(map).bindTooltip(`${ring.nama} · ${ring.label}`, { sticky: true });
});

mapData.spots.forEach((spot, index) => {
  const marker = L.circleMarker([spot.lat, spot.lng], {
    radius: 7, color: "#FFFFFF", weight: 2, fillColor: spot.kategori === "Diving" ? "#1F4E79" : spot.kategori === "Fishing" ? "#C97835" : "#2B9A91", fillOpacity: 1
  }).bindPopup(`<strong>${spot.nama}</strong><br>${spot.kategori} · ${spot.jarak}<br>${spot.desk}`);
  marker.on("click", () => selectSpot(index, false));
  marker.addTo(markerLayer);
  markers.push(marker);
});

function selectSpot(index, pan = true) {
  const spot = mapData.spots[index];
  spotCards.forEach((card, cardIndex) => card.classList.toggle("selected", cardIndex === index));
  markers.forEach((marker, markerIndex) => marker.setStyle({ radius: markerIndex === index ? 10 : 7 }));
  if (pan) map.flyTo([spot.lat, spot.lng], 14, { duration: .7 });
  markers[index].openPopup();
}

function applyFilter(filter) {
  let visible = 0;
  spotCards.forEach((card, index) => {
    const show = filter === "all" || card.dataset.ring === filter || card.dataset.category === filter;
    card.classList.toggle("hidden", !show);
    markers[index].setStyle({ opacity: show ? 1 : 0, fillOpacity: show ? 1 : 0 });
    if (show) visible += 1;
  });
  spotCount.textContent = `${visible} lokasi laut`;
}

document.querySelectorAll(".filter-btn").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll(".filter-btn").forEach((item) => item.classList.remove("active"));
  button.classList.add("active");
  applyFilter(button.dataset.filter);
}));

spotCards.forEach((card, index) => card.querySelector(".spot-link").addEventListener("click", () => selectSpot(index)));