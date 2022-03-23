const selectQuizModals = document.querySelectorAll("#selectQuizModal");
const selectQuizBtns = document.querySelectorAll("#selectQuizBtn");

function* enumerate(iterable) {
  let i = 0;

  for (const x of iterable) {
    yield [i, x];
    i++;
  }
}

for (const [i, btn] of enumerate(selectQuizBtns)) {
  btn.addEventListener("click", function () {
    selectQuizModals[i].style.display = "flex";
  });
}

window.onclick = function (event) {
  for (modal of selectQuizModals) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
};
