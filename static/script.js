document.addEventListener("DOMContentLoaded", function () {

    const progressBar = document.querySelector(".progress-bar");

    if (progressBar) {

        const finalWidth = progressBar.style.width;

        progressBar.style.width = "0%";

        setTimeout(() => {
            progressBar.style.width = finalWidth;
            progressBar.style.transition = "width 1.5s ease";
        }, 300);
    }

    const textarea = document.querySelector("textarea");

    if (textarea) {

        const counter = document.createElement("div");

        counter.style.textAlign = "right";
        counter.style.marginTop = "8px";
        counter.style.color = "#dbeafe";
        counter.style.fontSize = "14px";

        textarea.parentNode.appendChild(counter);

        function updateCounter() {
            counter.innerHTML = textarea.value.length + " / 5000 characters";
        }

        textarea.addEventListener("input", updateCounter);

        updateCounter();
    }

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            const button = form.querySelector("button");

            button.disabled = true;

            button.innerHTML =
                '<span class="spinner-border spinner-border-sm"></span> AI is analyzing...';

        });

    }

});