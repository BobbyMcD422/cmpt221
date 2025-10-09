function fadeAway() {
    document.getElementById("fade").style.zIndex = 6;
    document.getElementById("fade").style.animation = "newAnim 3s linear forwards";
    setTimeout(goHome, 3000);
}

function goHome() {
    location.href = "/";
}