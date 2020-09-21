let resetButtun = document.getElementById('btn-reset');
let loginButton = document.getElementById('btn-login');
let closeModalButton = document.getElementById('btn-close-modal');
let logoutButton = document.getElementById('btn-logout');

let usernameInput = document.getElementById('username');
let passwordInput = document.getElementById('password');

let modal = document.getElementById('modal');
let modalMessage = document.getElementById('modal-message');

let welcome = document.getElementById('welcome-container');
let userWelcome = document.getElementById('user-welcome');


function inputNull() {
    usernameInput.value = null;
    passwordInput.value = null;
 }

function resetInput() {
    // if inputs are empty, alert user, if not, run function
    return usernameInput.value.length == 0 && passwordInput.value.length == 0 ? 
    modal.style.display = 'block' : inputNull();
}

resetButtun.addEventListener('click', resetInput);

closeModalButton.addEventListener('click', function() {
    modal.style.display = 'none';
});

modal.addEventListener('click', function() {
    modal.style.display = 'none';
});

function loginAccepted() {
    welcome.style.display = 'block';
    userWelcome.innerText = 'Hello, ' + usernameInput.value + '.';
    inputNull();
}

function loginPerformed() {
    switch(true) {
        case usernameInput.value == "Amy", passwordInput.value == "coding":
            loginAccepted();
            break;
        case usernameInput.value == "Hannah", passwordInput.value == "fiat":
            loginAccepted();
            break;
        case usernameInput.value == "Shanice", passwordInput.value == "movie":
            loginAccepted();
            break;
        case usernameInput.value == "Katy", passwordInput.value == "spain":
            loginAccepted();
            break;
        case usernameInput.value == "Annie", passwordInput.value == "makeup":
            loginAccepted();
            break;
        default:
            modal.style.display = 'block';
            modalMessage.innerText = 'incorrect username or password. please try again';
            inputNull();
    }
}

loginButton.addEventListener('click', loginPerformed);

usernameInput.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
      event.preventDefault(); // cancel default
      loginButton.click();
    }
});

passwordInput.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
      event.preventDefault();
      loginButton.click();
    }
});

function logoutPerformed() {
    welcome.style.display = 'none';
}

logoutButton.addEventListener('click', logoutPerformed);