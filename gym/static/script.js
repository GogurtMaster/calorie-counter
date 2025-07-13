document.addEventListener('DOMContentLoaded', function () {
    const dropButton = document.getElementById('dropdownToggle');
    dropButton.addEventListener('click', function () {
        document.getElementById("list_dropdown").classList.toggle("show");
    });
});


window.onclick = function(event) {
    if (!event.target.matches('.drop_button')) {
        var dropdowns = document.getElementsByClassName("drop_content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var open_drop = dropdowns[i];
            if (open_drop.classList.contains('show')) {
                open_drop.classList.remove('show');
            }
        }
    }
}

console.log("JS is loaded!");
