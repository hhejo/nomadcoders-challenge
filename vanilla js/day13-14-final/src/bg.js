const body = document.querySelector("body");

const IMG_NUMBER = 8;

function paintImage(imgNumber) {
    const image = new Image(); // image 객체 생성
    image.src = `/images/${imgNumber + 1}.jpg`; // 파일 경로
    image.classList.add("bgImage"); // 클래스 추가
    image.classList.add("bgImageNone");
    body.appendChild(image); // 이미지를 드러냄
    image.onload = function () {
        image.classList.remove("bgImageNone");
    };
}

function genRandom() {
    const number = Math.floor(Math.random() * IMG_NUMBER); // 0에서 4
    return number;
}

function init() {
    const randomNumber = genRandom(); // 난수 생성해서 가져옴
    paintImage(randomNumber); // 이미지 생성하는 데에 난수 투입
}

init();