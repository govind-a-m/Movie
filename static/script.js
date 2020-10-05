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
let loginform = document.getElementById('loginform');


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
    if(usernameInput.value.length!=0)
    {
        if(passwordInput.value.length!=0)
        {
            $.ajax({
			        url: '/ajaxlogin',
			        data: $('#loginform').serialize(),
			        type: 'POST',
			        success: function(response){
				    OnloginResponse(response);
			        },
			        error: function(error){
                        console.log(error);
                    }
			});
        }
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

function OnloginResponse(response){
    rsp = JSON.parse(response);
    if(rsp.login=="SUCCESS")
    {
        var page = location.href+"Movies/1";
        console.log(page);
        location.replace(page);
    }
    else
    {
        modalMessage.innerHTML = "Wrong Password or user name"
        modal.style.display = 'block';
    }
}