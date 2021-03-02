// <⚠️ DONT DELETE THIS ⚠️>
//import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>

const slider = document.querySelector(".js-slider");
let sliderTitle = document.querySelector(".js-sliderTitle");
let maxValue;
const numberInput = document.querySelector(".js-numberInput");
const btn = document.querySelector(".js-button");
let answer;

const result = document.querySelector(".js-result");
const resultNumber = result.querySelector(".js-resultNumber");
const resultTitle = result.querySelector(".js-resultTitle");

function randomNumber(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    let result = Math.floor(Math.random() * (max - min + 1)) + min;
    return result;
}

function slideNumber() {
    slider.addEventListener("input", function() {
        maxValue = slider.value;
        sliderTitle.innerText = `Generate a number between 0 and ${maxValue}`;
        answer = randomNumber(0, maxValue);
    });
}

function getNumber() {
    btn.addEventListener("click", handleBtn);
}

function handleBtn(event) {
    event.preventDefault();
    if (numberInput.value !== "") {
        answer = randomNumber(0, maxValue);
        resultNumber.innerText = `You chose: ${numberInput.value}, the machine chose: ${answer}.`;
        if (numberInput.value == answer) {
            resultTitle.innerText = "You won!";
        } else {
            resultTitle.innerText = "You lost!";
        }
    } else {
        resultNumber.innerText = "";
        resultTitle.innerText = "";
    }
}

function init() {
    maxValue = slider.value;
    slideNumber();
    getNumber();
}

init();