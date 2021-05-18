const box = document.getElementById("box");
const itemsInner = document.querySelectorAll(".box-item-inner");
const title = document.querySelectorAll(".title");
const content = document.querySelectorAll(".content");
const closeBtn = document.querySelector(".closeBtn");
const boxItem = document.querySelectorAll(".box-item");
const expbtn = document.querySelectorAll(".expbtn");
const accord = document.querySelectorAll(".accord");

// esas sehifede acilan div
function addClick(event) {
  event.stopPropagation();
  const parentElement = this.parentElement;
  const parentClasses = parentElement.classList;
  console.log("parentClasses", parentClasses[1]);
  const hasClass = box.classList.contains(`box-${parentClasses[1]}-expand`);
  if (hasClass) {
    box.classList.remove(`box-${parentClasses[1]}-expand`);
    box.classList.remove(`expand`);
  } else {
    box.classList.add(`box-${parentClasses[1]}-expand`);
    box.classList.add(`expand`);
  }
}

itemsInner.forEach((item) => {
  item.addEventListener("click", addClick);
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
// image hover
