// <⚠️ DONT DELETE THIS ⚠️>
//import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>

const countryList = document.querySelector(".select");

function selectCountry() {
    const selectedIndex = countryList.options.selectedIndex;
    const selectedCountry = countryList.options[selectedIndex];
    const selectedCountryCode = selectedCountry.value;
    localStorage.setItem("country", selectedCountryCode);
}

function setInitialSelect() {
    if (localStorage.length > 0) {
        for (let i = 1; i < countryList.length; i++) {
            if (countryList.options[i].value === localStorage["country"]) {
                countryList.options[i].setAttribute("selected", "");
            } else {
                countryList.options[i].removeAttribute("selected");
            }
        }
    }
}

function init() {
    setInitialSelect();
}

init();