const inputs = document.querySelectorAll("input[type='checkbox']");
let labels = document.querySelectorAll(".options_container label");
inputs.forEach((input, index) =>
  input.addEventListener("click", () => {
    labels[index].classList.toggle("disabled");
  })
);
