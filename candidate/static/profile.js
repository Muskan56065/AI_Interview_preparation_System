
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("candidateForm");

    if (!form) return;

    form.addEventListener("submit", function (event) {

        const phone = document.querySelector(
            'input[name="phone"]'
        );

        const experience = document.querySelector(
            'input[name="experience"]'
        );

        const fullName = document.querySelector(
            'input[name="full_name"]'
        );

        // Validate full name
        if (fullName.value.trim().length < 3) {
            event.preventDefault();
            alert("Please enter your full name (at least 3 characters).");
            fullName.focus();
            return;
        }

        // Validate phone number
        const phonePattern = /^\d{10,15}$/;

        if (!phonePattern.test(phone.value.trim())) {
            event.preventDefault();
            alert("Enter a valid phone number with 10-15 digits.");
            phone.focus();
            return;
        }

        // Validate experience
        const years = Number(experience.value);

        if (
            experience.value.trim() === "" ||
            !Number.isInteger(years) ||
            years < 0
        ) {
            event.preventDefault();
            alert("Please enter valid experience in whole years.");
            experience.focus();
            return;
        }

        // Confirmation
        const confirmSave = confirm(
            "Are you sure you want to save your profile?"
        );

        if (!confirmSave) {
            event.preventDefault();
        }

    });

});
