// let detectionChart; // global reference for reuse

// function startDetection() {
//     fetch("/start")
//         .then(response => response.json())
//         .then(data => {
//             const ctx = document.getElementById('blinkChart').getContext('2d');

//             // Destroy previous chart if exists
//             if (detectionChart) {
//                 detectionChart.destroy();
//             }

//             detectionChart = new Chart(ctx, {
//                 type: 'line',
//                 data: {
//                     labels: data.timestamps,
//                     datasets: [
//                         {
//                             label: 'Left',
//                             data: data.left,
//                             borderColor: 'blue',
//                             borderWidth: 2,
//                             tension: 0,
//                             pointRadius: 0,
//                             pointStyle: false,
//                             showLine: true
//                         },
//                         {
//                             label: 'Right',
//                             data: data.right,
//                             borderColor: 'orange',
//                             borderWidth: 2,
//                             tension: 0,
//                             pointRadius: 0,
//                             pointStyle: false,
//                             showLine: true
//                         }
//                     ]
//                 },
//                 options: {
//                     responsive: true,
//                     plugins: {
//                         legend: {
//                             display: true
//                         },
//                         annotation: {
//                             annotations: {
//                                 line1: {
//                                     type: 'line',
//                                     yMin: 0.5,
//                                     yMax: 0.5,
//                                     borderColor: 'gray',
//                                     borderWidth: 1,
//                                     borderDash: [6, 6]
//                                 },
//                                 region1: {
//                                     type: 'box',
//                                     xMin: 5,
//                                     xMax: 10,
//                                     backgroundColor: 'rgba(255, 99, 132, 0.2)'
//                                 },
//                                 region2: {
//                                     type: 'box',
//                                     xMin: 20,
//                                     xMax: 25,
//                                     backgroundColor: 'rgba(255, 99, 132, 0.2)'
//                                 }
//                             }
//                         }
//                     },
//                     scales: {
//                         x: {
//                             title: {
//                                 display: true,
//                                 text: 'Time (s)'
//                             }
//                         },
//                         y: {
//                             min: -2,
//                             max: 2,
//                             title: {
//                                 display: true,
//                                 text: 'Z-Score Blink Rate'
//                             }
//                         }
//                     }
//                 },
//                 plugins: [Chart.registry.getPlugin('annotation')]
//             });
//         });
// }
let detectionChart; // global reference for reuse

function startDetection() {
    fetch("/start")
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('blinkChart').getContext('2d');

            // Destroy previous chart if it exists
            if (detectionChart) {
                detectionChart.destroy();
            }

            detectionChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.timestamps,
                    datasets: [
                        {
                            label: 'Left',
                            data: data.left,
                            borderColor: 'blue',
                            borderWidth: 2,
                            tension: 0,
                            pointRadius: 0,
                            pointStyle: false,
                            showLine: true
                        },
                        {
                            label: 'Right',
                            data: data.right,
                            borderColor: 'orange',
                            borderWidth: 2,
                            tension: 0,
                            pointRadius: 0,
                            pointStyle: false,
                            showLine: true
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: true
                        },
                        annotation: {
                            annotations: {
                                line1: {
                                    type: 'line',
                                    yMin: 0.5,
                                    yMax: 0.5,
                                    borderColor: 'gray',
                                    borderWidth: 1,
                                    borderDash: [6, 6]
                                },
                                region1: {
                                    type: 'box',
                                    xMin: 5,
                                    xMax: 10,
                                    backgroundColor: 'rgba(255, 99, 132, 0.2)'
                                },
                                region2: {
                                    type: 'box',
                                    xMin: 20,
                                    xMax: 25,
                                    backgroundColor: 'rgba(255, 99, 132, 0.2)'
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Time (s)'
                            }
                        },
                        y: {
                            min: 0,
                            max: 50,
                            stepSize: 1,
                            title: {
                                display: true,
                                text: 'Blink Frequency'
                            },
                            ticks: {
                                stepSize: 5
                            }
                        }
                    }
                },
                plugins: [Chart.registry.getPlugin('annotation')]
            });
        });
}
