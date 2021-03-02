// <⚠️ DONT DELETE THIS ⚠️>
//import "./styles.css";
const colors = ["#1abc9c", "#3498db", "#9b59b6", "#f39c12", "#e74c3c"];
// <⚠️ /DONT DELETE THIS ⚠️>

/*
✅ The text of the title should change when the mouse is on top of it.
✅ The text of the title should change when the mouse is leaves it.
✅ When the window is resized the title should change.
✅ On right click the title should also change.
✅ The colors of the title should come from a color from the colors array.
✅ DO NOT CHANGE .css, or .html files.
✅ ALL function handlers should be INSIDE of "superEventHandler"
*/
let mainText = document.querySelector("h2");

const superEventHandler = {
    mouseOver: function() {
        mainText.addEventListener("mouseover", function() {
            mainText.style.color = colors[0];
            mainText.innerText = "The mouse is here!";
        });
    },
    mouseOut: function() {
        mainText.addEventListener("mouseout", function() {
            mainText.style.color = colors[1];
            mainText.innerText = "The mouse is gone!";
        });
    },
    resized: function() {
        window.addEventListener("resize", function() {
            mainText.style.color = colors[2];
            mainText.innerText = "You just resized!";
        });
    },
    contextMenu: function() {
        window.addEventListener("contextmenu", function() {
            mainText.style.color = colors[4];
            mainText.innerText = "That was a right click!";
        });
    }
};

superEventHandler.mouseOver();
superEventHandler.mouseOut();
superEventHandler.resized();
superEventHandler.contextMenu();