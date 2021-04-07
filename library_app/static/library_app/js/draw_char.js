$(document).ready(function() {
    // char
    let ticksStyle = {fontColor: '#495057', fontStyle: 'bold'};

    let mode = 'index', intersect = true, $salesChart = $('#sales-chart')

    let salesChart = new Chart($salesChart, {
        type: 'bar',
        data: {
            labels: ['Earning details',],
            datasets: [
                {
                    backgroundColor: '#007bff',
                    borderColor: '#eeeeee',
                    data: ['50',]
                }, {
                    backgroundColor: '#ced4da',
                    borderColor: '#ced4da',
                    data: ['30',]
                }
            ]
        },

        options: {
            maintainAspectRatio: false,
            tooltips: {
                mode: mode,
                intersect: intersect
            },
            hover: {
                mode: mode,
                intersect: intersect
            },
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    // display: false,
                    gridLines: {
                        display: true,
                        lineWidth: '4px',
                        color: 'rgba(0, 0, 0, .2)',
                        zeroLineColor: 'transparent'
                    },
                    ticks: $.extend({
                        beginAtZero: true,

                        // Include a dollar sign in the ticks
                        callback: function (value, index, values) {
                            if (value >= 1000) {
                                value /= 1000
                                value += 'k'
                            }
                            return '$' + value
                        }
                    }, ticksStyle)
                }],
                xAxes: [{
                    display: true,
                    gridLines: {
                        display: false
                    },
                    ticks: ticksStyle
                }]
            }
        }
    });

    let pieChart = document.getElementById('visitors-chart').getContext('2d')

    let myPieChart = new Chart(pieChart, {
        type: 'pie',
        data: {
            datasets: [{
                data: ['35', '25', '40'],
                backgroundColor: ["#27c100", "#f3545d", "#fdaf4b"],
                borderWidth: 10,

            }],
            labels: ['Available', 'Sold', 'Rented']
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                position: 'bottom',
                labels: {
                    fontColor: '#000',
                    fontSize: 15,
                    usePointStyle: true,
                    padding: 20
                }
            },
            pieceLabel: {
                render: 'percentage',
                fontColor: 'white',
                fontSize: 14,
            },


        }
    })
})