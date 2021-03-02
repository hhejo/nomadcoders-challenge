const user = document.querySelector(".js-user"),
    userNameForm = user.querySelector(".js-userNameForm"),
    userNameInput = userNameForm.querySelector("input"),
    userGreeting = user.querySelector(".js-userGreeting");
const LOCAL_STORAGE_USERNAME = "username",
    HIDE = "hiding",
    SHOW = "showing";

function onScreen(u) {
    u.classList.remove(HIDE);
    u.classList.remove(SHOW);
}

function offScreen(u) {
    u.classList.remove(SHOW);
    u.classList.add(HIDE);
}

function handleSubmit(e) {
    e.preventDefault();
    localStorage.setItem(LOCAL_STORAGE_USERNAME, userNameInput.value);
    offScreen(userNameForm);
    greetingUser(userNameInput.value);
    userNameInput.value = "";
}

function askName() {
    onScreen(userNameForm);
    userNameForm.addEventListener("submit", handleSubmit);
}

function greetingUser(username) {
    userGreeting.innerText = `${username}님, 환영합니다!`;
    onScreen(userGreeting);
}

function loadName() {
    const username = localStorage.getItem(LOCAL_STORAGE_USERNAME);
    if (username !== null) {
        greetingUser(username);
    } else {
        askName();
    }
}

function init() {
    loadName();
}

init();