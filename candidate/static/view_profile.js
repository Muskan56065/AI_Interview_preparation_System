
document.addEventListener("DOMContentLoaded", function () {

    // Print profile
    const printButton = document.getElementById("printProfileBtn");

    if (printButton) {
        printButton.addEventListener("click", function () {
            window.print();
        });
    }

    // Confirm before editing profile
    const editButton = document.getElementById("editProfileBtn");

    if (editButton) {
        editButton.addEventListener("click", function (event) {
            const confirmEdit = confirm(
                "Do you want to edit your profile?"
            );

            if (!confirmEdit) {
                event.preventDefault();
            }
        });
    }

});
