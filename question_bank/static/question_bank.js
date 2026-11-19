
document.addEventListener("DOMContentLoaded", function () {

    const filterForm = document.getElementById("filterForm");

    const roleSelect = document.getElementById("role");
    const topicSelect = document.getElementById("topic");
    const difficultySelect = document.getElementById("difficulty");

    if (filterForm) {

        [roleSelect, topicSelect, difficultySelect].forEach(function (field) {

            if (field) {
                field.addEventListener("change", function () {
                    filterForm.submit();
                });
            }

        });

    }

});
