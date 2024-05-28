const inputs = document.querySelectorAll("input");
let labels = document.querySelectorAll("label");
inputs.forEach((input, index) =>
  input.addEventListener("click", () => {
    labels[index].classList.toggle("disabled");
  })
);
