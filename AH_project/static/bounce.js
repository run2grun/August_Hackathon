/*
    Reference: https://css-tricks.com/restart-css-animation/
*/

element = document.getElementById("hey");

element.addEventListener("click", function (e) {
    e.preventDefault;

    // -> removing the class
    element.classList.remove("bounce");

    // -> triggering reflow /* The actual magic */
    // without this it wouldn't work. Try uncommenting the line and the transition won't be retriggered.
    element.offsetWidth = element.offsetWidth;

    // -> and re-adding the class
    element.classList.add("bounce");
}, false);