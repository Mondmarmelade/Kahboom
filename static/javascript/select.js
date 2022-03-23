const btns = document.querySelectorAll(".btn");

for (const btn of btns) {
  btn.addEventListener("click", function () {
    window.open("https://kahboom.tk/quizID/" + btn.name, "_self");
  });
}

function copyToClipboard(IDToCopy) {
  navigator.clipboard.writeText(IDToCopy);
}
