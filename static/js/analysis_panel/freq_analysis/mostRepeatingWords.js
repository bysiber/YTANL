export function createMostActiveAuthorsPanel() {
    let rightPanel = document.querySelector('.right-panel');
    const mostActiveAuthorsDiv = document.createElement('div');
    mostActiveAuthorsDiv.classList.add('authors-panel', 'draggable');
    mostActiveAuthorsDiv.id = 'mostActiveAuthors';
    mostActiveAuthorsDiv.innerHTML = `
        <div class="panel-header">
            <h2>Most Active Authors</h2>
            <button class="close-btn">X</button>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Author</th>
                    <th>Count</th>
                </tr>
            </thead>
            <tbody><!-- Most active authors will be displayed here --></tbody>
        </table>
    `;
    rightPanel.appendChild(mostActiveAuthorsDiv);

    // Kapatma butonuna tıklanınca kutuyu gizle
    const closeButton = mostActiveAuthorsDiv.querySelector('.close-btn');
    closeButton.addEventListener('click', () => {
        mostActiveAuthorsDiv.style.display = 'none';
    });
}

function createAuthorChart(labels, data) {
    const chartCanvas = document.createElement('canvas');
    chartCanvas.id = 'authorChart';

    const rightPanel = document.querySelector('.right-panel');
    rightPanel.insertBefore(chartCanvas, rightPanel.firstChild);

    const ctx = chartCanvas.getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Time Spent',
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}


export function showMostRepeatingWordsPanel(authorsData) {
    console.log(authorsData);
    let mostActiveAuthorsDiv = document.getElementById('mostActiveAuthors');
    if (!mostActiveAuthorsDiv) {
        createMostActiveAuthorsPanel();
        mostActiveAuthorsDiv = document.getElementById('mostActiveAuthors');
    }

    let html = '<h2>Most Repating Words</h2><ul>';
    for (const word in authorsData) {

        const freq = authorsData[word]
        html += `<li>${word}: ${freq}</li>`;
    }
    html += '</ul>';
    mostActiveAuthorsDiv.innerHTML = html;
    mostActiveAuthorsDiv.style.display = 'block';

    const labels = Object.keys(authorsData);
    const data = labels.map(word => {
        const freq = authorsData[word];
        return freq;
    });

    createAuthorChart(labels, data);
}