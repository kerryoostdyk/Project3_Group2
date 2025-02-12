// Use D3 to select the table

// Use D3 to create a bootstrap striped table
// https://getbootstrap.com/docs/5.3/content/tables/#striped-rows

// Use D3 to select the table body

// BONUS: Dynamic table
// Loop through an array of grades and build the entire table body from scratch

// Use D3 to select the table
let table = d3.select("#UFO_table");
let tbody = table.select("tbody");

// Make Table Interactive
let dt_table = new DataTable('#UFO_table');

// Event Listener
d3.select("#filter-btn").on("click", function () {
  doWork();
});

// On Page Load
doWork();

// Helper Functions
function doWork() {
  // Fetch the JSON data and console log it

  // get value
  let min_year = d3.select("#min-year").property("value"); // user input
  let url1 = `/api/v1.0/bar_data/${min_year}`;
  let url2 = `/api/v1.0/table_data/${min_year}`

  // Make Request
  d3.json(url1).then(function (data) {
    // Make Plot
    makeBarPlot(data);
  });

  d3.json(url2).then(function (data) {
    // Make Table
    makeTable(data);
  });
}


function makeTable(data) {
  // Clear Table
  tbody.html("");
  dt_table.clear().destroy();

  // Create Table
  for (let i = 0; i < data.length; i++) {
    let row = data[i];

    // Create Table Row
    let table_row = tbody.append("tr");

    // Append Cells
    table_row.append("td").text(row.Year);
    table_row.append("td").text(row.Season);
    table_row.append("td").text(row.Country);
    table_row.append("td").text(row.Region);
    table_row.append("td").text(row.UFO_shape);
    table_row.append("td").text(row.Estimated_Encounter_Duration_Minutes);
  }

  // Make Table Interactive (again)
  dt_table = new DataTable('#UFO_table', {
    order: [[0, 'desc']] // Sort by column 1 desc
  });
}


function makeBarPlot(data) {
  // Create Trace
  let trace = {
    x: data.map(row => row.UFO_shape),
    y: data.map(row => row.num_UFO),
    type: 'bar',
    marker: {
      color: 'green'
    }
  }

  // Data trace array
  let traces = [trace];

  // Apply a title to the layout
  let layout = {
    title: {
      text: `UFO Sightings by Year`
    },
    yaxis: {
      title: {
        text: 'Number of UFO Sightings'
      }
    },
    xaxis: {
      title: {
        text: 'UFO Shape'
      }
    },
    height: 600
  }

  // Render the plot to the div tag with id "plot"
  Plotly.newPlot('plot', traces, layout);
}
