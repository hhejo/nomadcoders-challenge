const todoContainer = document.querySelector(".js-todo"),
    todoForm = todoContainer.querySelector(".js-todoForm"),
    todoInput = todoForm.querySelector("input"),
    todoList = todoContainer.querySelector(".js-todoList");
const LOCAL_STORAGE_TODOS = "todos";

let todos = [];
let todoCount = 0;

function deleteTodo(e) {
    const targetLi = e.target.parentNode;
    todoList.removeChild(targetLi);

    const cleanedTodos = todos.filter(function (todo) {
        return todo.id !== parseInt(targetLi.id);
    });
    todos = cleanedTodos;
    localStorage.setItem(LOCAL_STORAGE_TODOS, JSON.stringify(todos));
}

function saveTodo(todoText, todoIdx) {
    const todoObj = {
        text: todoText,
        id: todoIdx
    };
    todos.push(todoObj);
    localStorage.setItem(LOCAL_STORAGE_TODOS, JSON.stringify(todos));
}

function paintTodo(todoText, todoIdx) {
    const li = document.createElement("li"),
        delBtn = document.createElement("button"),
        span = document.createElement("span");
    delBtn.innerText = "X";
    delBtn.addEventListener("click", deleteTodo);
    span.innerText = todoText;
    li.appendChild(delBtn);
    li.appendChild(span);
    li.id = todoIdx;
    todoList.appendChild(li);
}

function createTodo(todoText) {
    const todoId = todoCount + 1;
    paintTodo(todoText, todoId);
    saveTodo(todoText, todoId);
    todoCount = todoId;
}

function handleSubmit(e) {
    e.preventDefault();
    const todoText = todoInput.value;
    todoInput.value = "";
    createTodo(todoText);
}

function loadTodos() {
    const loadedTodos = localStorage.getItem(LOCAL_STORAGE_TODOS);
    if (loadedTodos !== null) {
        const parsedTodos = JSON.parse(loadedTodos);
        parsedTodos.forEach(function (parsedTodo) {
            createTodo(parsedTodo.text);
        });
    }
}

function init() {
    loadTodos();
    todoForm.addEventListener("submit", handleSubmit);
}

init();