// Reading in the JSON File
const obj = JSON.parse(incoming)
const nameobj = JSON.parse(nameList)
var upnum = 0
var downnum = 0

for (var key in obj) {
    if (obj.hasOwnProperty(key)) {
        console.log(key + " -> " + obj[key]);
        if (obj[key] == 1){
            upnum++
        }
        else{
            downnum++
        }
    }
}
console.log(upnum)
console.log(downnum)

// Adding the Counters to the bar

document.getElementById("upnum").innerHTML = "Up: " + upnum
document.getElementById("downnum").innerHTML = "Down: " + downnum

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


// Listing the monitors that are down
var interval = 0
var htmladd1 = ""

for (var key in obj) {
    if (obj.hasOwnProperty(key)) {
        if (obj[key] == 0){
            htmladd1 += "<li class='downlist'> &#128308; <a href='http://ut.ls.byu.edu/dashboard/" + nameobj[key] + "' target='_blank'>" + key + "</a></li>" 
        }
    }
}

document.getElementById("col1").innerHTML = htmladd1