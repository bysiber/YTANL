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
                label: 'Message Count',
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


export function showMostActiveAuthorsPanel(authorsData) {
    let mostActiveAuthorsDiv = document.getElementById('mostActiveAuthors');
    if (!mostActiveAuthorsDiv) {
        createMostActiveAuthorsPanel();
        mostActiveAuthorsDiv = document.getElementById('mostActiveAuthors');
    }

    const sortedAuthors = Object.entries(authorsData).sort(([, countA], [, countB]) => countB - countA);

    let html = '<h2>Most Active Authors</h2><ul>';
    for (const [author, count] of sortedAuthors) {
        html += `<li>${author}: ${count}</li>`;
    }
    html += '</ul>';
    mostActiveAuthorsDiv.innerHTML = html;
    mostActiveAuthorsDiv.style.display = 'block';

    const labels = sortedAuthors.map(([author]) => author);
    const data = sortedAuthors.map(([, count]) => count);

    createAuthorChart(labels, data);
}