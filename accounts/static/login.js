
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("loginForm");

    if (!form) return;

    form.addEventListener("submit", function (event) {

        const username = form.querySelector(
            '[name="username"]'
        );

        const password = form.querySelector(
            '[name="password"]'
        );

        if (username && username.value.trim() === "") {
            event.preventDefault();
            alert("Please enter your username.");
            username.focus();
            return;
        }

        if (password && password.value.trim() === "") {
            event.preventDefault();
            alert("Please enter your password.");
            password.focus();
            return;
        }

    });

});
