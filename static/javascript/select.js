const btns = document.querySelectorAll(".btn");
const pres = document.querySelectorAll(".pre");

for (const btn of btns) {
  btn.addEventListener("click", function () {
    window.open("https://kahboom.tk/quizID/" + btn.name, "_self");
  });
}

function copyToClipboard(IDToCopy) {
  // ADD COPY CLIPBOARD FUNCTION
}
