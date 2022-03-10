const searchNameModal = document.getElementById("searchNameModal");
const searchIDModal = document.getElementById("searchIDModal");

const searchNameBtn = document.getElementById("searchNameBtn");
const searchIDBtn = document.getElementById("searchIDBtn");

searchNameBtn.onclick = function () {
  searchNameModal.style.display = "flex";
};

searchIDBtn.onclick = function () {
  searchIDModal.style.display = "flex";
};

window.onclick = function (event) {
  if (event.target == searchNameModal) {
    searchNameModal.style.display = "none";
  }

  if (event.target == searchIDModal) {
    searchIDModal.style.display = "none";
  }
};
