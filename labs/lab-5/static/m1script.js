let toggledButtons = []; 
let toggledAmt = 0;

function buttonToggle(button) {
    const element = document.getElementsByClassName("pipes")[button];
    
    if(toggledButtons[button] == null) {
        toggledButtons[button] = false;
    }
    let toggled = toggledButtons[button];

    if(element instanceof HTMLElement) {
        if(!toggled) {
            element.classList.remove("rotatedBack");
            element.classList.add("rotated");
            toggledAmt += 1;
        } else {
            element.classList.remove("rotated");
            element.classList.add("rotatedBack");
            toggledAmt -= 1;
        }
        toggled = !toggled;
        toggledButtons[button] = toggled;
    }
    checkCircuit();
}

function checkCircuit() {
    if(toggledAmt == 4) {
        document.getElementById("popup1").hidden = false;
    }
}

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