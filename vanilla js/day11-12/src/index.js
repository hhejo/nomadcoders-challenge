// <⚠️ DONT DELETE THIS ⚠️>
//import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>

const firstLine = document.querySelector(".js-firstLine"),
    secondLine = document.querySelector(".js-secondLine"),
    thirdLine = document.querySelector(".js-thirdLine"),
    fourthLine = document.querySelector(".js-fourthLine"),
    fifthLine = document.querySelector(".js-fifthLine");

const btnContainer = document.querySelector(".calculator");

const mainDisplay = firstLine.querySelector(".screen");

let firstValue = null,
    secondValue = null,
    prevKey = "",
    op = "",
    screen = "0";

function calc(operator) {
    let r = 0;
    switch (operator) {
        case "+" :
            r = firstValue + secondValue;
            break;
        case "-" :
            r = firstValue - secondValue;
            break;
        case "*" :
            r = firstValue * secondValue;
            break;
        case "/" :
            r = firstValue / secondValue;
            break;
    }
    return r;
}

function calculate(val) {
    console.log(val);
    if (val === "C") {
        screen = "0";
        firstValue = secondValue = null;
    } else if (val === "+" || val === "-" || val === "*" || val === "/") {
        if (firstValue === null) {
            firstValue = parseInt(screen);
        } else {
            secondValue = parseInt(screen);
            let result = calc(op);
            screen = String(result);
            firstValue = result;
            secondValue = null;
        }
        prevKey = op = val;
    } else if (val === "=") {
        secondValue = parseInt(screen);
        let result = calc(op);
        screen = String(result);
        firstValue = secondValue = null;
    } else {
        if (prevKey === "") {
            if (screen === "0") {
                screen = val;
            } else {
                screen += val;
            }
        } else {
            screen = val;
            prevKey = "";
        }
    }

    console.log(`firstValue: ${firstValue}, secondValue: ${secondValue}, screen: ${screen}`);

    mainDisplay.innerText = screen;
}

function handleClick(e) {
    const clicked = e.target;
    if (clicked.classList.contains("btn")) {
        calculate(clicked.value);
    }
}

function init() {
    btnContainer.addEventListener("click", handleClick);
}

init();