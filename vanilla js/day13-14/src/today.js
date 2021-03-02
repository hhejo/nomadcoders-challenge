const today = document.querySelector(".js-today"),
    tDate = today.querySelector(".js-date"),
    tTime = today.querySelector(".js-time");

function getTime(date) {
    const m = date.getMinutes();
    const h = date.getHours();
    //const s = date.getSeconds();
    //tTime.innerText = `${h < 10 ? `0${h}` : h}:${m < 10 ? `0${m}` : m}:${s < 10 ? `0${s}` : s }`;
    tTime.innerText = `${h < 10 ? `0${h}` : h} : ${m < 10 ? `0${m}` : m}`;
}

function getDate(date) {
    const dayIndex = String(date.getDay());
    let day = "";
    switch (dayIndex) {
        case "0" : day = "Sun"; break;
        case "1" : day = "Mon"; break;
        case "2" : day = "Tue"; break;
        case "3" : day = "Wed"; break;
        case "4" : day = "Thu"; break;
        case "5" : day = "Fri"; break;
        case "6" : day = "Sat"; break;
    }
    const dateIndex = date.getDate();
    const monthIndex = String(date.getMonth() + 1);
    let month = "";
    switch (monthIndex) {
        case "1" : month = "January"; break;
        case "2" : month = "February"; break;
        case "3" : month = "March"; break;
        case "4" : month = "April"; break;
        case "5" : month = "May"; break;
        case "6" : month = "June"; break;
        case "7" : month = "July"; break;
        case "8" : month = "August"; break;
        case "9" : month = "September"; break;
        case "10" : month = "October"; break;
        case "11" : month = "November"; break;
        case "12" : month = "December"; break;
    }
    tDate.innerHTML = `${day} ${dateIndex} ${"&nbsp;"} ${month}`;
}

function getToday() {
    const date = new Date();
    getDate(date);
    getTime(date);
}

function init() {
    setInterval(getToday, 1000);
}

init();