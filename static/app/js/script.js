const box = document.getElementById("box");
const itemsInner = document.querySelectorAll(".box-item-inner");
const title = document.querySelectorAll(".title");
const content = document.querySelectorAll(".content");
const boxItem = document.querySelectorAll(".box-item");
const expbtn = document.querySelectorAll(".expbtn");
const accord = document.querySelectorAll(".accord");
const closeBtn = document.querySelectorAll(".closeBtn");
// esas sehifede acilan div
function addClick(event) {
  event.stopPropagation();
  const parentElement = this.parentElement;
  const parentClasses = parentElement.classList;
  const hasClass = box.classList.contains(`box-${parentClasses[1]}-expand`);

  box.classList.add(`box-${parentClasses[1]}-expand`);
  box.classList.add(`expand`);
}

itemsInner.forEach((item) => {
  item.addEventListener("click", addClick);
});

closeBtn.forEach((item) => {
  item.addEventListener("click", function (e) {
    e.stopPropagation();
    const parentElement = this.parentElement.parentElement.parentElement;
    const parentClasses = parentElement.classList;
    box.classList.remove(`box-${parentClasses[1]}-expand`);
    box.classList.remove(`expand`);
  });
});

function openTab(evt, tabName) {
  let i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

$(".snake").snakeify({
  speed: 100,
});

content.forEach((item) => {
  item.addEventListener("click", function (e) {
    e.stopPropagation();
  });
});
