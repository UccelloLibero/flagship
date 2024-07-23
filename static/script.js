var correctGuesses = 0;
var incorrectGuesses = 0;
var timer;
var timeLeft = 60;

document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname === '/game') {
        startGameSession();
    }
});

function startGame() {
    window.location.href = '/game';
}

function startGameSession() {
    fetch('/start_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        loadFlag(data);
        startTimer();
    });
}

function loadFlag(data) {
    var flagImageContainer = document.getElementById('flagImageContainer');
    if (flagImageContainer) {
        flagImageContainer.innerHTML = `<img src="${data.flagUrl}" class="img-fluid" alt="Flag">`;
    }

    var optionsContainer = document.querySelector(".options-container");
    if (optionsContainer) {
        optionsContainer.innerHTML = "";
        data.options.forEach(option => {
            var button = document.createElement("button");
            button.className = "btn custom-button";
            button.textContent = option;
            button.onclick = function() {
                checkAnswer(option, button);
            };
            optionsContainer.appendChild(button);
        });
    }
}

function checkAnswer(selectedOption, button) {
    fetch('/check_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ selectedOption: selectedOption })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'correct') {
            button.style.backgroundColor = "#9BC13B";
            document.getElementById('correctGuesses').textContent = ++correctGuesses;
        } else {
            button.style.backgroundColor = "#683216";
            document.getElementById('incorrectGuesses').textContent = ++incorrectGuesses;
        }
        setTimeout(startGameSession, 1000); // Wait 1 second before loading the next flag
    });
}

function startTimer() {
    var timerElement = document.getElementById('timer');
    if (timerElement) {
        timerElement.textContent = timeLeft;
    }

    timer = setInterval(() => {
        timeLeft--;
        if (timerElement) {
            timerElement.textContent = timeLeft;
        }

        if (timeLeft <= 0) {
            clearInterval(timer);
            endGame();
        }
    }, 1000);
}

function endGame() {
    var gameContainer = document.querySelector('.container.mt-5');
    if (gameContainer) {
        gameContainer.innerHTML = `
            <div class="end-message text-center">
                <h2>Thank you for playing!</h2>
                <p>Correct guesses: ${correctGuesses}</p>
                <p>Incorrect guesses: ${incorrectGuesses}</p>
                <button class="btn btn-primary custom-button" style="background-color: #2A3814; color: #ffffff;" onclick="startGame()">Play Again</button>
                <button class="btn btn-secondary custom-button" onclick="learnFlags()">Learn Flags</button>
            </div>
        `;
    }
}

function learnFlags() {
    window.location.href = '/learnflags'; // This points to learnflags.html
}