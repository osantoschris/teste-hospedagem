function startCountdown(redirectUrl) {
    var countdown = 10;
    var countdownElement = document.getElementById('countdown');
    var interval = setInterval(function() {
        countdown--;
        countdownElement.textContent = countdown;
        if (countdown <= 0) {
            clearInterval(interval);
            window.location.href = redirectUrl;
        };
    }, 1000);
};

window.onload = function() {
    startCountdown(redirectUrl);
};