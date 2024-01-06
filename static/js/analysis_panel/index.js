import {showMostActiveAuthorsPanel } from './freq_analysis/mostActiveAuthors.js';
import { showTimeSpentAuthorsPanel } from './freq_analysis/timeSpentAuthor.js';
import { showMostRepeatingWordsPanel } from './freq_analysis/mostRepeatingWords.js';
document.addEventListener("DOMContentLoaded", function() {
    const options = document.querySelectorAll(".option");
    const popups = document.querySelectorAll(".popup");

    // if an option is clicked, show the corresponding popup
    options.forEach((option, index) => {
        option.addEventListener("click", () => {
            popups.forEach((popup, popupIndex) => {
                if (index === popupIndex) {
                    popup.style.display = "block";
                } else {
                    popup.style.display = "none";
                }
            });
        });
    });

    // if analyze or close button is clicked, close the popup
    const analyzeBtns = document.querySelectorAll('.analyze-btn');
    const closeBtns = document.querySelectorAll('.close-btn');

    analyzeBtns.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            popups[index].style.display = 'none';
        });
    });

    closeBtns.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            popups[index].style.display = 'none';
        });
    });

    // if there is a checkbox checked, uncheck the others
    const checkboxes = document.querySelectorAll('.sub-options input[type="checkbox"]');

    checkboxes.forEach((checkbox, index) => {
        checkbox.addEventListener('change', (event) => {
            if (event.target.checked) {
                checkboxes.forEach((cb, i) => {
                    if (i !== index) {
                        cb.checked = false;
                    }
                });
            }
        });
    });


    // if analyze button is clicked (right-panel)
    const frequencyAnalysisButton = document.querySelector('.option:nth-child(1)'); // Frekans Analizi butonunu seç
    frequencyAnalysisButton.addEventListener('click', () => {
        const analyzeButton = document.querySelector('.analyze-btn');
        analyzeButton.addEventListener('click', () => {
            const checkedCheckbox = document.querySelector('input[type="checkbox"]:checked');

            // if most_active_authors checkbox is checked
            if (checkedCheckbox && checkedCheckbox.value === 'most_active_authors') {
                fetch('/analysis_panel/get_most_active_authors')
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        resetRightPanel();
                        showMostActiveAuthorsPanel(data);
                    })
                    .catch(error => console.error('Error:', error));
            }
            // if most_active_authors checkbox is checked
            else if (checkedCheckbox && checkedCheckbox.value === 'time_spent_authors') {
                fetch('/analysis_panel/get_spent_time_authors')
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        resetRightPanel();
                        showTimeSpentAuthorsPanel(data);
                    })
                    .catch(error => console.error('Error:', error));
            }
            else if (checkedCheckbox && checkedCheckbox.value === 'most_repeating_words') {
                fetch('/analysis_panel/get_most_repeating_words')
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        resetRightPanel();
                        showMostRepeatingWordsPanel(data);
                    })
                    .catch(error => console.error('Error:', error));
            }
        });
    });

    function resetRightPanel() {
        const rightPanel = document.querySelector('.right-panel');
        rightPanel.innerHTML = ''; // Right panel içeriğini temizle
    }

    });