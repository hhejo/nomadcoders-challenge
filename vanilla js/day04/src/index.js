// <⚠️ DONT DELETE THIS ⚠️>
import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>

let body = document.querySelector("body");
body.innerHTML = "<h2>Hello!</h2>";
body.style.color = "white";

function setColor() {
  const windowWidth = window.innerWidth;
  if (windowWidth < 600) {
    body.style.backgroundColor = "#2D8ED6";
  } else if (windowWidth < 900) {
    body.style.backgroundColor = "#904EAD";
  } else {
    body.style.backgroundColor = "#EEBC12";
  }
}

setColor();

window.addEventListener("resize", setColor);
