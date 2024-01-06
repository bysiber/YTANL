let PrevChatData = [];
let scrapeFinished = false;
function getVideoIdAndEmbed(videoURL){
    const youtubeURL = videoURL;

    // Extracting videoId using split method
    const videoId = youtubeURL.split('v=')[1];

    // If there's additional parameters after videoId, remove them (if any)
    const ampersandPosition = videoId.indexOf('&');
    if (ampersandPosition !== -1) {
        videoId = videoId.substring(0, ampersandPosition);
    }

    // Create the embedded URL
    const embeddedURL = `https://www.youtube.com/embed/${videoId}`;

    return embeddedURL; // Log the embedded URL
}

function convertTimestampToSeconds(timestamp) {
    let parts = timestamp.split(':');
    let seconds = 0;

    if (parts.length === 3) {
        seconds = (+parts[0]) * 60 * 60 + (+parts[1]) * 60 + (+parts[2]);
    } else if (parts.length === 2) {
        seconds = (+parts[0]) * 60 + (+parts[1]);
    }

    // Eğer sonuç bir sayı değilse, 0 döndür
    return isNaN(seconds) ? 0 : seconds;
}

// JSON verisini düzenli bir HTML formatına dönüştürme
function formatJSON(jsonData) {
    let formattedHTML = '';
    jsonData.forEach((item, index) => {
        formattedHTML += `<div class="message-box">`;
        formattedHTML += `<div class="message-summary">`;
        formattedHTML += `<strong>${item.occurence_timestamp} - Yazan Kişi: ${item.author}</strong>`;
        formattedHTML += `<p><strong>Mesaj:</strong> ${item.content.message}</p>`;
        formattedHTML += `<button class="message-skip-button" data-timestamp="${item.occurence_timestamp}">Skip to Time</button>`;
        formattedHTML += `<button class="message-expand-button" data-index="${index}">Expand</button>`;
        formattedHTML += `</div>`;
        formattedHTML += `<div class="message-content" style="display: none;">`;
        //formattedHTML += `<p><strong>Full Content:</strong></p>`;
        formattedHTML += `<p><strong>Time:</strong> ${item.occurence_timestamp}</p>`;
        formattedHTML += `<p><strong>Author:</strong> ${item.author}</p>`;
        formattedHTML += `<p><strong>Content:</strong> ${JSON.stringify(item.content)}</p>`;
        formattedHTML += `</div></div>`;
    });
    return formattedHTML;
}

function getChatData() {
    scrapeFinished = false;
    const videoLink = document.getElementById('videoLinkInput').value;
    document.getElementById("iframeVideo").src = getVideoIdAndEmbed(videoLink);
    
    // Burada fetch API'si kullanarak backend'e istek yapılabilir
    fetch('/main/scrape_live_chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ videoLink: videoLink })
    })
    pollData();
}



function pollData() {
    fetch('/main/get_live_chat') // Endpoint'inizi buraya ekleyin
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Verileri kullanarak sayfayı güncelle
        const formattedData = formatJSON(data);
        document.getElementById('chatMessages').innerHTML = formattedData;

        /*const chatMessages = document.getElementById('chatMessages');
        // Chat mesajları burada data ile güncellenebilir
        // Örnek olarak:
        chatMessages.innerHTML = JSON.stringify(data, null, 2);*/
    })
    .catch(error => {
        console.error('Error:', error);
    })
    .finally(() => {
        // Belirli bir süre sonra tekrar anket yap
        //if the data len > 1 we can stop the time out
        data = document.getElementById('chatMessages').innerHTML;
        if (data.length > 1  && PrevChatData != data) {
            console.log("data geldi");
            PrevChatData = data;
            scrapeFinished = true;
            return;
        }
        else{
            if (scrapeFinished){
                return;
            }
            else{
                setTimeout(pollData, 1000); // 10 saniye sonra tekrar anket yapılacak
            }
            
            
        }
        
    });
}




// Örnek JSON verisini daha düzenli HTML'e dönüştürüp sayfada gösterme




document.addEventListener("DOMContentLoaded", function() {
    const chatMessages = document.getElementById('chatMessages');
    
    chatMessages.addEventListener('click', function(e) {
        if (e.target && e.target.classList.contains('message-expand-button')) {
            const index = e.target.getAttribute('data-index');
            const messageContent = chatMessages.querySelectorAll('.message-content')[index];
            if (messageContent.style.display === 'none') {
                messageContent.style.display = 'block';
            } else {
                messageContent.style.display = 'none';
            }
        } else if (e.target && e.target.classList.contains('message-skip-button')) {
            const timestamp = e.target.getAttribute('data-timestamp');
            const videoTime = convertTimestampToSeconds(timestamp); // Bu fonksiyonu tanımlamanız gerekiyor
            var iframe = document.getElementById('iframeVideo');
            var videoUrl = iframe.src.split('?')[0]; // URL'nin ?'den önceki kısmını al
            iframe.src = videoUrl + '?start=' + Math.max(videoTime, 0) + "&autoplay=1"; // URL'yi güncelle
        }
    });
});







