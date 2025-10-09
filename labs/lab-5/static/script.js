let list = [
    "/",
    "memory1.html",
    "memory2.html",
    "memory3.html",
    "theAbyss.html"
];

function getNewPage() {
    let randInt = Math.floor(Math.random() * 5);

    document.getElementById("newTab").href = list[randInt]; 
}

function on() {
    document.getElementById("overlay").style.display = "block";
}

function off() {
    document.getElementById("overlay").style.display = "none";
    document.body.style.overflow = "visible";
}


let timesClicked = 0;

function buttonClick() {
    let buttonTopPos = parseInt(document.getElementById("popup-button").style.top);
    let buttonLeftPos = parseInt(document.getElementById("popup-button").style.left);
    //console.log(buttonLeftPos);
    
    switch(timesClicked) {
        case 0:
            document.getElementById("popup-button").style.top = "10px";
            break;
        case 1:
        case 2:
        case 3:
            document.getElementById("popup-button").style.top = (buttonTopPos + 100).toString() + "px";
            break;
        case 4:
            document.getElementById("popup-button").style.left = "50px";
            break;
        case 5:
        case 6:
        case 7:
            document.getElementById("popup-button").style.left = (buttonLeftPos - 30).toString() + "px";
            break;
        case 8:
            off();
            break;
    }
    timesClicked++;
}

function pinUpdate(pinElement, numberDifference) {
    let elementName = "num" + pinElement;
    let oldNum = document.getElementById(elementName).textContent;
    let newNum = parseInt(oldNum) + parseInt(numberDifference);
    
    if(newNum >= 0) {
        document.getElementById(elementName).textContent = newNum;
        checkPassword();
    }
}

function checkPassword() {
    
    let currPin = "";

    for(let i = 1; i <= 5; i++) {
        let elementName = "num" + i;
        currPin += document.getElementById(elementName).textContent;
    }

    // Yes, I know this isn't secure but you said to make this poorly designed
    if(currPin == "25487") {
        document.getElementsByClassName("finalButton")[0].disabled = false;
    } else {
        document.getElementsByClassName("finalButton")[0].disabled = true;
    }
}

function fix() {
    document.body.style.overflow = "visible";
}