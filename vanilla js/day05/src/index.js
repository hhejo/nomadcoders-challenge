import "./styles.css";

const ddayDiv = document.querySelector(".js-dday"),
    ddayCounter = ddayDiv.querySelector(".js-counter");

// You're gonna need this
function getTime() {
    // Don't delete this.
    const xmasDay = new Date("2021-12-25:00:00:00+0900"),
        today = new Date(),
        dDay = xmasDay.getTime() - today.getTime();

    const d = Math.floor(dDay / (1000 * 60 * 60 * 24)),
        h = Math.floor((dDay % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
        m = Math.floor((dDay % (1000 * 60 * 60)) / (1000 * 60)),
        s = Math.floor((dDay % (1000 * 60)) / 1000);

    ddayCounter.innerText = `${d}d ${(h < 10) ? "0" + h : h}h ${(m < 10) ? "0" + m : m}m ${(s < 10) ? "0" + s : s}s`;
}

function init() {
    getTime();
    setInterval(getTime, 1000);
}

init();
