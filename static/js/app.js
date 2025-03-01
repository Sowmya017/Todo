document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("form[action='/']").addEventListener("submit", function (event) {

        let title = document.querySelector("#title").value.trim();
        let desc = document.querySelector("#desc").value.trim();

        if (!title || !desc) {
            alert("Title and description cannot be empty!");
            event.preventDefault(); // Stop form submission
        }
    });
});
