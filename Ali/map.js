function createMap(min_year) {
  let map_container = d3.select('#map_container');
  map_container.html("");
  map_container.append('div').attr('id', 'map');

  let street = L.titleLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

  let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });
  

  let url = `/api/v1.0/map_data/${min_year}`;
  console.log(url);

  d3.json(url).then(function (data) {

    console.log(data);

    let heatArray = [];

    let markers = L.markerClusterGroup();

    for (let i = 0; i < data.length; i++){
      let row = data[i];

      let marker = L.marker([row.latitude, row.longitude]).bindPopup(`<h1>${row.year}</h1><h2>${row.UFO_shape}</h2>`);
      markers.addLayer(marker);

      heatArray.push([row.latitude, row.longitude]);

      let heatLayer = L.heatLayer(heatArray, {
        radius: 25,
        blur: 10
      })
    }});

    let baseMaps = {
      Street: street,
      Topography: topo
    };

    let overlayMaps = {
      Sightings: markers,
      HeatMap: heatLayer 
    };

    let myMap = L.map("map", {
      center: [40.7128, -74.0059],
      zoom: 7,
      layers: [street, markers]
    });

    L.control.layers(baseMaps, overlayMaps).addTo(myMap);

  };
     
function init() {
  let min_year = d3.select("#min_year").property("value");
  createMap(min_year);
}

d3.select("filter-btn").on("click", function () {
  init();
});

init();