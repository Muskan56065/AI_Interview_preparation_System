
document.addEventListener("DOMContentLoaded", function () {

    // Confirm before logging out
    const logoutButton = document.getElementById("logoutButton");

    if (logoutButton) {
        logoutButton.addEventListener("click", function (event) {

            const confirmLogout = confirm(
                "Are you sure you want to log out?"
            );

            if (!confirmLogout) {
                event.preventDefault();
            }

        });
    }

});
