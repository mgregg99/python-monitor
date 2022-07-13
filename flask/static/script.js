

// Adding the Counters to the bar

// Displaying the Graph

const data = {
labels: [
'Up',
'Down'
],
datasets: [{
label: 'My First Dataset',
data: [upnum, downnum],
backgroundColor: [
  'rgb(75, 255, 192)',
  'rgb(255, 99, 132)'
],
hoverOffset: 10
}]
};

const config = {
  type: 'doughnut',
  data: data,
  options: {}
};

const myChart = new Chart(document.getElementById('myChart'), config);